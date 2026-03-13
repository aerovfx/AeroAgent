# 66 - Tổng quan về tập dữ liệu MNIST Tiếng Anh

---

Chào mừng trở lại.

Trong bài giảng này, chúng ta sẽ thảo luận về tập dữ liệu ân xá.

Trước khi chúng ta thực sự bắt đầu với mạng nơ-ron tích chập và Keris, tôi muốn nhanh chóng nắm bắt

một chút thời gian để thực sự hiểu được tập dữ liệu cổ điển này.

Và nếu bạn đã từng tham gia bất kỳ khóa học nào khác hoặc thậm chí đọc một cuốn sách về học sâu, có thể bạn đã từng

đã gặp phải tập dữ liệu này trước đây.

Nó cực kỳ nổi tiếng trong lĩnh vực này, đặc biệt là trong mạng lưới thần kinh tích chập và học sâu.

Tôi muốn trình bày nhanh một số điều cơ bản về nó, vì chúng ta sẽ sử dụng các khái niệm dữ liệu thực sự giống nhau,

cụ thể là cách chúng tôi sắp xếp các bộ dữ liệu này thành mảng bốn chiều.

Vì thế đây chính là lý do mà ý tưởng đó xuất hiện khá thường xuyên trong suốt khóa học.

Tôi muốn trình bày ngắn gọn điều đó.

Được rồi, bây giờ đối với tập dữ liệu cụ thể này, may mắn thay, nó thực sự dễ dàng truy cập, tất nhiên, bạn tải lên

nó có chức năng tích hợp và mang theo, đồng thời có sáu mươi nghìn hình ảnh đào tạo và mười nghìn bài kiểm tra

hình ảnh ngay lập tức.

Bạn có thể nói rằng đó là một tập dữ liệu khổng lồ.

Và tập dữ liệu nhiều nhất, trong trường hợp bạn chưa quen, nó chứa các chữ số đơn viết tay

từ số không đến chín.

Vì vậy, ở đây chúng ta thấy một số ví dụ về tất cả các cách khác nhau mà mọi người vẽ số không, số một, số hai, số ba và

vân vân.

Bây giờ, như bạn có thể tưởng tượng, một hình ảnh có một chữ số có thể được biểu diễn dưới dạng một mảng.

Vì vậy, cụ thể trong tập dữ liệu này, các mảng có kích thước 28 x 28 và chúng chỉ là pixel

trong đó giá trị 0 đại diện cho màu trắng và giá trị 1 đại diện cho màu đen.

Vì vậy, những giá trị này là thang độ xám, nghĩa là chúng ta chỉ có một kênh màu duy nhất.

Và điều quan trọng cần lưu ý ở đây là nó đã được chuẩn hóa hoặc chuẩn hóa.

Vì vậy, bạn có thể thấy tất cả các giá trị nằm trong khoảng từ 0 đến 1 thay vì các giá trị từ 0 đến 200 và

năm mươi lăm.

Điều đó thực sự sẽ giúp mạng lưới thần kinh của chúng ta tìm hiểu về các loại tập dữ liệu cụ thể này.

Vì vậy, thông thường khi làm việc với dữ liệu hình ảnh, chúng tôi sẽ chuẩn hóa mọi thứ để rơi vào khoảng từ 0 đến 1.

Tập dữ liệu này đã có bước đó cho chúng tôi.

Bây giờ chúng ta có thể coi toàn bộ nhóm 60000 nghìn hình ảnh hoặc đối với bộ thử nghiệm 10000 hình ảnh là một

mảng bốn chiều và bốn chiều của nó bởi vì chúng ta có thứ nguyên cho tất cả các hình ảnh,

kích thước của kênh màu.

Trong trường hợp này, nó là một chiều và sau đó là chiều của X và Y 28.

Vì vậy, chúng tôi có cái này thực sự lớn cho mảng có thể đề cập đó.

Và vì vậy nó sẽ có bốn chiều là 60.28 x 28 và sau đó là một.

Vì vậy, chúng tôi có các mẫu, X và Y và sau đó là số lượng kênh màu.

Trong trường hợp này chúng ta chỉ có một kênh màu duy nhất vì nó là thang độ xám.

Nhưng đối với hình ảnh màu, giá trị thứ nguyên cuối cùng đó sẽ là 3 vì chúng ta có một giá trị cho màu đỏ,

một giá trị cho màu xanh lá cây và một giá trị cho màu xanh lam.

Tất cả được tiêu chuẩn hóa giữa số không và một.

Bây giờ, đối với các nhãn thực tế, chúng ta sẽ sử dụng một thứ gọi là mã hóa nóng, điều này có nghĩa là

thay vì có các nhãn phân loại như chuỗi một, hai, v.v., chúng ta sẽ có một

mảng cho mỗi hình ảnh.

Bây giờ, các nhãn ban đầu, khi bạn tải nó lên Keris, chúng thực sự được cung cấp dưới dạng danh sách các số.

Vì vậy, nếu hình ảnh đầu tiên là hình vẽ của số năm thì nhãn tương ứng của nó chỉ là

chữ số năm.

Và điều chúng ta cần làm là chúng ta cần chuyển đổi nó thành một bảng mã hóa một lần nữa.

Tất nhiên, việc chuyển đổi này thực sự được thực hiện rất dễ dàng, nhưng tôi muốn đảm bảo rằng chúng ta hiểu

những gì đang xảy ra đằng sau hậu trường.

Vì vậy, điều xảy ra là nhãn được biểu diễn dựa trên vị trí chỉ mục và mảng nhãn, tương ứng

nhãn sẽ là một ở vị trí chỉ mục và bằng 0 ở mọi nơi khác.

Ví dụ: nếu bạn tình cờ có một chữ số được rút ra là bốn thì nó sẽ có nhãn cụ thể này

mảng.

Lưu ý chỉ số cho số 0 một, hai, ba, bốn.

Đó là một chiếc mũ và khoác nó thành một chiếc.

Và lý do chúng tôi sử dụng mã hóa nóng này là vì nó hoạt động thực sự tốt với đầu ra một lớp

nơi chúng ta có 10 nơ-ron và sau đó mỗi nơ-ron được kích hoạt để bắn ra một sigmoid về 0 hoặc

một.

Kết quả là bây giờ, các nhãn cho dữ liệu huấn luyện trở nên rất lớn đối với mảng, vì vậy

cuối cùng chúng ta có 60 nghìn x 10 vì mỗi nhãn đó hiện là một mảng 10.

Và trong trường hợp hình ảnh này không thực sự rõ ràng, khi chúng ta thực sự nhìn thấy nó trong chiếc bánh, nó trông giống thứ gì đó

như thế này.

Ví dụ, đây là đoàn tàu màu trắng của chúng tôi và chúng tôi có tất cả những mã hóa hấp dẫn này.

Vì vậy, điều đó có nghĩa là nếu bạn nhìn vào hàng thứ hai, con số đó, nhãn của nó bằng 0 vì nó là hàng nóng không tráng phủ

tại một chỉ số bằng không.

Và đối với một số cái khác, nó đã bị xóa.

Chà, nó có một hình elip biểu thị giá trị ở giữa, nên chúng ta không thể biết rõ được.

OK, vậy bây giờ chúng ta đã hiểu tập dữ liệu NSA và một mã hóa, hãy áp dụng kiến thức mới của chúng ta về

mạng lưới thần kinh tích chập, mang trên tập dữ liệu này.

Hãy bắt đầu.

Tôi sẽ gặp bạn ở bài giảng tiếp theo.