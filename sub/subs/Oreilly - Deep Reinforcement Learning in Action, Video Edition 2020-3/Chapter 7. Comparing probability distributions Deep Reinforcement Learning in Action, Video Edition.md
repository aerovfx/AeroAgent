# Chương 7. So sánh phân bố xác suất Học tăng cường sâu trong thực tế, Phiên bản video đã dịch

---

Phần 7.5, So sánh phân phối xác suất.

Bây giờ chúng ta đã có dist dqn và cách tạo phân phối mục tiêu,

chúng ta cần một hàm mất mát sẽ tính toán mức phân phối giá trị hành động được dự đoán khác với phân phối mục tiêu như thế nào.

Sau đó, chúng ta có thể truyền ngược lại và thực hiện giảm độ dốc như bình thường để cập nhật các tham số dist dqn chính xác hơn vào lần sau.

Chúng ta thường sử dụng sai số bình phương trung bình, mse, hàm mất mát, khi cố gắng giảm thiểu khoảng cách giữa hai tập vô hướng hoặc vectơ.

Nhưng đây không phải là hàm mất mát thích hợp giữa hai phân bố xác suất.

Nhưng có nhiều lựa chọn khả thi cho hàm mất mát giữa các phân bố xác suất.

Chúng tôi muốn một hàm sẽ đo lường mức độ khác nhau hoặc khoảng cách giữa hai phân bố xác suất và sẽ giảm thiểu khoảng cách đó.

Trong học máy, chúng ta thường cố gắng huấn luyện một mô hình tham số, ví dụ như mạng lưới thần kinh,

để dự đoán hoặc tạo ra dữ liệu gần giống với dữ liệu thực nghiệm từ một số tập dữ liệu.

Suy nghĩ theo xác suất, chúng ta có thể hình dung mạng lưới thần kinh đang tạo ra dữ liệu tổng hợp và cố gắng huấn luyện mạng lưới thần kinh để tạo ra nhiều dữ liệu thực tế hơn.

Dữ liệu gần giống với một số tập dữ liệu thực nghiệm.

Đây là cách chúng tôi đào tạo các mô hình tổng quát, các mô hình tạo ra dữ liệu.

Chúng tôi cập nhật các tham số của họ để dữ liệu họ tạo ra trông rất giống với một số tập dữ liệu thực nghiệm, huấn luyện.

Ví dụ: giả sử chúng ta muốn xây dựng một mô hình tổng quát tạo ra hình ảnh khuôn mặt của những người nổi tiếng, hình 7.16.

Để làm được điều này, chúng ta cần một số dữ liệu huấn luyện. Vì vậy, chúng tôi sử dụng bộ dữ liệu CelebA có sẵn miễn phí chứa hàng trăm nghìn bức ảnh chất lượng cao của nhiều người nổi tiếng khác nhau như Will Smith và Brittany Spears.

Hãy gọi mô hình tổng quát của chúng ta là P và tập dữ liệu thực nghiệm này là Q.

Hình 7.16. Một mô hình tổng quát có thể là một mô hình xác suất huấn luyện bằng cách tối đa hóa xác suất mà nó tạo ra các mẫu tương tự với một số tập dữ liệu thực nghiệm.

Quá trình đào tạo diễn ra theo một vòng lặp trong đó dữ liệu thực nghiệm được cung cấp cho mô hình tổng quát nhằm cố gắng tối đa hóa xác suất của dữ liệu thực nghiệm.

Trước khi đào tạo, mô hình tổng quát sẽ gán xác suất thấp cho các ví dụ lấy từ tập dữ liệu huấn luyện và mục tiêu là để mô hình tổng quát gán xác suất cao cho các ví dụ được lấy từ tập dữ liệu.

Sau đủ số lần lặp, mô hình tổng quát sẽ gán xác suất cao cho dữ liệu thực nghiệm và sau đó chúng ta có thể lấy mẫu từ phân phối này để tạo dữ liệu tổng hợp mới.

Các hình ảnh trong tập dữ liệu Q được lấy mẫu từ thế giới thực, nhưng chúng chỉ là một mẫu nhỏ trong vô số bức ảnh đã tồn tại nhưng không có trong tập dữ liệu và có thể đã được chụp nhưng lại không.

Ví dụ: có thể chỉ có một bức ảnh chụp chân dung của Will Smith trong tập dữ liệu nhưng một bức ảnh khác của Will Smith được chụp ở một góc khác cũng có thể dễ dàng trở thành một phần của tập dữ liệu.

Một bức ảnh chụp Will Smith với một chú voi con trên đầu, tuy không phải là không thể, nhưng sẽ ít có khả năng được đưa vào tập dữ liệu vì ít có khả năng tồn tại, ai sẽ đặt một chú voi con lên đầu mình.

Đương nhiên ngày càng có ít ảnh của những người nổi tiếng, vì vậy thế giới thực có sự phân bố xác suất đối với hình ảnh của những người nổi tiếng.

Chúng ta có thể biểu thị phân bố xác suất thực sự này của các bức ảnh của người nổi tiếng là Q của X, trong đó X là một số hình ảnh tùy ý và Q của X cho chúng ta biết xác suất hình ảnh đó tồn tại trên thế giới.

Nếu X là một hình ảnh cụ thể trong tập dữ liệu Q thì Q của X bằng 1,0 vì hình ảnh đó chắc chắn tồn tại trong thế giới thực.

Tuy nhiên, nếu chúng ta đưa vào một hình ảnh không có trong tập dữ liệu nhưng có khả năng tồn tại trong thế giới thực bên ngoài mẫu nhỏ của chúng ta thì Q của X có thể bằng 0,9.

Khi chúng tôi khởi tạo ngẫu nhiên mô hình tổng quát P của mình, nó sẽ tạo ra các hình ảnh trông ngẫu nhiên trông giống như nhiễu trắng.

Chúng ta có thể coi mô hình tổng quát của mình như một biến ngẫu nhiên và mọi biến ngẫu nhiên đều có phân bố xác suất liên quan mà chúng ta biểu thị là P của X.

Vì vậy, chúng ta cũng có thể hỏi mô hình tổng quát của mình về xác suất của một hình ảnh cụ thể với bộ tham số hiện tại của nó.

Khi chúng ta khởi tạo nó lần đầu tiên, nó sẽ nghĩ rằng tất cả các hình ảnh đều có khả năng xảy ra ít nhiều như nhau và tất cả sẽ được gán một xác suất khá thấp.

Vì vậy, nếu chúng ta hỏi truy vấn P cho bức ảnh của Will Smith, nó sẽ trả về một xác suất nhỏ nào đó.

Nhưng nếu chúng ta hỏi truy vấn Q cho ảnh Will Smith, chúng ta sẽ nhận được 1,0.

Để huấn luyện mô hình tổng quát P của chúng tôi tạo ra những bức ảnh thực tế về người nổi tiếng bằng cách sử dụng tập dữ liệu Q, chúng tôi cần đảm bảo mô hình tổng quát gán xác suất cao cho dữ liệu trong Q và cả dữ liệu không có trong Q, nhưng điều đó có thể hợp lý.

Về mặt toán học, chúng tôi muốn tối đa hóa tỷ lệ này.

Xem biểu hiện này.

Chúng tôi gọi đây là tỷ lệ khả năng, lr, giữa P của X và Q của X.

Khả năng xảy ra trong bối cảnh này chỉ là một từ khác để chỉ xác suất.

Nếu chúng ta lấy tỷ lệ cho một hình ảnh ví dụ về Will Smith tồn tại trong Q bằng cách sử dụng P chưa được huấn luyện, chúng ta có thể nhận được...

Biểu hiện này.

Đây là một tỷ lệ nhỏ.

Chúng tôi muốn truyền ngược vào mô hình tổng quát của mình và thực hiện giảm độ dốc để cập nhật các tham số của nó sao cho tỷ lệ này được tối đa hóa.

Tỷ lệ khả năng này là hàm mục tiêu mà chúng tôi muốn tối đa hóa hoặc giảm thiểu tiêu cực của nó.

Nhưng chúng tôi không muốn làm điều này chỉ cho một hình ảnh.

Chúng tôi muốn mô hình tổng quát tối đa hóa tổng xác suất của tất cả các hình ảnh trong tập dữ liệu Q.

Chúng ta có thể tìm tổng xác suất này bằng cách lấy tích của tất cả các ví dụ riêng lẻ, vì xác suất của A và B bằng xác suất của A nhân với xác suất của B khi A và B độc lập và có cùng phân phối.

Vì vậy, hàm mục tiêu mới của chúng tôi là tích của các tỷ lệ khả năng xảy ra đối với từng phần dữ liệu trong tập dữ liệu.

Chúng tôi sắp đưa ra một số phương trình toán học nhưng chúng tôi chỉ sử dụng chúng để giải thích các khái niệm xác suất cơ bản.

Đừng tốn thời gian để nhớ chúng.

Bảng 7.4, tỷ lệ khả năng trong toán học và Python, Xem bảng hình.

Một vấn đề với hàm mục tiêu này là máy tính gặp khó khăn khi nhân một loạt các xác suất.

Vì chúng là những số dấu phẩy động cực nhỏ nên khi nhân với nhau sẽ tạo ra những số dấu phẩy động thậm chí còn nhỏ hơn.

Điều này dẫn đến những sai số về mặt số học và cuối cùng là tình trạng tràn số liệu vì máy tính có một dãy số hữu hạn mà chúng có thể biểu diễn.

Để cải thiện tình trạng này, chúng ta thường sử dụng xác suất log, tương đương với khả năng log, bởi vì hàm logarit biến những xác suất nhỏ thành những con số lớn, từ vô cực âm khi xác suất tiến tới 0.

Tối đa bằng 0 khi xác suất là một.

Logarit cũng có một đặc tính hay là logarit của tích A và B bằng tổng logarit của A và logarit của B, vì vậy chúng ta có thể biến phép nhân thành phép cộng và máy tính có thể xử lý việc đó tốt hơn rất nhiều mà không gặp rủi ro về sự mất ổn định số hoặc tràn.

Chúng ta có thể chuyển đổi phương trình tỷ lệ khả năng xảy ra trong nhật ký sản phẩm trước đó thành phương trình này.

Bảng 7.5, tỷ lệ khả năng ghi nhật ký trong toán học và Python, Xem bảng Hình.

Phiên bản log xác suất này của phương trình đơn giản hơn và tốt hơn cho việc tính toán, nhưng một vấn đề khác là chúng ta muốn tính trọng số của từng mẫu một cách khác nhau.

Ví dụ: nếu chúng ta lấy mẫu hình ảnh của Will Smith từ tập dữ liệu, thì nó sẽ có xác suất cao hơn hình ảnh của một người nổi tiếng ít nổi tiếng hơn, vì người nổi tiếng ít nổi tiếng hơn có thể có ít ảnh chụp họ hơn.

Chúng tôi muốn mô hình của mình tập trung nhiều hơn vào việc học các hình ảnh có nhiều khả năng xảy ra trong thế giới thực, hay nói cách khác, đối với phân bố thực nghiệm q của x.

Chúng tôi sẽ tính trọng số của từng tỷ lệ khả năng ghi nhật ký theo xác suất q x của nó.

Bảng 7.6, tỷ lệ khả năng ghi nhật ký có trọng số trong toán học và Python, Xem bảng Hình.

Bây giờ chúng ta có một hàm mục tiêu để đo lường khả năng một mẫu từ mô hình tổng quát được so sánh với phân phối dữ liệu trong thế giới thực, được tính theo khả năng của mẫu trong thế giới thực.

Có một vấn đề nhỏ cuối cùng. Hàm mục tiêu này phải được tối đa hóa vì chúng tôi muốn tỷ lệ khả năng ghi nhật ký cao, nhưng theo sự thuận tiện và quy ước,

chúng tôi muốn có các hàm mục tiêu là các hàm lỗi hoặc mất mát được giảm thiểu.

Chúng ta có thể khắc phục điều này bằng cách thêm dấu âm, do đó tỷ lệ khả năng cao sẽ trở thành một lỗi hoặc mất mát nhỏ.

Bảng 7.7, sự phân kỳ của người báo lại lệnh gọi lại, Xem bảng Hình.

Bạn có thể nhận thấy chúng tôi đã thay đổi LR cho một số ký hiệu lạ, sự phân kỳ KL từ q thành p.

Hóa ra hàm mục tiêu mà chúng ta vừa tạo là một hàm rất quan trọng trong tất cả quá trình học máy.

Nó được gọi là phân kỳ gọi lại-lebler, gọi tắt là phân kỳ KL.

Phân kỳ KL là một loại hàm sai số giữa các phân bố xác suất. Nó cho bạn biết hai phân bố xác suất khác nhau như thế nào.

Thông thường, chúng ta đang cố gắng giảm thiểu khoảng cách giữa phân bố xác suất được tạo ra từ mô hình và một số phân bố thực nghiệm từ dữ liệu thực.

Vì vậy, chúng tôi muốn giảm thiểu sự phân kỳ KL.

Như bạn vừa thấy, việc giảm thiểu sự phân kỳ KL tương đương với việc tối đa hóa tỷ lệ khả năng ghi nhật ký chung của dữ liệu được tạo so với dữ liệu thực nghiệm.

Một điều quan trọng cần lưu ý là sự phân kỳ KL không đối xứng. Nghĩa là, phân kỳ KL từ q đến p không bằng phân kỳ KL từ p đến q, và điều này phải rõ ràng từ định nghĩa toán học của nó.

Phân kỳ KL chứa một tỷ lệ và không có tỷ lệ nào có thể bằng nghịch đảo của nó trừ khi cả hai đều bằng một. Nghĩa là, a chia cho b không bằng b chia cho a trừ khi a bằng b.

Mặc dù phân kỳ KL tạo nên một hàm mục tiêu hoàn hảo nhưng chúng ta có thể đơn giản hóa nó một chút để phục vụ mục đích của mình.

Hãy nhớ lại rằng logarit của a chia cho b bằng logarit của a trừ logarit của b nói chung.

Vì vậy chúng ta có thể viết lại phân kỳ KL dưới dạng.

Biểu hiện này.

Lưu ý rằng trong học máy, chúng ta chỉ muốn tối ưu hóa mô hình. Cập nhật các tham số của mô hình để giảm sai số.

Chúng ta không thể thay đổi phân bố thực nghiệm q của x. Vì vậy, chúng tôi thực sự chỉ quan tâm đến xác suất log có trọng số ở phía bên trái.

Xem biểu hiện này.

Phiên bản đơn giản hóa này được gọi là mất mát entropy chéo và được ký hiệu là entropy của q và p.

Đây là hàm tổn thất thực tế mà chúng ta sẽ sử dụng trong chương này để tìm ra sai số giữa phân bố giá trị hành động được dự đoán và phân bố thực nghiệm mục tiêu.

Trong danh sách 7.8, chúng tôi triển khai tổn thất entropy chéo dưới dạng hàm lấy một loạt phân phối giá trị hành động và tính toán tổn thất giữa phân phối đó và phân phối mục tiêu.

Liệt kê 7.8, hàm mất entropy chéo.

Hàm loss fn lấy phân phối dự đoán, x có kích thước b nhân 3 nhân 51 và phân phối mục tiêu, y có cùng thứ nguyên, sau đó làm phẳng phân phối trên thứ nguyên hành động để có được ma trận a b nhân 153.

Sau đó, nó lặp qua từng hàng một lần 153 trong ma trận và tính toán entropy chéo giữa phân phối dự đoán một lần 153 và phân phối mục tiêu một lần 153.

Thay vì tính tổng một cách rõ ràng tích của x và y, chúng ta có thể kết hợp hai thao tác này và nhận được kết quả trong một lần thực hiện bằng cách sử dụng toán tử tích bên trong.

Chúng tôi có thể chọn chỉ tính toán tổn thất giữa phân phối giá trị hành động cụ thể cho hành động đã được thực hiện, nhưng chúng tôi tính toán tổn thất cho cả ba phân phối giá trị hành động để dist dqn học cách giữ cho hai hành động còn lại không được thực hiện thay đổi.

Nó chỉ cập nhật phân phối giá trị hành động đã được thực hiện.