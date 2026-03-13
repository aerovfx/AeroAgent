# Chương 7. Sử dụng Q-learning phân phối để chơi Học tập tăng cường sâu trên xa lộ trong thực tế, Phiên bản video đã được dịch

---

Phần 7.7, sử dụng Q phân phối để chơi trên đường cao tốc.

Cuối cùng chúng tôi đã sẵn sàng sử dụng thuật toán distdqn để chơi trò chơi Atari trên đường cao tốc.

Chúng tôi không cần bất kỳ chức năng chính nào khác ngoài những gì chúng tôi đã mô tả.

Chúng ta sẽ có một mô hình distdqn chính và một bản sao, mạng mục tiêu để ổn định quá trình đào tạo.

Chúng tôi sẽ sử dụng chiến lược tham lam Epsilon với giá trị Epsilon giảm dần so với Epix.

Với xác suất Epsilon, việc lựa chọn hành động sẽ là ngẫu nhiên,

nếu không, hành động sẽ được chọn bởi hàm hành động gạch dưới,

được lựa chọn dựa trên giá trị kỳ vọng cao nhất.

Chúng tôi cũng sẽ sử dụng cơ chế phát lại trải nghiệm, giống như với DQN thông thường.

Chúng tôi cũng sẽ giới thiệu một hình thức phát lại được ưu tiên rất cơ bản.

Với tính năng phát lại trải nghiệm thông thường, chúng tôi lưu trữ tất cả trải nghiệm mà tác nhân có trong bộ nhớ đệm có kích thước cố định,

và những trải nghiệm mới ngẫu nhiên thay thế những trải nghiệm cũ.

Sau đó, chúng tôi lấy mẫu ngẫu nhiên một lô từ bộ nhớ đệm này để huấn luyện.

Tuy nhiên, trong một trò chơi như Freeway, nơi hầu hết mọi hành động đều dẫn đến phần thưởng trừ một,

và chúng ta hiếm khi nhận được phần thưởng cộng 10 hoặc trừ 10, trí nhớ phát lại trải nghiệm sẽ bị chi phối nặng nề bởi dữ liệu về cơ bản đều nói lên điều giống nhau.

Nó không cung cấp nhiều thông tin cho đại lý và những trải nghiệm thực sự quan trọng như thắng hay thua trong trò chơi sẽ mang lại kết quả tốt.

Trò chơi trở nên loãng đi nhiều, làm chậm đáng kể quá trình học tập.

Để giảm bớt vấn đề này, bất cứ khi nào chúng ta thực hiện một hành động dẫn đến trạng thái thắng hoặc thua của trò chơi,

nghĩa là khi chúng ta nhận được phần thưởng âm 10 hoặc cộng 10,

chúng tôi thêm nhiều bản sao của trải nghiệm này vào bộ đệm phát lại để ngăn trải nghiệm đó bị pha loãng bởi tất cả các trải nghiệm trừ một phần thưởng.

Do đó, chúng tôi ưu tiên những trải nghiệm có nhiều thông tin nhất định hơn những trải nghiệm ít thông tin khác,

bởi vì chúng tôi thực sự muốn đặc vụ của mình tìm hiểu hành động nào dẫn đến thành công hay thất bại thay vì chỉ tiếp tục trò chơi.

Nếu bạn truy cập mã của chương này trên GitHub của cuốn sách này tại liên kết này,

bạn sẽ tìm thấy mã mà chúng tôi đã sử dụng để ghi lại các khung hình của trận đấu trực tiếp trong quá trình luyện tập.

Chúng tôi cũng ghi lại những thay đổi theo thời gian thực trong phân phối giá trị hành động,

để bạn có thể thấy cách chơi ảnh hưởng đến phân phối được dự đoán và ngược lại.

Chúng tôi không đưa mã đó vào cuốn sách này vì nó sẽ chiếm quá nhiều dung lượng.

Trong danh sách 7.13, chúng ta khởi tạo các siêu tham số và các biến mà chúng ta cần cho thuật toán DIST-DQN.

Liệt kê 7.13, DIST-DQN phát sơ bộ đường cao tốc.

Đây là tất cả các cài đặt và đối tượng bắt đầu mà chúng ta cần trước khi chuyển sang vòng đào tạo chính.

Tất cả đều gần giống như những gì chúng tôi đã làm trong bài kiểm tra mô phỏng,

ngoại trừ việc chúng tôi có cài đặt phát lại được ưu tiên để kiểm soát số lượng bản sao của một trải nghiệm mang tính thông tin cao, chẳng hạn như một chiến thắng.

Chúng ta nên thêm vào replay.

Chúng tôi cũng sử dụng chiến lược Epsilon-Tham lam và chúng tôi sẽ bắt đầu với giá trị Epsilon ban đầu cao,

và giảm nó trong quá trình huấn luyện xuống giá trị tối thiểu để duy trì mức độ khám phá tối thiểu.

Liệt kê 7.14, vòng đào tạo chính.

Hầu như tất cả những thứ này đều giống với loại mã mà chúng ta đã sử dụng cho DQN thông thường vài chương trước.

Thay đổi duy nhất là chúng tôi đang xử lý phân phối Q thay vì các giá trị Q đơn lẻ và chúng tôi sử dụng tính năng phát lại được ưu tiên.

Nếu bạn vẽ đồ thị các khoản lỗ, bạn sẽ có được kết quả giống như Hình 7.20.

Hình 7.20, biểu đồ tổn thất cho việc huấn luyện DIST-DQN trên đường cao tốc trò chơi Atari.

Mức lỗ giảm dần nhưng có mức tăng đột biến đáng kể do mạng mục tiêu cập nhật định kỳ.

Biểu đồ mất mát trong Hình 7.20 nhìn chung giảm xuống nhưng có độ nhọn do các cập nhật của mạng mục tiêu, giống như chúng ta đã thấy với ví dụ mô phỏng.

Nếu bạn điều tra danh sách phần thưởng được gạch dưới đến, bạn sẽ nhận được danh sách các phần thưởng, 1-1-1-1-1, cho biết có bao nhiêu lần vượt gà thành công đã xảy ra.

Nếu bạn nhận được bốn hoặc nhiều hơn, điều đó cho thấy một đại lý được đào tạo thành công.

Hình 7.21 hiển thị ảnh chụp màn hình trò chơi giữa buổi tập cùng với phân bổ giá trị hành động được dự đoán tương ứng.

Một lần nữa, hãy tham khảo mã GitHub để biết cách thực hiện việc này.

Hình 7.21, bên trái, ảnh chụp màn hình trò chơi trực tiếp trên xa lộ Atari.

Đúng, sự phân bổ giá trị hành động tương ứng của từng hành động được phủ lên.

Mũi nhọn bên phải tương ứng với hành động lên và mũi nhọn bên trái chủ yếu tương ứng với hành động không hoạt động.

Vì mức tăng đột biến bên phải lớn hơn nên người đại diện có nhiều khả năng thực hiện hành động tăng giá hơn, đây có vẻ là điều đúng đắn nên làm trong trường hợp này.

Thật khó để nhìn thấy, nhưng hành động tăng cũng có mức tăng đột biến ở phía trên mức tăng đột biến không hoạt động ở bên trái, do đó, phân phối giá trị hành động tăng là hai phương thức, cho thấy rằng việc thực hiện hành động tăng có thể dẫn đến phần thưởng trừ 1 hoặc phần thưởng cộng 10, nhưng phần thưởng cộng 10 có nhiều khả năng xảy ra hơn vì mức tăng đột biến đó cao hơn.

Trong Hình 7.21, bạn có thể thấy rằng phân bổ giá trị hành động cho hành động đi lên có hai chế độ, đỉnh, 1 ở âm 1 và chế độ kia ở cộng 10.

Giá trị kỳ vọng của phân phối này cao hơn nhiều so với các hành động khác nên hành động này sẽ được chọn.

Hình 7.22 hiển thị một số phân phối đã học trong bộ đệm phát lại trải nghiệm để giúp bạn có cái nhìn rõ hơn về các phân phối.

Mỗi hàng là một mẫu từ bộ đệm phát lại được liên kết với một trạng thái duy nhất. Mỗi hình trong một hàng là sự phân bổ giá trị hành động tương ứng cho các hành động không hoạt động, lên và xuống.

Phía trên mỗi con số là giá trị kỳ vọng của sự phân bổ đó. Bạn có thể thấy rằng trong tất cả các mẫu, hành động tăng có giá trị mong đợi cao nhất và nó có hai đỉnh rõ ràng, 1 ở mức âm 1 và một ở mức cộng 10.

Sự phân bổ cho hai hành động còn lại có nhiều phương sai hơn, bởi vì một khi tác nhân biết rằng đi lên là cách tốt nhất để giành chiến thắng thì ngày càng có ít kinh nghiệm sử dụng hai hành động còn lại, vì vậy chúng vẫn tương đối đồng đều.

Nếu chúng tôi tiếp tục đào tạo lâu hơn, cuối cùng chúng sẽ hội tụ đến đỉnh ở âm 1 và có thể là đỉnh nhỏ hơn ở âm 10. Vì với Epsilon Greedy, chúng tôi vẫn sẽ thực hiện một số hành động ngẫu nhiên.

Hình 7.22, mỗi cột có phân bố giá trị hành động cho một hành động cụ thể cho một trạng thái, hàng nhất định. Con số phía trên mỗi ô là giá trị kỳ vọng cho phân phối đó, là giá trị trung bình có trọng số cho phân phối đó.

Nhìn bằng mắt thì các phân bố này trông khá giống nhau, nhưng các giá trị mong đợi đủ khác biệt để dẫn đến các lựa chọn hành động khác nhau đáng kể.

Q-learning phân phối là một trong những cải tiến lớn nhất của Q-learning trong vài năm qua và nó vẫn đang được tích cực nghiên cứu. Nếu bạn so sánh dist-dqn với dqn thông thường, bạn sẽ thấy hiệu suất tổng thể tốt hơn với dist-dqn.

Người ta vẫn chưa hiểu rõ tại sao dist-dqn lại hoạt động tốt hơn nhiều, đặc biệt là khi chúng ta chỉ chọn các hành động dựa trên các giá trị mong đợi, nhưng có thể có một số lý do.

Một là việc đào tạo một mạng lưới thần kinh để dự đoán nhiều thứ cùng lúc đã được chứng minh là cải thiện khả năng khái quát hóa và hiệu suất tổng thể.

Trong chương này, dist-dqn của chúng ta đã học cách dự đoán ba phân bố xác suất đầy đủ thay vì một giá trị hành động duy nhất, do đó, các tác vụ phụ trợ này buộc thuật toán phải tìm hiểu các khái niệm trừu tượng mạnh mẽ hơn.

Chúng tôi cũng đã thảo luận về một hạn chế đáng kể trong cách chúng tôi triển khai dist-dqn, cụ thể là chúng tôi đang sử dụng phân bố xác suất rời rạc với độ hỗ trợ hữu hạn, vì vậy chúng tôi chỉ có thể biểu thị các giá trị hành động trong một phạm vi rất nhỏ, từ âm 10 đến 10.

Chúng tôi có thể làm cho phạm vi này rộng hơn với chi phí xử lý tính toán nhiều hơn, nhưng chúng tôi không bao giờ có thể biểu thị một giá trị lớn hoặc nhỏ tùy ý bằng phương pháp này.

Cách chúng tôi triển khai là sử dụng một tập hợp hỗ trợ cố định nhưng tìm hiểu tập hợp các xác suất liên quan.

Một cách khắc phục vấn đề này là thay vào đó sử dụng một tập hợp xác suất cố định trên một tập hợp hỗ trợ có thể thay đổi, đã học.

Ví dụ: chúng ta có thể sửa tensor xác suất của mình trong phạm vi từ 0,1 đến 0,9, ví dụ: mảng 0,1, 0,2, 0,3, 0,4, 0,5, 0,6, 0,7, 0,8, 0,9.

Và thay vào đó, chúng tôi có dist-dqn, dự đoán tập hợp các hỗ trợ liên quan cho các xác suất cố định này.

Nghĩa là, chúng tôi đang yêu cầu dist-dqn của mình tìm hiểu giá trị hỗ trợ nào có xác suất là 0,1 và 0,2, v.v.

Điều này được gọi là hồi quy lượng tử, bởi vì những xác suất cố định này cuối cùng đại diện cho các lượng tử của phân bố, hình 7.23.

Chúng tôi tìm hiểu các mức hỗ trợ ở và dưới phân vị thứ 50, xác suất 0,5, phân vị thứ 60, v.v.

Hình 7.23. Trong hồi quy lượng tử, thay vì tìm hiểu xác suất nào được gán cho một tập hợp hỗ trợ cố định, chúng ta tìm hiểu một tập hợp hỗ trợ tương ứng với một tập hợp xác suất cố định, lượng tử.

Ở đây bạn có thể thấy rằng giá trị trung bình là 1 vì nó ở phân vị thứ 50.

Với cách tiếp cận này, chúng ta vẫn có phân bố xác suất rời rạc, nhưng giờ đây chúng ta có thể biểu thị bất kỳ giá trị hành động nào có thể xảy ra.

Nó có thể nhỏ hoặc lớn tùy ý và chúng ta không có phạm vi cố định.