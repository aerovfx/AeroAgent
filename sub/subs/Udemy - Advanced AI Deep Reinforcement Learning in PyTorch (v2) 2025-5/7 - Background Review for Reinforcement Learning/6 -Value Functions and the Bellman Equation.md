# 6 -Các hàm giá trị và phương trình Bellman đã được dịch

---

Trong bài giảng này, cuối cùng chúng ta sẽ hình thành phương trình đại diện cho một phần tăng cường chung

vấn đề học tập, và từ đó chúng ta có thể rút ra được giải pháp.

Hãy bắt đầu bằng cách thảo luận về các giá trị kỳ vọng.

Nhân tiện, nếu bạn chưa bao giờ tham gia một khóa học xác suất thì có lẽ bạn chưa bao giờ nghe nói đến

những giá trị mong đợi. Trong trường hợp đó, nếu bạn muốn hiểu điều này, bạn phải tham gia một khóa học

trong xác suất.

Nghĩ đơn giản thì giá trị kỳ vọng chỉ là giá trị trung bình. Vì vậy, ví dụ, giả sử

Tôi đã đo chiều cao của 1000 học sinh và tôi muốn mô hình hóa điều này dưới dạng phân phối Gaussian.

Tôi thấy chiều cao trung bình là 70 inch, độ lệch chuẩn là 4 inch. Trong này

trường hợp, giá trị trung bình của phân phối là 70 và do đó giá trị kỳ vọng là 70.

Hãy xem một đồng xu là ví dụ tiếp theo. Một đồng xu có kết quả nhị phân. Nếu tôi tung một đồng xu,

Tôi có thể nhận được 1 hoặc tôi có thể nhận được 0. Giả sử xác suất của cả 1 và 0 là 50%. Trong trường hợp này, cái gì

giá trị mong đợi? Vâng, vì nó là giá trị trung bình, có nghĩa là giá trị kỳ vọng là 0,5.

Đôi khi thuật ngữ này khiến mọi người bối rối. Họ hỏi, làm thế nào tôi có thể nhận được giá trị

là 0,5 nếu kết quả chỉ có thể là 0 hoặc 1? Điều quan trọng là nhận ra giá trị kỳ vọng,

mặc dù tên của nó, không phải là giá trị bạn mong đợi nhận được. Vì vậy, nếu tôi tung một đồng xu, tôi thực sự không

mong đợi để xem giá trị 0,5. Giá trị kỳ vọng thực sự có ý nghĩa chính xác cho cả hai

phân phối liên tục và rời rạc. Mặc dù trong phần lớn phần này, chúng ta sẽ giả định

rằng chúng tôi đang làm việc với các phân phối rời rạc. Ý tưởng là giá trị kỳ vọng là một

tổng trọng số của tất cả các giá trị có thể có của một biến ngẫu nhiên, trong đó các trọng số là

xác suất của các giá trị đó. Như một ví dụ đơn giản, chúng ta có thể quay lại ví dụ về tiền xu của mình. Nếu chúng ta

có một đồng xu thiên vị sao cho xác suất xuất hiện mặt ngửa là 0,6 thì giá trị kỳ vọng sẽ trở thành

0,6 nhân 1 cộng 0,4 nhân 0, bằng 0,6. Bởi vì xác suất của 1 bây giờ là một chút

cao hơn xác suất bằng 0 thì giá trị kỳ vọng cũng cao hơn một chút.

Được rồi, vậy tầm quan trọng của các giá trị kỳ vọng là gì? Được rồi, hãy nhớ rằng phần thưởng của chúng ta

cũng nâng cao lợi nhuận của chúng tôi, đó là tổng số phần thưởng, các biến ngẫu nhiên của chúng tôi. Ở mức cao

cấp độ, điều này có nghĩa là nếu tôi chơi một trò chơi 100 lần bằng chính sách tương tự trong

cùng một môi trường, tôi sẽ nhận được những phần thưởng khác nhau. Điều này là do cả động lực môi trường

và chính sách của tôi mang tính xác suất. Và do đó, thật hợp lý khi không nghĩ đến một lần hoàn vốn

của chính nó mà là giá trị kỳ vọng của lợi nhuận. Tôi muốn tối đa hóa tổng số tiền trong tương lai

phần thưởng, nhưng vì kết quả mang tính xác suất nên điều tôi thực sự muốn làm là tối đa hóa kết quả mong đợi

tổng số phần thưởng trong tương lai.

Tổng phần thưởng dự kiến ​​​​trong tương lai có tên đặc biệt và học tập tăng cường. Chúng tôi gọi nó

hàm giá trị. Tôi luôn nhắc rằng đây là một cái tên rất đáng tiếc, bởi vì từ này

giá trị là một từ chung chung. Tuy nhiên, đây là những gì nó được gọi. Bởi vì sự trở lại

là tổng các phần thưởng trong tương lai, sau khi chúng ta đã đến một trạng thái nào đó, hàm giá trị cũng vậy.

Như bạn có thể thấy, nó không chỉ là một giá trị mong đợi đơn giản mà còn phụ thuộc vào thực tế

rằng chúng tôi đã đến trạng thái s vào thời điểm t. Vì vậy, chúng tôi biểu thị đây là V của s, giá trị của trạng thái s.

Xin lưu ý thêm, đôi khi chúng tôi coi việc hoàn trả chỉ đơn giản là phần thưởng, mặc dù việc hoàn trả

phải là một tổng số phần thưởng. Vì vậy, bạn luôn phải chú ý đến bối cảnh.

Như bạn nhớ lại, tôi đã nói rằng một trong những điều quan trọng nhất về lợi nhuận là nó có thể

được xác định một cách đệ quy. Tiền lãi tại thời điểm t, g của t, bằng phần thưởng tại thời điểm t cộng 1,

cộng gamma nhân với lợi nhuận tại thời điểm t cộng 1. Và vì điều này, chúng ta cũng có thể xác định giá trị

hoạt động đệ quy. V của s là giá trị kỳ vọng của phần thưởng tại thời điểm t cộng gamma nhân V của

s nguyên tố, giá trị ở trạng thái tiếp theo của nguyên tố. Bây giờ chắc bạn đang thắc mắc mục đích của tất cả là gì?

cái này à? Có phải chúng ta chỉ xác định các phương trình vì lợi ích của nó? Tất nhiên, câu trả lời là không. Chỉ cần giữ trong

hãy nhớ đến hình ảnh cấp cao. Chúng ta đang đặt ra một vấn đề mà từ đó chúng ta có thể tìm ra giải pháp.

Để tìm ra giải pháp, chúng ta phải có một vấn đề. Và do đó, công việc của chúng ta lúc này là tiếp tục

xây dựng vấn đề sao cho nó được xác định rõ ràng. Bước tiếp theo là hãy nhớ rằng dự kiến

giá trị thực sự chỉ là tổng có trọng số trong đó trọng số là xác suất. Vì vậy nếu chúng ta viết nó ra

đầy đủ, đây là những gì chúng tôi nhận được. Đây là tổng của tất cả các hành động có thể xảy ra a và là tổng của tất cả

có thể là số nguyên tố tiếp theo của trạng thái đó và tổng của tất cả các phần thưởng có thể có là. Bên trong tổng, chúng ta có

xác suất thực hiện hành động a khi chúng ta đang ở trạng thái s nhân với xác suất

hạ cánh ở trạng thái tiếp theo và nhận phần thưởng r. Và sau đó số này được nhân với

phần thưởng r cộng gamma nhân v của s prime. Nói cách khác, nó bằng r cộng gamma nhân v của s nguyên tố nhân

bằng xác suất thực sự nhận được phần thưởng r và đạt đến vị trí cao nhất của bang. Nói cách khác,

giá trị kỳ vọng của lợi nhuận. Đây được gọi là phương trình Bellman. Nó là trung tâm của tất cả

các giải pháp tiếp theo cho việc học tăng cường mà chúng ta sẽ thảo luận.

Thật đáng để suy nghĩ về phương trình Bellman thêm một chút. Chú ý rằng để đưa ra

phương trình này, chúng ta chỉ sử dụng các quy tắc toán học, quy tắc xác suất. Có vẻ như chỉ là một

giá trị mong đợi của vai trò thường xuyên. Tuy nhiên, ý nghĩa của nó rất sâu sắc. Thật thú vị khi cho rằng hai

xác suất ở đây, pi của s cho trước và p của s nguyên tố và r cho s và a đến từ những nơi hoàn toàn khác nhau

các quá trình vật lý. Pi là chính sách của chúng tôi và nó đại diện cho đại lý của chúng tôi nên bạn có thể coi điều đó giống như

một con vật. Xác suất chuyển đổi trạng thái đại diện cho môi trường của chúng ta nên bạn có thể coi đó là

thế giới. Điều thú vị là trong khi chúng ta có thể tự do vận dụng phương trình này về mặt toán học,

hai đối tượng này thực sự hoàn toàn khác biệt về mặt vật lý.

Lúc này chắc hẳn bạn đang vô cùng mệt mỏi. Tất cả những gì chúng tôi đang làm là dần dần xây dựng các công thức của mình

phức tạp hơn mà không có điểm kết thúc. Nhưng trên thực tế, đây chính xác là nơi chúng tôi mong muốn.

Mặc dù điều này có vẻ phức tạp nhưng tôi sẽ chứng minh cho bạn thấy rằng trên thực tế những gì chúng ta đã đạt được

khá đơn giản. Bây giờ chúng ta có thể xác định vấn đề đầu tiên trong học tăng cường mà từ đó chúng ta

có thể tìm ra giải pháp. Hãy nhớ rằng trong một bài toán học tăng cường, bạn có thể có nhiều chính sách.

Một số có thể tốt, nhưng một số có thể xấu. Làm thế nào chúng ta có thể biết đâu là chính sách tốt và đâu là chính sách xấu

chính sách? Vâng, còn hàm giá trị thì sao? Nói cách khác, nếu tôi có thể tìm được hàm giá trị cho một

chính sách nhất định, điều đó cho tôi biết chính sách đó tốt như thế nào. Chúng ta gọi những chỉ số này là pi của s, giá trị

chức năng đưa ra chính sách pi. Chúng ta gọi bài toán tìm hàm giá trị đã cho là một chính sách,

vấn đề dự đoán. Như đã hứa, tôi đã nói rằng chúng ta đã đạt được một điều gì đó khá đơn giản.

Chúng ta hãy nhìn lại phương trình Bellman. Những xác suất này là một chút lừa dối.

Chúng có những biểu tượng phức tạp, nhưng chúng không phức tạp. Hãy nhớ rằng số pi chính sách chỉ là một

chức năng mà chúng tôi triển khai trong mã của riêng mình. Chúng tôi biết xác suất này. Vì vậy, nó không phải là một vấn đề.

Làm thế nào về xác suất chuyển trạng thái? Giả sử điều này cũng được biết đến. Điều này là hoàn toàn có thể.

Lấy ví dụ về môi trường thế giới lưới. Bây giờ, điều gì xảy ra nếu chúng ta biết hai xác suất này?

Điều đáng ngạc nhiên là đây trở thành một hệ phương trình tuyến tính mà bạn biết cách giải từ

đại số phổ thông. Giả sử chúng ta có ba trạng thái. Sau đó, nếu chúng ta đơn giản hóa phép tính tổng từ

Phương trình Bellman, chúng ta sẽ đạt được điều gì đó như thế này. Vì vậy, ở đây, b và c chỉ là

các hằng số bắt nguồn từ các xác suất mà chúng ta giả định rằng chúng ta biết. Từ đây,

chúng ta có thể gọi một hàm đơn giản như np.lynouts.solve và điều này sẽ cho chúng ta biết v của s1, v của s2 và v của s3.

Nói cách khác, nếu chúng ta biết cả động lực chính sách và môi trường của mình, chúng ta có thể giải quyết giá trị

hàm chỉ sử dụng đại số tuyến tính.