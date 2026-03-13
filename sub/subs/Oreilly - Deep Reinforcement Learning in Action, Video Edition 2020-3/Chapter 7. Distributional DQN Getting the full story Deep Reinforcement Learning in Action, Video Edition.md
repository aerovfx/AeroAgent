# Chương 7. DQN phân phối Nhận toàn bộ câu chuyện Học tăng cường sâu trong thực tế, Phiên bản video được dịch

---

Chương 7.

Phân phối DQN.

Nhận được toàn bộ câu chuyện.

Chương này đề cập đến lý do tại sao phân phối xác suất đầy đủ lại tốt hơn một số duy nhất.

Mở rộng mạng deep-q thông thường để tạo ra phân bố xác suất đầy đủ trên các giá trị q.

Triển khai biến thể phân phối của DQN để chơi đường cao tốc Atari.

Mở rộng phương trình Bellman thông thường và biến thể phân phối của nó.

Ưu tiên phát lại kinh nghiệm để cải thiện tốc độ đào tạo.

Chúng tôi đã giới thiệu QLearning trong Chương 3 như một cách để xác định giá trị của việc thực hiện từng hành động có thể thực hiện trong một trạng thái nhất định.

Các giá trị được gọi là giá trị hành động hoặc giá trị Q.

Điều này cho phép chúng tôi áp dụng chính sách cho các giá trị hành động này và chọn các hành động được liên kết với giá trị hành động cao nhất.

Trong chương này, chúng tôi sẽ mở rộng QLearning để không chỉ xác định ước tính điểm cho các giá trị hành động mà còn xác định toàn bộ phân bổ giá trị hành động cho từng hành động.

Điều này được gọi là QLearning phân phối.

QLearning phân phối đã được chứng minh là mang lại hiệu suất tốt hơn đáng kể trên các điểm chuẩn tiêu chuẩn.

Và nó cũng cho phép đưa ra quyết định có nhiều sắc thái hơn, như bạn sẽ thấy.

Các thuật toán QLearning phân phối, kết hợp với một số kỹ thuật khác được đề cập trong cuốn sách này, hiện được coi là một tiến bộ tiên tiến trong học tập tăng cường.

Hầu hết các môi trường mà chúng tôi muốn áp dụng phương pháp học tăng cường có liên quan đến một số mức độ ngẫu nhiên hoặc không thể đoán trước, trong đó phần thưởng mà chúng tôi quan sát được cho một cặp hành động trạng thái nhất định có một số khác biệt.

Trong QLearning thông thường, mà chúng ta có thể gọi là QLearning giá trị kỳ vọng, chúng ta chỉ tìm hiểu mức trung bình của tập hợp phần thưởng quan sát được.

Nhưng bằng cách lấy mức trung bình, chúng ta đã bỏ đi những thông tin có giá trị về động lực của môi trường.

Trong một số trường hợp, phần thưởng được quan sát có thể có mô hình phức tạp hơn là chỉ tập trung quanh một giá trị duy nhất.

Có thể có hai hoặc nhiều cụm giá trị phần thưởng khác nhau cho một hành động trạng thái nhất định.

Ví dụ: đôi khi cùng một hành động trạng thái sẽ dẫn đến phần thưởng tích cực lớn và đôi khi dẫn đến phần thưởng tiêu cực lớn.

Nếu chúng ta chỉ lấy mức trung bình, chúng ta sẽ nhận được thứ gì đó gần bằng 0, đây không bao giờ là phần thưởng được quan sát thấy trong trường hợp này.

QLearning phân phối tìm cách có được bức tranh chính xác hơn về việc phân bổ các phần thưởng được quan sát.

Một cách để làm điều này là ghi lại tất cả các phần thưởng quan sát được đối với một cặp hành động trạng thái nhất định.

Tất nhiên, điều này sẽ đòi hỏi nhiều bộ nhớ và đối với không gian trạng thái có nhiều chiều, nó sẽ không thực tế về mặt tính toán.

Đây là lý do tại sao chúng ta phải thực hiện một số phép tính gần đúng.

Nhưng trước tiên, hãy tìm hiểu sâu hơn về giá trị mong đợi mà QLearning đang thiếu và những gì QLearning phân phối mang lại.

Mục 7.1. QLearning có vấn đề gì?

Loại giá trị kỳ vọng của QLearning mà chúng ta quen thuộc có sai sót và để minh họa điều này, chúng ta sẽ xem xét một ví dụ y tế trong thế giới thực.

Hãy tưởng tượng chúng tôi là một công ty y tế và chúng tôi muốn xây dựng một thuật toán để dự đoán xem một bệnh nhân bị huyết áp cao sẽ phản ứng như thế nào với liệu trình bốn tuần của một loại thuốc chống tăng huyết áp mới có tên là thuốc X.

Điều này sẽ giúp chúng tôi quyết định có nên kê đơn thuốc này cho từng bệnh nhân hay không.

Chúng tôi thu thập nhiều dữ liệu lâm sàng bằng cách thực hiện một thử nghiệm lâm sàng ngẫu nhiên trong đó chúng tôi chọn một nhóm bệnh nhân bị tăng huyết áp và phân ngẫu nhiên họ vào một nhóm điều trị, những người sẽ dùng thuốc thật và nhóm đối chứng, những người sẽ dùng giả dược và một loại thuốc hoạt tính.

Sau đó, chúng tôi ghi lại huyết áp theo thời gian trong khi bệnh nhân trong mỗi nhóm đang dùng loại thuốc tương ứng.

Cuối cùng, chúng ta có thể biết bệnh nhân nào phản ứng với thuốc và họ phản ứng tốt hơn như thế nào so với giả dược, hình 7.1.

Hình 7.1. Trong một thử nghiệm đối chứng ngẫu nhiên về một loại thuốc, chúng tôi nghiên cứu kết quả của một số phương pháp điều trị so với giả dược, một chất không có hoạt tính.

Chúng tôi muốn tách biệt tác động mà chúng tôi đang cố gắng điều trị, vì vậy, chúng tôi lấy một nhóm dân số mắc một số bệnh nào đó và sắp xếp ngẫu nhiên họ thành hai nhóm, một nhóm điều trị và một nhóm đối chứng.

Nhóm điều trị nhận được loại thuốc thử nghiệm mà chúng tôi đang thử nghiệm và nhóm đối chứng nhận được giả dược.

Sau một thời gian, chúng tôi có thể đo lường kết quả cho cả hai nhóm bệnh nhân và xem liệu trung bình nhóm điều trị có phản ứng tốt hơn nhóm dùng giả dược hay không.

Sau khi thu thập dữ liệu, chúng tôi có thể vẽ biểu đồ về sự thay đổi huyết áp sau bốn tuần dùng thuốc cho nhóm điều trị và nhóm đối chứng.

Chúng ta có thể thấy kết quả giống như trong Hình 7.2.

Hình 7.2. Biểu đồ về sự thay đổi huyết áp đo được ở nhóm đối chứng và nhóm điều trị trong một thử nghiệm đối chứng ngẫu nhiên mô phỏng.

Trục X là sự thay đổi huyết áp từ khi bắt đầu, trước khi điều trị và sau khi điều trị.

Chúng ta muốn huyết áp giảm nên số âm là tốt.

Chúng tôi đếm số lượng bệnh nhân có từng giá trị huyết áp thay đổi, do đó, mức cao nhất ở mức âm 3 đối với nhóm đối chứng có nghĩa là hầu hết những bệnh nhân đó đều bị tụt huyết áp 3 mm thủy ngân.

Bạn có thể thấy rằng có hai nhóm bệnh nhân trong nhóm điều trị.

Một nhóm đã giảm huyết áp đáng kể và nhóm khác có tác dụng tối thiểu hoặc không có tác dụng.

Chúng tôi gọi đây là phân phối lưỡng kim, trong đó chế độ là một từ khác để chỉ đỉnh cao trong phân phối.

Nếu lần đầu tiên bạn nhìn vào biểu đồ của nhóm đối chứng trong Hình 7.2, nó có vẻ là một phân bố giống như chuẩn tắc tập trung quanh âm 3,0 mm thủy ngân, một đơn vị áp suất, là mức giảm huyết áp khá không đáng kể, như bạn mong đợi từ giả dược.

Thuật toán của chúng tôi sẽ chính xác khi dự đoán rằng đối với bất kỳ bệnh nhân nào được dùng giả dược, mức thay đổi huyết áp dự kiến ​​của họ sẽ trung bình là âm 3,0 mm thủy ngân, mặc dù từng bệnh nhân có những thay đổi lớn hơn hoặc ít hơn giá trị trung bình đó.

Bây giờ hãy nhìn vào biểu đồ nhóm điều trị.

Sự phân bố của sự thay đổi huyết áp là lưỡng hình, nghĩa là có hai đỉnh, như thể chúng ta đã kết hợp hai phân phối chuẩn riêng biệt.

Chế độ ngoài cùng bên phải tập trung ở mức âm 2,5 mm thủy ngân, giống như nhóm đối chứng, cho thấy rằng phân nhóm này trong nhóm điều trị không được hưởng lợi từ thuốc so với giả dược.

Tuy nhiên, chế độ ngoài cùng bên trái tập trung ở mức âm 22,3 mm thủy ngân, giúp giảm huyết áp rất đáng kể.

Trên thực tế, nó hiệu quả hơn bất kỳ loại thuốc chống tăng huyết áp nào hiện có. Điều này một lần nữa chỉ ra rằng có một phân nhóm trong nhóm điều trị, nhưng phân nhóm này được hưởng lợi rất nhiều từ thuốc.

Nếu bạn là một bác sĩ và một bệnh nhân bị tăng huyết áp bước vào văn phòng của bạn, tất cả những yếu tố khác đều bình đẳng, bạn có nên kê cho họ loại thuốc mới này không?

Nếu bạn lấy giá trị kỳ vọng, giá trị trung bình, của phân bố nhóm điều trị, bạn sẽ chỉ nhận được sự thay đổi huyết áp khoảng âm 13 mm thủy ngân, nằm giữa hai chế độ trong phân bố.

Điều này vẫn có ý nghĩa so với giả dược, nhưng nó tệ hơn nhiều loại thuốc chống tăng huyết áp hiện có trên thị trường.

Theo tiêu chuẩn đó, loại thuốc mới dường như không có hiệu quả lắm, mặc dù thực tế là một số lượng lớn bệnh nhân đã nhận được lợi ích to lớn từ nó.

Hơn nữa, giá trị kỳ vọng là âm 13 mm thủy ngân đại diện rất kém cho sự phân bố, vì rất ít bệnh nhân thực sự giảm được mức huyết áp đó.

Bệnh nhân hầu như không có phản ứng với thuốc hoặc phản ứng rất mạnh. Có rất ít người trả lời vừa phải.

Hình 7.3 minh họa những hạn chế của các giá trị kỳ vọng so với việc xem phân phối đầy đủ. Nếu bạn sử dụng giá trị dự kiến ​​về sự thay đổi huyết áp cho từng loại thuốc và chỉ chọn loại thuốc có giá trị dự kiến ​​thấp nhất về mặt thay đổi huyết áp, bỏ qua những phức tạp cụ thể của từng bệnh nhân như tác dụng phụ, thì bạn sẽ hành động tối ưu ở cấp độ quần thể, nhưng không nhất thiết ở cấp độ cá nhân.

Hình 7.3 ở đây chúng ta so sánh thuốc A với thuốc X để xem loại nào làm giảm huyết áp nhiều nhất. Thuốc A có giá trị trung bình thấp hơn, dự kiến ​​là âm 15,5 milimét thủy ngân và độ lệch chuẩn thấp hơn, nhưng thuốc X là thuốc theo chế độ với một chế độ tập trung ở âm 22,5 milimét thủy ngân.

Lưu ý rằng đối với thuốc X hầu như không có bệnh nhân nào có huyết áp thay đổi gần giá trị trung bình.

Vậy điều này có liên quan gì đến học tăng cường sâu? Chà, học Q, như bạn đã học, mang lại cho chúng ta các giá trị hành động trạng thái, trung bình, chiết khấu theo thời gian, được mong đợi.

Như bạn có thể tưởng tượng, điều này có thể dẫn đến những hạn chế tương tự mà chúng ta đã thảo luận trong trường hợp thuốc được phân phối đa phương thức.

Việc học phân bố xác suất đầy đủ của các giá trị hành động trạng thái sẽ mang lại cho chúng ta nhiều sức mạnh hơn là chỉ học giá trị kỳ vọng, như trong học Q thông thường.

Với phân phối đầy đủ, chúng ta có thể biết liệu có tính đa phương thức trong các giá trị hành động trạng thái hay không và có bao nhiêu phương sai trong phân phối.

Hình 7.4 mô hình hóa sự phân bổ giá trị hành động cho ba hành động khác nhau và bạn có thể thấy rằng một số hành động có nhiều phương sai hơn những hành động khác.

Với thông tin bổ sung này, chúng tôi có thể sử dụng các chính sách nhạy cảm với rủi ro, các chính sách không chỉ nhằm mục đích tối đa hóa lợi ích mong đợi mà còn kiểm soát mức độ rủi ro mà chúng tôi gặp phải khi làm như vậy.

Hình 7.4. Đứng đầu. Hàm Q thông thường lấy một cặp trạng thái-hành động và tính giá trị Q liên quan.

Ở giữa, hàm Q phân phối lấy một cặp hành động trạng thái và tính toán phân bố xác suất trên tất cả các giá trị Q có thể có.

Xác suất được giới hạn trong khoảng 0, 1, do đó, nó trả về một vectơ có tất cả các phần tử trong 0, 1 và tổng của chúng là 1.

Đáy. Một ví dụ về phân phối giá trị Q được tạo bởi hàm Q phân phối cho ba hành động khác nhau đối với một số trạng thái.

Hành động A có thể dẫn đến phần thưởng trung bình là âm 5, trong khi hành động B có thể dẫn đến phần thưởng trung bình là cộng 4.

Thuyết phục nhất, một nghiên cứu thực nghiệm đã được thực hiện để đánh giá một số phương sai phổ biến và các cải tiến đối với thuật toán DQN ban đầu, bao gồm cả biến thể phân phối của DQN, để xem cái nào hiệu quả nhất khi sử dụng riêng lẻ và cái nào là quan trọng nhất khi kết hợp.

Rainbow, kết hợp những cải tiến trong học tập tăng cường sâu của Hessel, 2017.

Hóa ra, Q học phân phối là thuật toán hoạt động tốt nhất về tổng thể, trong số tất cả các cải tiến riêng lẻ đối với DQN mà họ đã thử nghiệm.

Họ kết hợp tất cả các kỹ thuật lại với nhau thành một DQN cầu vồng, được chứng minh là hiệu quả hơn nhiều so với bất kỳ kỹ thuật riêng lẻ nào.

Sau đó, họ thử nghiệm để xem thành phần nào là quan trọng nhất đối với sự thành công của cầu vồng và kết quả là học Q phân phối, học Q nhiều bước, được đề cập trong chương 5 và phát lại được ưu tiên, sẽ được đề cập ngắn gọn trong phần 7.7, trong đó quan trọng nhất đối với hiệu suất của thuật toán cầu vồng.

Trong chương này, bạn sẽ tìm hiểu cách triển khai mạng DQN phân phối, DIST DQN, tạo ra phân bố xác suất trên các giá trị hành động trạng thái cho mỗi hành động có thể có trong một trạng thái.

Chúng ta đã thấy một số khái niệm xác suất trong chương 4, trong đó chúng ta sử dụng mạng lưới thần kinh sâu như một hàm chính sách trực tiếp đưa ra phân bố xác suất cho các hành động.

Nhưng chúng tôi sẽ xem xét các khái niệm này và đi sâu hơn nữa ở đây, vì những khái niệm này rất quan trọng để hiểu để triển khai DIST DQN.

Cuộc thảo luận của chúng ta về xác suất và thống kê ban đầu có vẻ hơi quá hàn lâm, nhưng nó sẽ trở nên rõ ràng tại sao chúng ta cần những khái niệm này để triển khai thực tế.

Chương này là chương khó nhất về mặt khái niệm trong toàn bộ cuốn sách, vì nó chứa rất nhiều khái niệm xác suất mà ban đầu khó nắm bắt.

Ở đây cũng có nhiều môn toán hơn bất kỳ chương nào khác. Vượt qua được chương này là một thành tựu lớn.

Bạn sẽ học hoặc xem lại nhiều chủ đề cơ bản trong học máy và học tăng cường để giúp bạn hiểu rõ hơn về các lĩnh vực này.