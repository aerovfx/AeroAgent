# 006 Cách sử dụng các phương thức setstate & getstate trên mô-đun ngẫu nhiên

---

Xin chào tất cả mọi người.

Chào mừng trở lại.

Trong bài học này, chúng ta sẽ xem cách sử dụng các phương thức Getstate và Setstate trong mô-đun ngẫu nhiên.

Mô-đun ngẫu nhiên cung cấp hai chức năng quan trọng.

Nhận trạng thái và đặt trạng thái để nắm bắt các trình tạo ngẫu nhiên.

Trạng thái nội bộ hiện tại.

Bằng cách sử dụng các hàm này, chúng ta có thể tạo ra các số hoặc chuỗi dữ liệu ngẫu nhiên giống nhau.

Phương thức hoặc hàm Getstate trả về một đối tượng tuple bằng cách nắm bắt trạng thái bên trong hiện tại của

máy phát ngẫu nhiên.

Sau đó, chúng ta có thể chuyển trạng thái này sang phương thức Setstate để khôi phục trạng thái này như trạng thái hiện tại.

Sau khi sử dụng trạng thái bên trong phương thức trạng thái đã đặt.

Hàm này khôi phục trạng thái bên trong của bộ tạo ngẫu nhiên về đối tượng trạng thái được truyền cho nó.

Có nghĩa là bằng cách thay đổi trạng thái về trạng thái trước đó.

Chúng ta có thể nhận được dữ liệu ngẫu nhiên giống nhau.

Ví dụ: nếu muốn lấy đi lấy lại cùng một mẫu, chúng ta có thể sử dụng hai hàm này.

Chúng ta hãy xem thực tế.

Cách sử dụng phương thức Getstate và Setstate.

Trước tiên chúng ta hãy nhập mô-đun ngẫu nhiên.

Và sau đó một danh sách các giá trị có nghĩa là một chuỗi dữ liệu.

Và sử dụng phương pháp mẫu.

Để lấy mẫu từ danh sách các số.

Bởi vì phương pháp mẫu này.

Sử dụng tổng thể và trả về k phần tử ngẫu nhiên duy nhất từ ​​tổng thể.

Là một danh sách phụ.

Vì vậy, ở đây chúng tôi đã có được bản tổng hợp mẫu từ quần thể chính có K.

Đối với phương tiện cho các phần tử trong quần thể mẫu này.

Bây giờ, bước thứ hai là trạng thái hiện tại là 160, 110 và 30.

Nhưng để lưu trữ trạng thái hiện tại, chúng ta phải sử dụng phương thức get state.

Chúng ta hãy sử dụng phương thức Getstate phản lực ngẫu nhiên để lấy trạng thái hiện tại và lưu trữ nó dưới tên State.

Chúng ta đã lưu trữ thành công trạng thái.

Vì vậy, đây là nhà nước.

Nó có.

Tuple với kích thước ba.

Một là ba và một là.

Bộ giá trị.

Và nó tiếp tục.

Vì vậy, nó chỉ hiển thị bộ dữ liệu thứ hai này.

Và ở đây chúng ta đang có cái thứ ba.

Được rồi.

Giá trị thứ ba.

Bây giờ hãy để chúng tôi.

Sử dụng trạng thái này bên trong trạng thái đã đặt.

Ở bước ba, hãy đặt trạng thái hiện tại trước khi in lại cùng một mẫu.

Hãy để chúng tôi chạy mã này.

Trạng thái đặt dấu chấm ngẫu nhiên.

Bên trong đó chúng ta phải vượt qua trạng thái.

Như vậy chúng ta đã lưu trữ thành công trạng thái và chúng ta đã đặt trạng thái trước đó là trạng thái hiện tại.

Trạng thái làm việc.

Bây giờ chúng ta hãy sử dụng phương pháp mẫu.

Trên mô-đun ngẫu nhiên này.

Cùng một dân số và có cùng quy mô.

Chúng ta có nhóm 2160 và 100.

Chúng ta hãy sử dụng trạng thái tập hợp dấu chấm ngẫu nhiên và sau đó lại ở trong trạng thái đó.

ĐẾN.

Đặt trạng thái làm việc hiện tại.

Có nghĩa là trạng thái trước đó là trạng thái làm việc hiện tại.

Như vậy chúng ta đã thiết lập trạng thái trước đó làm trạng thái làm việc hiện tại.

Và chạy mẫu.

Mẫu chấm ngẫu nhiên.

Một lần nữa.

Chúng ta có 21, 60, 40 và một trăm.

Nhìn vào đây.

Sau khi sử dụng phương pháp trạng thái tập hợp dấu chấm ngẫu nhiên.

Từ đây trở đi, đối với mẫu này, mẫu ngẫu nhiên chúng ta có 21, 60, 40 và 100 và.

Sau khi sử dụng Setstate.

Một lần nữa, chúng tôi lại nhận được mẫu ngẫu nhiên tương tự.

Bây giờ hãy để chúng tôi.

Cố gắng in cùng một mẫu mà không sử dụng hàm Random.

Trạng thái đặt dấu chấm.

Chúng tôi có các mẫu khác nhau.

Hãy để chúng tôi chạy lại điều này một lần nữa.

Hãy để chúng tôi có được trạng thái ngẫu nhiên.

Chúng tôi có.

Tưởng trạng thái ngẫu nhiên.

Hãy để chúng tôi lưu trữ trạng thái ngẫu nhiên này.

Chúng tôi đã lưu trữ nó.

Chúng ta hãy thử lấy mẫu từ dân số.

Chúng tôi có 3010.

100, 150.

Chúng ta hãy nhớ lại.

Trạng thái trước đó như trạng thái hiện tại.

Sử dụng phương pháp trạng thái thiết lập, chúng ta đã gọi lại trạng thái trước đó là 3010 101 50.

Nặng nề.

Bây giờ chúng ta hãy chạy lại phương pháp lấy mẫu ngẫu nhiên này một lần nữa.

Vì vậy bây giờ chúng ta có thể thấy chúng ta có 3201 50.

Bây giờ chúng ta hãy sử dụng ngẫu nhiên này.

Điều đó chạy thẳng vào đây để chứng minh cách nó tạo ra sự ngẫu nhiên tương tự.

Dân số.

Chúng ta hãy chạy trạng thái chấm ngẫu nhiên này trước khi chạy mẫu chấm ngẫu nhiên này.

Bây giờ nó phải tạo ra cùng một mẫu ngẫu nhiên là 3101 50.

Vì vậy, chúng tôi có cùng một mẫu.

Đây là bằng chứng của chúng tôi.

Vì vậy mỗi lần chúng ta lấy mẫu, quần thể mẫu ngẫu nhiên từ quần thể chính, chúng ta có

để sử dụng ngẫu nhiên.

Nhưng đã chạy phương thức Setstate.

Đầu tiên là trạng thái lấy dấu chấm ngẫu nhiên và sau đó là trạng thái đặt dấu chấm ngẫu nhiên.

Và sau đó là trạng thái trước đó.

Và sau đó chúng ta phải sử dụng.

Phương pháp lấy mẫu để lấy quần thể mẫu không chỉ cho quần thể mẫu.

Chúng ta có thể áp dụng điều này.

Đặt phương thức trạng thái cho bất kỳ.

Chức năng ngẫu nhiên như thế nào.

Randint.

Randrange.

Lựa chọn lựa chọn.

Nhà nguyện.

vân vân về bất kỳ hàm ngẫu nhiên nào.

Nhưng trước đây.

Chúng tôi sử dụng.

Chức năng ngẫu nhiên.

Chúng ta phải sử dụng phương pháp trạng thái thiết lập.

Sau đó, chỉ có chúng tôi sẽ nhận được trước đó.

Kết quả thực hiện.

Nếu không thì không.

Điều đó chúng ta đã thấy ở đây một cách thực tế.

Vì vậy, đây là cách chúng ta có thể sử dụng các phương thức getstate và Setstate để nhận được các giá trị hoặc chuỗi ngẫu nhiên giống nhau

dữ liệu từ mô-đun ngẫu nhiên.

Cảm ơn đã xem bài học này.

Hẹn gặp lại các bạn trong bài học tiếp theo.