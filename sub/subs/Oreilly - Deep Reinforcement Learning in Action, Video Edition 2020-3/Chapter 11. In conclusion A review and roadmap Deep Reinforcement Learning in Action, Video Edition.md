# Chương 11. Kết luận Đánh giá và lộ trình Học tăng cường sâu trong thực tế, Phiên bản video đã dịch

---

Chương 11. Kết luận, rà soát và lộ trình.

Trong chương cuối cùng này, trước tiên chúng ta sẽ dành chút thời gian để xem lại ngắn gọn những gì chúng ta đã học được,

làm nổi bật và chắt lọc những gì chúng tôi nghĩ là những kỹ năng và khái niệm quan trọng nhất để

mang đi. Chúng tôi đã đề cập đến các nguyên tắc cơ bản của học tăng cường và nếu bạn có

đã tiến xa đến mức này và đã tham gia vào các dự án, bạn có đủ điều kiện để thực hiện

nhiều thuật toán và kỹ thuật khác.

Cuốn sách này là một khóa học về các nguyên tắc cơ bản của học tăng cường sâu, không phải là sách giáo khoa

hoặc tham khảo. Điều đó có nghĩa là chúng tôi không thể giới thiệu tất cả những điều cần biết về

DRL, và chúng tôi đã phải đưa ra những lựa chọn khó khăn về những gì cần loại bỏ. Có một số điều thú vị

các chủ đề trong DRL mà chúng tôi ước mình có thể đưa vào và có một số chủ đề, mặc dù

tiêu chuẩn ngành, không phù hợp để đưa vào cuốn sách giới thiệu tập trung vào dự án

như cái này Tuy nhiên, chúng tôi muốn cung cấp cho bạn lộ trình để bắt đầu từ đâu

ở đây với những kỹ năng mới của bạn. Trong phần thứ hai của chương này, chúng tôi sẽ giới thiệu một

cấp cao một số chủ đề, kỹ thuật và thuật toán trong DRL đáng để biết nếu bạn nghiêm túc

về việc tiếp tục trong lĩnh vực DRL. Chúng tôi không đề cập đến những lĩnh vực này vì hầu hết chúng liên quan đến

môn toán cao cấp mà chúng tôi không mong đợi độc giả của cuốn sách này sẽ quen thuộc, và

chúng tôi không có không gian để dạy thêm toán.

Mục 11.1. Chúng ta đã học được gì? Học tăng cường sâu là sự kết hợp của học sâu

và học tăng cường. Học tăng cường là một khuôn khổ để giải quyết vấn đề kiểm soát

nhiệm vụ, đó là những vấn đề trong đó một tác nhân có thể thực hiện các hành động dẫn đến kết quả tích cực hoặc

phần thưởng tiêu cực, trong một số môi trường. Môi trường là vũ trụ trong đó

hành động đại lý. Tác nhân có thể có toàn quyền truy cập vào trạng thái của môi trường hoặc

nó có thể chỉ có quyền truy cập một phần vào trạng thái của môi trường, được gọi là một phần

khả năng quan sát. Môi trường tiến hóa theo các bước thời gian riêng biệt theo một số động lực

quy tắc và tại mỗi bước thời gian, tác nhân thực hiện một hành động có thể ảnh hưởng đến trạng thái tiếp theo.

Sau khi thực hiện mỗi hành động, nhân viên sẽ nhận được phản hồi dưới dạng tín hiệu khen thưởng. Chúng tôi

đã mô tả một hình thức hóa toán học của quá trình này được gọi là quá trình quyết định Markov, MDP.

MDP là một cấu trúc toán học bao gồm một tập hợp các trạng thái S mà môi trường có thể

tham gia và một tập hợp các hành động A mà tác nhân có thể thực hiện, có thể phụ thuộc vào cụ thể

trạng thái của môi trường. Có một hàm phần thưởng, R của S, T, A, T, S, T cộng một, đó là

tạo ra tín hiệu khen thưởng, khi chuyển từ trạng thái hiện tại sang trạng thái tiếp theo và

hành động của đại lý. Môi trường có thể tiến triển một cách tất định hoặc ngẫu nhiên, nhưng

trong cả hai trường hợp, tác nhân ban đầu không biết các quy luật động của môi trường,

vì vậy tất cả các chuyển đổi trạng thái phải được mô tả theo xác suất từ góc độ của

đại lý. Do đó chúng ta có xác suất có điều kiện

phân bố trên các trạng thái tiếp theo, S, T cộng một, với trạng thái hiện tại và hành động được thực hiện

bởi tác nhân ở bước thời gian hiện tại, xác suất của trạng thái tiếp theo được ký hiệu là

viết hoa S, T cộng một, với trạng thái hiện tại, ST và hành động A T. Đại lý tuân theo một số

chính sách pi, là hàm ánh xạ phân bố xác suất cho các hành động đã cho

tình trạng hiện tại. ST là hàm pi ánh xạ các trạng thái từ tập S tới xác suất

phân phối trên các hành động trong tập PR của A. Mục tiêu của tác nhân là thực hiện các hành động

giúp tối đa hóa thời gian chiết khấu phần thưởng tích lũy trong một khoảng thời gian nào đó. Thời gian giảm giá

phần thưởng tích lũy được gọi là tiền lãi, thường được ký hiệu bằng ký tự G hoặc R và bằng nhau

đến. Tiền lãi Gt tại thời điểm T bằng tổng số phần thưởng được chiết khấu cho mỗi lần

bước cho đến khi kết thúc tập, đối với môi trường nhiều tập hoặc cho đến khi trình tự hội tụ

đối với môi trường không epitotic. Hệ số gamma là một tham số trong khoảng 0, 1 và

là tỷ lệ chiết khấu xác định chuỗi sẽ hội tụ nhanh như thế nào và do đó xác định

tương lai được giảm giá. Tỷ lệ chiết khấu gần bằng 1 sẽ có nghĩa là phần thưởng trong tương lai sẽ được trao

trọng số tương tự như phần thưởng ngay lập tức, tối ưu hóa về lâu dài, trong khi mức chiết khấu thấp

dẫn đến việc chỉ ưu tiên những khoảng thời gian ngắn hạn. Một khái niệm bắt nguồn từ cơ sở này

Khung MDP là một hàm giá trị. Hàm giá trị gán một giá trị cho một trong hai

trạng thái hoặc cặp hành động trạng thái, nghĩa là giá trị để thực hiện hành động ở trạng thái nhất định,

với cái trước được gọi là hàm giá trị trạng thái hoặc thường chỉ là hàm giá trị và

cái sau là giá trị hành động hoặc hàm Q. Giá trị của một trạng thái đơn giản là giá trị được mong đợi

trả về với điều kiện là tác nhân bắt đầu ở trạng thái đó và tuân theo một số pi chính sách, vì vậy giá trị

các chức năng hoàn toàn phụ thuộc vào chính sách. Tương tự, giá trị hành động hoặc giá trị Q của trạng thái

cặp hành động là lợi nhuận kỳ vọng khi tác nhân thực hiện hành động ở trạng thái đó và

tuân theo chính sách pi cho đến cuối cùng. Một trạng thái đặt tác nhân vào vị trí gần gũi với

ví dụ: thắng một trò chơi sẽ được gán một giá trị trạng thái cao giả định cơ bản

chính sách đã hợp lý. Chúng ta ký hiệu hàm giá trị là v pi của s, với chỉ số pi

biểu thị sự phụ thuộc của giá trị vào chính sách cơ bản và hàm Q

như Q pi của s, a, mặc dù chúng ta thường bỏ chỉ số pi để thuận tiện.

Bây giờ chúng ta hiểu hàm Q pi của s, a là một loại hộp đen nào đó

cho chúng ta biết chính xác phần thưởng mong đợi cho hành động trạng thái a ở trạng thái s, nhưng tất nhiên, chúng ta không

có quyền truy cập vào một chức năng biết tất cả như vậy. Chúng ta phải ước tính nó. Trong cuốn sách này, chúng tôi

đã sử dụng mạng lưới thần kinh để ước tính các hàm giá trị và các hàm chính sách, mặc dù bất kỳ phương pháp nào phù hợp

chức năng có thể hoạt động. Trong trường hợp Q pi dựa trên nơ-ron của s, a, chúng tôi đã huấn luyện các mạng nơ-ron để

dự đoán phần thưởng dự kiến. Các hàm giá trị được xác định và xấp xỉ theo cách đệ quy, chẳng hạn như

Q pi của s, a, được cập nhật là. Biểu thức này, trong đó s đề cập đến trạng thái tiếp theo, hoặc s, t

cộng 1. Ví dụ: trong thế giới lưới, việc hạ cánh xuống ô mục tiêu sẽ dẫn đến cộng 10, hạ cánh

trên hố sẽ bị trừ 10 và thua trò chơi cũng như tất cả các nước đi không kết thúc khác,

bị phạt trừ 1. Nếu người đại diện còn cách ô mục tiêu chiến thắng hai bước,

trạng thái cuối cùng giảm xuống v pi của s, 3 bằng 10. Khi đó, nếu gamma bằng 0,9 thì trạng thái trước đó

trạng thái có giá trị v pi của s, 2 bằng r, 2 cộng 0,9 v pi của s, 3 bằng trừ 1 cộng

9 bằng 8. Nước đi trước đó phải là v pi của s, 1 bằng r, 1 cộng 0,9 v pi của s,

2 bằng trừ 1 cộng 0,8 nhân 8 bằng 5,4. Như bạn có thể thấy, các trạng thái ở xa trạng thái chiến thắng hơn

được đánh giá ít hơn. Khi đó, việc đào tạo một tác nhân học tăng cường chỉ là thành công

đào tạo một mạng lưới thần kinh để gần đúng với hàm giá trị, do đó tác nhân sẽ chọn

hành động dẫn đến trạng thái có giá trị cao hoặc gần đúng trực tiếp chức năng chính sách bằng cách

quan sát phần thưởng sau các hành động và củng cố các hành động dựa trên phần thưởng nhận được. Cả hai

Các phương pháp tiếp cận đều có ưu và nhược điểm, nhưng chúng ta thường kết hợp việc học cả chính sách và giá trị

hoạt động cùng nhau, được gọi là thuật toán phê bình tác nhân, trong đó tác nhân đề cập đến

chính sách và nhà phê bình đề cập đến hàm giá trị.