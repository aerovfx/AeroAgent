# 8 -Giải phương trình Bellman bằng học tăng cường (pt 1) đã dịch

---

Trong bài giảng này, cuối cùng chúng ta sẽ đi sâu vào một số thuật toán học tăng cường thực sự.

Trước đây, chúng ta đã xem xét một số giải pháp đơn giản và đơn giản để học tăng cường.

Hãy tóm tắt lại chúng là gì.

Đầu tiên, chúng ta nhớ lại rằng có hai loại vấn đề, vấn đề dự đoán và vấn đề điều khiển.

vấn đề.

Bài toán dự đoán có nghĩa là đưa ra một chính sách V tinh của S. Bài toán điều khiển có nghĩa là

tìm chính sách tốt nhất mang lại V tối đa của S. Để giải quyết vấn đề dự đoán, chúng tôi

lưu ý rằng nếu chúng ta có sự phân bổ chính sách và xác suất chuyển đổi trạng thái, thì nó

trở thành một bài toán đại số tuyến tính đơn giản.

Có nhiều thuật toán và hàm chúng ta có thể sử dụng để giải hệ phương trình tuyến tính.

Đối với vấn đề điều khiển, chúng ta đã xem xét phương pháp đơn giản là lặp qua tất cả

các chính sách có thể có và tìm ra chính sách nào là tốt nhất.

Bây giờ chúng ta hãy xem tại sao cả hai cách tiếp cận này đều không thực tế.

Đầu tiên, hãy xem xét vấn đề dự đoán.

Trước đây, giải pháp yêu cầu chúng tôi phải biết cả phân phối chính sách và môi trường

động lực học.

Nhưng thực tế là, nếu bạn tưởng tượng, chẳng hạn, bất kỳ trò chơi Atari nào, chúng ta sẽ không biết về môi trường

động lực học.

Nói một cách thực tế, tất cả những gì chúng ta thực sự có thể làm là chơi trò chơi này hàng nghìn lần.

Nhưng thông thường không gian trạng thái quá lớn nên không thể đo được trạng thái

xác suất chuyển tiếp.

Và vì vậy, trừ khi bạn đang chơi trong môi trường đồ chơi, bạn cũng sẽ không được biết những xác suất này.

Bây giờ hãy xem xét vấn đề điều khiển.

Có thực sự có thể liệt kê tất cả các chính sách có thể?

Hãy xem xét liệu chúng ta có những trạng thái lớn nhất có thể và những hành động lớn nhất có thể xảy ra hay không.

Trong trường hợp này, tổng số chính sách có thể có là lớn A mũ lớn như.

Nói cách khác, điều này phát triển theo cấp số nhân.

Và do đó, việc liệt kê tất cả các chính sách có thể áp dụng cho hầu hết các vấn đề thực tế là không khả thi.

Hơn nữa, điều này thậm chí sẽ không hoạt động trong trường hợp không gian trạng thái hoặc không gian hành động

là vô cùng lớn.

Được rồi, bây giờ chúng ta đã nhận ra rằng có vấn đề, giải pháp là gì?

Bí quyết để làm điều này là hãy nhớ mối quan hệ giữa giá trị kỳ vọng và giá trị trung bình.

Vấn đề với giá trị kỳ vọng là nó đòi hỏi chúng ta phải biết phân bố xác suất

của biến ngẫu nhiên đang xét.

Nhưng quan trọng là có cách để chúng ta ước tính giá trị trung bình hoặc tương đương giá trị kỳ vọng.

Đây được gọi là giá trị trung bình mẫu.

Đây là cơ sở cho nhiều thí nghiệm khoa học.

Ví dụ: nếu chúng tôi muốn thử nghiệm một loại thuốc, chúng tôi không biết giá trị thực, nhưng chúng tôi có thể thực hiện

thử nghiệm trên một số lượng người nhất định và tính giá trị trung bình.

Giá trị trung bình mẫu chỉ đơn giản là tổng của tất cả các mẫu chúng tôi thu thập chia cho số

của các mẫu.

Ý tưởng là, vì cách tiếp cận là vô cùng nên ước tính này sẽ ngày càng chính xác hơn.

Được rồi, vậy điều này có liên quan gì đến việc học tăng cường?

Vâng, hãy nhớ rằng hàm giá trị chỉ đơn giản là lợi nhuận kỳ vọng.

Do đó, bằng cách sử dụng phương pháp lấy mẫu, điều chúng ta có thể làm là lấy mẫu một tập hợp lợi nhuận cho mỗi

trạng thái trong không gian trạng thái và lấy giá trị trung bình.

Điều đó sẽ cho chúng ta ước tính giá trị của từng trạng thái.

Bạn sẽ nhận thấy rằng tôi đã lạm dụng ký hiệu một chút ở đây bằng cách sử dụng các chỉ số khác nhau

để trả lại g.

Khi tôi nói g của t, tôi muốn nói đến một kết quả tổng quát g, kết quả trả về của trạng thái tại thời điểm t.

Nhưng khi tôi lập chỉ mục g bằng cách sử dụng i và s, ý tôi là đây là một mẫu của kết quả trả về.

Đó là mẫu thứ i trả về từ trạng thái s.

Bây giờ có một điểm rõ ràng nhưng có lẽ không quá rõ ràng.

Những mẫu này đến từ đâu?

Bạn có thể nhớ lại rằng khi chúng ta gặp khó khăn và chúng ta muốn lấy mẫu từ tiêu chuẩn

bình thường, chúng ta có thể gọi một hàm đơn giản là np.random.randn.

Nhưng việc lấy mẫu lợi nhuận có nghĩa là gì?

Chà, hãy nhớ rằng khi chúng tôi phát một tập, ngay cả khi chúng tôi sử dụng cùng một chính sách và

chính xác cùng một môi trường, kết quả sẽ khác nhau.

Điều này là do cả động lực chính sách và môi trường đều mang tính xác suất.

Vì vậy, chỉ cần chơi trò chơi sẽ thu thập được các mẫu.

Sử dụng khái niệm này, bây giờ chúng ta hãy thử viết một số mã giả để mô tả thuật toán này.

Nhân tiện, cách tiếp cận này được gọi là cách tiếp cận Monte Carlo vì đây là một dạng của Monte

Lấy mẫu Carlo.

Đầu tiên chúng ta sẽ mô tả vấn đề dự đoán.

Nói cách khác, với một chính sách nhất định, hãy tìm hàm giá trị.

Trước tiên chúng ta hãy nghĩ về điều này ở mức độ cao.

Giả sử chúng ta chơi một tập của trò chơi.

Điều này bao gồm việc nhập một loạt trạng thái và phần thưởng tương ứng.

Vì vậy chúng ta có thể gọi chúng là s1 lên tới st và r1 lên tới rt.

Từ đó, làm thế nào để chúng ta tính toán lợi nhuận của mỗi trạng thái?

Chà, thật sự rất hữu ích khi quay ngược lại.

Ví dụ g của t lớn là 0.

Điều quan trọng cần lưu ý là tiền lãi chỉ là tổng số phần thưởng trong tương lai.

Vì trạng thái kết thúc là phần cuối của một tập phim nên điều đó có nghĩa là không có trạng thái nào trong tương lai.

Không có trạng thái tương lai có nghĩa là không có phần thưởng trong tương lai.

Do đó, giá trị trả về của trạng thái đầu cuối luôn bằng 0 và do đó giá trị của đầu cuối

trạng thái cũng luôn bằng 0.

Trong mọi trường hợp, hãy tiếp tục.

Làm cách nào để tính toán lợi nhuận của bước thời gian trước đó?

Vâng theo định nghĩa, g của t lớn trừ 1 bằng r của t lớn.

Được rồi, cái tiếp theo.

Còn g của t lớn trừ 2 thì sao?

Nó là g của t lớn trừ 2 bằng r của t lớn trừ 1 cộng gamma nhân r của t.

Nhưng quan trọng, hãy nhớ rằng kết quả trả về là đệ quy.

Vậy cái này cũng bằng r của big t trừ 1 cộng gamma nhân g của big t trừ 1.

Chúng ta có thể lặp lại mô hình này.

Vậy g của big t trừ 3 bằng r của big t trừ 2 cộng gamma nhân g của big t trừ

2.

Và tất nhiên, điều này đúng với mọi giá trị của t.

Vì vậy, chúng ta có thể nói g của t bằng r của t cộng 1 cộng gamma nhân g của t cộng 1.

Vì vậy, bạn có thể tiếp tục lặp lại cùng một mẫu cho đến khi tính toán kết quả trả về cho mỗi trạng thái.

Thực tế mà nói, đây là cách bạn thực hiện điều đó bằng mã.

Trước tiên, bạn sẽ phát một tập bằng chính sách của mình và bạn sẽ nhận được một loạt trạng thái

và phần thưởng.

Tiếp theo, chúng tôi khởi tạo danh sách trả về một danh sách trống và chúng tôi khởi tạo trả về

ở mức không.

Sau đó và đây là phần quan trọng, bạn lặp lại các phần thưởng theo chiều ngược lại.

Bên trong vòng lặp chúng ta chỉ sử dụng định nghĩa đệ quy của g.

g bằng r cộng gamma nhân g.

Sau đó, chúng tôi thêm g vào danh sách trả về của mình.

Được rồi, vậy làm cách nào để đưa thuật toán trên vào mã giả?

Vâng, điều đó thật đơn giản.

Mọi thứ chúng ta vừa làm, bây giờ chúng ta chỉ làm theo vòng lặp.

Hãy làm điều chúng ta vừa làm vài trăm hoặc vài nghìn lần.

Sau đó, đối với mỗi tiểu bang, hãy lấy lợi nhuận trung bình.

Đầu tiên, chúng tôi giả định rằng chúng tôi được cung cấp một số chính sách.

Sau đó, chúng tôi khởi tạo một từ điển trống để lưu trữ kết quả trả về mẫu của mình.

Khóa của từ điển này sẽ là trạng thái và giá trị sẽ là danh sách các kết quả trả về gặp phải

xuyên suốt mỗi tập phim.

Sau đó, chúng tôi bước vào một vòng lặp tiếp tục với số tập được xác định trước.

Trong vòng lặp, trước tiên chúng tôi phát một tập bằng chính sách đã cho.

Điều này trả về cho chúng ta một danh sách các trạng thái và phần thưởng tương ứng.

Từ đó chúng ta có thể tính toán lợi nhuận cho từng trạng thái như đã mô tả trước đây.

Tiếp theo, chúng ta lặp qua từng trạng thái và trả về theo thứ tự tương ứng.

Đối với mỗi lần trả lại mà chúng tôi gặp phải, chúng tôi sẽ thêm thông tin đó vào danh sách trả lại cho trạng thái đó.

Vòng lặp này là cách chúng tôi thu thập mẫu của mình.

Cuối cùng, khi vòng lặp đầu tiên hoàn tất, chúng tôi đã hoàn tất việc thu thập mẫu của mình.

Bây giờ chúng ta có thể tính lợi nhuận trung bình theo định nghĩa là hàm giá trị.

Vì vậy, chúng tôi lặp qua từng mục trong từ điển trả về mẫu của mình.

Đối với mỗi lần lặp, chúng ta nhận được trạng thái s và danh sách mẫu trả về danh sách g.

Bên trong vòng lặp, V của s được gán đơn giản là giá trị trung bình mẫu của danh sách g.

Điều quan trọng là phải nhận ra điều đó.

Có một số vấn đề phức tạp với thuật toán như được mô tả.

Đầu tiên, vì chúng tôi chỉ đang lấy mẫu nên làm cách nào để đảm bảo rằng chúng tôi thực sự gặp phải mọi trạng thái có thể có trong số tập chúng tôi đã phát?

Trên thực tế, chúng tôi không thể.

Mặc dù chúng tôi có thể phỏng đoán rằng vì chúng tôi không gặp phải một trạng thái cụ thể nào đó nên chúng tôi không cần biết giá trị của nó vì chính sách của chúng tôi không cho phép chúng tôi đến đó.

Bạn có thể chỉ cần bỏ qua giá trị của các trạng thái đó trong bất kỳ hàm tiếp theo nào mà bạn cắm hàm giá trị vào.

Nhưng có một giải pháp tốt hơn.

Để hiểu được điều đó, chúng ta sẽ chuyển sang vấn đề thứ hai, vấn đề kiểm soát hay tìm ra chính sách tốt nhất.