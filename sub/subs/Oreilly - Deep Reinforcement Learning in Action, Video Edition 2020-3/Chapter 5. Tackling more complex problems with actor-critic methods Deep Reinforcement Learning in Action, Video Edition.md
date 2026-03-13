# Chương 5. Giải quyết các vấn đề phức tạp hơn bằng phương pháp phê bình tác nhân Học tăng cường sâu trong thực tế, Phiên bản video được dịch

---

Chương 5. Giải quyết các vấn đề phức tạp hơn bằng phương pháp phê bình diễn viên.

Chương này đề cập đến những hạn chế của thuật toán tăng cường.

Giới thiệu một nhà phê bình để cải thiện hiệu quả mẫu và giảm phương sai.

Sử dụng hàm lợi thế để tăng tốc độ hội tụ.

Tăng tốc mô hình bằng cách đào tạo song song.

Trong chương trước, chúng tôi đã giới thiệu một phiên bản cơ bản của phương pháp gradient chính sách được gọi là củng cố.

Thuật toán này hoạt động tốt với ví dụ thăm dò giỏ hàng đơn giản,

nhưng chúng tôi muốn có thể áp dụng phương pháp học tăng cường vào những môi trường phức tạp hơn.

Bạn đã thấy rằng mạng Q sâu có thể khá hiệu quả khi không gian hành động rời rạc,

nhưng nó có nhược điểm là cần có một chức năng chính sách riêng biệt, chẳng hạn như Epsilon tham lam.

Trong chương này, bạn sẽ học cách kết hợp các ưu điểm của cốt thép và của DQN.

để tạo ra một lớp thuật toán gọi là mô hình phê bình diễn viên.

Những điều này đã được chứng minh là mang lại kết quả tiên tiến trong nhiều lĩnh vực.

Thuật toán tăng cường thường được triển khai như một thuật toán phân đoạn,

nghĩa là chúng tôi chỉ áp dụng nó để cập nhật các tham số mô hình của mình sau khi tác nhân đã hoàn thành toàn bộ tập,

và thu thập phần thưởng trên đường đi.

Hãy nhớ rằng chính sách là một chức năng. Tích của pi và s hàm ý xác suất xảy ra sự kiện a.

Nghĩa là, đó là một hàm nhận một trạng thái và trả về phân bố xác suất cho các hành động, hình 5.1.

Hình 5.1. Hàm chính sách nhận một trạng thái và trả về phân bố xác suất theo các hành động,

trong đó xác suất cao hơn cho biết hành động có nhiều khả năng mang lại phần thưởng cao nhất.

Sau đó, chúng tôi lấy mẫu từ phân phối này để có được một hành động sao cho hành động có thể xảy ra nhất, hành động tốt nhất, có nhiều khả năng được lấy mẫu nhất.

Vào cuối tập, chúng tôi tính toán lợi nhuận của tập, về cơ bản là tổng số phần thưởng đã giảm giá trong tập.

Tiền lãi được tính như...

Biểu hiện này...

Sau khi trò chơi kết thúc, phần thưởng cho tập đó là tổng của tất cả các phần thưởng nhận được nhân với tỷ lệ chiết khấu tương ứng,

trong đó gamma t phân rã theo cấp số nhân theo thời gian.

Ví dụ: nếu hành động 1 được thực hiện ở trạng thái a và dẫn đến kết quả là cộng 10,

xác suất hành động 1 cho trước trạng thái a sẽ tăng lên một chút,

trong khi nếu hành động 2 được thực hiện ở trạng thái a và dẫn đến kết quả là âm 20,

xác suất của hành động 2 cho trạng thái a sẽ giảm. Về cơ bản, chúng tôi giảm thiểu hàm mất mát này.

Xem biểu hiện này.

Điều này nói lên rằng, giảm thiểu logarit của xác suất xảy ra hành động ở một trạng thái nhất định s nhân với kết quả trả về r.

Nếu phần thưởng là một số dương lớn và xác suất xảy ra sự kiện a,

1 với điều kiện s a bằng 0,5, ví dụ:

giảm thiểu tổn thất này sẽ liên quan đến việc tăng xác suất này.

Vì vậy, với phần củng cố, chúng tôi chỉ tiếp tục lấy mẫu các giai đoạn hoặc quỹ đạo nói chung,

từ tác nhân và môi trường, đồng thời cập nhật định kỳ các tham số chính sách bằng cách giảm thiểu tổn thất này.

Lưu ý...

Hãy nhớ rằng, chúng ta chỉ áp dụng logarit cho xác suất vì xác suất bị giới hạn bởi 0 và 1,

trong khi xác suất log được giới hạn bởi âm vô cực và 0,

cho rằng các số được biểu diễn bằng số bit hữu hạn, chúng ta có thể biểu diễn rất nhỏ,

gần bằng 0 hoặc rất lớn, gần bằng 1.

Xác suất không tràn hoặc tràn độ chính xác số của máy tính.

Logarit cũng có các tính chất toán học hay hơn mà chúng tôi sẽ không đề cập đến,

nhưng đó là lý do tại sao bạn hầu như luôn thấy xác suất nhật ký được sử dụng trong các thuật toán và bài viết về máy học,

mặc dù về mặt khái niệm chúng tôi quan tâm đến xác suất thô.

Bằng cách lấy mẫu toàn bộ tập phim, chúng tôi hiểu khá rõ về giá trị thực sự của một hành động,

bởi vì chúng ta có thể thấy những tác động xuôi chiều của nó chứ không chỉ là tác động tức thời,

có thể gây hiểu nhầm do tính ngẫu nhiên trong môi trường.

Việc lấy mẫu tập phim đầy đủ này được thực hiện dưới sự bảo trợ của các phương pháp tiếp cận Monte Carlo,

nhưng không phải tất cả các môi trường đều có tính chất từng đợt và đôi khi chúng tôi muốn có thể cập nhật

theo kiểu gia tăng hoặc trực tuyến, nghĩa là thực hiện cập nhật đều đặn bất kể điều gì đang diễn ra trong môi trường.

Mạng Q sâu của chúng tôi hoạt động tốt trong cài đặt không theo giai đoạn và nó có thể được coi là một thuật toán học tập trực tuyến,

nhưng nó đòi hỏi một bộ đệm phát lại trải nghiệm để học một cách hiệu quả.

Bộ đệm phát lại là cần thiết vì việc học trực tuyến thực sự nơi cập nhật tham số được thực hiện sau mỗi hành động

không ổn định do sự khác biệt vốn có của môi trường.

Một hành động được thực hiện một lần có thể tình cờ dẫn đến một phần thưởng tiêu cực lớn,

nhưng trong kỳ vọng, phần thưởng dài hạn trung bình, nó có thể là một hành động tốt,

cập nhật sau một hành động có thể dẫn đến cập nhật tham số sai, cuối cùng sẽ ngăn cản việc học tập đầy đủ.

Trong chương này, chúng tôi sẽ giới thiệu một loại phương pháp gradient chính sách mới được gọi là Nhà phê bình tác nhân lợi thế phân tán,

DA2C, sẽ có lợi thế học tập trực tuyến của DQN mà không cần bộ đệm phát lại.

Nó cũng sẽ có những ưu điểm của các phương pháp chính sách trong đó chúng ta có thể lấy mẫu trực tiếp các hành động từ phân bổ xác suất theo các hành động,

do đó loại bỏ nhu cầu lựa chọn một chính sách, chẳng hạn như Chính sách tham lam của Epsilon,

rằng chúng ta cần Phần 5.1, kết hợp chức năng giá trị và chính sách.

Điều tuyệt vời về QLearning là nó học trực tiếp từ thông tin có sẵn trong môi trường, đó chính là phần thưởng.

Về cơ bản, nó học cách dự đoán phần thưởng mà chúng tôi gọi là Giá trị.

Nếu chúng ta sử dụng DQN để chơi pinball, nó sẽ học cách dự đoán các giá trị cho hai hành động chính, vận hành các mái chèo trái và phải.

Sau đó, chúng tôi có thể tự do sử dụng các giá trị này để quyết định hành động nào sẽ thực hiện, thường chọn hành động được liên kết với giá trị cao nhất.

Hàm gradient chính sách được kết nối trực tiếp hơn với khái niệm củng cố, vì chúng tôi củng cố tích cực các hành động dẫn đến phần thưởng tích cực,

và củng cố tiêu cực các hành động dẫn đến phần thưởng tiêu cực.

Do đó, hàm chính sách sẽ tìm hiểu hành động nào là tốt nhất theo cách ẩn hơn.

Trong pinball, nếu chúng ta đánh vào mái chèo bên trái và ghi được nhiều điểm, hành động đó sẽ được củng cố tích cực và sẽ có nhiều khả năng được chọn vào lần tiếp theo khi trò chơi ở trạng thái tương tự.

Nói cách khác, QLearning, chẳng hạn như DQN, sử dụng hàm có thể huấn luyện để mô hình hóa trực tiếp giá trị, phần thưởng mong đợi của một hành động ở một trạng thái.

Đây là một cách rất trực quan để giải quyết quá trình ra quyết định Markov, MDP.

Vì chúng tôi chỉ quan sát các trạng thái và phần thưởng nên việc dự đoán phần thưởng là điều hợp lý và sau đó chỉ thực hiện các hành động có phần thưởng được dự đoán cao.

Mặt khác, chúng tôi thấy được lợi ích của việc học chính sách trực tiếp, chẳng hạn như độ dốc chính sách.

Cụ thể là, chúng ta nhận được phân bố xác suất có điều kiện thực sự cho các hành động, xác suất của sự kiện A, với các điều kiện S, mà chúng ta có thể trực tiếp lấy mẫu để thực hiện một hành động.

Đương nhiên, ai đó đã quyết định rằng có thể nên kết hợp hai cách tiếp cận này để tận dụng được lợi ích của cả hai.

Khi xây dựng thuật toán học chính sách giá trị kết hợp như vậy, chúng ta sẽ bắt đầu với người học chính sách làm nền tảng.

Có hai thách thức mà chúng tôi muốn vượt qua để tăng cường khả năng vững chắc cho người học chính sách.

Chúng tôi muốn cải thiện hiệu quả mẫu bằng cách cập nhật thường xuyên hơn.

Chúng tôi muốn giảm sự khác biệt của phần thưởng mà chúng tôi đã sử dụng để cập nhật mô hình của mình.

Những vấn đề này có liên quan với nhau, vì phương sai phần thưởng phụ thuộc vào số lượng mẫu chúng tôi thu thập, càng nhiều mẫu thì phương sai càng ít.

Ý tưởng đằng sau thuật toán chính sách giá trị kết hợp là sử dụng người học giá trị để giảm sự khác biệt về phần thưởng được sử dụng để đào tạo chính sách.

Nghĩa là, thay vì giảm thiểu tổn thất được tăng cường bao gồm tham chiếu trực tiếp đến lợi nhuận quan sát được, R, từ một tập, thay vào đó, chúng tôi thêm một giá trị cơ sở sao cho tổn thất hiện tại.

Xem hình này.

Ở đây, V của S là giá trị của trạng thái S, là hàm giá trị trạng thái, hàm của trạng thái, chứ không phải là hàm giá trị hành động, hàm của cả trạng thái và hành động, mặc dù hàm giá trị hành động cũng có thể được sử dụng.

Đại lượng này, V(S trừ R), được gọi là lợi thế.

Theo trực giác, số lượng lợi thế cho bạn biết một hành động tốt hơn như thế nào so với những gì bạn mong đợi.

Ghi chú.

Hãy nhớ rằng hàm giá trị, giá trị trạng thái hoặc giá trị hành động, hoàn toàn phụ thuộc vào việc lựa chọn chính sách.

Vì vậy chúng ta nên viết V pi của S để làm cho nó rõ ràng.

Tuy nhiên, chúng tôi đã bỏ chỉ số pi để đơn giản về mặt ký hiệu.

Ảnh hưởng của chính sách lên giá trị là rất quan trọng, vì chính sách luôn thực hiện các hành động ngẫu nhiên sẽ dẫn đến kết quả là tất cả các trạng thái ít nhiều có giá trị thấp như nhau.

Hãy tưởng tượng rằng chúng ta đang đào tạo một chính sách trong trò chơi thế giới lưới với các hành động riêng biệt và một không gian trạng thái riêng biệt nhỏ, sao cho chúng ta có thể sử dụng một vectơ trong đó mỗi vị trí trong vectơ đại diện cho một trạng thái riêng biệt và phần tử là phần thưởng trung bình được quan sát sau khi truy cập trạng thái đó.

Bảng tra cứu này sẽ là V của S. Chúng tôi có thể lấy mẫu hành động thứ nhất từ ​​chính sách và quan sát phần thưởng cộng 10, nhưng sau đó chúng tôi sẽ sử dụng bảng tra cứu giá trị của mình và thấy rằng trung bình chúng tôi nhận được cộng 4 sau khi truy cập trạng thái này.

Ưu điểm của hành động ở trạng thái này là 10 trừ 4 bằng cộng 6.

Điều này có nghĩa là khi thực hiện hành động đầu tiên, chúng tôi nhận được phần thưởng tốt hơn đáng kể so với những gì chúng tôi mong đợi, dựa trên phần thưởng trước đây từ trạng thái đó, điều này cho thấy rằng đó là một hành động tốt.

So sánh điều này với trường hợp chúng ta thực hiện hành động một và nhận được phần thưởng cộng 10, nhưng bảng tra cứu giá trị của chúng ta cho biết chúng ta dự kiến sẽ thấy cộng 15, vì vậy lợi thế là 10 trừ 15 bằng trừ 5.

Điều này cho thấy đây là một hành động tương đối tồi tệ mặc dù thực tế là chúng tôi đã nhận được phần thưởng tích cực khá lớn.

Thay vì sử dụng bảng tra cứu, chúng tôi sẽ sử dụng một số loại mô hình được tham số hóa, chẳng hạn như mạng nơ-ron có thể được huấn luyện để dự đoán phần thưởng mong đợi cho một trạng thái nhất định, vì vậy, chúng tôi muốn huấn luyện đồng thời mạng nơ-ron chính sách và mạng nơ-ron giá trị hành động hoặc giá trị trạng thái.

Các thuật toán thuộc loại này được gọi là phương pháp phê bình diễn viên trong đó diễn viên đề cập đến chính sách, bởi vì đó là nơi các hành động được tạo ra và nhà phê bình đề cập đến hàm giá trị, bởi vì đó một phần là điều cho tác nhân biết hành động của họ tốt như thế nào.

Vì chúng ta đang sử dụng R trừ V của S để huấn luyện chính sách thay vì chỉ V của S, đây được gọi là nhà phê bình tác nhân lợi thế, hình 5.2.

Hình 5.2. Việc học Q thuộc danh mục các phương pháp giá trị, vì chúng tôi cố gắng tìm hiểu các giá trị hành động, trong khi các phương pháp gradient chính sách như củng cố trực tiếp cố gắng tìm hiểu các hành động tốt nhất cần thực hiện.

Chúng ta có thể kết hợp hai kỹ thuật này thành cái gọi là kiến ​​trúc phê bình tác nhân.

Ghi chú. Những gì chúng tôi đã mô tả cho đến nay sẽ không được một số người coi là phương pháp phê bình diễn viên thực sự vì chúng tôi chỉ sử dụng hàm giá trị làm đường cơ sở chứ không sử dụng nó để khởi động bằng cách đưa ra dự đoán về trạng thái tương lai dựa trên trạng thái hiện tại.

Bạn sẽ thấy việc khởi động sớm phát huy tác dụng như thế nào.

Mạng chính sách có chức năng mất mát nhạy cảm phụ thuộc vào phần thưởng thu được ở cuối tập.

Nếu chúng ta cố gắng cập nhật trực tuyến với loại môi trường không phù hợp một cách ngây thơ, chúng ta có thể không bao giờ học được điều gì vì phần thưởng có thể quá thưa thớt.

Trong GridWorld mà chúng tôi đã giới thiệu ở chương 3, phần thưởng sẽ bị trừ 1 cho mỗi nước đi ngoại trừ cuối tập.

Phương pháp gradient chính sách cơ bản sẽ không biết nên củng cố hành động nào vì hầu hết các hành động đều dẫn đến cùng một phần thưởng là trừ 1.

Ngược lại, mạng Q có thể học các giá trị Q hợp lý, ngay cả khi phần thưởng thưa thớt, vì nó tự khởi động.

Khi chúng tôi nói thuật toán khởi động, chúng tôi muốn nói rằng nó có thể đưa ra dự đoán từ một dự đoán.

Nếu chúng tôi hỏi bạn nhiệt độ trong hai ngày tới sẽ như thế nào, trước tiên bạn có thể dự đoán nhiệt độ ngày mai sẽ như thế nào, sau đó dựa vào đó để dự đoán hai ngày nữa, hình 5.3.

Quá trình khởi động của bạn. Nếu dự đoán đầu tiên của bạn không tốt thì dự đoán thứ hai của bạn có thể còn tệ hơn, vì vậy việc khởi động sẽ tạo ra một nguồn sai lệch.

Độ lệch là độ lệch hệ thống so với giá trị thực của một cái gì đó, trong trường hợp này là so với giá trị Q thực.

Mặt khác, việc đưa ra dự đoán từ các dự đoán đưa ra một kiểu tự nhất quán dẫn đến phương sai thấp hơn.

Phương sai đúng như tên gọi của nó, là sự thiếu chính xác trong các dự đoán, có nghĩa là các dự đoán có thể thay đổi rất nhiều.

Trong ví dụ về nhiệt độ, nếu chúng ta đưa ra dự đoán nhiệt độ của ngày thứ hai dựa trên dự đoán của ngày thứ nhất, thì nó có thể sẽ không khác quá xa so với dự đoán của ngày thứ nhất.

Hình 5.3. Đọc từ trái qua phải. Dữ liệu thô được đưa vào mô hình nhiệt độ dự đoán để dự đoán nhiệt độ của ngày hôm sau.

Dự đoán đó sau đó được sử dụng trong một mô hình dự đoán khác dự đoán nhiệt độ của ngày thứ hai.

Chúng ta có thể tiếp tục làm điều này, nhưng những sai sót ban đầu sẽ tăng lên và những dự đoán của chúng ta sẽ trở nên không chính xác đối với những dự đoán ở xa.

Xu hướng và biến thể là những khái niệm chính liên quan đến tất cả quá trình học máy, không chỉ học sâu hay học tăng cường sâu, hình 5.4.

Nói chung, nếu bạn giảm độ lệch thì bạn sẽ tăng phương sai và ngược lại, hình 5.5.

Ví dụ: nếu chúng tôi yêu cầu bạn dự đoán nhiệt độ cho ngày mai và ngày hôm sau, bạn có thể cung cấp cho chúng tôi nhiệt độ cụ thể.

Dự báo nhiệt độ trong hai ngày là 20,1 độ C và 20,5 độ C. Đây là một dự đoán có độ chính xác cao.

Bạn đã đưa cho chúng tôi dự đoán nhiệt độ đến một phần mười độ, nhưng bạn không có quả cầu pha lê, vì vậy dự đoán của bạn gần như chắc chắn sẽ sai lệch một cách có hệ thống, thiên về bất kỳ quy trình dự đoán nào của bạn có liên quan.

Hoặc bạn có thể cho chúng tôi biết, dự báo nhiệt độ trong hai ngày là 15,25 độ C và 18,27 độ C.

Trong trường hợp này, dự đoán của bạn có nhiều mức chênh lệch hoặc chênh lệch vì bạn đưa ra phạm vi khá rộng, nhưng nó có độ lệch thấp, nghĩa là bạn có nhiều khả năng nhiệt độ thực sẽ giảm trong khoảng thời gian của mình.

Sự chênh lệch này có thể là do thuật toán dự đoán của bạn không đặt trọng số quá mức cho bất kỳ biến nào được sử dụng để dự đoán, do đó, nó không đặc biệt thiên vị theo bất kỳ hướng nào.

Thật vậy, các mô hình học máy thường được chính quy hóa bằng cách áp dụng hình phạt đối với độ lớn của các tham số trong quá trình đào tạo, nghĩa là các tham số lớn hơn hoặc nhỏ hơn 0 đáng kể sẽ bị phạt.

Chính quy hóa về cơ bản có nghĩa là sửa đổi quy trình học máy của bạn theo cách giảm thiểu tình trạng trang bị quá mức.

Hình 5.4. Sự đánh đổi phương sai thiên vị là một khái niệm học máy cơ bản cho biết bất kỳ mô hình học máy nào cũng sẽ có một mức độ sai lệch hệ thống nào đó so với phân phối dữ liệu thực và một mức độ phương sai nào đó.

Bạn có thể cố gắng giảm phương sai của mô hình của mình, nhưng nó sẽ luôn phải trả giá bằng độ lệch tăng lên.

Hình 5.5. Sự đánh đổi phương sai sai lệch, việc tăng độ phức tạp của mô hình có thể làm giảm sai lệch, nhưng nó sẽ làm tăng phương sai. Giảm phương sai sẽ làm tăng độ lệch.

Chúng tôi muốn kết hợp dự đoán giá trị phương sai thấp có độ lệch cao tiềm năng với dự đoán chính sách có độ lệch cao có khả năng sai lệch thấp để có được thứ gì đó có độ lệch và phương sai vừa phải, thứ sẽ hoạt động tốt trong cài đặt trực tuyến.

Hy vọng rằng vai trò của nhà phê bình đang bắt đầu trở nên rõ ràng. Tác nhân, mạng lưới chính sách, sẽ hành động, nhưng người phê bình, mạng lưới giá trị nhà nước, sẽ cho tác nhân biết hành động đó tốt hay xấu như thế nào thay vì chỉ sử dụng các tín hiệu khen thưởng thô có thể thưa thớt từ môi trường.

Như vậy, nhà phê bình sẽ là một thuật ngữ trong hàm mất mát của tác nhân. Nhà phê bình, giống như phương pháp học Q, sẽ học trực tiếp từ các tín hiệu khen thưởng đến từ môi trường, nhưng trình tự khen thưởng sẽ phụ thuộc vào hành động của tác nhân.

Vì vậy, diễn viên cũng ảnh hưởng đến nhà phê bình, mặc dù gián tiếp hơn. Hình 5.6.

Hình 5.6. Tổng quan chung về các mô hình phê bình diễn viên. Đầu tiên, tác nhân dự đoán hành động tốt nhất và chọn hành động sẽ thực hiện, hành động này sẽ tạo ra một trạng thái mới. Mạng phê bình tính toán giá trị của trạng thái cũ và trạng thái mới.

Giá trị tương đối của ST cộng 1 được gọi là lợi thế của nó và đây là tín hiệu được sử dụng để củng cố hành động mà người thực hiện đã thực hiện.

Tác nhân được đào tạo một phần bằng cách sử dụng các tín hiệu đến từ nhà phê bình, nhưng chính xác thì chúng ta huấn luyện hàm giá trị trạng thái trái ngược với giá trị hành động như thế nào? Q, các chức năng đã quen thuộc hơn.

Với các giá trị hành động, chúng tôi đã tính toán lợi nhuận kỳ vọng, tổng số phần thưởng được chiết khấu trong tương lai, cho một cặp hành động trạng thái nhất định.

Do đó, chúng ta có thể dự đoán liệu một cặp hành động trạng thái sẽ mang lại phần thưởng tích cực tốt đẹp, phần thưởng tiêu cực tồi tệ hay điều gì đó ở giữa.

Nhưng hãy nhớ lại rằng với DQN, mạng Q của chúng tôi trả về các giá trị hành động riêng biệt cho từng hành động riêng biệt có thể có. Vì vậy, nếu chúng ta sử dụng một chính sách hợp lý như Epsilon Gritty, giá trị trạng thái về cơ bản sẽ là giá trị hành động cao nhất.

Do đó, hàm giá trị trạng thái chỉ tính giá trị hành động cao nhất này thay vì tính toán riêng các giá trị hành động cho từng hành động.