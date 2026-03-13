# 6 -Nút Nhắc được dịch

---

Có một thành phần khác có thể rất hữu ích cho chúng ta khi tạo các luồng và tham chiếu

đến thành phần nhắc nhở.

Thành phần này cho phép chúng ta tạo một mẫu nhắc nhở với ưu điểm là chúng ta có thể sử dụng

các biến để xây dựng một dấu nhắc phức tạp hơn.

Chúng ta hãy xem nó trong thực tế.

Bạn có thể tìm thấy thành phần này trong phần được gọi là lời nhắc.

Lưu ý, đây là thành phần duy nhất có sẵn.

Tôi sẽ kéo và thả nó.

Là một phần trong các tính năng của lời nhắc này, bạn có thể thấy ở đây rằng chúng tôi có một mẫu cụ thể

cho phép bạn nhập một giá trị vào thành phần.

Làm thế nào chúng ta có thể sử dụng nó?

Chà, tôi sẽ xóa kết nối mà chúng ta có trước đây giữa hai thành phần này.

Họ trò chuyện thành phần đầu vào và họ mở thành phần y.

Tôi sẽ đặt thành phần nhắc nhở ở giữa.

Và điều khiến chúng tôi quan tâm là có thể sửa đổi lời nhắc đầu vào bằng cách nào đó.

Làm thế nào bạn có thể làm điều này?

Lưu ý rằng nếu bạn muốn kết nối hai thành phần này, nó có thể được gửi bởi vì

mẫu được gửi với mong đợi một tin nhắn hoặc nút văn bản làm đầu vào.

Và tại sao điều này lại xảy ra?

Bởi vì bên trong thành phần nhắc nhở, tôi phải xác định một tập hợp các biến để có thể kết nối

các thành phần trước đó.

Chúng ta làm điều này như thế nào?

Chà, hãy mở rộng thuộc tính này được gọi là mẫu.

Và hãy tưởng tượng rằng chúng tôi muốn lấy những gì người dùng yêu cầu.

Chúng tôi muốn dịch câu hỏi ban đầu đó sang ngôn ngữ trong trường hợp này là tiếng Pháp và nhận được

câu trả lời bằng tiếng Pháp.

Điều này hoạt động rất tốt nếu bạn muốn sửa đổi trong một số trường hợp nhất định phản hồi được tạo bởi

mô hình AI.

Trong trường hợp của tôi, tôi muốn dịch câu trả lời sang tiếng Pháp.

Bước tiếp theo là xác định các biến đầu vào.

Chúng ta làm điều này như thế nào?

Chà, chúng ta sẽ thêm một cặp dấu ngoặc nhọn và xác định tên mà chúng ta muốn cho biến này.

Bạn có thể thấy điều đó tự động ở phía dưới trong phần được gọi là các biến nhắc, phần

biến bạn xác định được gọi là truy vấn đã xuất hiện.

Bạn có thể xác định bao nhiêu biến tùy thích.

Ví dụ: tôi có thể xác định biến thứ hai, nhưng trong trường hợp này, tôi sẽ chỉ giữ biến đầu tiên này

biến được gọi giữa truy vấn dấu ngoặc nhọn để xác minh rằng mọi thứ đều chính xác và lưu

những thay đổi của bạn, hãy nhấp vào nút kiểm tra và lưu.

Với điều này, hãy xem chúng tôi đã sửa đổi thành phần có tên là nhắc nhở này như thế nào.

Thuộc tính cho mẫu đã được sửa đổi.

Ngoài ra, phần mới này đã được tạo, tương ứng với biến chúng tôi đã xác định

gọi là truy vấn.

Ở đây bạn có thể nhập văn bản mặc định hoặc trong trường hợp này, tôi sẽ liên kết thành phần này có tên

chat vào biến để nội dung mà người dùng nhập sẽ được thay thế bằng biến này.

Nói cách khác, wordy sẽ được cập nhật theo yêu cầu của người dùng.

Điều này sẽ khiến câu trả lời được dịch sang tiếng Pháp, giống như được chỉ ra trong mẫu.

Vì bạn sẽ không còn tương tác trực tiếp với thành phần nhập trò chuyện nữa nên tôi muốn làm rõ

rằng thông báo nhắc bạn đã tạo trong phần này hoặc trong thuộc tính này có tên là mẫu

sẽ là những gì bạn sử dụng làm đầu vào trong thành phần openAI.

Ở phía bên phải, mọi thứ vẫn giữ nguyên vì chúng ta sẽ tương tác với

chơi đùa.

Điều đã thay đổi là bây giờ tôi đã thêm một người trung gian và tại đây bạn có thể thực hiện bất kỳ điều gì

những sửa đổi mà bạn muốn.

Nếu bạn muốn thêm nhiều biến hơn cho lời nhắc phức tạp hơn, bạn có thể tạo các biến khác nhau

đầu vào văn bản và, ví dụ, xác định các phần của lời nhắc trong các thành phần này.

Chúng ta cần kiểm tra xem điều này có hoạt động chính xác không.

Hãy tiếp tục và khởi chạy trò chơi rồi nhập hướng dẫn, ví dụ:

tạo kịch bản hoặc câu chuyện hư cấu cho một bộ phim mới có tên Back to the Future Part

Gấp.

Hãy gửi những yêu cầu này và chờ phản hồi của họ.

Sau vài giây, bạn có thể thấy chúng tôi đã nhận được phản hồi chính xác bằng tiếng Pháp.

Tôi không nói được tiếng Pháp, nhưng tôi có thể xác định được một số dấu hiệu cho thấy phản ứng này là

viết bằng tiếng Pháp.

Vì vậy, tôi đã sửa đổi đầu ra và phản hồi của mô hình nhờ sử dụng lời nhắc này hoặc điều này

thành phần được gọi là nhắc nhở.

Chúng ta có thể sửa đổi lại mẫu để thêm, ví dụ, biến thứ hai, sau khi dịch

phản hồi bằng tiếng Pháp, chúng tôi cũng nhận được một loạt hướng dẫn bổ sung mà bạn

có thể xác định chính mình trong một thành phần khác.

Hãy tạo các hướng dẫn bổ sung có tên biến mới này.

Lưu ý rằng điều này đã tạo ra một thuộc tính mới để bạn có thể liên kết thông tin với thành phần khác

hoặc viết một hướng dẫn mặc định.

Ví dụ: tôi kéo một thành phần nhập văn bản và hoàn thành văn bản bằng thông báo tạo

một tập hợp các thẻ gắn nhãn truy vấn của người dùng.

Vì vậy, đây sẽ là hướng dẫn bổ sung của tôi sẽ được thêm vào lời nhắc mà chúng tôi đã gửi tới

mô hình LTI

Hãy thử lại một lần nữa.

Tôi sẽ đưa ra yêu cầu tương tự như tôi đã chỉ cho bạn trước đây, nhưng bây giờ, bằng cách sử dụng hướng dẫn mới, tôi

được đề cập.

Chào bạn, bước cuối cùng tôi đã bỏ lỡ là thêm hướng dẫn này hoặc mục nhập văn bản này vào

giao thức hướng dẫn bổ sung.

Vì vậy, một lần nữa, tôi sẽ chạy hướng dẫn này và bạn có thể xác minh xem lời nhắc có đúng không

hay không.

Tid, tôi đợi vài giây trong khi phản hồi đang được tạo.

Sau vài giây, bạn đã có thể thấy kết quả.

Chúng tôi thấy bản dịch sang tiếng Pháp và điều quan trọng nhất là bây giờ

hành động đã được thêm vào nơi tôi đã hiển thị cho bạn các thẻ liên quan đến việc sử dụng truy vấn, xác nhận

rằng mọi thứ đang hoạt động chính xác.

Để làm điều này, tôi sử dụng thành phần có tên là nhắc nhở, cho phép tôi tạo các hướng dẫn phức tạp hơn

thậm chí có thể đến từ các thành phần khác nhau.

Bằng cách này, tôi thêm các tính năng hoặc mô tả vào lời nhắc để có được kết quả phức tạp hơn.