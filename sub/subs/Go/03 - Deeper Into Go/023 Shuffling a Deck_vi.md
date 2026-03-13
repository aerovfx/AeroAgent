# 023 Xáo trộn bộ bài vi

---

Các chức năng cuối cùng mà chúng tôi phải tổng hợp lại hiện nay là chức năng tổng hợp.

Bây giờ, tôi cá là bạn có thể mong đợi sự hỗn hợp chính xác sẽ diễn ra.

Nó sẽ lấy một bộ bài và sắp xếp ngẫu nhiên thứ tự của tất cả các quân bài bên trong

nó.

Và vì vậy, nếu chúng tôi đặt nó ở dạng sơ đồ, nó sẽ trông giống như thế này.

Vì vậy, đây là danh sách bắt đầu của chúng tôi.

Chúng tôi có quân át chủ bài hai, ba, bốn quân bạc.

Và sau khi chúng tôi trộn nó, tôi sẽ tìm thấy thứ tự ngẫu nhiên trong đó.

Vì vậy, một cái gì đó như ba cho ace hai.

Vì vậy, chúng tôi tận dụng một chút nghiên cứu để tìm ra cách chính xác mà chúng tôi sẽ trộn lẫn danh sách này.

Thực tế là không thể, hiện tại, Thư viện tiêu chuẩn vàng không có bất kỳ hợp nhất chức năng nào để tự động trộn

một lát hoặc trộn một mảng, trộn một lát hoặc một danh sách cho chúng tôi.

Vì vậy, thay vào đó, chúng ta sẽ phải tập hợp tùy chỉnh logic của riêng mình để trộn công cụ tất cả các phần tử

bên trong đây.

Và đây là logic mà chúng tôi sẽ áp dụng.

Chúng tôi sẽ lặp lại toàn bộ thẻ của chúng tôi một lần.

Sau đó, đối với mỗi thẻ hoặc mỗi mục trong thời gian đó, chúng tôi sẽ tạo ra một số ngẫu nhiên

từ 0 đến tối đa chiều dài của thẻ lát.

Sau đó, chúng tôi sẽ lấy thẻ hiện tại mà chúng tôi đang xem và thay đổi nó với thẻ có

ngẫu nhiên ở một số thời điểm trong đó.

Vì vậy, nếu chúng tôi áp dụng logic này cho ví dụ nhỏ này ngay tại đây, chúng tôi sẽ nói rằng ngay lần này

lần đầu tiên chúng tôi lặp lại danh sách các lá bài này, chúng tôi sẽ xem xét quân tại chủ bài.

Sau đó, chúng tôi sẽ tạo một số từ 0 đến 3, đại diện cho thẻ cuối cùng

ở đây, và sau đó bất kể số ngẫu nhiên nào là gì, chúng tôi sẽ đổi thẻ tại chỉ mục đó

thẻ đầu tiên trong lát.

Vì vậy, ví dụ, nếu chúng tôi tạo ra nhiều ba, chúng tôi sẽ giành được quân tại chủ bài.

Chúng tôi sẽ vứt nó vào lát cuối cùng.

Chúng tôi sẽ lấy bốn quân trang và đặt nó ngay từ đầu.

Vì vậy, một cái gì đó như vậy.

Sau đó, chúng tôi sẽ chuyển sang thẻ tiếp theo trong lát.

Vì vậy, hai bạn thuổng.

Vì vậy, một lần nữa, chúng tôi sẽ tạo ra một số ngẫu nhiên.

Có thể lần này nó là con số không.

Sau đó, chúng tôi sẽ thay đổi thẻ này thành thẻ số 0 và sau đó chúng tôi sẽ lặp lại quá trình đó trong toàn bộ bộ

chiều dài của lát cắt.

Vì vậy, tôi nghĩ rằng điều đó chắc chắn có ý nghĩa và điều đó có thể không phải là hỗn hợp tốt nhất

trên thế giới, nhưng chắc chắn sẽ có thứ tự ngẫu nhiên của các thẻ ở đây.

Vì vậy, hiện tại chúng tôi cần phải tìm ra cách chính xác mà chúng tôi sẽ thực hiện điều này.

Vì vậy, tôi nghĩ rằng các quy thức thực sự ở đây là tìm ra cách chúng ta ngẫu nhiên hoặc cách chúng

ta tạo ra một số ngẫu nhiên giữa số 0 và toàn bộ chiều dài của lát thẻ.

Vì vậy, chúng tôi kiểm tra chuẩn thư viện tài liệu.

Một lần nữa, hãy nhớ rằng bạn có thể truy cập trang này bằng cách truy cập Golang dot org và sau đó nhấp vào nút

gói ở trên cùng.

Bây giờ bên trong đây, chúng ta sẽ cuộn xuống gói học.

Và ngay tại đây, đây là toán học.

Bây giờ, một trong những gói bên trong học toán là gói RAND, chúng ta có thể sử dụng gói này để tạo các gói

ngẫu nhiên một số.

Vì vậy, chúng ta hãy xem xét các tài liệu xung quanh điều đó.

Bên trong gói RAND, hãy tìm mục chỉ mục và chúng tôi đang tìm một hàm có tên là int DN ngay tại

đây.

Vì vậy, đây là int NN.

Về cơ bản, chúng ta có thể gọi hàm int end với một số nguyên của chúng ta.

Sau đó, hàm int end sẽ tạo ra một số nằm trong khoảng từ 0 đến số mà chúng ta chuyển vào.

Và đây sẽ luôn là một số nguyên, có nghĩa là chúng ta có thể sử dụng nó trực tiếp trên lát cắt mà chúng

ta đang cố gắng sử dụng, vì hãy nhớ rằng, chúng ta cần một số nguyên để truy cập các phần tử thực tế bên trong

đó.

Vì vậy, tôi nghĩ rằng chúng tôi thực sự cần làm về cơ bản là gọi hàm này ngay tại đây và sử dụng nó để sắp xếp

hoặc trộn lát cắt của chúng ta.

Vì vậy, chúng tôi thử điều này.

Tôi sẽ thay đổi lại mã soạn thảo của mình.

Và ở trang trí tệp cuối cùng, chúng tôi sẽ tạo một chức năng mới có tên là Shuffle.

Bây giờ, như thường lệ, chúng ta cần nghĩ về chữ ký hàm ở đây.

Tôi nghĩ rằng rất có ý nghĩa khi muốn nói rằng chúng tôi muốn làm điều đó

như nói hỗn hợp thẻ và sau đó mong đợi thẻ này ngay tại đây sẽ được sắp xếp ngẫu nhiên.

Vì vậy, tôi nghĩ rằng chúng ta cần thiết lập hỗn hợp với một máy thu của một bộ bài.

Vì vậy, chúng tôi sẽ nói bộ bài DH như vậy bây giờ tôi không nghĩ rằng hàm này sẽ cần phải chấp nhận bất kỳ đối luận nào

số nào khác.

Và tôi cũng không nghĩ rằng họ cần phải có bất kỳ khoản hoàn trả giá trị nào từ đó.

Về cơ bản, chúng tôi sẽ chỉ lấy bộ bài mà chúng tôi đang làm việc, sắp xếp thứ tự ngẫu nhiên bên trong nó,

và thế là xong.

Không có gì khác để trả lại.

Được rồi, vậy hãy thử xem.

Đầu tiên chúng ta sẽ bắt đầu bằng cách viết ra vòng lặp cho chúng ta.

Vì vậy, chúng tôi sẽ nói về một số vi phạm của bộ bài.

Bây giờ bạn sẽ thấy rằng lần này chúng tôi nói chỉ mục và chúng tôi không thực sự có quyền truy cập vào thẻ

in here.

Vì vậy, chúng tôi không cần phải luôn nhận được một tham chiếu đến phần tử mà chúng tôi đang lặp lại trong trường hợp này.

Chúng tôi thực sự chỉ quan tâm đến số lượng.

Và tôi sẽ chỉ chọn lý do tại sao chỉ sau một giây.

Bây giờ, chúng tôi đã tìm thấy chỉ mục từ ngay tại đây, nhân tiện, chúng tôi sẽ kèm theo quy ước

Se khít hơn một chút.

Và chúng tôi sẽ viết điều này đơn giản là Tôi và chỉ cần nhớ về cơ sở là chỉ mục của thẻ mà chúng tôi

đang xem vào thời điểm này.

Vì vậy, hiện tại trong vòng lặp, đầu tiên chúng ta sẽ tạo ra một số ngẫu nhiên cho chúng ta.

Vì vậy, chúng tôi sẽ nói vị trí mới.

Và như thường lệ, hãy nhớ rằng, tên biến này thực sự dài hơn chúng ta muốn theo quy ước, nhưng chúng ta sẽ viết những

Hiện tại, biến tên này ở dạng dài chỉ để đảm bảo rằng nó thực sự rõ ràng những gì

chúng tôi đang làm .

Vì vậy, chúng tôi sẽ nói rằng vị trí mới sẽ là chức năng int của chúng trong Thư viện Rand.

Vì vậy, chúng tôi sẽ nói rand dot int NN và chúng tôi muốn tạo một số từ 0 đến chiều dài của lát

trừ đi một.

Vì vậy, chúng tôi sẽ nói chiều dài của lát trừ đi một phần như vậy.

Vì vậy, điều này ngay tại đây là điều mà chúng tôi đã không làm trước đây.

Đây là cách chúng tôi có được chiều dài của một lát cắt.

Len đã tắt chiều dài và chúng tôi có thể chuyển bất kỳ cắt cũ nào vào đó và trả về một số nguyên

Phản hồi độ dài thực thi của lát cắt.

Vì vậy, bây giờ lệnh gọi này ngay tại đây sẽ tạo ra một số ngẫu nhiên từ 0 đến một trừ hoặc một ít hơn

lát cắt dài.

Vì vậy, giờ đây chúng ta có thể thực hiện trao đổi logic của mình hoặc logic để trao đổi hai yếu tố bên trong bộ bài của chúng ta.

Và đây là lúc chúng ta sẽ sử dụng một loại cú pháp thú vị khác.

Vì vậy, chịu đựng với tôi ở đây.

Hãy viết mã cho nó và chúng tôi sẽ nói về chính xác những gì nó đang làm.

Chúng ta sẽ nói bên trong bộ bài của chúng ta ở mục I và sau đó là dấu comma, sau đó là bên trong bộ bài của chúng ta

ở mục chỉ của vị trí mới.

Và giá trị này ngay tại đây sẽ đến từ bên trong bộ bài ở vị trí mới và bên trong bộ

bài ở vị trí I.

Vì vậy, đây là một sự thay đổi một dòng thực sự thú vị ngay tại đây.

Vì vậy, chúng tôi đang sử dụng biểu thức này để thay đổi các phần tử ở cả tôi và vị trí mới trong phần cắt của chúng tôi.

Vì vậy, hãy lưu ý rằng chúng tôi có một comcomma giữa cả hai bên hoặc mỗi tham chiếu đến bộ bài.

Vì vậy, về cơ bản, chúng tôi đang nói rằng hãy nhận bất cứ điều gì ở vị trí mới và giao nó cho a và sau đó nhận bất kỳ

điều gì ở tôi và giao nó cho vị trí mới.

Vì vậy, có khá nhiều đó.

Vì vậy, điều này lặp lại tất cả các phần tử bên trong phần cắt của chúng ta, tạo ra một số ngẫu nhiên và sau đó là Kích thước

thay đổi các phần tử.

Vì vậy, tôi nghĩ rằng chúng tôi đã sẵn sàng thực hiện một thử nghiệm nhỏ với điều này.

Bây giờ, tôi sẽ nói với bạn ngay bây giờ, trước khi chúng tôi kiểm tra nó, mã mà chúng tôi đã

viết ở đây sẽ hoạt động, nhưng sẽ có điều gì thực sự chưa biết về nó.

Có điều gì đó rất lạ.

Vì vậy, it sẽ hoạt động, nhưng nó sẽ rất lạ.

Vì vậy, hãy chạy điều này và sau đó chúng tôi sẽ nói về độ chính xác của những điều rất lạ.

Bây giờ, một điều tôi muốn nhắc bạn, khi tôi lưu tệp, chúng tôi đã sử dụng gói Rand này ngay lập tức

tại đây.

Vì vậy, nếu bạn đang sử dụng trình soạn thảo mã bên cạnh so với mã biên tập, hãy nhớ thêm một lệnh nhập cho rand

học toán ở đây.

Vì vậy, chúng tôi sẽ quay lại tệp chính của chúng tôi.

Bây giờ chúng tôi sẽ tạo một danh sách thẻ mới.

Vì vậy, giả sử các thẻ là bộ bài mới và chúng tôi sẽ gọi nó là thẻ, trộn hỗn hợp và sau đó gắn thẻ chấm để ra tất cả các thẻ

tag bên trong đó.

Vì vậy, chúng tôi sẽ lưu tệp.

Tôi không tìm thấy bất kỳ lỗi nào, có nghĩa là tôi nghĩ rằng chúng tôi đã sẵn sàng để kiểm tra điều này.

Vì vậy, quay trở lại bên trong thiết bị đầu cuối, chúng ta sẽ chạy, đi, chạy, chính, đi, boong, đi và OC.

Nhìn kỹ hơn, có vẻ như chúng tôi đã có một số ngẫu nhiên ở đây.

Vì vậy, tôi thấy hai chữ A, ba, hai chữ A, bốn, ba, ba.

, chắc chắn có vẻ như ngẫu nhiên Vâng, nhưng tôi muốn bạn tìm thấy một thú vị thứ hai.

Vui lòng ghi lại mục cuối cùng bên trong đây.

Chúng tôi có hai quân quân.

Hai câu lạc bộ, bốn câu lạc bộ, ba viên kim cương.

Vì vậy, chúng tôi sẽ chạy lại chương trình và bạn sẽ nhận thấy rằng lần thứ hai chúng tôi vẫn còn hai

quân dư.

Hai câu lạc bộ, bốn viên kim cương.

Ba viên kim cương.

Vì vậy, hai trong số quân bội thu.

Hai câu lạc bộ, bốn viên kim cương, ba viên kim cương.

Vì vậy, tôi không nghĩ rằng tôi phải nói với bạn rằng chúng tôi khó có thể nhận được một sự chính xác ngẫu nhiên như thế

bất cứ khi nào chúng tôi chạy chương trình này.

Vì vậy, tôi nghĩ thực sự an toàn khi nói rằng mặc dù có vẻ như chúng tôi đã đặt ra những ngẫu nhiên ngẫu nhiên của mình

lại với nhau một cách chính xác ở đây để trộn hỗn hợp hoặc trộn các phần, nhưng có vẻ như có gì

đó không hoạt động chính xác.

Vì vậy, chúng tôi nghỉ ngơi nhanh chóng.

Chúng tôi sẽ quay lại phần tiếp theo và chúng tôi sẽ tìm hiểu chính xác lý do tại sao hỗn hợp này không có chức năng

hoạt động tốt như chúng tôi mong đợi.

Vì vậy, tôi sẽ gặp bạn trong phần tiếp theo.