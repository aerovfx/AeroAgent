# 05 - Giải pháp Tạo cảm xúc bằng BERT

---

(nhạc sôi động)

- [Người hướng dẫn] Hy vọng bạn thích thử thách thứ ba.

Chúng ta hãy xem giải pháp.

Vì vậy, tôi sẽ đi tới bảng điều khiển này và tải tập tin vào,

và tất nhiên tôi nhận được cảnh báo thông thường

để đảm bảo rằng các tập tin của tôi được lưu ở nơi khác.

Được rồi, bây giờ tôi sẽ cuộn xuống

và nhập một số thư viện và chạy ô này.

Và tất nhiên, yêu cầu của tôi đã được đáp ứng

bởi vì tôi đã thực thi ô này trước đây.

Và bây giờ ở đây, tôi sẽ tải

tệp CSV vào khung dữ liệu và đó là ở đây.

Và tất nhiên, như một cách thực hành tốt nhất,

Tôi muốn chắc chắn rằng tôi có thể nhìn thấy

năm hàng đầu tiên của khung dữ liệu,

và họ đây rồi.

Vì vậy bài tập số một

là tải mô hình DistilBERT và Tokenizer được đào tạo trước,

và mã sẽ trông như thế này.

Và tôi sẽ xử tử tế bào.

Và sau đó bài tập thứ hai là tải DistilBERT Sentiment,

đường ống phân tích,

vì vậy tôi sẽ chỉ cho bạn xem nó trông như thế nào.

Vì vậy, trước tiên, bạn tải đường dẫn ở đây, phải,

và sau đó bạn cần lặp lại các hàng

và thực hiện phân tích tình cảm với DistilBERT.

Và ở đây, bạn đang tạo một danh sách,

và bạn đang xem xét từng câu trong tập tin.

Bạn sẽ gán một nhãn hiệu và một điểm số,

và một khi việc đó xong,

bạn sẽ lặp lại các kết quả cảm tính

và in từng mục.

Và một lần nữa, đây chính là công việc mà vòng lặp for thực hiện ở đây.

Và sau đó, tất nhiên, có một dòng trống để dễ đọc,

và sau đó kết quả sẽ được lưu vào tệp CSV mới.

Vậy nên hãy để ý khu vực này khi tôi điều hành phòng giam.

Được rồi, đây là kết quả của tôi, nhưng tôi không thấy tập tin nào ở đây,

vì vậy tôi sẽ đi và làm mới cửa sổ này.

Và nó đây rồi.

Được rồi, đây là đầu ra của tôi.

Câu đầu tiên của tôi là "Sản phẩm của bạn rất tuyệt vời.

"Tôi thực sự yêu thích chất lượng."

Vậy là có năm sao,

và ở đây, có bốn sao cho,

"Đội ngũ dịch vụ khách hàng ở New York rất hữu ích."

Đây là kết quả đầu ra mà bạn có thể nhìn thấy.

Và ở đây, như một cách thực hành tốt nhất,

Tôi thực sự muốn hiểu được kết quả của cảm xúc,

nên tôi sẽ làm

một chút phân tích thăm dò.

Đầu tiên, tôi muốn kéo năm hàng đó vào.

Và bạn sẽ nhận thấy ở đây, đột nhiên,

so với bảng kia, bây giờ tôi có điểm,

Tôi có điểm tình cảm và nhãn tình cảm.

Và tôi muốn thấy một đám mây từ ngữ,

và đây là đám mây từ của tôi từ văn bản phân tích tình cảm.

Và tôi muốn xem biểu đồ hình tròn,

và đây là sự phân bổ nhãn tình cảm của tôi.

Và tôi muốn xem biểu đồ thanh,

và nó đây,

ngôi sao của tôi theo nhãn tình cảm.