# 001 Tổng quan dự án vi

---

Bây giờ chúng tôi đã hiểu rõ hơn nhiều về những điều cơ bản khi chuyển đổi.

Vì vậy, một số ý tưởng đằng sau các gói và lệnh nhập, và không, chúng ta sẽ chuyển sang

dự án thực tế đầu tiên của chúng ta.

Vì vậy, dự án của chúng tôi mà chúng tôi sẽ thực hiện sẽ là một gói mô phỏng

xung quanh một bộ bài chơi.

Và vì vậy khi tôi nói chơi bài, tôi đang nói cụ thể về cùng một loại bài

mà chúng tôi sẽ chơi blackjack hoặc gin rummy hoặc chơi cá hoặc poker.

Vì vậy, những thứ như quân át chủ bài, hai trái tim, ba viên kim cương, v.v.

Bây giờ gói mà chúng tôi tạo sẽ có một số chức năng khác nhau trong

nó mà chúng tôi sẽ tạo để mô phỏng việc quay bằng một bộ bài.

Vì vậy, họ hãy thử xem xét một số chức năng khác nhau và mục tiêu của họ.

Chức năng đầu tiên mà chúng tôi thực hiện sẽ là một thứ được gọi là Bộ bài mới.

Bất cứ khi nào chúng tôi gọi điều này, nó sẽ tạo ra một bộ bài chơi mới mà chúng tôi sẽ

Ý tưởng về cơ sở tương tự như một chuỗi hoặc một danh sách các chuỗi trong đó mỗi phần tử trong mảng này sẽ

đại diện cho một thẻ chơi duy nhất.

Tất nhiên, hiện tại chúng tôi chưa nói về mảng hoặc chuỗi hoặc bất kỳ thứ gì tương tự với Go, bởi vì

vì vậy chúng tôi chắc chắn sẽ phải thực hiện một số công việc nhất định ở đây ngay với chức năng đầu tiên này.

Khi chúng tôi có khả năng tạo một bộ bài mới, tôi muốn có khả năng đưa ra danh sách tất cả các bài đó

quân bài bên trong thẻ.

Tôi muốn có khả năng trộn tất cả các quân bài bên trong nó và tôi cũng muốn có khả năng xử lý

lý do một tay chơi bài ra khỏi bộ bài.

Vì vậy, đồng ý ngay tại đây, hãy tưởng tượng rằng nếu chúng ta tạo ra một bộ bài mới và có 52 lá

Bên trong, nếu sau đó tôi giải quyết được vấn đề đó, hãy giả sử tôi chia ra năm lá chơi.

Sau đó, tôi mong đợi sẽ có một danh sách các thẻ chơi bao gồm thẻ năm và sau đó là 47 thẻ còn lại

mà tôi đã chia sẻ.

Cuối cùng, tôi muốn tìm cách chúng tôi có thể lấy một bộ bài và lưu nó vào một tệp trên ổ cứng cục bộ của chúng tôi.

Và sau đó tìm một tệp hoặc tải một bộ bài mà chúng tôi đã lưu trước đó vào ổ cứng của mình.

Vì vậy, chất thực sự là ghi thông tin và lấy thông tin từ ổ cứng.

Vì vậy, đây chắc chắn sẽ là một dự án khá thú vị mà chúng ta sẽ bắt tay vào

thực hiện và chúng ta sẽ học được nhiều điều hơn nữa về cách viết, viết mã và các mẫu thiết kế phổ biến.

Vì vậy, chúng tôi nghỉ ngơi nhanh chóng.

Khi quay lại phần tiếp theo, chúng tôi sẽ tạo một gói mới.

Chúng tôi sẽ tạo một thư mục mới để chứa gói mới của chúng tôi, tôi nên nói, để tập hợp tất cả mã hóa

cho dự án của thẻ này.

Vì vậy, hãy nhanh chóng nghỉ ngơi và chúng tôi sẽ bắt đầu chỉ trong giây lát.