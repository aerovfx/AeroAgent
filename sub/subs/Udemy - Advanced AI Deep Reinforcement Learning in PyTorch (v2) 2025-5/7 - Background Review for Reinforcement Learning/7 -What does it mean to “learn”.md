# 7 -Dịch “học” nghĩa là gì

---

Trong bài giảng này, tôi sẽ thảo luận về ý nghĩa của việc học trong học tập tăng cường.

vấn đề. Trong học tăng cường, có hai loại nhiệm vụ chính. Trước đây chúng ta đã thảo luận

cái mà tôi gọi là vấn đề dự đoán, nghĩa là, với một chính sách pi, cuối cùng là giá trị liên quan

hàm tại V của S. Loại nhiệm vụ thứ hai được gọi là bài toán điều khiển. Điều này có nghĩa

để tìm chính sách pi tối ưu, dẫn đến V tối đa của S. Nói cách khác,

vấn đề kiểm soát là tối đa hóa tổng số phần thưởng trong tương lai. Bạn đã biết từ khi

đầu phần này rằng đây là mục tiêu của chúng tôi. Bây giờ, chúng ta có thể xác định chính xác điều này

nghĩa và từ đó tìm ra giải pháp.

Đầu tiên, chúng ta cần thêm một chút toán học và một vài ký hiệu nữa để mô tả chính xác những gì

chúng tôi đang làm. Bạn đã biết về hàm giá trị tại trạng thái V cho trước của S. Nói chính xác hơn,

chúng tôi gọi đây là hàm giá trị trạng thái. Có một đại lượng khác được gọi là hành động

hàm giá trị, trong đó giá trị phụ thuộc cả vào trạng thái S và hành động A. Chúng tôi biểu thị nó

với ký hiệu Q. Như bạn có thể thấy, nó có định nghĩa gần như giống nhau về V của S, ngoại trừ việc

nó cũng phụ thuộc vào hành động A. Và như vậy, trong phương trình Bellman, vì A được cho,

chúng tôi không tổng hợp việc phân phối chính sách. Một câu hỏi thú vị để xem xét từ

Quan điểm khoa học máy tính là cần bao nhiêu không gian để lưu trữ các hàm giá trị.

Hãy xem xét kịch bản trong đó cả trạng thái và hành động đều rời rạc và chúng ta có một

số lượng hữu hạn của chúng. Vì vậy, giả sử chúng ta có trạng thái S lớn và hành động A lớn. Trong trường hợp này,

chúng ta có thể lưu trữ hàm giá trị trạng thái trong một mảng có kích thước S lớn. Nhưng đối với giá trị hành động

hàm, chúng ta sẽ phải lưu trữ nó trong một mảng hai chiều có kích thước S lớn nhân A lớn. Và do đó,

dung lượng lưu trữ cần thiết cho Q là bậc hai, trong khi dung lượng lưu trữ cần thiết cho V chỉ là tuyến tính.

Được rồi, vậy tại sao chúng ta cần khái niệm về giá trị hành động này? Chà, điều này sẽ giúp chúng ta tìm ra

chính sách tối ưu. Hãy nhớ rằng, một số chính sách có thể tốt và một số chính sách có thể xấu. Tối ưu

chính sách là chính sách tốt nhất, chính sách tối đa hóa giá trị. Đầu tiên, chúng ta hãy nghĩ về cách

so sánh hai chính sách khác nhau Chúng ta có thể nói rằng chính sách một tốt hơn chính sách hai nếu V của S

cho pi một lớn hơn V của S cho pi hai cho tất cả các trạng thái S trong không gian trạng thái. Vậy cái này

giúp chúng ta mô tả mức độ tốt tương đối của các chính sách khác nhau. Từ đây có thể xác định tốt nhất

chính sách và hàm giá trị tốt nhất. Hàm giá trị tốt nhất là hàm giá trị có

không có hàm giá trị lớn hơn. Đó là mức tối đa trên tất cả các chính sách có thể có của V trên S cho pi. Vì vậy chúng tôi sẽ

biểu thị nó bằng ký hiệu ngôi sao V. Tương tự, chính sách tốt nhất sẽ là arg max trên tất cả các chính sách

pi. Vì vậy chúng tôi gọi đó là ngôi sao pi. Cho đến nay, chúng ta chưa cần gọi hàm giá trị hành động, nhưng chúng ta hãy

xem nó liên quan thế nào. Đầu tiên, giá trị tác động tối ưu được xác định tương tự như trạng thái tối ưu

giá trị. Đó là giá trị lớn nhất trên tất cả các chính sách có thể có của Q cho pi. Chúng ta sẽ gọi đây là sao Q.

Điều này phải bao trùm mọi trạng thái và mọi hành động. Hơn nữa, giá trị trạng thái tối ưu bằng

mức tối đa trên tất cả các hành động từ giá trị hành động tối ưu. Vì vậy, từ đây, chúng ta có thể xác định mối quan hệ

giữa Q và V. Giá trị thực, không có ý định chơi chữ, của hàm giá trị hành động là giá trị này.

Giả sử chúng ta đang chơi một trò chơi nào đó và muốn biết hành động nào là tốt nhất để thực hiện đúng không?

bây giờ. Chà, chúng ta có một cuốn từ điển cho chúng ta biết chính xác phải làm gì. Tất cả những gì chúng ta phải làm là tìm ra

arg max trên Q với trạng thái S. Nói cách khác, hành động tốt nhất để thực hiện trở thành đơn giản

tra cứu từ điển. Với tư cách là một signo, hãy lưu ý rằng chính sách tối ưu không phải là duy nhất. Nó có thể là nhiều

các chính sách khác nhau dẫn đến cùng một hàm giá trị tốt nhất. Trong trường hợp này, chỉ cần tìm một

của họ. Mặt khác, hàm giá trị tối ưu là duy nhất vì nếu có hai giá trị khác nhau

các hàm giá trị, thì về mặt logic, một trong số chúng phải lớn hơn hàm kia.

Trước khi tiếp tục, chúng ta hãy nghĩ xem cách tiếp cận tốt đầu tiên có thể là gì để thực sự tìm được một

chính sách tối ưu. Hãy nhớ rằng, đây được gọi là vấn đề kiểm soát. Giả sử chúng ta đang chơi một trò chơi như

GridWorld hoặc TicTacTo trong đó không gian trạng thái và không gian hành động đều hữu hạn. Trong trường hợp này, một người ngây thơ

tìm kiếm có thể giải quyết vấn đề này. Đầu tiên, hãy tạo một danh sách tất cả các chính sách có thể tồn tại.

Rõ ràng, một số có thể xấu và một số có thể tốt, nhưng một hoặc nhiều trong số chúng có thể được xác định là tốt nhất.

Sau đó, trong một vòng lặp, chúng ta có thể kiểm tra từng chính sách. Vì vậy, đầu tiên chúng ta gọi một hàm để tìm giá trị cho

chính sách hiện tại, đó là hàm đánh giá. Hãy nhớ rằng, như chúng ta đã thảo luận trước đó, đây chỉ là

một bài toán đại số tuyến tính. Sau đó, khi có hàm giá trị, chúng ta có thể so sánh nó với hàm hiện tại

hàm giá trị tốt nhất. Nếu hàm giá trị mới tốt hơn thì chúng ta biến hàm này thành hàm giá trị mới tốt nhất

và biến chính sách này thành chính sách mới tốt nhất. Khi chúng ta hoàn thành việc lặp qua tất cả các chính sách,

chúng tôi đã tìm ra chính sách tối ưu. Trong bài giảng tiếp theo chúng ta sẽ thảo luận về 2 chức năng này tại đây

chi tiết hơn. Bạn có thể nhận thấy rằng chúng ta vẫn chưa thực sự biết cách triển khai chúng.

Điều tôi muốn bạn biết bây giờ là điều này. Đầu tiên, hàm đánh giá, tìm V của S cho một chính sách,

không phải là tất cả khó khăn. Trên thực tế, chúng ta đã thảo luận về cách thực hiện việc này nếu bạn biết cả chính sách

sự phân bố và động thái môi trường. Nó trở thành một hệ phương trình tuyến tính đơn giản.

Trong bài giảng tiếp theo, chúng ta sẽ xem xét một cách thực tế hơn để thực hiện điều này.

Thứ hai, chức năng khác, liệt kê tất cả các chính sách có thể, đơn giản về mặt khái niệm nhưng thực tế.

Như một bài tập, bạn có thể muốn thử triển khai điều này trong mã cho một ví dụ đơn giản như thế giới lưới.

Nói cách khác, mặc dù phương pháp này ở đây có vẻ hay và đơn giản nhưng thực tế lại không thực tế để thực hiện.