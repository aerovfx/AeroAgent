# 008 Cấu trúc với con trỏ vi

---

Trong phần trước, chúng tôi đã thảo luận về cách chuyển đổi theo ngôn ngữ giá trị.

Điều đó có nghĩa là bất cứ khi nào chúng ta chuyển một giá trị vào một hàm, hãy sao chép giá trị đó và sau đó

bản sao được tạo sẵn cho mã hóa bên trong hàm.

Vì vậy, kết quả mạng cho điều đó có ý nghĩa là bất cứ khi nào chúng tôi chuyển Jim vào bản cập nhật tên chức năng, hãy tạo một

bản sao của cấu hình và bản sao sau đó được cung cấp cho bản cập nhật chức năng tên.

Và vì vậy, bất kể khi nào chúng tôi cập nhật người bên trong bản cập nhật tên, sự thay đổi không bao giờ được truyền lại cho

Jim.

Vì vậy, bây giờ chúng tôi hãy tìm cách chúng tôi sẽ sử dụng con trỏ để giải quyết vấn đề này ngay tại đây

và chắc chắn rằng bất cứ khi nào chúng tôi gọi bản cập nhật tên Jim, chúng tôi thực sự đang cập nhật Jim thay vì bản sao này

ngay tại đây.

Vì vậy, hãy nói về cách chúng tôi sẽ tiếp cận vấn đề này.

Vì vậy, chúng tôi sẽ tiếp cận điều này bằng cách cập nhật mã của chúng tôi trước đây và chúng tôi sẽ không nói về tính chính xác của những gì

chúng tôi đang làm.

Chúng tôi sẽ chỉ cập nhật mã của mình và chúng tôi sẽ đảm bảo rằng nó sẽ hoạt động theo cách mà chúng tôi mong đợi.

Nói cách khác, chúng tôi chắc chắn rằng sau khi chúng tôi gọi tên cập nhật ngay tại đây, tên của

Jim now or must be Jimmy.

Vì vậy, chúng tôi sẽ thực hiện các thay đổi đó và sau đó chúng tôi sẽ nói về những gì chúng tôi đã làm.

Vì vậy, chúng tôi sẽ viết mã trước và sau đó chúng tôi sẽ nói về những gì chúng tôi đã làm.

Vì vậy, hay thực hiện ngay bây giờ.

Thay đổi đầu tiên mà chúng tôi sẽ thực hiện ngay trên dòng tên Jim Update.

Vì vậy, trên dòng ngay phía trên này, chúng tôi sẽ viết ra Jim Pointer dấu hai chấm bằng dấu và.

Sau đó Jim ở ngay bên dưới nó mà chúng tôi gọi là bản cập nhật tên.

Chúng tôi sẽ đổi Jim ngay tại đây thành Jim Pointer.

Và hiện tại đã có thêm hai thay đổi nhanh chóng về chức năng cập nhật tên.

Chúng tôi sẽ xóa tên và loại người đã nhận được và chúng tôi sẽ thay thế

nó dùng con trỏ tới từng người và sau đó sẽ là ngôi sao.

Và cuối cùng trên P chấm tên đầu tiên ngay tại đây, chúng tôi sẽ xóa chữ P, hãy đảm bảo rằng bạn giữ

Khoảng thời gian ngay sau đó chúng ta sẽ đặt dấu ngoặc đơn và sau đó bên trong dấu ngoặc đơn, chúng ta sẽ nói con

trỏ sao với từng người.

Vì vậy, chúng tôi hãy lưu điều này ngay bây giờ.

Bây giờ, khi chúng tôi lưu nó, bạn có thể nhận thấy một thông báo cảnh báo màu xanh lá cây xuất hiện trên bản ở đây.

Điều đó hoàn toàn ổn định.

Chúng tôi sẽ bỏ qua điều đó ngay bây giờ.

Bây giờ, trước khi chúng ta nói một từ nào đó về điều này, hãy chạy mã của chúng ta và chỉ cần đảm bảo rằng nó đang hoạt động

theo cách chúng tôi mong đợi.

Vì vậy, tôi sẽ lại thiết bị đầu cuối của mình.

Tôi sẽ chạy, đi, chạy, chính, đi một lần nữa.

Và khi tôi làm như vậy, bạn sẽ nhận thấy rằng tên đầu tiên đã được cập nhật thành công thành công Jimmy, đây

chắc chắn là hành động mà chúng tôi có thể mong muốn.

Đã xong, bây giờ cuộc thảo luận về chính xác lý do tại sao mã này hoạt động ngay tại đây và tất cả các khoản toán

Cái mới này giống như thế nào, ký hiệu và dấu sao sẽ hơi dài một chút.

Vì vậy, chúng tôi sẽ tạm thời nghỉ ngơi ngay bây giờ, quay lại phần tiếp theo và chúng tôi sẽ nói về chính xác những gì đang xảy ra

ra đoạn mã này ngay tại đây.

Vì vậy, hãy nhanh chóng nghỉ ngơi và chúng tôi sẽ quay lại ngay với nó.