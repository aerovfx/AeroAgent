# 03 - Đào tạo mô hình deep learning bằng Python

---

- [Người hướng dẫn] Trong video này,

bạn sẽ học cách biên soạn và đào tạo một mô hình học sâu

bằng Python bằng Keras.

Tôi sẽ viết mã hoàn chỉnh vào tệp 04_03e.

Bạn có thể làm theo bằng cách hoàn thành các ô mã trống

trong tệp 04_03b.

Lưu ý rằng đây là video thứ ba trong chuỗi ba video

dạy bạn cách xây dựng mô hình deep learning

bằng Python bằng Keras.

Nếu bạn chưa làm như vậy, hãy xem hai video trước

để được giải thích chi tiết về mã trước đó.

Trước khi chúng ta bắt đầu,

hãy chạy đoạn mã chúng ta đã tạo trong những video đó

để môi trường của chúng ta tăng tốc.

Vì vậy, ở đây, chúng ta sẽ xuống đây như chúng ta đã làm trước đây

và chạy mã trước đó.

Vì vậy, hãy đợi cho đến khi nó hoàn thành.

Tôi sẽ cuộn lên một chút

để đảm bảo rằng mã được thực hiện.

Được rồi, bây giờ chúng ta hãy quay trở lại nơi chúng ta đang ở.

Vì vậy, bây giờ chúng ta đã xác định được kiến trúc của mô hình,

và chúng tôi đã làm điều đó trong video trước,

bước tiếp theo là chuẩn bị cho việc đào tạo.

Điều này liên quan đến việc biên dịch mô hình

bằng cách chỉ định hàm mất mát, trình tối ưu hóa,

và các thước đo đánh giá.

Lần này, trình tối ưu hóa chúng ta sẽ sử dụng,

chúng ta sẽ sử dụng adam.

Đối với số liệu tổn thất,

chúng ta sẽ sử dụng categorical_crossentropy.

Và đối với các số liệu của chúng tôi, chúng tôi sẽ sử dụng độ chính xác.

Vì vậy, hãy tiếp tục xác định điều đó và chạy mã của chúng ta.

Vì vậy chúng ta sẽ biên dịch mô hình.

Để huấn luyện mô hình, chúng ta gọi là phương pháp phù hợp, phải không?

Chỉ định dữ liệu đào tạo,

nhãn cho dữ liệu huấn luyện, số lượng kỷ nguyên,

kích thước lô mà chúng ta sẽ đặt là 128,

và mức phân chia xác thực là 0,1,

điều đó có nghĩa là chúng ta nên sử dụng 10%

dữ liệu của chúng tôi để xác thực và 90% cho việc đào tạo.

Vì vậy, hãy tiếp tục và chạy nó.

Vậy mô hình bây giờ đang huấn luyện dựa trên dữ liệu, được chứ?

Vậy là mô hình đã được huấn luyện xong.

Đối tượng lịch sử, đó là những gì chúng tôi đã chỉ định ở đây

là đầu ra mà mô hình của chúng tôi trả về,

chứa các số liệu về độ chính xác đào tạo và xác nhận

cho từng thời đại.

Vì vậy, nếu chúng ta vẽ sơ đồ này, nó cho chúng ta cảm giác

về hiệu suất của mô hình qua các thời kỳ.

Vì vậy điều chúng ta sắp làm ở đây là thực sự hình dung

hiệu suất của mô hình qua các thời đại,

chỉ để xem mọi thứ tiến triển thế nào

trong mỗi thời đại đó.

Vì vậy, hãy tiếp tục và chạy các số liệu chính xác

để xác nhận và đào tạo để xem nó trông như thế nào.

Và vì vậy, chúng ta có thể thấy chính xác những gì đang xảy ra ở đây, phải không?

Vì vậy, độ chính xác khi huấn luyện bắt đầu thấp hơn một chút,

nhưng sau đó tăng lên và tăng dần lên một chút,

và sau đó bắt đầu ổn định một chút.

Và chúng tôi thấy độ chính xác của quá trình xác thực vẫn được duy trì

hơi giống một chút.

Nó tăng lên một chút về phía

khi chúng tôi tiến triển chúng với nhiều kỷ nguyên hơn.

Vì vậy, chúng ta có thể làm điều tương tự với sự mất mát.

Vì vậy, chúng ta có thể làm điều tương tự ở đây với sự mất mát

từ cùng một đối tượng lịch sử.

Vì vậy, thay vì chỉ định độ chính xác,

chúng ta sẽ chỉ định mất mát và mất xác thực.

Vậy chúng ta hãy tiếp tục và xem chuyện gì đã xảy ra ở đó, được chứ?

Và lần này chúng ta thấy một mô hình tương tự, phải không?

Vì vậy, sự mất mát xác nhận dần dần giảm xuống

và bắt đầu ổn định một chút,

xin lỗi, mất tập luyện,

nhưng bản thân việc mất xác nhận vẫn tương tự một chút.

Vì vậy chúng ta sẽ nói thêm một chút về điều này

khi chúng ta tiến bộ trong phần sau của khóa học.

Nhưng điều này gần như mang lại cho chúng ta cảm giác tốt

về cách cải thiện hiệu suất của mô hình của chúng tôi

khi chúng ta tiến triển theo các kỷ nguyên.

Bây giờ chúng ta đã huấn luyện xong một mô hình, chúng ta có thể lưu nó,

để chúng ta có thể sử dụng nó cho những đánh giá khác

và áp dụng vào các vấn đề khác sau này.

Vì vậy, các đối tượng mô hình mà chúng ta đã tạo có một phương thức lưu.

Và một khi chúng ta gọi điều đó,

chúng ta có thể chỉ định tên cho mô hình của mình trong phương thức lưu,

để chúng tôi có thể lưu nó vào hệ thống tệp cục bộ của mình.

Được rồi, trong ví dụ này ở đây,

Tôi có thể nói model.save,

và tôi chỉ định tên của chính mô hình đó,

Tôi sẽ nói đó là mô hình nnet_.

Và tôi phải sử dụng tiện ích mở rộng Keras cho mô hình.

Và một khi tôi lưu nó, tôi cũng có thể tải mô hình này sau

bằng cách nói keras.model.load_model,

và sau đó chỉ định tên và đường dẫn

của chính mô hình đó.

Vì vậy, bây giờ chúng ta có thể tải mô hình của mình vào môi trường

mà không cần phải đào tạo lại mô hình.

Được rồi, chúc mừng nhé.

Nếu bạn đã theo dõi

qua cả ba video ở đây,

điều đó có nghĩa là sử dụng Python,

bạn đã nhập và xử lý trước thành công

một tập dữ liệu học sâu mẫu.

Điều đó cũng có nghĩa là bạn đã xác định, biên dịch thành công,

và đào tạo mô hình deep learning bằng Python bằng Keras.