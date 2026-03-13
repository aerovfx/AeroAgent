# Chương 9. Học tăng cường đa tác nhân Học tăng cường sâu trong hành động, Phiên bản video được dịch

---

Chương 9. Học tăng cường đa tác nhân

Chương này đề cập đến lý do tại sao Q-learning thông thường có thể thất bại trong cài đặt đa tác nhân.

Làm thế nào để đối phó với lời nguyền của chiều với nhiều tác nhân.

Cách triển khai các mô hình Q-learning đa tác nhân có thể nhận biết các tác nhân khác.

Cách mở rộng quy mô Q-learning đa tác nhân bằng cách sử dụng xấp xỉ trường trung bình.

Cách sử dụng DQN để điều khiển hàng chục tác nhân trong trò chơi và mô phỏng vật lý đa tác nhân.

Cho đến nay, các thuật toán học tăng cường mà chúng tôi đã đề cập, Q-learning, độ dốc chính sách và thuật toán phê bình tác nhân đều đã được áp dụng để kiểm soát một tác nhân duy nhất trong một môi trường.

Nhưng còn những tình huống mà chúng ta muốn kiểm soát nhiều tác nhân có thể tương tác với nhau thì sao?

Ví dụ đơn giản nhất về điều này là trò chơi hai người chơi trong đó mỗi người chơi được triển khai như một tác nhân học tăng cường.

Nhưng có những tình huống khác mà chúng ta có thể muốn lập mô hình hàng trăm hoặc hàng nghìn tác nhân riêng lẻ đều tương tác với nhau, chẳng hạn như mô phỏng lưu lượng truy cập.

Trong chương này, bạn sẽ tìm hiểu cách điều chỉnh những gì bạn đã học cho đến nay vào kịch bản đa tác nhân này bằng cách triển khai một thuật toán có tên là Q-learning trường trung bình, MFQ.

Lần đầu tiên được mô tả trong một bài báo có tiêu đề Học tập tăng cường đa tác nhân trường trung bình của Yao Dong Yang năm 2018.

Mục 9.1. Từ một đến nhiều đại lý.

Trong trường hợp trò chơi, môi trường có thể chứa các tác nhân khác mà chúng ta không kiểm soát, thường được gọi là nhân vật không phải người chơi, NPC.

Ví dụ, trong chương 8, chúng tôi đã đào tạo một đặc vụ để chơi Super Mario Brothers, trò chơi có nhiều NPC.

Những NPC này được điều khiển bởi một số logic trò chơi vô hình khác, nhưng họ có thể và thường tương tác với người chơi chính.

Từ quan điểm của mạng Q sâu, đặc vụ DQN của chúng tôi, những NPC này không gì khác hơn là những khuôn mẫu về trạng thái môi trường thay đổi theo thời gian.

DQN của chúng tôi không trực tiếp biết được hành động của những người chơi khác. Đây không phải là vấn đề vì những NPC này không học được. Họ có chính sách cố định.

Như bạn sẽ thấy trong chương này, đôi khi chúng tôi muốn vượt ra ngoài các NPC đơn thuần và thực sự mô hình hóa hành vi của nhiều tác nhân tương tác học hỏi, Hình 9.1.

Và điều này đòi hỏi phải điều chỉnh lại một chút khung học tập tăng cường cơ bản mà bạn đã học được trong cuốn sách này.

Hình 9.1. Trong cài đặt nhiều tác nhân, hành động của mỗi tác nhân không chỉ ảnh hưởng đến sự phát triển của môi trường mà còn ảnh hưởng đến chính sách của các tác nhân khác dẫn đến các tương tác tác nhân rất năng động.

Môi trường sẽ tạo ra trạng thái và phần thưởng mà mỗi tác nhân giành được thông qua J sử dụng để thực hiện các hành động bằng chính sách của riêng họ.

Tuy nhiên, chính sách của mỗi đại lý sẽ ảnh hưởng đến tất cả các chính sách của đại lý khác.

Ví dụ: hãy tưởng tượng rằng chúng ta muốn trực tiếp kiểm soát hành động của nhiều tác nhân tương tác trong một số môi trường bằng thuật toán học tăng cường sâu.

Ví dụ: có những trò chơi có nhiều người chơi được nhóm thành các đội và chúng tôi có thể muốn phát triển một thuật toán có thể cho một nhóm người chơi trong một đội đấu với một đội khác.

Hoặc chúng ta có thể muốn điều khiển hành động của hàng trăm chiếc ô tô mô phỏng để mô hình hóa các mô hình giao thông. Hoặc có thể chúng tôi là nhà kinh tế học và chúng tôi muốn mô hình hóa hành vi của hàng nghìn tác nhân theo mô hình nền kinh tế.

Đây là một tình huống khác với việc có NPC vì không giống như NPC, các đặc vụ khác này đều học và việc học của họ bị ảnh hưởng lẫn nhau.

Cách đơn giản nhất để mở rộng những gì chúng ta đã biết vào cài đặt nhiều tác nhân là khởi tạo nhiều DQN hoặc một số thuật toán tương tự khác cho các tác nhân khác nhau.

Tại mỗi tác nhân, hãy nhìn nhận môi trường như hiện tại và thực hiện hành động.

Nếu các tác nhân mà chúng tôi đang cố gắng kiểm soát đều sử dụng cùng một chính sách, đó là một giả định hợp lý trong một số trường hợp, chẳng hạn như trong trò chơi nhiều người chơi trong đó mỗi người chơi giống hệt nhau, thì chúng tôi thậm chí có thể sử dụng lại một DQN duy nhất.

Đó là một tập hợp các tham số để mô hình hóa nhiều tác nhân.

Cách tiếp cận này được gọi là QLearning độc lập, ILQ và nó hoạt động khá tốt, nhưng nó bỏ sót một thực tế là sự tương tác giữa các tác nhân ảnh hưởng đến việc ra quyết định của mỗi tác nhân.

Với thuật toán ILQ, mỗi tác nhân hoàn toàn không biết các tác nhân khác đang làm gì và hành động của các tác nhân khác có thể ảnh hưởng đến chính nó như thế nào.

Mỗi tác nhân chỉ nhận được một đại diện trạng thái của môi trường, bao gồm trạng thái hiện tại của mỗi tác nhân khác.

Nhưng về cơ bản, nó coi hoạt động của các tác nhân khác trong môi trường là tiếng ồn, vì hành vi của các tác nhân khác nhiều nhất chỉ có thể dự đoán được một phần, Hình 9.2.

Hình 9.2. Trong QLearning độc lập, một tác nhân không trực tiếp nhận thức hành động của các tác nhân khác mà giả vờ rằng họ là một phần của môi trường.

Đây là một giá trị gần đúng làm mất đi sự đảm bảo hội tụ mà QLearning có trong cài đặt tác nhân duy nhất, vì các tác nhân khác làm cho môi trường không cố định.

Trong QLearning thông thường mà chúng tôi đã thực hiện cho đến nay, khi chỉ có một tác nhân duy nhất trong môi trường, chúng tôi biết hàm Q sẽ hội tụ đến giá trị tối ưu, vì vậy chúng tôi sẽ hội tụ về một chính sách tối ưu.

Về mặt toán học, nó được đảm bảo hội tụ trong thời gian dài.

Điều này là do trong cài đặt tác nhân đơn lẻ, môi trường là cố định, nghĩa là việc phân phối phần thưởng cho một hành động nhất định ở một trạng thái nhất định luôn giống nhau, Hình 9.3.

Tính năng cố định này bị vi phạm trong cài đặt nhiều tác nhân, vì phần thưởng mà một tác nhân riêng lẻ nhận được sẽ thay đổi không chỉ dựa trên hành động của chính nó mà còn dựa trên hành động của các tác nhân khác.

Điều này là do tất cả các tác nhân đều là các tác nhân học tăng cường, học qua kinh nghiệm, chính sách của chúng liên tục thay đổi để đáp ứng với những thay đổi của môi trường.

Nếu chúng tôi sử dụng ILQ trong môi trường không cố định này, chúng tôi sẽ mất đảm bảo hội tụ và điều này có thể làm giảm đáng kể hiệu suất của QLearning độc lập.

Hình 9.3. Trong một môi trường đứng yên, giá trị dự kiến, tức là giá trị trung bình, theo thời gian đối với một trạng thái nhất định sẽ không đổi, đứng yên.

Bất kỳ quá trình chuyển đổi trạng thái cụ thể nào cũng có thể có thành phần ngẫu nhiên, do đó chuỗi thời gian trông có vẻ ồn ào, nhưng giá trị trung bình của chuỗi thời gian là không đổi.

Trong môi trường không cố định, giá trị mong đợi của một quá trình chuyển đổi trạng thái nhất định sẽ thay đổi theo thời gian, giá trị này được mô tả trong chuỗi thời gian này dưới dạng giá trị trung bình hoặc đường cơ sở thay đổi theo thời gian.

Hàm Q đang cố gắng tìm hiểu giá trị kỳ vọng của các hành động trạng thái và nó chỉ có thể hội tụ nếu các giá trị hành động trạng thái đứng yên.

Nhưng trong cài đặt nhiều tác nhân, các giá trị hành động trạng thái dự kiến ​​có thể thay đổi theo thời gian do chính sách phát triển của các tác nhân khác.

Hàm Q thông thường là hàm Q của S, A, lấy đầu vào từ các tập S và A rồi ánh xạ tới tập số thực R, Hình 9.4.

Đó là một chức năng từ cặp hành động trạng thái đến phần thưởng, một số thực.

Chúng ta có thể khắc phục các vấn đề với ILQ bằng cách tạo ra hàm Q phức tạp hơn một chút, kết hợp kiến ​​thức về hành động của các tác nhân khác.

Đây là hàm Q dành cho tác nhân được lập chỉ mục bởi J, lấy một bộ trạng thái, hành động của tác nhân J và tất cả các hành động của tác nhân khác, được ký hiệu là trừ J, phát âm là không phải J, cho phần thưởng dự đoán cho bộ dữ liệu này.

Một lần nữa, chỉ là một con số thực.

Được biết, hàm Q thuộc loại này lấy lại sự đảm bảo hội tụ rằng cuối cùng nó sẽ học các hàm chính sách và giá trị tối ưu, và do đó, hàm Q được sửa đổi này có thể hoạt động tốt hơn nhiều.

Hình 9.4. Hàm Q nhận một trạng thái và tạo ra các giá trị hành động trạng thái, các giá trị Q, sau đó được hàm chính sách sử dụng để tạo ra một hành động.

Ngoài ra, chúng ta có thể huấn luyện trực tiếp một hàm chính sách hoạt động trên một trạng thái và trả về phân bố xác suất cho các hành động.

Thật không may, hàm Q mới này không thể thực hiện được khi số lượng tác nhân lớn, bởi vì không gian tác động chung A, chứ không phải J, cực kỳ lớn và tăng theo cấp số nhân theo số lượng tác nhân.

Hãy nhớ cách chúng ta mã hóa một hành động? Chúng tôi sử dụng một vectơ có độ dài bằng số lượng hành động.

Nếu chúng ta muốn mã hóa một hành động đơn lẻ, chúng ta biến đây thành một vectơ một điểm nóng trong đó tất cả các phần tử đều bằng 0, ngoại trừ vị trí tương ứng với hành động được đặt thành một.

Ví dụ: trong môi trường thế giới lưới, tác nhân có bốn hành động lên, xuống, trái, phải.

Vì vậy, chúng tôi mã hóa các hành động dưới dạng vectơ có độ dài bốn, trong đó một không không không có thể được mã hóa thành lên và 0 một không không có thể được mã hóa xuống, v.v.

Hãy nhớ rằng, chính sách pi, ánh xạ các trạng thái từ tập S tới các hành động trong tập A, là một hàm nhận một trạng thái và trả về một hành động.

Nếu đó là một chính sách xác định, nó sẽ phải trả về một trong những vectơ nóng này. Nếu đó là chính sách ngẫu nhiên, nó sẽ trả về phân bố xác suất cho các hành động, ví dụ: 0,25, 0,25, 0,2, 0,3.

Sự tăng trưởng theo cấp số nhân là do nếu chúng ta muốn mã hóa rõ ràng một hành động chung.

Ví dụ: hành động chung của hai tác nhân với bốn hành động trong thế giới lưới, khi đó chúng ta phải sử dụng một vectơ bốn bình phương bằng 16 chiều dài một vectơ nóng thay vì chỉ một vectơ bốn chiều dài.

Điều này là do có 16 cách kết hợp hành động khác nhau có thể có giữa hai tác nhân, mỗi tác nhân có bốn hành động.

Đặc vụ một, hành động một, tác nhân hai, hành động bốn, tác nhân một, hành động ba, tác nhân hai, hành động ba, v.v. Xem Hình 9.5.

Nếu mỗi tác nhân có một không gian hành động có kích thước bốn, nghĩa là nó được biểu thị bằng một vectơ nóng bốn phần tử, thì không gian tác động chung của hai tác nhân là bốn bình phương bằng 16, hoặc bốn lũy thừa của N, trong đó N là số lượng tác nhân.

Điều này có nghĩa là sự tăng trưởng của không gian hoạt động chung theo cấp số nhân theo số lượng tác nhân.

Hình bên phải hiển thị kích thước không gian hành động chung cho các tác nhân có không gian hành động riêng lẻ có kích thước hai.

Ngay cả khi chỉ có 25 tác nhân, không gian hành động chung sẽ trở thành một vectơ nóng gồm 33.554.432 phần tử, điều này không thực tế về mặt tính toán để làm việc.

Nếu chúng ta muốn mô hình hóa hành động chung của ba tác nhân, chúng ta phải sử dụng một vectơ bốn lập phương có độ dài 64.

Vì vậy, nói chung đối với thế giới lưới, chúng ta phải sử dụng vectơ có độ dài N, trong đó N là số lượng tác nhân.

Đối với bất kỳ môi trường nào, kích thước của vectơ hành động chung sẽ là ống A lũy thừa N, trong đó ống A đề cập đến kích thước của không gian hành động, nghĩa là số lượng hành động rời rạc.

Đó là một vectơ tăng trưởng theo cấp số nhân về số lượng tác nhân, và điều này là không thực tế và khó điều trị đối với bất kỳ số lượng tác nhân đáng kể nào.

Tăng trưởng theo cấp số nhân luôn là một điều xấu, vì điều đó có nghĩa là thuật toán của bạn không thể mở rộng quy mô.

Không gian hành động chung lớn theo cấp số nhân này là vấn đề phức tạp mới chính mà việc học tăng cường đạo đức đa tác nhân mang lại và đó là vấn đề chúng ta sẽ dành trong chương này để giải quyết.