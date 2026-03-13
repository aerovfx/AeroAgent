# 07 - Giải pháp xử lý nhiễu trong ảnh

---

(nhạc sôi động)

- Được rồi, giờ chúng ta cùng nhau tìm giải pháp nhé.

Vì vậy, chúng ta sẽ tiếp tục và định nghĩa một hàm add noise.

Vì vậy, đối với chức năng này, chúng ta sẽ tiếp tục

và xác định một hình ảnh ồn ào.

Và hình ảnh nhiễu sẽ là hình ảnh cộng với số lần hệ số nhiễu

và sau đó ở đây chúng ta sẽ sử dụng phương pháp ngẫu nhiên hóa,

thật ngẫu nhiên.randn

sau đó chúng ta sẽ tiếp tục và nói image.shape.

Vì vậy, điều này định nghĩa một hàm có tên là "thêm tiếng ồn",

và nó có hai tham số, hình ảnh và hệ số nhiễu.

Và image chính là hình ảnh mà chúng ta đang nhập vào.

Và yếu tố tiếng ồn là yếu tố

that determines the amount of noise edit.

Và nếu chúng ta không đưa ra số tiền mặc định bằng 0,

sau đó chúng ta sẽ tiếp tục với hình ảnh ồn ào

bằng np.clip hình ảnh ồn ào bằng không một.

Vì vậy, chức năng này đảm bảo rằng tất cả các giá trị trong ảnh nhiễu

nằm trong phạm vi từ 0 đến một.

Điều này là cần thiết vì giá trị pixel phải

trong phạm vi này để thể hiện hình ảnh hợp lệ.

Sau đó chúng ta gần như đã hoàn tất,

thực ra chúng tôi tiếp tục và trả lại hình ảnh nhiễu,

và bây giờ chúng ta có một hình ảnh nhiễu.

Vì vậy, đây là cách chúng tôi làm điều đó.

Và sau đó chúng ta tiếp tục áp dụng điều này cho hình ảnh ồn ào của mình.

Vì vậy, hình ảnh nhiễu tương đương với việc thêm nhiễu.

Và sau đó chúng tôi cung cấp dữ liệu huấn luyện để làm cho dữ liệu của chúng tôi

ồn ào hơn, do đó dữ liệu của chúng tôi đa dạng hơn

và mô hình của chúng tôi sẽ được chuẩn bị

vì đã xử lý dữ liệu ồn ào.

Vì vậy sẽ tốt hơn khi thấy dữ liệu bị nhiễu.

Và sau đó chúng ta tiếp tục thêm các hàm vẽ đồ thị cho nó,

và sau đó chúng ta sẽ tiếp tục và lưu nó vào,

và sau đó chúng ta sẽ lưu nó vào thư mục lô đầu ra

dưới dạng 03_07_noisy_imagePNG.

Tại sao bảy?

Bởi vì nếu bạn nhấp vào video giải pháp,

chức năng tiếng ồn này đã được triển khai cho chúng tôi,

chúng ta có thể tiếp tục và chạy tệp python 03_07_solution

và sau đó xem nó thực hiện như thế nào khi thêm tiếng ồn.

Vì vậy chúng tôi sẽ dành cho nó một vài phút

và nó sẽ trải qua tất cả các thời đại và mọi thứ

và nó sẽ tạo ra một số nhiễu trong hình ảnh của chúng ta.

Được rồi, tuyệt vời.

Vậy là mã của chúng ta đã hoàn tất và chúng ta có thể thấy rằng chúng ta có

các ô hình ảnh ồn ào đã được lưu

vào thư mục mà chúng ta đã xác định.

Vì vậy chúng ta tiếp tục và tìm nó trong thư mục đầu ra,

vẽ hình ảnh 03_07_noisy và sau đó chúng tôi nhấp vào nó

và vâng, chúng tôi đã tạo ra hình ảnh ồn ào của mình.

Đây là cách chúng tôi thêm nhiễu vào hình ảnh của mình

và chúng ta thấy điều này rất nhiều trong cuộc sống thực.

Vì vậy, để làm cho dữ liệu của chúng ta đa dạng hơn, dễ bị nhiễu hơn,

đây là cách chúng tôi thêm nhiễu vào tập dữ liệu của mình.