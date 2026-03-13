# 001 Non-Volatile Storage (NVS) Implementation Overview en

---

Xin chào và chào mừng bạn đến với phần triển khai lưu trữ bất biến trong phần này, tôi sẽ trình bày ngắn gọn

tổng quan về SPF trong vs thư viện và cách chúng tôi sẽ sử dụng nó để lưu và tải thông tin đăng nhập wi fi.

Vì vậy, trước tiên, chúng ta hãy xem việc thực hiện.

Sau khi SB 32 kết nối thành công với điểm truy cập thông qua trang Web, SSA, ID và mật khẩu

được sử dụng để kết nối sẽ được lưu vào thịt và khi khởi động.

SB 32 sẽ kiểm tra flash xem có thông tin xác thực nào đã lưu không và nếu có, chúng sẽ được sử dụng để

cố gắng kết nối ngay lập tức.

Đây là một thiết lập rất phổ biến trong các ứng dụng DeFi.

Ngoài ra khi khởi động.

Nếu sau khi đạt đến mức truy xuất kết nối Max và không thể thiết lập nỗ lực kết nối.

Chúng tôi sẽ xóa flash để những thông tin đăng nhập đó sẽ không được sử dụng để kết nối nữa.

Nếu nút ngắt kết nối trên trang Web được sử dụng để ngắt kết nối, thông tin xác thực cũng sẽ bị xóa

từ thịt trong trường hợp này là tốt.

Và khi bạn có ý tưởng thiết lập máy trạng thái và ứng dụng Wi-Fi để những hành động này

có thể được xử lý, bạn sẽ có thể tùy chỉnh hoặc điều chỉnh ứng dụng theo nhu cầu của mình.

Được rồi, chúng ta hãy xem xét một số API từ thư viện nghịch đảo ấn tượng và

làm thế nào chúng ta có thể sử dụng chúng.

Được rồi, đây là liên kết đến tài liệu ấn tượng về thư viện và API lưu trữ bất biến

tham khảo.

Tôi khuyên bạn nên tự mình đọc ở đây và ít nhất hãy duyệt qua phần giới thiệu cơ bản

khóa và giá trị lưu trữ trong phần không gian tên.

Bạn cũng có thể tìm thấy các ví dụ và thông tin về các tính năng khác mà chúng tôi sẽ không sử dụng trong khóa học này.

Nói chung, các thành phần NCVHS lưu và tải dữ liệu từ bộ lưu trữ được bảo toàn giữa các lần khởi động để bạn

có thể tắt thiết bị hoặc nếu nó mất nguồn.

Dữ liệu bạn đã lưu trữ sẽ vẫn ở đó để truy xuất khi khởi động lại.

Trong tài liệu có lưu ý rằng đầu tư bằng cách sử dụng khung phát triển ấn tượng là hoạt động tốt nhất

để lưu trữ các giá trị nhỏ, ví dụ: Thông tin xác thực Wi-Fi trong trường hợp của chúng tôi.

Và về khóa và giá trị, envious hoạt động trên các cặp giá trị khóa, khóa hoặc chuỗi và giá trị ASCII

là các loại, ví dụ: loại số nguyên, chuỗi và dữ liệu nhị phân byte có độ dài thay đổi, còn được gọi là

như những đốm màu.

Và về các không gian tên, chúng tôi gán từng cặp giá trị khóa cho một không gian tên và chúng tôi chỉ định không gian tên này

chẳng hạn như khi sử dụng một số API nghịch đảo nhất định và ngược lại.

Được rồi, chúng ta hãy xem một số chi tiết cụ thể hơn về việc lưu và truy xuất thông tin xác thực chuyến bay màu trắng

để bắt đầu với việc lưu thông tin đăng nhập.

Chúng ta cần mở vùng lưu trữ với không gian tên đã cho.

Chúng ta sẽ gọi PNB là open và chỉ định tên không gian tên.

Mở ở chế độ đọc ghi trong trường hợp của chúng tôi và chuyển tay cầm sẽ được sử dụng cho các cuộc gọi tiếp theo để kết thúc thông qua bộ

và đầu tư các chức năng cam kết để đặt SSA, ID và mật khẩu cũng như cho chức năng mở của Hải quân.

Tham số đầu tiên được lấy là không gian tên, sau đó là chế độ đáng ghen tị, đọc, viết hoặc đầu tư,

chỉ đọc và tham số thứ ba là phần điều khiển.

Và nếu thành công thì mã trả về bằng 0.

Sau đó, chúng tôi sẽ đặt giá trị nhị phân có độ dài thay đổi cho xã hội và mật khẩu bằng cách sử dụng blub đã đặt của Nvidia,

lấy phần xử lý thu được từ hàm mở đáng ghen tị.

Lưu ý rằng chúng ta không thể sử dụng chức năng cài đặt nếu tay cầm đã được mở và ở chế độ chỉ đọc.

Được rồi, vậy thì tên khóa, chẳng hạn, chúng ta sẽ nói tự sát trong dấu ngoặc kép, sau đó là tên tiếp theo

tham số là giá trị thực tế cần đặt, là ID và mật khẩu tự sát, sau đó chúng tôi sẽ chỉ định

chiều dài.

Sau khi thiết lập các giá trị, chúng ta cần ghi các thay đổi vào bộ lưu trữ cố định bằng cách sử dụng cam kết NCVHS,

lấy phần điều khiển làm tham số duy nhất và để nhận thông tin xác thực khi khởi động, cũng sẽ

cần phải gọi và cởi mở.

Và sau đó, trong trường hợp của chúng ta, chúng ta sẽ gọi bill get blub, nó sẽ xử lý tên khóa mà chúng ta đã có

được sử dụng trước đó khi lưu và giá trị sẽ phải phân bổ động bộ nhớ cho và

kích thước hoặc chiều dài là tốt.

Khi chúng tôi cần xóa thông tin xác thực, sẽ lại mở vùng lưu trữ bằng cách sử dụng tính năng mở đọc ghi của NGV

thì chúng ta sẽ xóa các cặp giá trị khóa bằng cách sử dụng ghen tị, kết quả là nó chỉ chiếm phần điều khiển và

sau khi đua, sẽ cam kết các thay đổi đối với NPS bằng cam kết NCVHS.

Vì vậy, đó là tất cả những gì chúng ta cần trình bày bây giờ.

Hãy giải mã.