# 04 - Giải pháp tiền xử lý dữ liệu viễn thông

---

(âm nhạc sôi động bắt đầu)

- [Người hướng dẫn] Trong phòng thí nghiệm thử thách này,

chúng tôi xử lý trước tập dữ liệu viễn thông.

Trước tiên, hãy đảm bảo tập dữ liệu của bạn đã được tải,

sau đó chạy tất cả các ô

trong phần tải và khám phá dữ liệu.

Để làm điều đó, nếu sổ ghi chép của bạn hiển thị

phần tải và khám phá của bạn đã được mở rộng, bạn chỉ cần thu gọn nó

và chạy tất cả các ô.

Phòng thí nghiệm thử thách bắt đầu trong phần xử lý trước dữ liệu.

Vì vậy, hãy mở rộng điều đó.

Đầu tiên, chúng tôi muốn xử lý các giá trị còn thiếu.

Vì vậy, hãy thực hiện một phương thức df.info

để nhắc nhở bản thân chúng là gì.

Chúng tôi có 7.043 mục, nhưng một số tính năng có ít hơn thế.

Đây là ưu đãi với 3.166 mục.

Đây là loại internet với 5.517 mục.

Và bạn sẽ nhận thấy rằng một số mục có dạng số

bị thiếu và một số là đối tượng hoặc chuỗi.

Vì vậy có thể tốt hơn nếu tính toán các giá trị còn thiếu

cho các cột số và đối tượng.

Và đó là những gì chúng tôi làm ở đây.

Phần này tính toán các giá trị còn thiếu

cho các cột số và đối tượng,

và phần này hiển thị kết quả.

Hãy xử lý các giá trị còn thiếu cho các cột đối tượng.

Vì vậy trước tiên, chúng ta sẽ xem xét mọi tính năng,

mọi cột, mọi tính năng,

và gán nó cho một biến gọi là cột phân loại.

Và sau đó chúng ta có một vòng lặp for,

để với mỗi đặc điểm trong cột phân loại đó,

chúng ta sẽ điền vào nó giá trị chung nhất.

Và sau đó, như một cách thực hành tốt nhất,

bạn luôn muốn thực hiện một phương thức df.info

để đảm bảo rằng nó đã được điền vào.

Vì vậy hãy xem.

Oops, looks like we missed a few.

Và đó là bài tập số một,

xử lý các giá trị còn thiếu.

Đối với cột đối tượng, chúng tôi đã bỏ lỡ ưu đãi,

và đó là nơi chúng ta bắt đầu bài tập số một,

xử lý các giá trị còn thiếu.

Vì vậy, ở đây chúng ta sẽ điền vào giá trị còn thiếu cho ưu đãi

và phương thức thanh toán.

Và bất cứ khi nào thiếu một giá trị cho lời đề nghị,

chúng tôi sẽ không đặt gì cả.

Và đối với phương thức thanh toán, chúng ta sẽ đặt thẻ tín dụng.

Và việc đó sẽ xử lý các cột đối tượng bị bỏ sót.

Đối với các cột số, chúng tôi sử dụng gigabit,

và chúng ta sẽ hiểu ý nghĩa của điều đó,

gán nó cho một biến có tên là Mean_gigabits.

Và chúng ta sẽ làm điều tương tự để có thu nhập.

Chúng ta sẽ có được ý nghĩa.

Đây là sự quy kết sử dụng giá trị trung bình

để điền vào các giá trị còn thiếu.

Và sau đó chúng ta sẽ tính toán điều đó.

Và tất nhiên, như một cách thực hành tốt nhất,

bạn cũng muốn luôn thực hiện phương thức df.info

để đảm bảo rằng mọi thứ diễn ra như bạn mong đợi.

Và chúng tôi có nó.

Mỗi tính năng hiện có 7.043 giá trị.

Ở bước hai, bạn phải tìm các giá trị trùng lặp,

nhưng không có ai cả.

Ở bước ba, bạn phải xử lý sự không nhất quán về kiểu dữ liệu.

Mã Zip là loại dữ liệu không chính xác.

Nó được hiển thị dưới dạng số nguyên,

nhưng nó không phải là một con số.

Trong xử lý và phân tích dữ liệu,

Mã Zip thường không được coi là số nguyên

hoặc giá trị số, mặc dù chúng bao gồm các chữ số.

Vì vậy, hãy xem bài học của khóa học về lý do tại sao lại như vậy.

Vì vậy, bài tập số hai là xử lý

dữ liệu không nhất quán đó.

Và ở đây chúng ta chỉ sử dụng phương thức chuỗi .asType,

lấy mã zip ra khỏi khung dữ liệu,

và về cơ bản là in nó ra để đảm bảo

rằng nó là một đối tượng chứ không phải một số nguyên.

Và sau đó là bước bốn, bạn phải xử lý các giá trị ngoại lệ.

Và chúng tôi đang sử dụng phương pháp Z-sore để làm điều đó.

Ở đây chúng tôi đang kiểm tra các hàng có Z-sore trên 3.

Và ở đây chúng tôi nhận thấy rằng có năm hàng

với Z-sore trên 3,

và chúng ta cần xóa bất kỳ hàng nào có Z-sore lớn hơn 3.

Và đó là nơi chúng tôi đặt đoạn mã nhỏ này vào.

Và sau đó chúng tôi muốn kiểm tra để chắc chắn

rằng chúng tôi đã loại bỏ tất cả chúng

và không còn cột nào nữa,

hay đúng hơn là các hàng, với Z-sore trên ba, và không có hàng nào cả.

Vì vậy, nhiệm kỳ dường như không có bất kỳ ngoại lệ nào.

Vì vậy, chúng tôi ổn ở đó.

Chỉ muốn kiểm tra một cột để đảm bảo.

Và cuối cùng, chúng tôi cần mã hóa theo các giá trị phân loại.

Và ở đây trong bài tập thứ ba,

chúng tôi đã mã hóa các giá trị phân loại.

Chúng ta có thể đã sử dụng cùng một biến

categorical_columns vì chúng tôi đã khởi tạo nó.

Nhưng đây là để tham khảo để cho bạn thấy

rằng tất cả các cột đang được gán cho biến này.

Và ở đây chúng tôi muốn lấy từng cột đối tượng này

và mã hóa chúng từ một chuỗi đối tượng thành một số,

nên họ sẽ được biến đổi.

Vì vậy, chúng ta hãy xem nó trông như thế nào.

Chúng ta chỉ có thể đảm bảo rằng bây giờ chúng là số nguyên

chứ không phải đối tượng bằng cách thực hiện df.dtypes.

Và chúng ta có thể thấy rằng mọi thứ đều là số nguyên

đó đã từng là một đối tượng, ngoại trừ mã zip.

Và hãy xem bài học về lý do tại sao lại như vậy.

Và ở đây chúng tôi thực hiện df.head để thấy rằng đúng vậy, thực sự,

việc mã hóa các biến phân loại của chúng tôi đã được thực hiện.

Và bài tập số bốn, chúng tôi chạy ô

để lưu tập tin sạch.

Bởi vì chúng tôi đã thực hiện những chuyển đổi này,

chúng ta cần lưu nó dưới dạng tên mới.

Tập tin sạch này sau đó sẽ được sử dụng

trong giai đoạn phân tích dữ liệu thăm dò của chúng tôi.

Vì vậy, chúng ta hãy tiếp tục và lưu nó.

Và nếu tôi vào thư mục của mình, nó ở đó.

Được rồi, hẹn gặp lại bạn ở video tiếp theo.