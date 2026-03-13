# 03 - Phân tích cảm xúc với các mô hình được đào tạo trước trong Python

---

- [Người kể chuyện] Trong video này,

chúng ta sẽ sử dụng một mô hình được đào tạo trước

để phân tích tình cảm.

Ý tưởng đằng sau phân tích tình cảm là xác định

hoặc để định lượng tính phân cực của văn bản.

Ví dụ: đưa ra một đánh giá về sản phẩm,

chúng ta có thể sử dụng phân tích cảm tính để phân loại đánh giá

là tích cực, tiêu cực hoặc trung tính.

Trước khi bắt đầu, hãy để kernel.

Vì vậy, một phần của các bước tiền xử lý trước

mà chúng tôi ghi lại trong video này là để giảm thiểu vận tốc

của gói máy biến áp.

Vì vậy, đoạn mã này ở đây sẽ giảm thiểu

số lượng cảnh báo và nhật ký thông tin

mà chúng tôi nhận được trên đường đi.

Sau đó, chúng tôi muốn bắt đầu bằng cách khởi tạo

hoặc khởi tạo quy trình để phân tích tình cảm.

Vì vậy, cách chúng tôi làm điều này,

trước hết chúng ta có nhập hàm đường dẫn không

từ gói máy biến áp.

Sau đó, chúng tôi khởi tạo một quy trình gọi là cảm xúc,

trong đường ống, chúng tôi chỉ định một nhiệm vụ.

Nhiệm vụ của chúng tôi là phân tích tình cảm,

đó là bí danh để phân loại văn bản.

Vì vậy, chúng ta hãy tiếp tục và chạy nó.

Vì vậy, khi đã hoàn thành, điều tiếp theo chúng tôi muốn làm bây giờ là

là chuyển một số văn bản mẫu tới quy trình của chúng tôi.

Vì vậy, văn bản này chúng ta sẽ sử dụng ở đây,

"Tôi hoàn toàn thích sản phẩm này.

"Nó vượt quá mọi mong đợi của tôi."

Vì vậy chúng ta sẽ chuyển văn bản mẫu này

đến đường dẫn tình cảm mà chúng tôi vừa khởi tạo.

Và sau đó chúng ta sẽ hiển thị kết quả.

Như bạn có thể thấy, quy trình đã định lượng cảm xúc

đánh giá văn bản này là tích cực và nó cho điểm 0,9998.

Vì vậy, điều tiếp theo chúng ta sẽ làm bây giờ là xem

đường dẫn này hoạt động như thế nào với một đoạn văn bản lớn hơn.

Vì vậy, một số ví dụ văn bản.

Vì vậy, chúng ta sẽ tạo một danh sách các câu khác nhau,

và chúng tôi sẽ chuyển từng câu này vào hệ thống của chúng tôi

để xem nó hoạt động như thế nào.

Vì vậy, chúng ta sẽ tiếp tục và vượt qua

các câu vào đường dẫn,

và bằng cách sử dụng một vòng lặp, chúng ta có thể lặp đi lặp lại

rồi xuất kết quả cho từng câu.

Vì vậy, câu đầu tiên,

chúng tôi đã nói rằng nó được phân loại là tích cực.

Cái thứ hai là tiêu cực, cái thứ ba là tích cực,

và thứ tư là tiêu cực.

Và với mỗi câu này, chúng ta cũng thấy điểm số,

điều này cho chúng ta biết mức độ tin cậy của mô hình

trong phân loại của nó.

Vì vậy, trong ví dụ đơn giản này, trong vài dòng mã ở đây,

chúng tôi có thể sử dụng một mô hình được đào tạo trước, phải không,

sử dụng tác vụ đường ống mặc định trong gói máy biến áp

để thực hiện phân tích tình cảm.

Một điều khác chúng ta có thể làm là tốt,

là chỉ định kiểu máy nào trong Hugging Face Hub

chúng tôi muốn sử dụng cho nhiệm vụ phân loại của mình.

Vì vậy, trong ví dụ trước,

nó được mặc định là một mô hình có hậu trường.

Nhưng nếu chúng ta muốn chỉ định một mô hình cụ thể

để sử dụng để phân tích tình cảm,

chúng tôi làm như vậy bằng cách chỉ định đối số mô hình

trong chức năng đường ống.

Vì vậy, ở đây chúng tôi chỉ định mô hình

tình cảm-roberta-large-english

là mô hình mà chúng tôi muốn sử dụng từ Hugging Face Hub.

Và chúng tôi chỉ định một tên mô hình biến,

khởi tạo một đường ống mới.

Lần này chúng tôi gọi nó là tình cảm_,

và chúng tôi chỉ định nhiệm vụ là phân tích cảm xúc,

và mô hình như mô hình này chúng tôi vừa liệt kê ở đây.

Vì vậy, hãy tiếp tục và khởi tạo quy trình mới này.

Vì vậy, chúng tôi cho bạn một chút thời gian ở đây để hoàn thành.

Và chúng ta sẽ làm điều tương tự như chúng ta đã làm trước đây.

Khi mô hình này được thực hiện trong quá trình khởi tạo,

chúng ta sẽ chuyển qua cùng một danh sách các câu

tới đường ống mới này,

và xem chính xác cách nó phân loại từng câu đó.

Vì vậy, đó là những gì chúng ta sẽ làm ở đây

trong dòng mã tiếp theo.

Ở đây chúng tôi có kết quả.

Vậy ở đây chúng ta thấy rằng câu đầu tiên được phân loại

là tích cực, lần thứ hai là tiêu cực, lần thứ ba là tiêu cực,

điều này hơi khác một chút so với những gì chúng tôi đã có ở trên.

Vì vậy, trong ví dụ trước,

câu thứ ba được phân loại là tích cực.

Điều này được mong đợi vì hiện tại chúng tôi đang sử dụng một mô hình khác

được đào tạo hơi khác một chút.

Vì vậy, quá trình tập luyện, mức tạ được sử dụng,

dữ liệu được sử dụng để huấn luyện mô hình,

khác với cái chúng ta có trước đây.

Vì vậy chúng tôi kỳ vọng rằng kết quả có thể

hoặc có thể không khác.

Vì vậy, ý tưởng ở đây là bất cứ khi nào chúng ta cố gắng sử dụng

các mô hình được đào tạo trước cho bất kỳ nhiệm vụ NLP nào,

việc thử các loại mô hình khác nhau luôn là một ý tưởng hay.

Vì vậy, hãy thoải mái thử một mẫu khác với mẫu

mà chúng tôi đã chọn ở đây để xem kết quả của bạn thay đổi như thế nào.