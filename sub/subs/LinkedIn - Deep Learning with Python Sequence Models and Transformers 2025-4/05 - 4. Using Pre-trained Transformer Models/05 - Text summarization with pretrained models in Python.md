# 05 - Tóm tắt văn bản bằng các mô hình được đào tạo trước trong Python

---

- [Người hướng dẫn] Trong video này,

chúng ta sẽ sử dụng một mô hình được đào tạo trước

để tóm tắt văn bản.

Có hai cách tiếp cận chính để tóm tắt văn bản.

Đầu tiên là tóm tắt khai thác,

trong đó lựa chọn và kết hợp các câu quan trọng

từ văn bản gốc.

Và thứ hai là tóm tắt trừu tượng,

tạo ra các câu mới nắm bắt được ý chính

một cách tự nhiên và mạch lạc hơn.

Trong hướng dẫn này, chúng ta sẽ sử dụng phương pháp đầu tiên,

đó là tóm tắt khai thác.

Hãy bắt đầu bằng cách chọn kernel,

sau đó chúng tôi chạy đoạn mã này ở đây

để giảm thiểu tính dài dòng trong nhật ký của chúng tôi.

Vì vậy, bây giờ chúng ta đã sẵn sàng khởi tạo một quy trình

để tóm tắt văn bản.

Vì vậy, ở đây, chúng tôi nhập hàm đường ống

từ gói máy biến áp,

sau đó chúng tôi khởi tạo một quy trình có tên là trình tóm tắt.

Chúng tôi gọi nó là tóm tắt.

Và trong chức năng đường ống,

chúng tôi đã chỉ định một nhiệm vụ là tóm tắt.

Vì vậy, hãy tiếp tục và chạy nó.

Khi đường ống được khởi tạo xong,

điều tiếp theo chúng ta sẽ làm ở đây, như bạn có thể thấy,

là chúng ta sẽ chuyển cho nó một đoạn văn bản khá dài

để xem chính xác nó giải quyết vấn đề đó như thế nào.

Ý tưởng ở đây là để xem liệu nó có thể trích xuất được không,

một lần nữa, chúng tôi đang sử dụng phương pháp khai thác,

một tập hợp con của văn bản đó cung cấp cho chúng ta một khái niệm chung

về nội dung của văn bản.

Vì vậy ở đây chúng ta sẽ vượt qua

thông qua đoạn văn bản khá quan trọng này về AI,

và chúng tôi sẽ gọi trước và gọi đến quy trình tóm tắt,

mà chúng ta vừa khởi tạo,

và kết quả, chúng ta sẽ gọi là tóm tắt.

Vì vậy, trong quy trình tóm tắt,

chúng ta sẽ chỉ định một vài điều.

Một là văn bản mà chúng tôi chuyển đến nó.

Chúng tôi sẽ chỉ định độ dài tối đa

của bản tóm tắt mà chúng ta muốn, độ dài tối thiểu.

Chúng ta cũng sẽ nói do_sample,

điều đó có nghĩa là chúng tôi muốn giới thiệu một số tính ngẫu nhiên

đến quá trình,

và chúng tôi sẽ chỉ định trong khi nó đang ngẫu nhiên hóa,

sử dụng mã thông báo top_k và sau đó là tỷ lệ phần trăm

cho những giá trị hàng đầu mà nó muốn giới thiệu

khi ngẫu nhiên hóa bản tóm tắt.

Vì vậy, khi chúng tôi chỉ định những đối số này,

bây giờ chúng ta có thể chạy cái này và sau đó xuất kết quả.

Hãy để chúng tôi xem những gì chúng tôi nhận được ở đây. Vì vậy, hãy chạy nó ở đây.

Điều này cung cấp cho chúng tôi một số thông báo cảnh báo về việc sử dụng CPU

trái ngược với GPU, điều đó cũng ổn.

Không có vấn đề gì ở đây.

Rất nhanh thôi, chúng ta sẽ thấy bản tóm tắt

mà hệ thống mô hình của chúng tôi sẽ cung cấp cho chúng tôi.

Vì vậy, chúng tôi thấy bản tóm tắt ở đây.

Nó có thể không rõ ràng lắm với bạn,

nhưng đây là bản tóm tắt ở đây.

Bản tóm tắt nói,

"Tự động hóa được hỗ trợ bởi AI đang định hình lại lực lượng lao động

bằng cách hợp lý hóa các hoạt động và giảm nhu cầu

để can thiệp thủ công", v.v.

Vì vậy, đó là một bản tóm tắt khai thác.

Vì vậy, nó đã xác định được khá nhiều phần chính của văn bản gốc

điều đó đã cho chúng tôi một ý tưởng chung

về nội dung tổng thể của văn bản.

Vì vậy, trong ví dụ này,

chúng tôi đã sử dụng chức năng đường ống

và chúng tôi đã không chỉ định một mô hình.

Vậy những gì Ôm Mặt đã làm ở phía sau,

chức năng đường dẫn mô hình đã thực hiện trong phần phụ trợ đã được chỉ định

hoặc chọn mô hình riêng của mình.

Vì vậy, chúng ta cũng có thể chỉ định một mô hình do chúng ta lựa chọn

nếu chúng tôi muốn.

Vì vậy, trong ví dụ này,

chúng ta sẽ sử dụng mô hình bart-large-cnn.

Vì vậy chúng ta sẽ chỉ định mô hình này.

Đây là mô hình mà chúng tôi đã xác định được trong Ôm mặt Hub

mà chúng tôi muốn sử dụng để tóm tắt văn bản.

Vì vậy, chúng tôi bắt đầu bằng cách chỉ định tên của mô hình,

và sau đó chúng tôi khởi tạo một quy trình mới.

Lần này, chúng ta sẽ gọi nó là trình tóm tắt_,

và chúng tôi chỉ định nhiệm vụ

và tên của mô hình chúng tôi muốn sử dụng.

Vì vậy, chúng tôi sẽ chuyển sang hệ thống mới này văn bản tương tự

mà chúng ta đã có từ trước,

chúng ta sẽ giữ nguyên các lập luận,

và chúng ta sẽ thấy

kết quả lần này trông như thế nào.

Vì vậy, hãy tiếp tục và khởi tạo quy trình.

Và khi việc đó xong,

chúng ta sẽ tiếp tục và chạy lại phần tóm tắt

để xem kết quả lần này của chúng tôi như thế nào.

Được rồi, thế là xong.

Vì vậy hãy tiếp tục và thực hiện quá trình tóm tắt của chúng ta.

Được rồi, vậy là phần tóm tắt đã hoàn tất.

Và bây giờ chúng ta thấy hơi khác một chút, không phải một chút,

nó khác, đó là một kết quả hoàn toàn khác.

Đó là "Trí tuệ nhân tạo

và học máy đã trở thành những thành phần cơ bản."

Vì vậy, điều này khác với bản tóm tắt

mà chúng tôi đã nhận được từ trước nơi nó nói,

"Tự động hóa được hỗ trợ bởi AI đang định hình lại lực lượng lao động."

Một lần nữa, bằng cách chọn hai mô hình khác nhau,

đúng rồi, một cái là mẫu mặc định

và một là mô hình mà chúng tôi đã chỉ định,

chúng ta có hai bản tóm tắt khác nhau, phải không?

Vậy ý tưởng ở đây, một lần nữa,

Tôi chỉ muốn nhấn mạnh khái niệm này

rằng đó luôn là một ý tưởng hay

để thử các mô hình khác nhau bất cứ khi nào chúng tôi thử

để hoàn thành một nhiệm vụ bằng cách sử dụng các mô hình được đào tạo trước.

Vì vậy, hãy thoải mái thử các mẫu khác, phải không?

Vì vậy hãy trải qua quá trình xác định một mô hình

điều đó hữu ích cho việc tóm tắt văn bản

và thử nó trong mã của bạn,

và sau đó xem chính xác kết quả khác nhau như thế nào.