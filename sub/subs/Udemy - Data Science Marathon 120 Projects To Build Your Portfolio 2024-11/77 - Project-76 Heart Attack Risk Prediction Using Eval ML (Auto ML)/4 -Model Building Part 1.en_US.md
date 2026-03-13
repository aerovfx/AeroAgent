# 4 -Xây dựng mô hình Phần 1.en US

---

WEBVTT

Xin chào.

Bây giờ chúng ta hãy thảo luận một phần về cách chúng ta sẽ xây dựng mô hình của mình trước khi xây dựng một mô hình.

Chúng ta hãy nhìn vào dữ liệu.

Như bạn có thể thấy, dữ liệu của chúng tôi có nhiều tham số khác nhau và chúng liên tục hoặc mang tính phân loại.

Vì vậy, trước khi đưa dữ liệu của chúng ta vào các thuật toán học máy, điều đó là rất cần thiết, rất cần thiết.

bước này được gọi là tiền xử lý dữ liệu.

Bây giờ ở đây tôi sẽ áp dụng một kỹ thuật tiền xử lý được gọi là bộ chia tỷ lệ tiêu chuẩn, về cơ bản nó sẽ chuẩn hóa

hoặc chia tỷ lệ các giá trị của tôi thành một nền tảng chung để mô hình của tôi không có nhiều biến thể trong dữ liệu của tôi và

sẽ hoạt động tốt hơn.

Có nhiều kỹ thuật tiền xử lý khác như kỹ thuật mã hóa cho các biến phân loại.

Tôi chưa thực hiện những kỹ thuật này ở đây vì mục tiêu chính của chúng tôi là dự đoán những điều này, dự đoán những điều này

với sự trợ giúp của các kỹ thuật tự động, chúng ta sẽ thực hiện điều này trong phần sắp tới.

Bây giờ để mở rộng quy mô phù hợp với mô hình của tôi.

Tôi đã sử dụng vô hướng chuẩn, vì vậy giả sử nhập vô hướng chuẩn.

Sau đó, chúng tôi sẽ điều chỉnh dữ liệu của chúng tôi cho phù hợp với nó.

Sau đó chúng ta sẽ biến đổi nó.

Chúng tôi sẽ tạo khung dữ liệu và sau đó chúng tôi sẽ xem dữ liệu của chúng tôi thay đổi như thế nào.

Như bạn có thể thấy, dữ liệu của chúng tôi đã được thay đổi hoặc thu nhỏ lại thành các giá trị chung từ âm một

đến khoảng một, sau này sẽ được áp dụng cho các mô hình của chúng tôi.

Bây giờ chúng tôi sẽ sử dụng các mô hình sau để dự đoán.

Đầu tiên là quyết định hồi quy logistic.

Lõi ngẫu nhiên đang tăng tốc.

Sau đó, chúng tôi cũng sẽ sử dụng một số kỹ thuật hiểu biết sâu sắc khác nhau để xem liệu chúng tôi có thể siêu mô hình hay không

không.

Bây giờ, trước những điều này, chúng ta phải phân chia dữ liệu.

Chúng ta phải chia dữ liệu thành các biến phụ thuộc và biến độc lập.

Như bạn có thể thấy, X dành cho các biến độc lập của chúng ta, là các thuộc tính khác nhau và thông minh hơn

đầu ra, đó là biến phụ thuộc của chúng tôi.

Bây giờ, giả sử nhập phần tách thử nghiệm tàu, là dữ liệu được phân tách với 3470 cạnh, tức là 70% cho đào tạo

dữ liệu và 30% cho dữ liệu thử nghiệm.

Chúng tôi có các thông số thử nghiệm x3x khác nhau bằng tàu hỏa.

Tại sao thử nghiệm sẽ được sử dụng trong các mô hình khác nhau của chúng tôi.

Bây giờ từ việc chuyển sang hồi quy logistic, chúng ta sẽ nhập hồi quy logistic từ Excel và Thư viện.

Sau đó, tôi đã sử dụng bộ mã hóa nhãn ở đây vì tôi xử lý biến mục tiêu.

Ngoài ra để cung cấp dữ liệu của tôi hoặc dữ liệu của tôi, tôi phải mang cái này đến a01 cho.

Đó là lý do tại sao tôi đang sử dụng bộ mã hóa nhãn.

Để tránh điều này, bạn có thể bỏ qua dữ liệu đầu ra trong bộ chia tỷ lệ tiêu chuẩn và chỉ chia tỷ lệ đầu vào

dữ liệu sẽ giống nhau.

Như thế này.

Bây giờ chúng tôi đã chuyển đổi một phạm vi rộng.

Bây giờ chúng ta hãy nhập một mô hình.

Mô hình tốt hơn.

Như bạn có thể thấy, mô hình của chúng tôi có các thuộc tính khác nhau.

Bây giờ chúng ta thấy điều đó.

Đây là một dự đoán.

Bạn thấy đấy, chúng tôi đã dự đoán và chúng tôi đã nhập cho một ma trận như độ chính xác, vì vậy ma trận nhầm lẫn nên

để chúng tôi có thể biết mô hình của chúng tôi hoạt động tốt như thế nào.

Chúng tôi thấy ma trận nhầm lẫn và chúng tôi sẽ thấy điểm khi chúng tôi thấy hồi quy logistic chưa được thực hiện

với độ chính xác 85%, khá tốt.

Bây giờ chuyển sang mô hình cây quyết định, chúng ta sẽ nhập quyết định, trình phân loại cây sẽ phù hợp với nó

và chúng ta sẽ thấy kết quả.

Như bạn có thể thấy, việc sửa sang lại mang tính nghệ thuật đã được thực hiện với độ chính xác khoảng 71%, tức là

ít hơn một chút so với mô hình hồi quy logistic.

Bây giờ, chuyển sang mô hình rừng ngẫu nhiên, chúng tôi áp dụng bộ phân loại rừng ngẫu nhiên và chúng tôi sẽ điều chỉnh dữ liệu của mình

và chúng ta sẽ xem chúng ta tìm thấy độ chính xác như thế nào.

Như bạn có thể thấy, nó mang lại độ chính xác ngẫu nhiên khoảng 80% hoặc 78% mà chúng tôi có được cho mô hình này.

Bây giờ chúng ta có mô hình hàng xóm gần nhất trong hàng xóm gần nhất.

Chúng ta sẽ sử dụng một phương pháp để tìm ra con số tối ưu mà chúng ta phải sử dụng cho việc này là bao nhiêu.

Tôi sẽ xác định một Tôi sẽ xác định một hàm trong đó tôi sẽ xác định tỷ lệ lỗi và tôi sẽ lặp lại chữ I trong

phạm vi từ 1 đến 40

Đây sẽ là giá trị chính của tôi và tôi sẽ phù hợp.

Tôi sẽ áp dụng tất cả. Tôi sẽ đặt mô hình của mình với tất cả các giá trị khóa và sau đó tôi sẽ cố gắng tìm ra khóa nào

value là tốt nhất và mang lại cho tôi tỷ lệ lỗi thấp nhất.

Bây giờ, với sự trợ giúp của một con số, chúng ta sẽ tìm ra khóa nào có giá trị tốt nhất.

Như bạn có thể thấy trên hình, giá trị khóa từ 11, 11 đến 12 là một con số rất tốt như hiện tại

hiển thị tỷ lệ lỗi tối thiểu thay vì 26.

Nếu chúng ta sử dụng 27, điều này có thể dẫn đến việc mô hình bị khớp quá mức.

Vì vậy, chúng ta sẽ chọn K bằng 12, vì nó cho chúng ta khoảng cách tốt nhất tới bàn.

Bây giờ, sau khi lắp nó, chúng ta sẽ thấy rằng nó mang lại cho chúng ta độ chính xác là 84%, cũng khá tốt.

So với các mô hình logistic của chúng tôi và các mô hình khác.

Bây giờ một mô hình khác là các máy vectơ hỗ trợ của chúng tôi sẽ áp dụng mô hình này và chúng tôi sẽ xem độ chính xác của chúng tôi là bao nhiêu

nhận được.

Chúng tôi sẽ thấy rằng nó mang lại cho chúng tôi độ chính xác khoảng 80% vì chúng tôi thấy rằng tất cả các mô hình này đều hoạt động tốt và

xung quanh đang hoạt động khá tốt.

Bây giờ chúng ta hãy chuyển đổi chúng một cách chính xác dưới dạng khung dữ liệu để chúng ta có ý tưởng tốt hơn

là tốt nhất

Những gì tôi đã làm ở đây là lấy tất cả các điểm chính xác của mô hình và chuyển đổi nó thành khung dữ liệu.

Khung dữ liệu và tôi đã sử dụng tăng dần bằng false để nó sẽ cung cấp cho tôi khung dữ liệu theo hướng giảm dần

đặt hàng.

Như bạn thấy, hồi quy logistic có độ chính xác cao nhất là 85%, tiếp theo là hàng xóm gần nhất

và SVM.

Đây là một số kỹ thuật học mô hình nguyên thủy mà chúng tôi hiện đang sử dụng.

Chúng tôi có các kỹ thuật khác, trong các kỹ thuật đơn giản, được gọi là phân loại mạnh mẽ

và các kỹ thuật đơn giản khác mà chúng ta sẽ thảo luận.