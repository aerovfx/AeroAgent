# 9 -CodeChallenge HellaSwag evals in two models (phần 2) đã dịch

---

Và bây giờ hãy tiếp tục với thử thách viết mã mà chúng ta đã bắt đầu ở video trước.

Bài tập 2 khá đơn giản và tôi hy vọng nó sẽ ít khó hiểu hơn nhiều.

Bài tập 1.

Tất cả những gì bạn cần làm là viết một hàm Python tính toán độ chính xác của một Helliswag

mẫu dữ liệu.

Vì vậy, điều đó có nghĩa là một bối cảnh có bốn kết thúc và một trong số đó là chính xác.

Bạn có thể sao chép mã từ hai video trước.

Đảm bảo rằng mã Python của bạn lấy một mẫu Helliswag, một mô hình và một mã thông báo làm đầu vào.

Bạn cần có khả năng nhập mô hình và mã thông báo vì bạn sẽ sử dụng

chức năng tương tự cho hai mô hình khác nhau, mỗi mô hình có mã thông báo riêng.

Và hàm bạn viết ở đây sẽ đưa ra độ chính xác của mẫu đó.

Vì vậy, liệu mô hình có nhật ký softmax nhật ký tổng hợp cao nhất để có kết thúc chính xác hay không.

Và bạn cũng nên kiểm tra chức năng của mình trên một mẫu bằng mô hình Zephyr chỉ để thực hiện

chắc chắn rằng nó hoạt động.

Nhưng đừng lo lắng về việc thực sự sử dụng chức năng này cho đến bài tập tiếp theo.

Dù sao thì bây giờ các bạn có thể tạm dừng video và bây giờ mình sẽ chuyển sang code.

Tôi không có quá nhiều điều để nói về bài tập này.

Tất cả mã ở đây, hãy xem, tất cả mã ở đây thực chất là được sao chép từ

hai video trước đây, từ các tập tin mã hai video trước đây.

Tôi đã thay đổi nó một chút chỉ để cập nhật một số tên biến.

Ở đây bạn có thể thấy tôi chỉ đang nhập một mẫu mà sau này chúng tôi sẽ trích xuất từ tập dữ liệu

trong mã.

Ở đây tôi đang nhập mô hình và đây là mã thông báo được liên kết với mô hình này.

Bây giờ trong các trang trình bày, về mặt kỹ thuật tôi đã nói rằng bạn chỉ có thể xuất giá trị chính xác.

Những gì tôi thực sự quay lại ở đây là tổng của các thăm dò nhật ký cho mỗi phần cuối và sau đó

câu trả lời đúng ở đây.

Vì vậy, hãy chạy ô đó.

Và bây giờ tôi đang nhập bộ xác thực Helliswag.

Sự khác biệt duy nhất giữa tập tàu và tập xác thực về cơ bản là ở chỗ

đoàn tàu lớn hơn nhiều.

Nhưng chúng ta không cần nhiều như vậy.

Có, chúng ta có thể tin tưởng vào mã này.

Không sao đâu.

Tôi nghĩ tôi thực sự sẽ đặt cái này trở lại để bạn không phải tự mình làm việc này.

Cho đến khi bộ xác thực này chứa 10.000 mục, điều đó vẫn ổn.

Thế là quá đủ rồi.

Được rồi, tôi đang thử nghiệm chức năng này.

Tôi chỉ muốn đảm bảo rằng mã hoạt động và không tạo ra bất kỳ lỗi nào.

Vì vậy tôi chọn một ví dụ từ tập dữ liệu này.

Tôi nghĩ đây là cái chúng tôi đã sử dụng trong một vài video trước đây.

Nhập cả mô hình Zephyr và mã thông báo.

Phải mất một hoặc hai giây để chạy qua.

Và ở đây chúng ta thấy rằng mô hình đã đúng.

Bây giờ trong trường hợp này, theo cách tôi thiết lập đầu ra của hàm này, tôi nhận được tất cả

khả năng xảy ra và câu trả lời.

Và tôi có thể xác nhận rằng cái nào là lớn nhất.

Nếu đó là câu trả lời thì mô hình đã đúng.

Nếu không, mô hình cần được đào tạo thêm một chút.

Bây giờ để đánh giá.

Bạn nên nhập phiên bản nhỏ GPT2 và đó là mã thông báo.

Đảm bảo bạn đang sử dụng các tên biến khác với tên mà bạn gọi là Zephyr

model và mã thông báo Zephyr vì hiện tại chúng tôi có hai mô hình và hai mã thông báo rất khác nhau.

Sau đó, bạn muốn thiết lập vòng lặp for và chạy từng mô hình qua 500 mẫu Hella Swag.

Và bạn muốn đảm bảo rằng đó là cùng một tập dữ liệu và các mẫu giống hệt nhau

được sử dụng cho cả hai mô hình.

Điều đó sẽ cho phép bạn so sánh trực tiếp màn trình diễn của họ.

Bạn có thể hiển thị kết quả dưới dạng biểu đồ phân tán trông như thế này.

Vì vậy, ở đây trên trục x, tôi có mục mẫu.

Và trên trục y, tôi chỉ có hai dấu tích để biết các mô hình đúng hay sai.

Cái mà tôi đang sử dụng, các hộp màu xanh lá cây để biểu thị kết quả của mô hình Zephyr và các vòng tròn màu xanh lam

cho kết quả GPT2.

Và sau đó bạn có thể thấy rằng tôi cũng đã thêm một chút khoảng lệch dọc giữa những điều này

chỉ để làm cho nó rõ ràng hơn một chút.

Bây giờ tôi cũng là một người hâm mộ hình ảnh trực quan, nhưng cốt truyện phân tán này không thực sự là cách tốt nhất

để xem những dữ liệu này.

Trên thực tế, chỉ cần tính trung bình hiệu suất và hiển thị nó dưới dạng văn bản như thế này là đủ.

Hiện nay, một mặt, mô hình Zephyr có 7 tỷ tham số và mô hình GPT2 có

124 triệu thông số.

Vì vậy, sẽ không có gì ngạc nhiên khi mô hình Zephyr sẽ hoạt động tốt hơn.

Câu hỏi đặt ra là nó sẽ hoạt động tốt hơn bao nhiêu và hiệu suất của nó là bao nhiêu?

Tôi muốn bạn suy nghĩ về điều đó trước khi bạn nhìn thấy kết quả.

Và tôi cũng muốn bạn nghĩ xem hiệu suất ở mức độ ngẫu nhiên trong bài kiểm tra này là bao nhiêu.

Nghĩa là, giả sử chúng ta không có một số mô hình phức tạp để thực hiện nhiệm vụ này,

nhưng thay vào đó, chúng tôi thực sự chỉ chọn ngẫu nhiên từ một trong bốn kết thúc cho mỗi câu hỏi.

Mức độ chính xác mong đợi khi đoán hoàn toàn ngẫu nhiên là bao nhiêu?

Và phần cuối cùng của bài tập này là tìm một số mẫu mà Zephyr

đã đúng và GPT2 đã sai.

Ở đây tôi chỉ in một ví dụ.

Vì vậy, bất kể câu hỏi này là gì, phần thực tế của cốt truyện đã bị cắt bỏ ở đây nên chúng ta không thể

thực sự đọc nó.

Dù sao thì đây là một mục mà Zephyr đã đúng và GPT2 đã sai.

Tôi hy vọng bạn thích làm bài tập này và bây giờ tôi sẽ chuyển sang viết mã.

Ở đây tôi đang tải GPT2, cũng sử dụng .evil và tải mã thông báo của nó bằng cách sử dụng một

tên biến.

Được rồi, 500 mẫu.

Đây là nơi tôi sẽ lưu trữ hiệu suất.

Và đây là nơi tôi có thư viện TQDM sẽ chạy thanh tiến trình này mà tôi đã đề cập

vào đầu lần đầu tiên tôi chuyển sang mã.

Được rồi, cách hoạt động của thư viện này là bạn nhập vào vòng lặp của mình và một số tiêu đề và

bạn sẽ thấy tiêu đề đó xuất hiện ở đâu.

Và về cơ bản điều này sẽ làm là tạo một thanh tiến trình cập nhật động phía dưới

ở đây sẽ cho thấy khoảng cách dọc theo vòng lặp.

Tôi thường không sử dụng loại điều này.

Tôi chỉ thấy nó hơi gây mất tập trung về mặt thị giác một chút, nhưng rất nhiều người thích điều này.

Vì vậy, đôi khi tôi sẽ sử dụng điều này chỉ để bạn biết về nó.

Dù sao, ở đây tôi trích xuất một mẫu của tập dữ liệu.

Đây là nơi tôi tính toán hiệu suất cho Zephyr.

Và dòng mã này hoàn toàn giống nhau, nhưng nó dành cho mẫu GPT2.

Được rồi, vậy chúng ta có thể chạy nó.

Và ở đây bạn thấy thông báo này ở đây, văn bản ở dưới đây là những gì tôi đã viết ở đây

tham số mô tả.

Và bây giờ bạn có thể thấy khi vòng lặp này diễn ra, chúng tôi nhận được cập nhật liên tục về hiệu suất.

Vì vậy, việc đánh giá với 500 mẫu mất chưa đến bốn phút.

Bây giờ chúng ta có thể tính toán độ chính xác, cũng như giá trị trung bình của độ chính xác.

Và chúng tôi thấy rằng Zephyr có độ chính xác khoảng 51% và GPT2 chỉ có độ chính xác 35%.

Mặt khác, hiệu suất ở mức độ cơ hội đối với bốn vật phẩm là 25%.

Vì vậy GPT vẫn đang hiểu điều gì đó về nhiệm vụ.

Nó có một số kiến ​​thức thế giới.

Nhưng 35 thì tốt hơn 25 nhưng cũng không đến nỗi nào.

Thành thật mà nói, độ chính xác 51% cũng không phải là quá lớn.

Nó chắc chắn là tốt hơn cơ hội.

Một lần nữa, cơ hội là độ chính xác 25%.

Độ chính xác của nó không phải là 50%, nhưng nó vẫn không quá tuyệt vời.

Nếu bạn tò mò về cách điều chỉnh các mô hình và hướng dẫn hiện đại cũng như tinh chỉnh

các mô hình hoạt động, bạn có thể thấy rằng nó có độ chính xác cao hơn 50% một chút.

Nhưng điều này thực sự không tệ đối với chỉ một mô hình được đào tạo trước.

Được rồi, và ở đây chúng ta có thể tạo ra con số đó.

Như tôi đã nói trong các slide, tôi nghĩ đây là một hình dáng đẹp, giống như vẻ ngoài của nó.

Nhưng tiếc là không có nhiều thông tin theo nghĩa chỉ nhìn vào những con số

ở đây rất rõ ràng hai mô hình này đã làm như thế nào.

Và điều này không quá rõ ràng, không thể hiện tính chính xác một cách rất dễ hiểu.

hiểu đường đi.

Được rồi, đây là một ví dụ trong đó Zephyr đã đúng và GPT2 đã bỏ lỡ mục mẫu rất

dễ dàng.

Chúng tôi chỉ muốn biết hàng đầu tiên đúng ở đâu và hàng thứ hai bằng 0.

Điều đó sẽ cung cấp cho chúng tôi các mẫu kết quả.

Và ở đây tôi chỉ chọn ngẫu nhiên một cái để đi đến cái cuối cùng ở đây.

Hai điểm rút ra quan trọng từ thử thách mã này trước hết là có sự gia tăng

sự đa dạng của kiến trúc mô hình.

Khối biến áp và các vectơ nhúng khá cơ bản và phổ quát.

Vì vậy tất cả các mô hình ngôn ngữ thành công đều có hai đặc điểm đó.

Nhưng có rất nhiều người thông minh đang nghĩ ra những sửa đổi thông minh cho những kiến ​​trúc đó.

Một số sửa đổi đó được thiết kế để làm cho mô hình hoạt động tốt hơn ở một số nhiệm vụ nhất định.

Một số sửa đổi được thiết kế để làm cho mô hình nói chung tốt hơn và một số sửa đổi

được thiết kế để làm cho các mô hình càng nhỏ và nhẹ càng tốt mà không phải hy sinh

quá nhiều hiệu suất.

Điểm thứ hai chỉ là sự nhắc lại chủ đề trọng tâm của phần này và các phần tiếp theo,

đó là không có tiêu chuẩn hoặc phương pháp đánh giá nào là hoàn hảo.

Bạn không bao giờ nên chỉ dựa vào một phương pháp.

Trong một số video tiếp theo, tôi sẽ giới thiệu cho bạn một cách khác để tiếp cận đánh giá,

nghĩa là không tập trung vào các mã thông báo riêng lẻ và không phải vào các câu mà là vào sự phân phối

trên các đoạn văn bản lớn hơn.