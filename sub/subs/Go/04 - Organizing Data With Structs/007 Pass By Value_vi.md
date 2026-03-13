# 007 Truyền theo giá trị vi

---

Trong phần trước, chúng tôi đã tìm cách xác định một hàm bằng cách sử dụng struct làm bộ thu.

Vì vậy, chúng tôi đã xác định chức năng và cập nhật tên chức năng, cả hai đều có người nhận

type user.

Và vì vậy, chúng tôi có thể gọi tên cập nhật Jim và Jim in chỉ vì Jim thuộc loại bình thường.

Sau đó, chúng tôi chạy bản cập nhật tên này và chúng tôi nhận thấy rằng nếu chúng tôi cố gắng gửi bản cập nhật tên của Jim ngay

tại đây và sau đó ở Jim ngay sau đó, có vẻ như bản cập nhật or không thực sự được lưu giữ.

Vì vậy, trong phần này, chúng tôi sẽ đi sâu vào vấn đề đó và cố gắng hiểu chính xác tại sao công việc cập nhật

tên của Jim không thực sự có hiệu lực trong ứng dụng của chúng ta.

Bây giờ, toàn bộ chủ đề này sẽ xoay quanh ý tưởng về các con trỏ đang hoạt động.

Nếu bạn đã quen với các con trỏ đang làm việc với C, C ++ hoặc bất kỳ loại ngôn ngữ nào khác, thì

Rất có thể bạn không thích con trỏ cho lắm, nhưng đừng lo lắng, con trỏ và đi tương đối đơn

đơn giản và thực tế không phải điều chỉnh tiền tệ nhất trên thế giới.

Vì vậy, chúng tôi bắt đầu và tìm hiểu chính xác những gì đang xảy ra.

Vì vậy, chúng tôi sẽ xem xét từng dòng mã của chúng tôi tại đây.

Nhưng trước khi thực hiện, tôi muốn cung cấp cho bạn bản cập nhật thông tin nhanh chóng về cách RAM hoặc cách bộ nhớ hoạt động trên máy, trên máy của bạn

tính toán của bạn ngay bây giờ.

Bây giờ, khi chúng tôi đang nói về Ram, tôi sẽ cung cấp cho bạn một loại máy bay phi khoa học định nghĩa.

Vì vậy, tôi sẽ chỉ cung cấp cho bạn một cái nhìn tổng thể về cách thức hoạt động của RAM, bởi vì

tôi muốn bạn suy nghĩ nhiều hơn về những gì Đang làm ngay bây giờ thay vì đi sâu 20 phút về cách Ram

active on your local.

Vì vậy, tất cả những gì tôi thực sự muốn bạn hiểu về Ram ngay bây giờ là bộ nhớ trên máy cục bộ

Bạn có thể coi đó là một loạt các sở thích nhỏ hoặc một loạt các khe cắm nhỏ hoặc một loạt các hộp nhỏ.

Mỗi hộp mực trong máy tính của bạn có thể lưu trữ một số dữ liệu và mỗi hộp nhỏ này

hoặc các vùng chứa giá trị nhỏ này có một số địa chỉ riêng biệt.

Và vì vậy, bất cứ khi nào chương trình của bạn nói, Ồ, tôi muốn truy xuất một số thông tin từ bộ nhớ của máy tính, nó

will look on it and find a address that, and then it get value from that.

Và vì vậy, mỗi hộp nhỏ ngay tại đây có thể chứa một lượng thông tin.

Và đó thực sự là tất cả những gì tôi muốn nói về RAM ngay bây giờ.

Chỉ cần tổng hợp nhanh chóng về cách thức hoạt động chính xác của nó.

Được chứ.

Vì vậy, bây giờ chúng tôi hãy phân tách chương trình của chúng tôi ra từng bước và suy nghĩ về cách chương trình chúng tôi đang hoạt động

RAM trên local của chúng ta.

Vì vậy, trước tiên chúng ta sẽ bắt đầu với dòng này, nơi chúng ta tạo một kiểu cấu trúc mới

và chỉ định nó cho Jim biến.

Vì vậy, khi chúng tôi làm điều này, khi chúng tôi tạo cấu trúc mới này của loại người sẽ tạo cấu trúc đó.

Sau đó, nó sẽ chuyển đến bộ nhớ cục bộ sang máy tính xách tay của chính chúng ta hoặc máy cục bộ của chúng ta và nó sẽ cố gắng

Tìm một số vùng chứa hoặc một số vị trí miễn phí và có khả năng nhận được một số dữ liệu.

Vì vậy, chúng tôi có thể tưởng tượng rằng hãy lấy cấu trúc này ngay tại đây, nó sẽ đi và tìm một số không gian hoặc vị trí nào

it to set the configstructure and after that no redirect data that to the vùng chứa kích thước nhỏ này ngay tại đây.

Và vì vậy, họ có thể tưởng tượng rằng Jim này có cấu trúc ngay tại đây hoặc người này đang ngồi ở địa chỉ 0001.

Và vì vậy, bất kể khi nào chúng ta nhìn vào biến thể, Jim, Jim đang trực tiếp vào vùng chứa nhỏ này ngay tại

đây.

Và vì vậy, nếu chúng tôi lấy được giá trị của Jim, chúng tôi sẽ luôn thấy giá trị chính xác này ngay tại đây.

Được chứ.

Vì vậy, với suy nghĩ đó, bây giờ chúng tôi nghĩ về điều gì sẽ xảy ra khi chúng tôi gọi tên cập nhật Jim bằng Jimmy.

Và tôi cũng muốn nghĩ ra một chút về bộ thu mà chúng tôi đã tạo ra chức năng cập nhật tên ngay lập tức

tại đây.

Vì vậy, chúng tôi vẫn có Jim ngay tại đây.

Đúng?

Jim vẫn ở tuổi 001 và cấu trúc đó vẫn giống nhau.

Bây giờ, đây là nơi mà mọi thứ trở nên thực sự, thực sự thú vị với cờ vây.

Lượt đi là những gì chúng tôi đề xuất như một giá trị vượt qua.

Ngôn ngữ ngôn ngữ truyền đạt giá trị có ý nghĩa là bất cứ khi nào chúng ta truyền giá trị nào vào một hàm, go sẽ lấy giá trị đó hoặc

get config that.

Nó sẽ sao chép tất cả dữ liệu trong cấu trúc và sau đó đặt nó vào một vùng chứa bất kỳ dữ liệu nào trong bộ nhớ

ta nhớ máy tính của chúng ta.

Vì vậy, khi chúng tôi chuyển Jim vào bản cập nhật chức năng tên này, Jim vẫn tồn tại dưới dạng cấu trúc này

với tên đầu tiên của Jim tại địa chỉ 0001 nhưng khi sao chép giá trị đó, nó không tìm thấy một số vùng chứa

một chỗ trống khác và không có bản sao nào đó trong vùng chứa đó và sau đó nó sẽ chạy mã bên trong bản cập nhật tên

với bộ thu P này vào bản sao đó.

Vì vậy, khi bạn và tôi sửa đổi trường tên trong hàm đó, khi chúng tôi chạy đoạn mã này ngay tại đây

cho biết tên sẽ là tên mới, chúng tôi sẽ không cập nhật ban cấu trúc cấu hình của

Jim.

Chúng tôi đang cập nhật.

Sao chép vừa phải cho chức năng gọi công cụ của chúng tôi.

Bây giờ, điều này nghe có vẻ đầu tiên, không có thể gây nhầm lẫn, điều này hoàn toàn ổn, hoàn toàn có thể

được mong đợi.

Và sau đó là số hai, nó có vẻ điên cuồng như sao trên thế giới lại làm điều này?

Tại sao lại tạo một bản sao khi nó chuyển dữ liệu này sang chức năng khác?

Chà, có rất nhiều lý do chính đáng cho điều đó, và chúng ta sẽ tìm hiểu về một số lý do sau đó

một khoảnh khắc.

Nhưng hiện tại, trước đây tôi muốn tập trung vào việc họ giải quyết vấn đề này như thế nào?

Tương tự như vậy, hãy loại bỏ bất kỳ thời điểm nào trong một chương trình của chúng tôi, chúng tôi chắc chắn sẽ muốn thực hiện

điều gì chính xác như thế này ngay tại đây.

Đúng.

Chúng tôi chắc chắn sẽ muốn xác định một hàm nhận một số đối số và sau đó cập nhật cấu hình

trúc mà hàm đang được chấp nhận như một bộ nhận.

Vì vậy, chúng tôi nghỉ ngơi nhanh chóng.

Chúng tôi sẽ quay lại phần tiếp theo và chúng tôi sẽ tìm ra cách chính xác mà chúng tôi sử dụng con trỏ

để giải quyết vấn đề này.

Vì vậy, hãy nhanh chóng nghỉ ngơi và tôi sẽ gặp bạn chỉ sau một phút.