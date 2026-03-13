# Chương 8. Thiết lập hoạt động học tập tăng cường sâu của Super Mario Bros., Phiên bản video đã được dịch

---

Phần 8.3, thiết lập Super Mario Brothers.

Cùng với nhau, các mô hình thuận, nghịch và bộ mã hóa tạo thành mô-đun tò mò nội tại, ICM,

mà chúng ta sẽ thảo luận chi tiết sau trong chương này.

Các thành phần của ICM hoạt động cùng nhau với mục đích duy nhất là tạo ra giá trị nội tại

phần thưởng thúc đẩy sự tò mò ở đại lý.

ICM tạo ra tín hiệu khen thưởng nội tại mới dựa trên thông tin từ môi trường,

vì vậy nó độc lập với cách triển khai mô hình tác tử.

ICM có thể được sử dụng cho bất kỳ loại môi trường nào, nhưng nó sẽ hữu ích nhất khi có phần thưởng thưa thớt.

môi trường.

Chúng tôi có thể sử dụng bất kỳ cách triển khai mô hình tác nhân nào mà chúng tôi muốn, chẳng hạn như nhà phê bình diễn viên phân tán

mô hình được trình bày ở chương 5.

Trong chương này, chúng ta sẽ sử dụng mô hình Q-learning để giữ mọi thứ đơn giản và tập trung vào việc triển khai

ICM.

Chúng tôi sẽ sử dụng Super Mario Brothers làm giường thử nghiệm.

Super Mario Brothers không thực sự gặp phải vấn đề phần thưởng thưa thớt.

Việc triển khai môi trường cụ thể mà chúng tôi sẽ sử dụng mang lại phần thưởng một phần dựa trên

trong tiến trình tiếp theo của trò chơi, vì vậy các phần thưởng tích cực hầu như được cung cấp liên tục.

Tuy nhiên Super Mario Brothers vẫn là sự lựa chọn tuyệt vời để thử nghiệm ICM vì chúng ta có thể lựa chọn

để tắt môi trường bên ngoài được cung cấp, tín hiệu khen thưởng.

Chúng ta có thể thấy tác nhân khám phá môi trường tốt như thế nào chỉ dựa trên sự tò mò và

chúng ta có thể thấy phần thưởng bên ngoài và bên trong có mối tương quan tốt như thế nào.

Việc triển khai Super Mario Brothers mà chúng tôi sẽ sử dụng có 12 hành động riêng biệt có thể

được thực hiện tại mỗi bước thời gian, bao gồm lệnh cấm, không thao tác, hành động, bảng 8.1, danh sách

tất cả các hành động.

Anh em nhà Super Mario

Bạn có thể tự cài đặt Super Mario Brothers bằng PIP.

Xem mã này.

Sau khi cài đặt xong, bạn có thể kiểm tra môi trường.

Ví dụ: hãy thử chạy mã này trong sổ ghi chép Jupyter bằng cách đóng vai một tác nhân ngẫu nhiên và lấy

những hành động ngẫu nhiên

Để xem lại cách sử dụng OpenAI Jim, vui lòng tham khảo lại chương 4.

Trong danh sách sau đây, chúng tôi khởi tạo môi trường Super Mario Brothers và thử nghiệm

nó bằng cách thực hiện các hành động ngẫu nhiên.

Liệt kê 8.1, thiết lập môi trường Super Mario Brothers.

Nếu mọi việc suôn sẻ, một cửa sổ nhỏ sẽ bật lên hiển thị Super Mario Brothers,

nhưng nó sẽ thực hiện các hành động ngẫu nhiên và không đạt được bất kỳ tiến bộ nào thông qua

cấp độ.

Đến cuối chương này, bạn sẽ đào tạo được một nhân viên có thể đạt được tiến bộ nhất quán trong tương lai

và đã học cách tránh hoặc nhảy vào kẻ thù và nhảy qua chướng ngại vật.

Điều này chỉ sử dụng phần thưởng dựa trên sự tò mò nội tại.

Trong giao diện OpenAI Jim, môi trường được khởi tạo dưới dạng đối tượng lớp được gọi là

NV, và phương thức chính bạn cần sử dụng là hàm bước của nó với các đối số bên trong

phương pháp dấu ngoặc đơn.

Phương thức bước lấy một số nguyên biểu thị hành động sẽ được thực hiện.

Giống như tất cả các môi trường OpenAI Jim, môi trường này trả về trạng thái, phần thưởng, thành tích và thông tin

dữ liệu sau mỗi hành động được thực hiện.

Trạng thái là một mảng có nhiều kích thước, 240, 256, 3, biểu thị khung video RGB.

Phần thưởng được giới hạn trong khoảng từ âm 15 đến âm 15 và dựa trên mức độ tiến bộ về sau.

Biến done là một giá trị Boolean cho biết trò chơi đã kết thúc hay chưa.

Ví dụ, liệu Mario có chết hay không.

Biến thông tin là một từ điển Python có siêu dữ liệu được liệt kê trong Bảng 8.2.

Bảng 8.2.

Siêu dữ liệu được trả về sau mỗi hành động trong biến thông tin, nguồn tại liên kết này, Xem bảng

Hình.

Chúng ta sẽ chỉ cần sử dụng phím PoS gạch dưới X.

Ngoài việc lấy trạng thái sau khi gọi phương thức bước, bạn cũng có thể truy xuất

trạng thái tại bất kỳ thời điểm nào bằng cách gọi hàm kết xuất của môi trường của mảng gạch dưới RGB.

Về cơ bản đó là tất cả những gì bạn cần biết về môi trường để đào tạo một đại lý

để chơi nó.