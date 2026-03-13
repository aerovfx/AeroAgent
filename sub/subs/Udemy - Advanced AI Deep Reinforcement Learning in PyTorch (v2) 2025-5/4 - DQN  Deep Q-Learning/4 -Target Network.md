# 4 -Target Network được dịch

---

Được rồi, trong video này chúng ta sẽ xem xét sửa đổi tiếp theo của Q learning

sang học Q sâu, tức là mạng mục tiêu.

Vậy đó là mạng mục tiêu.

Được rồi, về cơ bản cách thức hoạt động của nó là thay vì có một mạng lưới thần kinh mà chúng ta sẽ sử dụng

để có hai. Được rồi, thay vì một mạng lưới thần kinh, chúng ta sẽ có hai mạng. Được rồi, vậy chúng ta sẽ sử dụng cái gì

hai mạng lưới thần kinh này để làm gì? Vì vậy, như tên gọi của nó gợi ý, chúng ta sẽ có một mạng lưới

là một cái gì đó để làm với mục tiêu. Và vì vậy bạn nhớ lại điều đó với việc học Q. Vậy học Q

hàm mất mát là sai số bình phương giữa một số mục tiêu Y và sau đó là giá trị Q. Vậy Q

S A. Và sau đó chúng ta lấy bình phương của cái đó. Và vì vậy chúng tôi sử dụng phần mất mát này để cập nhật Q. Được rồi, nhưng

có điều gì đó kỳ lạ về học tăng cường trái ngược với học có giám sát

trong đó chúng tôi cũng sử dụng sai số bình phương là Y cũng phụ thuộc vào Q. Vì vậy, bạn nhớ lại Y là R

cộng gamma nhân mức tối đa trên tất cả các hành động tiếp theo có thể có của Q của tất cả các trạng thái tiếp theo có thể có

và sau đó là một số nguyên tố. Được rồi, ở đây chúng ta có Q ở hai nơi khác nhau. Và quan trọng là bạn

hãy nhớ lại rằng chúng tôi không lấy độ dốc cho Y. Chúng tôi chỉ lấy độ dốc cho dự đoán Q

Q S A cho trạng thái hiện tại. Được rồi, tôi sẽ nhân cơ hội này để giới thiệu một số điều mới

ký hiệu. Được rồi, vậy chúng ta sẽ nói Q S A Q S A dấu hai chấm theta. Đây sẽ là mạng lưới thần kinh.

Dự đoán mạng lưới thần kinh cho trạng thái S. Rất tiếc, tôi quên mất, tôi quên mất lỗi của mình. Bang S. Hành động

A với trọng số theta. Được rồi, khi chúng ta tính toán gradient này và đây chỉ là phần ôn tập, bạn đã

biết điều này nếu bạn đã thực hiện các điều kiện tiên quyết. Nhưng khi chúng ta lấy gradient theo theta

của L, điều này mang lại cho chúng ta. Vì vậy, nếu chúng ta thực hiện phép tính, chúng ta sẽ nhận được hai Y trừ hoặc tôi sẽ đặt toàn bộ

ở đây. Ta được R cộng gamma max Ray prime Q của S prime A prime và sau đó sử dụng các tham số

theta, bất kể chúng là gì, lấy mức tối đa đó và sau đó trừ Q S A cũng được tham số hóa bởi theta.

Được rồi, như bạn đã biết từ quy tắc dây chuyền, bây giờ chúng ta lấy đạo hàm bên trong. Vì vậy bây giờ bạn đang

nhìn thấy chi tiết những gì tôi đang nói. Vì vậy chúng ta muốn lấy đạo hàm của biểu thức này. Vì vậy đối với

số hạng này là hằng số đối với theta. Vì vậy, chúng tôi không phân biệt đối với

đó. Nó cứ thế biến mất. Đối với thuật ngữ này, đây là thuật ngữ khó vì nó phụ thuộc vào theta. Nhưng

chúng ta cũng sẽ coi đây là hằng số đối với theta. Được rồi, vì tổng mục tiêu là

không đổi đối với theta theo quan điểm của chúng tôi về học tăng cường, đó là cái mà chúng tôi gọi đây là

bán gradient. Vì vậy, đó là bán gradient. Được rồi, điều duy nhất phụ thuộc vào theta ở đây

biểu hiện theo học tăng cường là điều này. Được rồi, về cơ bản thì ngay cả chúng ta cũng lấy

gradient của Q S A theta so với theta. Được rồi, đó là cách hoạt động của việc học Q cho đến nay.

Vì vậy, để học Q sâu, chúng tôi sẽ thay đổi điều này nhiều hơn nữa. Vì vậy chúng tôi sẽ giới thiệu một mục tiêu

mạng. Và mạng mục tiêu chịu trách nhiệm tính toán mục tiêu này. Vì vậy chúng ta sẽ sử dụng mục tiêu

mạng để cung cấp giá trị này. Được rồi, vậy bây giờ bạn đã có một số ý tưởng về cách thức hoạt động của nó.

Và bây giờ là thời điểm tốt để nói về động cơ tại sao chúng ta sử dụng mạng mục tiêu.

Được rồi, về cơ bản là mạng mục tiêu, nó giúp giảm thiểu các vấn đề mất ổn định và phân kỳ trong Q

học tập. Được rồi, vậy chúng ta có ý gì khi nói điều đó? Vì vậy, động lực cho mạng lưới mục tiêu. Được rồi, vậy một cái ở đó

có thể gây mất ổn định trong quá trình tập luyện. Sự thiếu ổn định trong tập luyện, bạn đã thấy rồi phải không? Vì vậy khi

phần thưởng tăng giảm, vì vậy có vẻ như bạn đã học được cách nhận được phần thưởng tối đa và sau đó tất cả

đột nhiên nó giảm xuống mức tối thiểu. Điều đó có thể xảy ra, chúng tôi gọi đó là sự bất ổn. Và thế là một

cách bạn có thể nghĩ về sự không ổn định là các ước tính giá trị Q liên tục thay đổi trong suốt quá trình

đào tạo phải không? Bởi vì chúng tôi đang cập nhật Q ở mỗi bước. Và về cơ bản, dự đoán và

mục tiêu đang di chuyển liên tục. Và về cơ bản bạn có một mục tiêu di động. Được rồi, vậy tôi sẽ viết nó ra.

Một mục tiêu di động. Vì vậy, nếu bạn nghĩ về việc bạn đang bắn cung và mũi tên, sẽ rất nhiều

khó hơn nếu mục tiêu của bạn đang di chuyển trái ngược với, bạn biết đấy, bạn chỉ đang bắn một mảnh giấy, phải không?

Được rồi, một điểm khác ở đây là vấn đề phân kỳ. Các vấn đề khác biệt. Được rồi, vậy điều này có nghĩa là gì?

Vì các giá trị mục tiêu phụ thuộc vào cùng một mạng mà chúng tôi đang cập nhật. Vậy mục tiêu là

được tạo từ mạng mà chúng tôi hiện đang cập nhật. Điều này có thể tạo ra các vòng phản hồi, có thể

gây ra sự cập nhật giá trị Q thất thường, có thể dẫn đến sự phân kỳ. Được rồi, vậy điểm thứ ba là

có một sự thiên vị đánh giá quá cao.

Được rồi, vậy điều đó có nghĩa là gì? Vì vậy, về cơ bản điều này là do chúng tôi luôn lấy mức tối đa.

Và vì chúng tôi đang lấy mức tối đa nên chúng tôi luôn nhận được giá trị lớn nhất có thể.

Mặc dù giá trị đó vẫn chỉ là dự đoán và không nhất thiết phải đúng.

Và bây giờ hãy nói về cách sử dụng mạng mục tiêu. Vậy làm thế nào để sử dụng mạng mục tiêu?

Được rồi, vậy về cơ bản bạn đã biết điều này. Vì vậy, bây giờ chúng tôi có hai câu hỏi bạn có thể nghĩ ra. Vậy là chúng ta có QSA.

Bây giờ chúng ta sẽ gọi nó là theta trực tuyến. Vì vậy, đây là cái chúng tôi sử dụng để xác định hành động nào cần thực hiện.

Được rồi, hãy sử dụng epsilon 3D. Và sau đó chúng ta có mạng mục tiêu. Vậy mục tiêu theta

được sử dụng để hình thành các mục tiêu. Được rồi, và vì vậy chúng sẽ không hoàn toàn khác nhau. Vậy điều chúng tôi làm,

dễ nhất là coi nó như một thuật toán. Đúng vậy, khi bạn bắt đầu quá trình Qlin của mình,

bạn sẽ đặt mục tiêu theta bằng theta trực tuyến. Và điều này sẽ chỉ là ngẫu nhiên

được khởi tạo. Và sau đó bạn có vòng lặp huấn luyện của mình, vòng lặp này sẽ sửa đổi mục tiêu theta và theta.

Và cách thức hoạt động của nó về cơ bản là cứ sau vài bước. Cho nên mỗi nói, nói T mục tiêu bước.

Chúng tôi sẽ cập nhật lại mục tiêu theta lên theta trực tuyến. Được rồi, vậy điều này về cơ bản có nghĩa là ở giữa

ở các bước mục tiêu T này, mục tiêu theta sẽ là bản sao cũ của theta trực tuyến. Nó sẽ là bản sao cũ.

Được rồi, vấn đề ở đây là mục tiêu theta sẽ là một bản sao cũ

của theta trực tuyến cho đến khi nó được cập nhật. Được rồi, về cơ bản điều đó sẽ giải quyết được vấn đề mất ổn định này

bởi vì nó sửa được mục tiêu. Được rồi, bây giờ chúng ta hãy xem xét một số biến thể của mạng mục tiêu

cập nhật cũng hữu ích.