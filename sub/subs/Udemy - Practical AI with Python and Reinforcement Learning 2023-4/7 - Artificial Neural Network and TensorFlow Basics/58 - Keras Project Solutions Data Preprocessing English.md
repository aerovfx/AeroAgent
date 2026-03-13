# 58 - Xử lý trước dữ liệu của Keras Project Solutions

---

Chào mừng mọi người quay trở lại và bài giảng này chúng ta sẽ thực hiện một số bước xử lý trước dữ liệu mà chúng ta đã có.

xử lý các giá trị còn thiếu và chuyển đổi bất kỳ giá trị phân loại nào, các cuộc gọi liên tục hoặc giả

các biến.

Bây giờ là lúc thực hiện phân tách thử nghiệm tàu ​​và chuẩn hóa dữ liệu sau đó.

Sau đó chúng ta có thể tạo mô hình.

Hãy bắt đầu.

Được rồi, chúng ta quay lại với cuốn sổ.

Bước tiếp theo là nhập phần tách thử nghiệm tàu ​​từ Saikat.

Tìm hiểu để chúng ta có thể làm điều đó chỉ bằng cách nói từ České tìm hiểu cách lựa chọn mô hình, tiếp tục và nhập

đào tạo để chia tay.

Và sau khi thực hiện xong, nhiệm vụ tiếp theo là bỏ cột trạng thái khoản vay mà chúng ta đã tạo trước đó, vì

về cơ bản nó là một bản sao của cột hoàn trả khoản vay và chúng tôi sẽ sử dụng cột hoàn trả khoản vay vì nó

đã có số không và số một.

Vì vậy chúng ta sẽ làm như sau.

Sẽ nói D.F. bằng với giọt nước.

Và sau đó nói trạng thái gạch dưới đơn độc.

Và sau đó nói trục bằng một, được chứ?

Sau đó, chúng ta sẽ đặt biến X và Y thành giá trị của đối tượng địa lý và nhãn.

Vì vậy, chúng ta có thể làm điều đó bằng cách nói X bằng DF, tiếp tục và thả khoản vay được hoàn trả dọc theo trục bằng nhau

đến một.

Và tôi chỉ muốn các giá trị ở đó.

Và sau đó tại sao sẽ bằng D.F. khoản vay được hoàn trả?

Và sau đó lấy những giá trị đó và chạy nó.

Được rồi, bây giờ, bước tiếp theo này hoàn toàn không bắt buộc, nó thực sự phụ thuộc vào cách bạn chạy bước này.

Vì vậy, nếu bạn không chạy ứng dụng này trên nền tảng đám mây của Google mà thay vào đó bạn đang chạy ứng dụng này cục bộ,

nếu bạn có RAM thấp hơn hoặc bạn không sử dụng GPU, bạn có thể tùy ý tiết kiệm một chút trên

thời gian đào tạo, chỉ cần lấy mẫu từ toàn bộ tập dữ liệu này.

Bây giờ, hãy nhớ rằng, nếu bạn chỉ lấy một mẫu, bạn có thể sẽ không thực hiện tốt vì bạn không

thấy có nhiều ví dụ đúng.

Vì vậy, có những phương pháp ở đây để bạn lấy mẫu.

Và đó là bạn có thể nói mẫu ADV và bạn có thể cung cấp mẫu mà bạn muốn lấy.

Có thể bạn chỉ muốn lấy 10 phần trăm hoặc 20 phần trăm dữ liệu và đặt dữ liệu đó làm khung dữ liệu của mình.

Vì tôi đang chạy ứng dụng này trên GPU nên tôi sẽ tiếp tục và giữ toàn bộ khung dữ liệu.

Nhưng hãy nhớ rằng, nếu bạn chỉ theo dõi nhưng không thực sự cần phải dành toàn bộ thời gian

với quá trình đào tạo, bạn có thể chỉ lấy một mẫu dữ liệu.

Tiếp theo, chúng tôi sẽ thực hiện phân chia thử nghiệm đoàn tàu để có thể nói đơn giản rằng đoàn tàu đã phân tách.

Chúng ta sẽ tiếp tục và sao chép cái này từ chuỗi dock.

Vậy hãy cuộn xuống đây.

Cho đến khi bạn thấy kết quả này, hãy sao chép và dán nó vào.

Và chúng ta sẽ tiếp tục đặt kích thước thử nghiệm của mình thành 0 phẩy 2 và để đảm bảo bạn nhận được mức chia tương tự, tôi

làm, hãy tiếp tục và đặt trạng thái ngẫu nhiên của bạn thành giá trị tùy ý là một không một.

Chúng tôi điều hành nó.

Và bây giờ chúng ta đã hoàn tất quá trình phân tách, chúng ta có thể chuẩn hóa dữ liệu của mình.

Chúng ta sẽ tiếp tục và sử dụng chúng ở dạng vô hướng tối đa mà chúng ta đã sử dụng trong suốt khóa học.

Chúng tôi sẽ nói từ quá trình nhập tiền xử lý Escalon.

Vô hướng tối thiểu tối đa.

Tạo một phiên bản của Mad Max Gahler đó rồi tiếp tục chuyển đổi dữ liệu của bạn.

Vì vậy, chúng ta sẽ nói chuỗi X bằng vô hướng và chúng ta sẽ chỉ gọi nó là phép biến đổi trong một bước.

Vào ngày đào tạo hiện tại của chúng tôi chạy dữ liệu đó và sau đó là tập dữ liệu thử nghiệm, chúng tôi không muốn phù hợp với điều đó.

Chúng tôi chỉ muốn chuyển đổi để ngăn chặn bất kỳ rò rỉ dữ liệu nào từ tập thử nghiệm của mình.

Được rồi, anh ấy đã chuẩn hóa dữ liệu và tiếp theo, chúng ta sẽ tiếp tục tạo mô hình để xem

bạn trong bài giảng tiếp theo nơi chúng tôi tập trung vào việc tạo mô hình.

Tôi sẽ gặp bạn ở đó.