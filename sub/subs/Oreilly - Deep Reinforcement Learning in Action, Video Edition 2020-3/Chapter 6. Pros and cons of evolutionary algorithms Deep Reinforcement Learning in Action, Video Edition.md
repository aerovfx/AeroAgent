# Chương 6. Ưu và nhược điểm của các thuật toán tiến hóa Học tăng cường sâu trong thực tế, Phiên bản video đã dịch

---

Phần 6.4, ưu và nhược điểm của thuật toán tiến hóa.

Thuật toán chúng tôi triển khai trong chương này hơi khác so với các phương pháp trước đây mà chúng tôi đã sử dụng trong cuốn sách này.

Có những trường hợp mà cách tiếp cận tiến hóa hoạt động tốt hơn, chẳng hạn như với những vấn đề sẽ được hưởng lợi nhiều hơn từ việc khám phá.

Các trường hợp khác làm cho nó không thực tế, chẳng hạn như các vấn đề tốn kém để thu thập dữ liệu.

Trong phần này, chúng ta sẽ thảo luận về ưu và nhược điểm của các thuật toán tiến hóa và bạn có thể hưởng lợi từ việc sử dụng chúng theo phương pháp giảm độ dốc.

Phần 6.4.1, các thuật toán tiến hóa khám phá thêm.

Một lợi thế của các phương pháp tiếp cận không có độ dốc là chúng có xu hướng khám phá nhiều hơn so với các phương pháp tiếp cận dựa trên độ dốc.

Cả DQN và độ dốc chính sách đều tuân theo một chiến lược tương tự, thu thập kinh nghiệm và thúc đẩy đại lý thực hiện các hành động dẫn đến phần thưởng lớn hơn.

Như chúng ta đã thảo luận, điều này có xu hướng khiến các tác nhân từ bỏ việc khám phá các trạng thái mới nếu họ đã thích một hành động hơn.

Chúng tôi đã giải quyết vấn đề này bằng DQN bằng cách kết hợp chiến lược Epsilon-Greedy, nghĩa là có rất ít khả năng tác nhân sẽ thực hiện một hành động ngẫu nhiên, ngay cả khi hành động đó có hành động ưa thích.

Với gradient chính sách ngẫu nhiên, chúng tôi dựa vào việc vẽ ra nhiều hành động khác nhau từ vectơ xác suất hành động đầu ra theo mô hình của chúng tôi.

Mặt khác, các tác nhân trong thuật toán di truyền không bị đẩy theo bất kỳ hướng nào.

Chúng tôi tạo ra rất nhiều tác nhân trong mỗi thế hệ và với rất nhiều biến thể ngẫu nhiên giữa chúng, hầu hết chúng sẽ có các chính sách khác nhau.

Vẫn còn một vấn đề giữa khám phá và khai thác trong các chiến lược tiến hóa, bởi vì hai đột biến nhỏ có thể dẫn đến sự hội tụ sớm, trong đó toàn bộ quần thể trở nên chứa đầy những cá thể gần như giống hệt nhau.

Nhưng nhìn chung, việc đảm bảo khám phá đầy đủ bằng các thuật toán di truyền sẽ dễ dàng hơn so với các thuật toán dựa trên độ dốc.

Phần 6.4.2, các thuật toán tiến hóa có cường độ mẫu cực kỳ cao.

Như bạn có thể thấy từ đoạn mã trong chương này, chúng tôi cần chạy từng tác nhân trong quần thể 500 người trong môi trường để xác định mức độ phù hợp của chúng.

Điều đó có nghĩa là chúng tôi cần thực hiện 500 phép tính lớn trước khi có thể cập nhật dân số.

Các thuật toán tiến hóa có xu hướng sử dụng nhiều mẫu hơn các phương pháp dựa trên độ dốc vì chúng tôi không điều chỉnh trọng số của các tác nhân một cách chiến lược.

Chúng tôi chỉ đang tạo ra nhiều tác nhân và hy vọng rằng những đột biến và tái tổ hợp ngẫu nhiên mà chúng tôi giới thiệu sẽ mang lại lợi ích.

Chúng tôi sẽ nói rằng các thuật toán tiến hóa kém hiệu quả về dữ liệu hơn các phương pháp DQN hoặc PG.

Giả sử chúng ta muốn giảm kích thước quần thể để làm cho thuật toán chạy nhanh hơn.

Nếu chúng ta giảm quy mô quần thể, sẽ có ít tác nhân hơn để lựa chọn khi chúng ta chọn cả bố và mẹ.

Điều này sẽ khiến những cá nhân kém phù hợp hơn có khả năng lọt vào thế hệ tiếp theo.

Chúng tôi dựa vào một số lượng lớn các tác nhân được sản xuất với hy vọng tìm ra sự kết hợp mang lại hiệu quả tốt hơn.

Ngoài ra, cũng như trong sinh học, đột biến thường có tác động tiêu cực và dẫn đến thể lực kém hơn.

Việc có dân số lớn hơn sẽ làm tăng khả năng có ít nhất một vài đột biến có lợi.

Dữ liệu không hiệu quả sẽ là một vấn đề nếu việc thu thập dữ liệu tốn kém, chẳng hạn như trong chế tạo robot hoặc bằng phương tiện tự hành.

Để một robot thu thập một tập dữ liệu thường mất vài phút và chúng tôi biết từ các thuật toán trước đây rằng việc đào tạo một tác nhân đơn giản phải mất hàng trăm, nếu không muốn nói là hàng nghìn tập.

Hãy tưởng tượng một chiếc xe tự hành sẽ cần bao nhiêu tập để khám phá đầy đủ không gian trạng thái của nó, thế giới.

Ngoài việc mất nhiều thời gian hơn, việc đào tạo với các tác nhân vật lý còn tốn kém hơn nhiều vì bạn cần mua robot và tính toán mọi khoản bảo trì.

Sẽ thật lý tưởng nếu chúng ta có thể huấn luyện những đặc vụ như vậy mà không cần phải cung cấp cho họ cơ thể vật chất.

Phần 6.4.3, Trình mô phỏng

Trình mô phỏng giải quyết các mối quan tâm trước đó. Thay vì sử dụng robot đắt tiền hoặc chế tạo ô tô với các cảm biến cần thiết, thay vào đó chúng ta có thể sử dụng phần mềm máy tính để mô phỏng những trải nghiệm mà môi trường sẽ mang lại.

Ví dụ: khi đào tạo các đặc vụ lái ô tô tự động, thay vì trang bị cho ô tô những cảm biến cần thiết và triển khai mô hình trên ô tô thực, chúng ta có thể chỉ đào tạo các đặc vụ trong môi trường phần mềm, chẳng hạn như trò chơi lái xe, Grand Theft Auto.

Tác nhân sẽ nhận đầu vào là hình ảnh xung quanh và nó sẽ được đào tạo để đưa ra các hành động lái xe đưa phương tiện đến đích đã được lập trình một cách an toàn nhất có thể.

Các trình mô phỏng không chỉ rẻ hơn đáng kể để đào tạo các đại lý mà các đặc vụ còn có thể đào tạo nhanh hơn nhiều vì họ có thể tương tác với môi trường mô phỏng nhanh hơn nhiều so với trong đời thực.

Nếu bạn cần xem và hiểu một bộ phim dài hai giờ, bạn sẽ phải mất hai giờ. Nếu bạn tập trung cao độ hơn, bạn có thể tăng tốc độ phát lại lên hai hoặc ba, giảm lượng thời gian cần thiết xuống còn một giờ hoặc ít hơn một chút.

Mặt khác, máy tính có thể được hoàn thành trước khi bạn xem màn đầu tiên. Ví dụ: một máy tính 8GPU, có thể thuê từ dịch vụ đám mây, chạy ResNet 50, một mô hình học sâu đã được thiết lập để phân loại hình ảnh, có thể xử lý hơn 700 hình ảnh mỗi giây.

Trong một bộ phim dài hai giờ chạy ở tốc độ 24 khung hình/giây, tiêu chuẩn ở Hollywood, có 172.800 khung hình cần được xử lý. Điều này sẽ cần bốn phút để hoàn thành.

Chúng tôi cũng có thể tăng tốc độ phát lại cho mô hình học sâu của mình một cách hiệu quả bằng cách giảm từng khung hình, điều này sẽ giảm thời gian xử lý của chúng tôi xuống dưới hai phút.

Chúng ta cũng có thể sử dụng nhiều máy tính hơn để giải quyết vấn đề để tăng sức mạnh xử lý. Để có một ví dụ về học tăng cường gần đây hơn, các bot Open AI 5 có thể chơi 180 năm trò chơi Dota 2 mỗi ngày.

Bạn có được hình ảnh. Máy tính có thể xử lý nhanh hơn chúng ta và đó là lý do tại sao các trình mô phỏng lại có giá trị.