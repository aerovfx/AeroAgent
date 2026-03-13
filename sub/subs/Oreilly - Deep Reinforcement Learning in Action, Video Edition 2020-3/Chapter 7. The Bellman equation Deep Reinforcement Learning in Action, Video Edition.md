# Chương 7. Phương trình Bellman Học tập tăng cường sâu trong thực tế, Phiên bản video được dịch

---

Phần 7.3, Phương trình Bellman.

Chúng ta đã đề cập đến Richard Bellman trong Chương 1, nhưng ở đây chúng ta sẽ thảo luận về Phương trình Bellman,

điều này củng cố phần lớn việc học tăng cường.

Phương trình Bellman xuất hiện khắp nơi trong các tài liệu về học tăng cường, nhưng

nếu tất cả những gì bạn muốn làm là viết Python, bạn có thể làm điều đó mà không cần hiểu Bellman

Phương trình.

Phần này là tùy chọn.

Nó dành cho những người quan tâm đến nền tảng toán học hơn một chút.

Như bạn sẽ nhớ lại, hàm Q cho chúng ta biết giá trị của một cặp hành động trạng thái và giá trị

được định nghĩa là tổng số phần thưởng được chiết khấu theo thời gian dự kiến.

Ví dụ: trong trò chơi thế giới lưới, Q pi của SA, cho chúng ta biết phần thưởng trung bình mà chúng ta sẽ nhận được.

nhận được nếu chúng ta thực hiện hành động A ở trạng thái S và tuân theo chính sách pi từ đó trở đi.

Hàm Q tối ưu được ký hiệu là sao Q và là hàm Q hoàn toàn chính xác.

Khi chúng ta lần đầu tiên bắt đầu chơi một trò chơi với hàm Q được khởi tạo ngẫu nhiên, nó sẽ diễn ra

để cung cấp cho chúng tôi những dự đoán giá trị Q rất không chính xác, nhưng mục tiêu là cập nhật lặp đi lặp lại giá trị Q

hoạt động cho đến khi nó tiến gần đến sao Q tối ưu.

Phương trình Bellman cho chúng ta biết cách cập nhật hàm Q khi quan sát thấy phần thưởng.

Xem biểu hiện này.

Trong đó V pi của S T cộng 1 bằng cực đại Q pi của S T cộng 1 A.

Vì vậy giá trị Q của trạng thái hiện tại, Q pi của S T A, cần được cập nhật thành giá trị quan sát được

thưởng RT cộng với giá trị trạng thái tiếp theo V pi của S T cộng 1 A.

Nhân với hệ số giảm giá gamma, mũi tên hướng sang trái trong phương trình có nghĩa là,

gán giá trị ở bên phải cho biến ở bên trái.

Giá trị của trạng thái tiếp theo chỉ đơn giản là giá trị Q cao nhất dành cho trạng thái tiếp theo.

Vì chúng ta nhận được giá trị Q khác nhau cho mỗi hành động có thể xảy ra, nếu chúng ta sử dụng mạng nơ-ron để

gần đúng hàm Q, chúng ta cố gắng giảm thiểu sai số giữa Q pi dự đoán của S T

A T ở vế trái của phương trình Bellman và đại lượng ở vế phải bằng cách cập nhật

các tham số của mạng nơ-ron.

Mục 7.3.1, phương trình Bellman phân phối.

Phương trình Bellman ngầm giả định rằng môi trường có tính chất quyết định và do đó

rằng phần thưởng được quan sát có tính quyết định, nghĩa là phần thưởng được quan sát sẽ luôn là

tương tự nếu bạn thực hiện hành động tương tự trong cùng một trạng thái.

Trong một số trường hợp điều này đúng, nhưng trong những trường hợp khác thì không.

Tất cả các trò chơi chúng tôi đã và sẽ sử dụng, ngoại trừ GridWorld, đều liên quan đến ít nhất một số lượng.

của sự ngẫu nhiên.

Ví dụ: khi chúng tôi lấy mẫu các khung hình của trò chơi, hai trạng thái ban đầu khác nhau

sẽ được ánh xạ vào cùng một trạng thái được lấy mẫu xuống, dẫn đến một số điều không thể đoán trước được trong quan sát

phần thưởng.

Trong trường hợp này, chúng ta có thể biến biến xác định R T thành biến ngẫu nhiên R của S T A

có một số phân phối xác suất cơ bản.

Nếu có sự ngẫu nhiên trong cách các trạng thái phát triển thành các trạng thái mới thì hàm Q phải là một hàm ngẫu nhiên.

cũng có thể thay đổi.

Phương trình Bellman ban đầu bây giờ có thể được biểu diễn dưới dạng hàm Q là ngẫu nhiên

có thể thay đổi vì chúng ta giải thích môi trường có sự chuyển đổi ngẫu nhiên.

Thực hiện một hành động có thể không dẫn đến trạng thái tiếp theo tương tự, vì vậy chúng tôi nhận được phân phối xác suất

qua các trạng thái và hành động tiếp theo.

Giá trị Q kỳ vọng của cặp hành động trạng thái tiếp theo là giá trị Q có nhiều khả năng xảy ra nhất

có thể là cặp hành động trạng thái tiếp theo.

Nếu loại bỏ toán tử kỳ vọng, chúng ta sẽ có được phương trình Bellman phân phối đầy đủ.

Xem biểu hiện này.

Ở đây chúng tôi sử dụng Z để biểu thị hàm giá trị Q phân phối, chúng tôi cũng sẽ đề cập đến hàm này

để phân phối giá trị.

Khi chúng ta học Q bằng phương trình Bellman ban đầu, hàm Q của chúng ta sẽ học

giá trị kỳ vọng của sự phân bổ giá trị vì đó là điều tốt nhất nó có thể làm được.

Nhưng trong chương này, chúng ta sẽ sử dụng một mạng lưới thần kinh phức tạp hơn một chút.

trả về một phân phối giá trị và do đó có thể tìm hiểu cách phân phối phần thưởng được quan sát thay vì

hơn là chỉ giá trị mong đợi.

Điều này hữu ích vì những lý do chúng tôi đã mô tả trong phần đầu tiên.

Bằng cách học cách phân phối, chúng ta có cách sử dụng các chính sách nhạy cảm với rủi ro

xem xét phương sai và tính đa phương thức có thể có của phân phối.