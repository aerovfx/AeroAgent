# 5 -Sự Trở Lại dịch

---

Trong bài giảng này, chúng ta sẽ định nghĩa thêm một thuật ngữ xứng đáng có bài giảng riêng.

Cho đến nay, tôi đã nói với bạn rằng mục tiêu của đại lý là tối đa hóa phần thưởng.

Nhưng như bạn nhớ lại, phần thưởng có thể được cấu trúc khác nhau trong các trò chơi khác nhau.

Ví dụ: trong Tic Tac Toe, bạn có thể nhận được điểm cộng nếu thắng hoặc điểm trừ nếu thua.

Mặt khác, nếu bạn đang giải một mê cung, bạn có thể bị trừ một ở mỗi bước.

Vậy việc tối đa hóa phần thưởng có ý nghĩa gì?

Nó có nghĩa là tối đa hóa phần thưởng ở bước tiếp theo?

Hay nó có nghĩa là tối đa hóa tổng phần thưởng trong toàn bộ tập phim?

Đây là câu trả lời.

Nói một cách chính xác hơn, mục tiêu của đại lý là tối đa hóa tổng số phần thưởng trong tương lai.

Tại sao vậy?

Chà, nó không thể tối đa hóa phần thưởng mà nó đã nhận được.

Những điều đó đã là quá khứ.

Chúng không thể thay đổi được.

Hơn nữa, chúng tôi không muốn chỉ tối đa hóa phần thưởng ở bước tiếp theo.

Điều gì sẽ xảy ra nếu chúng ta đang giải một mê cung và bị trừ một bước cho bất kỳ bước nào chúng ta thực hiện?

Trong trường hợp đó, người đại diện không được khuyến khích làm bất cứ điều gì hữu ích vì dù có làm gì đi nữa,

phần thưởng trước mắt vẫn là trừ một.

Vì vậy, mục tiêu thực sự của đặc vụ là tối đa hóa tổng số phần thưởng trong tương lai cho đến khi tập phim kết thúc.

Bằng cách này, đại lý cũng đang lên kế hoạch cho các bước đi trong tương lai của mình.

Nó phải có một số khái niệm về nơi nó sẽ kết thúc vì đó là cách duy nhất nó biết cách tối đa hóa phần thưởng trong tương lai.

Lấy một ví dụ thực tế, hãy xem xét lại ý tưởng chuẩn bị cho kỳ thi toán.

Đối với bài thi toán, bạn không nhận được bất kỳ phần thưởng nào cho đến khi hoàn thành bài thi.

Tín hiệu khen thưởng là điểm của bạn trong bài kiểm tra.

Nhưng hãy tưởng tượng tất cả những hành động cần thực hiện để thực sự tối đa hóa phần thưởng đó.

Bạn sẽ phải học, bạn sẽ phải làm bài tập về nhà, bạn sẽ phải từ bỏ việc giao lưu với bạn bè.

Trên thực tế, tất cả những hành động đó nghe có vẻ không bổ ích chút nào.

Và do đó, nếu động lực duy nhất của bạn là sự hài lòng ngay lập tức, nói cách khác, phần thưởng bạn sẽ nhận được ngay lập tức,

thì bạn sẽ không làm tốt bài kiểm tra toán của mình.

Thay vào đó, bạn phải tận dụng kế hoạch dài hạn.

Chắc chắn rồi, hôm nay tôi có thể không muốn học.

Nó có thể rất khó chịu và tôi sẽ bỏ lỡ chương trình truyền hình yêu thích của mình.

Nhưng vì bạn đang lên kế hoạch dài hạn nên bạn không chỉ nghĩ đến ngày hôm nay.

Bạn đang nghĩ về kết quả bài kiểm tra toán của mình.

Mong muốn tối đa hóa tổng lợi ích trong tương lai là cần thiết cho việc lập kế hoạch dài hạn.

Chúng tôi gọi tổng số phần thưởng trong tương lai là tiền lãi.

Chúng tôi mô tả lợi nhuận về mặt toán học bằng cách sử dụng ký hiệu G.

Bởi vì nó chỉ phụ thuộc vào phần thưởng trong tương lai nên nó phụ thuộc vào thời gian nên chúng tôi lập chỉ mục cho nó bằng chữ T.

Có thể nói lợi nhuận thu được tại thời điểm T là tổng số phần thưởng tại thời điểm T cộng 1 cho đến trạng thái cuối tại thời điểm T lớn.

Bây giờ có thể bạn đang thắc mắc, điều gì sẽ xảy ra nếu chúng ta có MDP chân trời vô hạn, một trò chơi không bao giờ kết thúc?

Trong trường hợp này, lợi nhuận của bạn có thể là vô cùng.

Vì vậy, chúng tôi giới thiệu một khái niệm được gọi là chiết khấu.

Giảm giá được sử dụng cho các nhiệm vụ dài vô tận, nhưng nó cũng được sử dụng cho các nhiệm vụ theo từng giai đoạn.

Chúng tôi giới thiệu một yếu tố chiết khấu được gọi là gamma.

Mỗi phần thưởng trong tương lai được tính bằng gamma theo sức mạnh nào đó.

Gamma thường là một số gần bằng 1, như 0,9 hay 0,99 hoặc 0,99.

Đó là một siêu tham số nên bạn sẽ phải chọn giá trị của nó dựa trên hiệu suất của nhân viên hỗ trợ.

Ý tưởng là, bạn càng đi sâu vào tương lai thì càng khó dự đoán.

Vì vậy, chúng tôi quan tâm đến việc nhận phần thưởng bây giờ nhiều hơn một chút so với sau này.

Theo trực giác, điều này hoạt động giống như tiền.

Tôi thà nhận 100 USD hôm nay còn hơn nhận 100 USD sau 10 năm nữa.

Trong 10 năm nữa, 100 USD sẽ có giá trị thấp hơn nhiều so với hiện nay do lãi suất.

Một tính năng quan trọng của việc hoàn trả mà chúng ta sẽ sử dụng trong suốt phần còn lại của phần này,

là nó có thể được định nghĩa đệ quy, nói cách khác, theo chính nó.

Cụ thể, lợi nhuận tại thời điểm t bằng lợi nhuận tại thời điểm t cộng 1 cộng gamma nhân lợi nhuận tại thời điểm t cộng 1.

Điều này bây giờ có vẻ không khác gì một sự thay thế hàng loạt đơn giản,

nhưng bạn sẽ thấy sau này nó sẽ trở nên rất hữu ích như thế nào.