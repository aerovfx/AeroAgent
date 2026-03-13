# 9 -Giải phương trình Bellman bằng học tăng cường (pt 2) đã dịch

---

Theo mô hình chung, lưu ý rằng đối với bài toán dự đoán, thông thường chúng ta quan tâm đến việc tìm

VFS, đó là điều chúng ta vừa làm.

Đối với bài toán điều khiển, chúng ta thường quan tâm đến việc làm việc với giá trị tác dụng Q của SA.

Lý do cho điều này là, nếu bạn nhớ lại, hàm Q giúp bạn dễ dàng tra cứu những gì

hành động cần thực hiện, với trạng thái S. Chúng tôi luôn lấy argmax cho tất cả các hành động có thể,

chúng ta gọi đây là hành động tham lam.

Bằng cách này, chúng tôi tối đa hóa những gì chúng tôi tin là tổng số phần thưởng trong tương lai.

Vì vậy, chỉ cần ghi nhớ mô hình chung này.

Đối với vấn đề dự đoán, chúng tôi làm việc với VFS.

Đối với bài toán điều khiển, chúng ta làm việc với Q của SA.

Để hiểu cách áp dụng phương pháp Monte Carlo vào bài toán điều khiển,

trước tiên chúng ta phải hiểu nguyên tắc lặp lại chính sách và cải tiến chính sách.

Hãy xem xét hai sự thật cơ bản.

Thứ nhất, với một chính sách nhất định, chúng ta có thể sử dụng Monte Carlo để đánh giá hàm giá trị, liệu

đó là giá trị trạng thái hoặc giá trị hành động.

Chúng ta vừa thấy điều đó ở bài giảng trước.

Với một hàm giá trị hành động, dựa trên điều này, chúng ta luôn có thể chọn những gì chúng ta tin tưởng

là hành động tốt nhất trong tình trạng hiện tại.

Đây chỉ là argmax của tất cả các hành động có thể xảy ra A.

Chà, hóa ra hai sự thật này phụ thuộc lẫn nhau.

Đưa ra một chính sách, chúng ta có thể tìm thấy giá trị hành động tương ứng của nó và từ đó, chúng ta có thể lấy

argmax để tìm một chính sách có thể tốt hơn.

Nhưng nếu chính sách này khác với chính sách ban đầu thì sao?

Sau đó chúng ta có thể tìm thấy hàm giá trị cho chính sách mới này.

Và từ đó, chúng ta có thể lấy lại argmax để tìm một cái mới khác và có thể tốt hơn,

nhưng ít nhất là chính sách tốt.

Từ đó, chúng ta có thể tìm lại hàm giá trị.

Bạn thấy đấy, đây chỉ là một vòng lặp, trong đó chúng ta quay đi quay lại để tìm hàm giá trị

đưa ra một chính sách và cải thiện chính sách dựa trên hàm giá trị đó.

Bạn có thể thấy rằng chúng tôi đã đặt tên cho hai bước này.

Hành động tìm hàm giá trị được gọi là bước đánh giá và hành động tìm

chính sách tốt nhất dựa trên hàm giá trị đó được gọi là bước cải tiến.

Và nói rõ hơn, lý do tại sao đây là một vòng lặp là vì cả hai đều thay đổi lẫn nhau.

Vì vậy, bằng cách thực hiện bước một, bạn thay đổi chính sách và bằng cách thực hiện bước hai, bạn thay đổi giá trị.

Điều đó đã được chứng minh, mặc dù chúng ta sẽ không thảo luận ở đây, rằng việc thực hiện các bước này sẽ dẫn đến

đến một sự cải thiện đơn điệu trong chính sách.

Vì vậy, nếu chúng ta cứ tiếp tục thực hiện quá trình này thì cuối cùng chúng ta sẽ đạt được chính sách tối ưu.

Vậy làm thế nào chúng ta có thể áp dụng điều này cho Monte Carlo?

Đây là một phác thảo thô.

Đầu tiên, chúng tôi bắt đầu bằng cách khởi tạo Q của SA và chính sách của chúng tôi đều là ngẫu nhiên.

Tiếp theo, chúng ta nhập một vòng lặp dành cho số tập được xác định trước.

Bên trong vòng lặp, trước tiên chúng ta đánh giá chính sách bằng cách tìm Q của SA cho chính sách đã cho.

Chúng tôi gọi đây là bước đánh giá chính sách.

Sau khi thực hiện xong việc đó, chúng tôi sẽ tìm ra chính sách mới trong đó đối với mỗi tiểu bang, chúng tôi sẽ thực hiện hành động để

là argmax của tất cả các hành động đối với Q của SA với một trạng thái nhất định.

Đây được gọi là bước cải tiến chính sách.

Điều này khá đơn giản và không khác gì bài toán dự đoán ngoại trừ một khác biệt nhỏ.

Lưu ý rằng trước đó khi chúng ta thảo luận về vấn đề đánh giá, chúng ta đã thảo luận cách tìm V của S.

Nhưng bây giờ chúng ta phải tìm Q của SA.

Để tìm Q của SA nơi chúng tôi đánh giá chính sách của mình, chúng tôi không chỉ cần theo dõi

các trạng thái và phần thưởng cũng như các hành động.

Vì vậy, chúng tôi sẽ ghi lại bộ ba trạng thái, hành động và phần thưởng.

Vì vậy, S1, A1, R1, S2, A2, R2, v.v.

Mã giả cho bước đánh giá sẽ trông như thế này.

Như bạn có thể thấy, điều này khá giống với việc tính V của S ngoại trừ khi chúng ta lưu trữ

mẫu trả về, chúng tôi lập chỉ mục từ điển theo cả trạng thái và hành động.

Trong phần thứ hai, Q lại là một từ điển nhưng bây giờ khóa là một bộ hành động trạng thái.

Ngoài ra, quá trình này hoàn toàn giống nhau.

Chúng tôi vẫn tính giá trị trung bình mẫu của từng danh sách trả về cho một khóa nhất định.

Tại thời điểm này, giải pháp của chúng tôi hoạt động nhưng không phải là giải pháp lý tưởng.

Hãy suy nghĩ về lý do tại sao.

Đầu tiên, nếu bạn nhớ lại, V của S chỉ lưu trữ các giá trị S lớn nhưng Q của SA lưu trữ các giá trị S lớn nhân với A lớn.

Như bạn đã biết, với việc lấy mẫu Monte Carlo, bạn thu thập càng nhiều mẫu thì càng chính xác.

câu trả lời của bạn trở thành

Khi chúng ta sử dụng Q của SA, chúng ta có nhiều giá trị hơn để ước tính và do đó chúng ta phải thu thập

nhiều mẫu hơn để có được ước tính chính xác.

Nhưng có một vấn đề thứ hai.

Mỗi bước đánh giá chính sách là một ước tính Monte Carlo, nghĩa là chúng ta phải tính toán

một số lượng lớn các mẫu.

Nhưng bây giờ chúng ta đã lồng vòng lặp này vào trong một vòng lặp khác.

Tác dụng của việc này là gì?

Giả sử vòng lặp chính sách của chúng ta cần chạy 1000 lần để tìm ra chính sách tối ưu.

Bây giờ, giả sử vòng lặp bên trong của chúng ta cần chạy 1000 lần để có được ước tính chính xác

của Q của S và A.

Chúng ta phải chơi bao nhiêu tập?

Câu trả lời là 1000 lần 1000 tức là 1 triệu.

Như bạn có thể thấy, việc sử dụng dữ liệu của chúng tôi không hiệu quả và số lần chúng tôi cần chơi trò chơi

trò chơi phát triển khá nhanh.

Một giải pháp tốt hơn là sử dụng cái gọi là lặp lại chính sách tổng quát.

Lúc đầu, cách tiếp cận này có vẻ kỳ quặc nhưng thực tế nó đã được chứng minh là có hiệu quả.

Ý tưởng là thế này.

Đối với bước đánh giá chính sách, thay vì phát nhiều tập để có kết quả tốt

ước tính giá trị của chính sách của chúng tôi, chúng tôi sẽ chỉ phát một tập.

Sau khi chơi tập này, chúng ta sẽ nhận được một loạt trạng thái, hành động và phần thưởng từ

mà chúng ta có thể tính toán lợi nhuận tương ứng.

Từ đó, chúng ta có thể lặp qua từng hành động trạng thái và trả về cũng như sử dụng mẫu mới nhất của

quay trở lại cập nhật Q của S và A.

Bây giờ bạn sẽ nhận thấy rằng tôi vừa đặt một số mã giả ở đây, cập nhật Q của S và A, nhưng

Tôi chưa nói với bạn chính xác chúng tôi sẽ làm điều đó như thế nào.

Chúng ta sẽ thảo luận về vấn đề này trong thời gian ngắn.

Điều quan trọng cần lưu ý ngay bây giờ là chúng tôi sẽ chỉ giữ một bản sao đang chạy của

Q của S và A. Bước tiếp theo và bước cuối cùng giống như trước.

Chúng tôi cập nhật chính sách bằng cách lấy argmax trên Q cho một trạng thái nhất định trên tất cả các hành động.

Vậy chuyện gì đang xảy ra với dòng này ở đây?

Làm cách nào để cập nhật Q của S và A, dựa trên ước tính cũ về Q của S và A?

Đối với điều này, chúng ta cần thực hiện một phép hồi quy ngắn để quay lại giá trị trung bình mẫu và giá trị mong đợi

một lần nữa.

Vì tôi chắc rằng đến giờ bạn đã chán việc tôi nhắc lại, đây là biểu thức của mẫu

nghĩa là.

Chúng tôi tổng hợp tất cả các mẫu và chia cho tổng số mẫu.

Câu hỏi chúng ta phải đặt ra là liệu đây có phải là một phép tính hiệu quả?

Câu trả lời là không.

Tổng hợp và giá trị là tất cả của n.

Càng lưu trữ nhiều giá trị thì càng mất nhiều thời gian để tính toán.

Điều này không tốt.

Vì vậy, câu hỏi đặt ra là có cách nào để giảm thời gian tính toán mẫu không?

nghĩa là mỗi lần tôi thu thập một mẫu mới?

Để xem điều này được thực hiện như thế nào, hãy biểu thị ý nghĩa mẫu theo mẫu trước đó

trung bình và mẫu mới nhất.

Trước khi chúng ta tiếp tục, hãy đảm bảo rằng bạn có thể tự mình rút ra điều này trên giấy.

Trong đạo hàm mà bạn thấy ở đây, x bar n có nghĩa là giá trị trung bình mẫu sử dụng n mẫu đầu tiên.

Do đó, x bar n trừ 1 có nghĩa là giá trị trung bình của mẫu sử dụng n mẫu đầu tiên trừ 1.

Bí quyết là chúng ta có thể biến biểu thức trên thành một biểu thức trông giống và trên thực tế

là sự giảm độ dốc.

Chúng ta có thể viết nó sao cho nó trông quen thuộc hơn một chút.

Ước tính mới bằng ước tính cũ cộng 1 trên n lần mẫu trừ đi ước tính cũ

ước tính.

Trong trường hợp này, mục tiêu là mẫu mới nhất mà chúng tôi đã thu thập trong khi ước tính cũ

là dự đoán của chúng tôi

1 trên n là tốc độ học, do đó tốc độ học này giảm dần theo thời gian.

Bằng cách sử dụng tốc độ học như vậy, chúng ta sẽ thu được chính xác giá trị trung bình của mẫu.

Hãy nhớ rằng, tất cả những gì chúng ta đã làm cho đến nay là đại số cơ bản.

Đây là giao diện nếu chúng tôi dịch nó sang học tập tăng cường Monte Carlo

mã để cập nhật Q.

Ước tính mới về Q của S và A được cập nhật thành ước tính cũ cộng 1 trên n lần

lợi nhuận mới nhất trừ đi ước tính cũ.

Chỉ cần lưu ý rằng dấu bằng ở đây có nghĩa là phép gán khi không nói rằng cả hai bên đều bằng nhau.

Bên trái là ước tính mới, bên phải là ước tính cũ.

Chúng tôi chỉ không bận tâm đến việc đăng ký chúng.

Tuy nhiên, chúng tôi vẫn chưa hoàn thành vì chúng tôi sẽ thực hiện một sửa đổi khác cho vấn đề này.

Hãy nhớ rằng trong vòng lặp chính sách tổng quát mới nhất của chúng tôi, chúng tôi đang cập nhật cùng một

Từ điển Q sử dụng các chính sách khác nhau.

Chính sách này đang được cập nhật theo từng bước.

Và do đó, các mẫu mà chúng tôi đang sử dụng để tính Q của S và A không đến từ

sự phân bố giống nhau.

Trong trường hợp này, chúng tôi không muốn sử dụng chính xác giá trị trung bình mẫu.

Theo trực giác, các mẫu cũ nhất đến từ các chính sách cũ nhất.

Họ không thực sự quan trọng đến thế.

Các mẫu mới nhất đến từ các chính sách mới nhất và chúng quan trọng hơn.

Điều quan trọng là sử dụng tốc độ học tập không đổi thay vì tốc độ giảm dần theo thời gian.

Làm như vậy sẽ cho chúng ta cái gọi là trung bình phân rã theo cấp số nhân.

Ý tưởng là khi bạn lấy giá trị trung bình của mẫu thông thường, mỗi mẫu sẽ có trọng số như nhau.

Như chúng tôi đã nói, chúng tôi không muốn điều đó bởi vì những giá trị cũ đến từ những chính sách cũ và vì thế chúng đến.

từ một bản phân phối khác với bản phân phối mà chúng ta đang quan tâm.

Mặt khác, trọng số trung bình giảm dần theo cấp số nhân của mỗi mẫu theo cấp số nhân

thời trang mục nát.

Mẫu gần đây nhất quan trọng nhất và trọng lượng của mỗi mẫu giảm dần theo cấp số nhân

khi bạn quay ngược lại thứ tự chúng được thu thập.

Vì vậy, bây giờ chúng ta có thể diễn đạt lại mã lặp chính sách tổng quát của mình, nhưng lần này chúng ta có thể

điền chi tiết còn thiếu này về cách cập nhật Q của S A.

Vì vậy, đây chính xác là mã giả như trước đây, ngoại trừ việc tôi đã thay thế khối mã ở giữa

với bản cập nhật thực tế chúng ta có thể sử dụng để cập nhật Q.

Thật không may, tại thời điểm này, có một chi tiết tế nhị nhưng quan trọng mà chúng ta vẫn chưa thảo luận.

Vì vậy, chúng tôi chưa hoàn tất việc xác định thuật toán của mình nhưng chúng tôi đã đặt ra hầu hết nền tảng.