# 01 - Nhận dạng thực thể được đặt tên với các mô hình được đào tạo trước trong Python

---

- [Người hướng dẫn] Trong video này,

chúng ta sẽ sử dụng một mô hình được đào tạo trước

cho Nhận dạng thực thể được đặt tên, NER.

Ý tưởng đằng sau NER là xác định

và phân loại các thực thể quan trọng, chẳng hạn như con người,

địa điểm và tổ chức trong văn bản.

Nếu bạn chưa làm như vậy,

Tôi khuyên bạn nên chọn kernel.

Tôi sẽ tiếp tục và chọn kernel ở đây.

Và đối với ví dụ này,

Tôi sẽ chạy mã trong tệp 04_01e.

Tệp 04_01b rất giống nhau,

nhưng không có tất cả mã được điền vào.

Vì vậy, trong ví dụ này, chúng ta sẽ tải một số gói,

tenorflow, máy ảnh, gấu trúc,

ipywidget và máy biến áp.

Chúng ta cũng sẽ bắt đầu bằng cách giảm thiểu

hoặc giảm mức độ chi tiết của nhật ký được tạo

bằng gói máy biến áp.

Tiếp theo, chúng tôi nhập hàm đường ống

đó sẽ là chức năng cốt lõi

chúng tôi sẽ sử dụng cho hầu hết các mô hình được đào tạo trước,

và khóa học này từ gói máy biến áp.

Trong chức năng đường ống, chúng tôi chỉ định một nhiệm vụ.

Lần này vì chúng tôi đang thực hiện NER,

nhiệm vụ sẽ là phân loại mã thông báo.

Và chúng tôi sẽ gọi đường ống mới này là

mà chúng tôi tạo ra trình nhận dạng.

Thông tin trên màn hình là được.

Đó không phải là lỗi, đó chỉ là thông tin

tại thời điểm này, chỉ cần xác định rõ,

cho chúng tôi biết rằng chúng tôi đang sử dụng

rất nhiều bộ nhớ cho nhiệm vụ này.

Vì vậy, khi đường ống đã được khởi tạo,

điều tiếp theo chúng tôi muốn làm là sử dụng quy trình.

Vì vậy chúng ta sẽ sử dụng văn bản mẫu.

Barack Obama sinh ra ở Hawaii,

và mục tiêu ở đây là

để xác định các thực thể trong văn bản này.

Vì vậy, chúng ta sẽ tạo một tập kết quả mới gọi là result.

Chúng ta sẽ chuyển văn bản mẫu

đến đường dẫn ban đầu của chúng tôi,

và chúng tôi sẽ hiển thị kết quả.

Vì vậy, chúng tôi có nó.

Vì vậy, những gì chúng ta đang xem xét ở đây là một danh sách

của các từ điển trong đó mỗi từ điển chỉ rõ từng từ

của các thực thể được xác định.

Vì vậy, chúng ta thấy ở đây rằng một người đã được xác định

và với số điểm 0,999 và con người,

từ hoặc mã thông báo đã được xác định là Barack.

Tiếp theo, chúng ta thấy một người khác được xác định, Obama,

và chúng tôi thấy một địa điểm được xác định, Hawaii.

Vì vậy, rõ ràng, như bạn có thể thấy ở đây,

các token được cá nhân hóa.

Chúng tôi cũng có thể yêu cầu quy trình tổng hợp các mã thông báo.

Vì vậy, để làm điều đó, ví dụ,

chúng tôi muốn thấy Barack và Obama cùng nhau,

chúng ta có thể chỉ định một chiến lược tổng hợp đối số

đơn giản như vậy trong đường ống.

Vì vậy, hãy thử cách tiếp cận đó và xem điều gì sẽ xảy ra ở đây.

Lần này chúng ta thấy

kết quả hơi khác một chút phải không?

Vì vậy chúng ta thấy rằng Barack và Obama

hiện được nhóm lại với nhau thành một mã thông báo,

và nó cũng được xác định là một con người.

Nhưng, Hawaii, như chúng ta mong đợi từ ví dụ trước,

vẫn được xác định là một địa điểm.

Vì vậy, định dạng của dữ liệu này,

kết quả này xuất hiện là bạn có thể hiểu khá nhiều

chuyện gì đang xảy ra vậy, nhưng đôi khi, chúng ta có thể muốn định dạng lại cái này,

để chúng tôi có thể sử dụng hoặc tích hợp những kết quả này

vào một ứng dụng khác.

Vậy điều chúng ta sẽ làm tiếp theo ở đây là

để cơ cấu lại đầu ra này thành khung dữ liệu gấu trúc.

Vì vậy chúng ta sẽ nhập gói pandas,

và chúng ta sẽ gọi khung dữ liệu,

hàm xây dựng và chúng tôi chuyển kết quả của mình cho nó.

Và khung dữ liệu mới mà chúng ta sắp tạo bây giờ,

chúng ta sẽ gọi các thực thể được đặt tên.

Vì vậy, chúng tôi có nó.

Vì vậy, bây giờ, chúng ta có các hàng riêng lẻ

đối với mỗi thực thể được xác định,

đó là một nhóm thực thể, một điểm số, một từ,

và họ bắt đầu một chỉ số kết thúc

về nơi thực thể thực tế được xác định trong văn bản.

Vì vậy, đây là một ví dụ đơn giản,

và vì vậy chúng ta có thể áp dụng điều này cho bất kỳ văn bản có kích thước nào.

Vì vậy điều chúng tôi dự định làm trong năm tới là

để áp dụng cách tiếp cận tương tự này cho một đoạn văn bản lớn hơn.

Và đoạn văn bản này còn hơn thế nữa

hoặc ít giống với những gì bạn mong đợi

từ đánh giá phản hồi của khách hàng

hoặc đánh giá sản phẩm từ khách hàng của bạn.

Ở đây, chúng ta có một đoạn văn bản dài hơn,

và chúng ta sẽ áp dụng cùng một chiến lược

mà chúng tôi đã sử dụng trước đây để xem chính xác

những thực thể nào sẽ được xác định trong văn bản của chúng tôi.

Vì vậy chúng ta hãy tiếp tục và chạy cái này.

Và ở đây, chúng ta thấy rằng một số thực thể

đã được xác định trong văn bản.

Ví dụ: chúng ta thấy, Apple iPhone 14,

được xác định là một thực thể linh tinh.

Một tổ chức, Best Buy,

đã được xác định vị trí, Manhattan.

Một người, John Smith.

Tổ chức, một lần nữa, chúng ta thấy Samsung,

và thực thể linh tinh, iPhone.

Vì vậy, bạn có nó.