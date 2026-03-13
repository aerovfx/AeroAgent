# 5 -Xây dựng mô hình Phần 2.en US

---

WEBVTT

Xin chào.

Vì vậy bây giờ chúng ta hãy tiếp tục con đường xây dựng mô hình của chúng ta.

Trình phân loại tiếp theo sẽ được sử dụng là một trình phân loại.

Trình phân loại là một kỹ thuật chính thức và đơn giản được sử dụng cho các kỹ thuật xây dựng mô hình khác nhau.

Nó sử dụng các cây quyết định khác nhau dưới dạng đầu vào và mang lại cho chúng ta đầu ra tốt nhất, tốt nhất.

Bây giờ chúng ta sẽ nhập bộ phân loại từ thang cuốn vào biểu tượng.

Chúng tôi sẽ xác định nó sẽ phù hợp với mô hình của chúng tôi, sẽ dự đoán kết quả và chúng tôi sẽ xem nó hoạt động như thế nào.

Như bạn có thể thấy, những thứ tôi đã làm đã được phân loại không mang lại nhiều hiệu quả như chúng ta so sánh với

so với các mô hình khác nhau.

Điều này có thể xảy ra do nhiều thông số khác nhau.

Chúng tôi phải điều chỉnh mô hình Airbus này để duy trì độ chính xác cao nhất.

Bây giờ, tiếp tục, chúng ta sẽ sử dụng tham số tìm kiếm dạng lưới để xem các mô hình hoạt động tốt nhất của bộ siêu điều chỉnh của chúng ta nhằm

duy trì sản lượng tối đa.

Bây giờ, hãy nhập CV tìm kiếm lưới từ lựa chọn mô hình hình trụ và sau đó chúng ta sẽ xem ba

những mô hình hoạt động tốt nhất.

Như chúng ta có thể thấy, hồi quy logistic có thể kích hoạt SPM hoặc các mô hình hoạt động tốt nhất.

Vì vậy, trước tiên, áp dụng điều chỉnh siêu tham số này trong hồi quy logistic, đây là các tham số khác nhau

của hồi quy logistic, mà là hồi quy logistic trong đó hình phạt của người giải và đây là các thuộc tính khác nhau.

Chúng tôi đã xác định chúng trong lưới tham số và sau đó chúng tôi sẽ cung cấp tham số này cho mô hình tìm kiếm lưới của mình

sau đó chúng tôi sẽ điều chỉnh mô hình và tìm ra những thông số tốt nhất.

Như bạn có thể thấy, các tham số tốt nhất là xem hình phạt L2 0,01 này và bộ giải là tuyến tính.

Chúng ta sẽ áp dụng các tham số này cho mô hình của mình và xem mô hình của chúng ta hoạt động như thế nào?

Chúng tôi làm những điều tương tự mà bạn đã làm trước đây.

Và như chúng tôi thấy, mô hình của chúng tôi có độ chính xác là 81%.

Bây giờ, tiếp tục với trình phân loại chuẩn, chúng ta sẽ làm những việc tương tự, xác định các tham số.

Chúng ta sẽ đưa nó vào mô hình tìm kiếm dạng lưới và sau đó chúng ta sẽ xem mô hình đó hoạt động như thế nào?

Nhưng tìm ra các thông số tốt nhất.

Sẽ mất một chút thời gian vì nó liên quan đến nhiều số lần lặp và cung cấp cho chúng ta các tham số cơ bản.

Như bạn thấy, các thông số tốt nhất là.

Số liệu là số liệu là số khoảng cách của những người hàng xóm ở Manhattan.

11.

Điều này cũng giống như vậy.

Hàng xóm, như bạn đã dự đoán trong biểu đồ trong đó là khoảng cách.

Bây giờ hãy áp dụng các mô hình này ở hàng xóm gần nhất.

Như bạn thấy, nó mang lại cho chúng tôi độ chính xác là 82,5%, tăng nhẹ so với trước đó.

Hiện đang sử dụng mô hình SPM.

Chúng ta sẽ xem.

Tìm ra các thông số tốt nhất, những gì phù hợp với chúng.

Và như chúng ta thấy, chúng ta nhận được thông số tốt nhất, là 0,1 và thang gamma là sigma.

Sau khi áp dụng những điều này vào mô hình SVC của chúng tôi, chúng tôi thấy rằng nó mang lại cho chúng tôi số điểm khoảng 81%.

Bây giờ, sau khi so sánh tất cả các mô hình này và sau khi siêu điều chỉnh, chúng ta có thể nói rằng chúng ta có thể nói rằng logistic

hồi quy không có siêu miền cho chúng tôi độ chính xác tốt nhất khoảng 85%.

Vì vậy, chúng tôi sẽ sử dụng mô hình đó làm mô hình cuối cùng để dự đoán kết quả.

Bây giờ, để đi đến kết luận cuối cùng về các kỹ thuật học máy nguyên thủy của chúng ta, hãy xây dựng một

ma trận nhầm lẫn cho mô hình của chúng tôi.

Điều chúng tôi sẽ làm ở đây là, như tất cả các bạn, đều biết về ma trận nhầm lẫn, nó cho chúng ta biết về

đúng, dương và âm của mô hình.

Những gì tôi đã làm ở đây là tôi đã sử dụng một phương pháp gọi là các ô phụ của chuyến bay ở sân bay và sau đó tôi sử dụng nhiều thủ thuật khác nhau

và nhãn X để tạo ma trận nhầm lẫn của tôi.

Và sau đó tôi đặt tên cho cấp độ X, cấp độ Y và danh hiệu của mình.

Và đây là ma trận nhầm lẫn của tôi.

Và tôi cũng in ra độ chính xác của mẫu của mình, nó thể hiện độ chính xác của mẫu 85.7.

Vì vậy, chúng tôi đã sử dụng mô hình hồi quy logistic làm mô hình hoạt động tốt nhất.

Nhưng tất cả những điều này đều được thực hiện với sự trợ giúp của các kỹ thuật học máy nguyên thủy mà các nhà khoa học dữ liệu

làm.

Và phần tiếp theo, chúng ta sẽ thấy làm thế nào chúng ta có thể bỏ qua tất cả những rắc rối này và thực hiện chúng chỉ bằng một

dòng mã?

Với sự trợ giúp của tất cả các kỹ thuật học máy mà chúng ta sẽ sử dụng, chúng ta sẽ sử dụng cái ác.

ML Trong kỹ thuật này sẽ được thảo luận trong phần tiếp theo của video.