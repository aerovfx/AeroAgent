# Chương 2. Dự đoán phần thưởng trong tương lai Chức năng giá trị và chính sách Học tăng cường sâu trong thực tế, Phiên bản video

---

Phần 2.7 Dự đoán các phần thưởng, giá trị và chức năng chính sách trong tương lai

Dù bạn có tin hay không, chúng tôi thực sự đã đưa rất nhiều kiến thức vào các phần trước.

Cách chúng tôi thiết lập các giải pháp cho kẻ cướp không vũ trang và kẻ cướp theo ngữ cảnh, tiêu chuẩn của chúng tôi

phương pháp học tăng cường, và do đó, có rất nhiều thuật ngữ đã được thiết lập

và toán học đằng sau những gì chúng tôi đã làm.

Chúng tôi đã giới thiệu một số thuật ngữ như không gian trạng thái và hành động, nhưng chúng tôi chủ yếu chỉ

mô tả sự vật bằng ngôn ngữ tự nhiên.

Để bạn hiểu các tài liệu nghiên cứu RL mới nhất và để chúng tôi tạo dựng tương lai

các chương ít dài dòng hơn, điều quan trọng là phải làm quen với các thuật ngữ và

toán học.

Hãy xem lại và chính thức hóa những gì bạn đã học được cho đến nay, được tóm tắt trong Hình 2.9.

Thuật toán học tăng cường về cơ bản xây dựng một tác nhân hoạt động trong một số môi trường.

Môi trường thường là một trò chơi, nhưng nói chung hơn là bất cứ quá trình nào tạo ra các trạng thái,

hành động và phần thưởng.

Tác nhân có quyền truy cập vào trạng thái hiện tại của môi trường, đó là tất cả dữ liệu

về môi trường tại một thời điểm cụ thể, S_T Epsilon viết hoa S. Sử dụng trạng thái này

thông tin, tác nhân thực hiện một hành động, A_T Epsilon viết hoa A, có thể mang tính quyết định

hoặc có xác suất thay đổi môi trường sang trạng thái mới, S_T cộng 1.

Hình 2.9.

Quy trình chung của một thuật toán học tăng cường.

Môi trường tạo ra trạng thái và phần thưởng.

Tác nhân thực hiện một hành động, A_T, với trạng thái S_T, tại thời điểm T và nhận được phần thưởng, R_T.

Mục tiêu của đại lý là tối đa hóa phần thưởng bằng cách học cách thực hiện các hành động tốt nhất trong một môi trường nhất định.

trạng thái.

Xác suất liên quan đến việc ánh xạ một trạng thái sang một trạng thái mới bằng cách thực hiện một hành động là

gọi là xác suất chuyển tiếp.

Tác nhân nhận được phần thưởng, R_T, vì đã thực hiện hành động A_T ở trạng thái S_T dẫn đến

trạng thái mới, S_T cộng 1.

Và chúng tôi biết rằng mục tiêu cuối cùng của tác nhân, thuật toán học tăng cường của chúng tôi,

là tối đa hóa phần thưởng của nó.

Đó thực sự là sự chuyển đổi trạng thái, mũi tên S_T S_T cộng 1, tạo ra phần thưởng chứ không phải

bản thân hành động, vì hành động đó có thể dẫn đến một trạng thái xấu.

Nếu bạn đang tham gia một bộ phim hành động, không có ý chơi chữ, và bạn nhảy từ mái nhà này sang mái nhà khác,

bạn có thể tiếp đất một cách duyên dáng trên mái nhà kia hoặc trượt hoàn toàn và ngã.

Sự nguy hiểm của bạn mới là điều quan trọng.

Hai trạng thái có thể xảy ra, không phải việc bạn đã nhảy.

Hành động.

Phần 2.7.1 Chức năng chính sách.

Chúng ta sử dụng thông tin trạng thái hiện tại của mình một cách chính xác như thế nào để quyết định hành động cần thực hiện?

Đây là nơi phát huy tác dụng của các khái niệm chính về hàm giá trị và hàm chính sách.

chúng tôi đã có một chút kinh nghiệm với.

Trước tiên hãy giải quyết các chính sách.

Nói cách khác, chính sách, pi, là chiến lược của một tác nhân trong một môi trường nào đó.

Ví dụ: chiến lược của người chia bài trong trò blackjack là luôn đánh cho đến khi họ đạt được

giá trị thẻ từ 17 trở lên.

Đó là một chiến lược cố định đơn giản.

Trong vấn đề tên cướp có vũ trang N, chính sách của chúng tôi là một chiến lược tham lam.

Nói chung, chính sách là một hàm ánh xạ một trạng thái tới một phân bố xác suất trên

tập hợp các hành động có thể xảy ra ở trạng thái đó.

Bảng 2.5.

Chức năng chính sách

Xem hình bảng.

Trong ký hiệu toán học, S là một trạng thái và P_r(A) cho trước S là phân bố xác suất

trên tập hợp các hành động, Một trạng thái cho trước S. Xác suất của mỗi hành động trong phân bố

là xác suất mà hành động đó sẽ tạo ra phần thưởng lớn nhất.

Mục 2.7.2 Chính sách tối ưu.

Chính sách này là một phần trong thuật toán học tăng cường của chúng tôi nhằm chọn các hành động được đưa ra

trạng thái hiện tại của nó.

Sau đó chúng ta có thể xây dựng chính sách tối ưu.

Đó là chiến lược tối đa hóa phần thưởng.

Bảng 2.6.

Chính sách tối ưu.

Xem hình bảng.

Hãy nhớ rằng, một chính sách cụ thể là một bản đồ hoặc hàm, vì vậy chúng ta có một số loại tập hợp có thể

chính sách.

Chính sách tối ưu chỉ là một argmax, chọn mức tối đa trên tập hợp có thể này

chính sách như một chức năng của phần thưởng mong đợi của họ.

Một lần nữa, toàn bộ mục tiêu của thuật toán học tăng cường, tác nhân của chúng ta, là chọn các hành động

dẫn đến phần thưởng mong đợi tối đa.

Nhưng có hai cách để chúng ta có thể đào tạo nhân viên hỗ trợ của mình thực hiện việc này.

Trực tiếp.

Chúng ta có thể hướng dẫn tác nhân tìm hiểu hành động nào là tốt nhất, với trạng thái của nó.

Một cách gián tiếp.

Chúng ta có thể hướng dẫn tác nhân tìm hiểu trạng thái nào có giá trị nhất và sau đó thực hiện hành động

dẫn đến những trạng thái có giá trị nhất.

Phương pháp gián tiếp này dẫn chúng ta đến ý tưởng về các hàm giá trị.

Học 2.7.3 Hàm giá trị.

Hàm giá trị là các hàm ánh xạ một trạng thái hoặc một cặp hành động trạng thái tới giá trị mong đợi

– phần thưởng mong đợi – ở trạng thái nào đó hoặc thực hiện hành động nào đó ở trạng thái nào đó.

Bạn có thể nhớ lại từ số liệu thống kê rằng phần thưởng mong đợi chỉ là phần thưởng trung bình dài hạn

nhận được sau khi ở trạng thái nào đó hoặc thực hiện một số hành động.

Khi nói đến hàm giá trị, chúng ta thường muốn nói đến hàm giá trị trạng thái.

Ví dụ 2.7 Hàm giá trị trạng thái (Xem hình bảng)

Đây là hàm chấp nhận trạng thái S và trả về phần thưởng mong đợi khi bắt đầu

ở trạng thái đó và thực hiện các hành động theo chính sách của chúng tôi, pi.

Có thể không rõ ràng ngay tại sao hàm giá trị lại phụ thuộc vào chính sách.

Hãy xem xét điều đó trong vấn đề kẻ cướp theo ngữ cảnh của chúng tôi, nếu chính sách của chúng tôi là chọn hoàn toàn ngẫu nhiên

hành động, nghĩa là hành động mẫu từ sự phân bố đồng đều, giá trị (phần thưởng mong đợi)

của một tiểu bang có lẽ sẽ khá thấp, vì chúng tôi chắc chắn không chọn được trạng thái tốt nhất có thể

hành động.

Thay vào đó, chúng tôi muốn sử dụng một chính sách không phải là sự phân bổ thống nhất cho các hành động mà là

là phân bố xác suất sẽ tạo ra phần thưởng tối đa khi được lấy mẫu.

Nghĩa là, chính sách là yếu tố quyết định phần thưởng được quan sát và hàm giá trị là sự phản ánh

của các phần thưởng được quan sát.

Trong bài toán tên cướp n-armed đầu tiên của chúng tôi, bạn đã được giới thiệu về các hàm giá trị hành động trạng thái.

Các hàm này thường có tên là hàm Q hoặc giá trị Q, đây là nơi học sâu Q

đến từ, vì như bạn sẽ thấy trong chương tiếp theo, các thuật toán học sâu có thể được sử dụng

như hàm Q.

Bảng 2.8 Hàm Giá trị Hành động (Q) (Xem Hình Bảng)

Trên thực tế, chúng tôi đã triển khai một mạng Q sâu để giải quyết vấn đề kẻ cướp theo ngữ cảnh của mình, mặc dù

đó là một mạng lưới thần kinh khá nông, vì về cơ bản nó hoạt động như một hàm Q.

Chúng tôi đã huấn luyện nó để đưa ra ước tính chính xác về phần thưởng mong đợi khi thực hiện một hành động

đưa ra một trạng thái.

Hàm chính sách của chúng tôi là hàm softmax trên đầu ra của mạng nơ-ron.

Chúng ta đã đề cập đến nhiều khái niệm cơ bản trong học tăng cường chỉ bằng cách sử dụng n-armed

và kẻ cướp theo ngữ cảnh làm ví dụ.

Chúng tôi cũng bắt tay vào học tập củng cố sâu trong chương này.

Trong chương tiếp theo, chúng ta sẽ triển khai mạng Q sâu toàn diện, tương tự như thuật toán

DeepMind từng chơi game Atari ở cấp độ siêu phàm.

Nó sẽ là phần mở rộng tự nhiên của những gì chúng ta đã đề cập ở đây.