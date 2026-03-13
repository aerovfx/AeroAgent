# 3 -States, Hành động, Khen thưởng, Chính sách dịch

---

Trong bài giảng này, chúng ta sẽ thảo luận sâu hơn về khái niệm trạng thái, hành động và phần thưởng.

chiều sâu.

Bài giảng này nói về cách chúng ta mã hóa các trạng thái và hành động khi lập trình.

Nói về trạng thái, hành động và phần thưởng, về mặt lý thuyết thì hay, nhưng cuối cùng chúng ta lại

sẽ phải đưa cái này vào mã.

Xin lưu ý thêm, vì phần thưởng chỉ là những con số nên điều này không quan trọng.

Không cần phải thảo luận về cách chúng ta biểu diễn các con số trong mã.

Hãy bắt đầu với nhà nước.

Như đã đề cập trước đó, trạng thái có thể rời rạc hoặc liên tục.

Trong trò chơi như Tic Tac Toe, các trạng thái rời rạc vì chúng chỉ có cấu hình khác nhau

của bảng Tic Tac Toe.

Nếu chúng ta chế tạo một robot có các cảm biến như máy ảnh, micrô, con quay hồi chuyển, khoảng cách

cảm biến, v.v., tất cả đều là những giá trị liên tục.

Vì vậy, bạn sẽ thu được một vectơ có giá trị liên tục.

Trên thực tế, điều này đưa chúng ta trở lại quá trình học tập có giám sát thường xuyên.

Nếu mục tiêu của chúng ta được phân loại, chúng ta thể hiện chúng như thế nào?

Trong mã, nếu có K danh mục, chúng ta sẽ sử dụng các số nguyên từ 0 đến K trừ 1.

Vì vậy, chúng ta có thể nói rằng con chó bằng 0, con mèo bằng 1, con chuột bằng 2, v.v.

Rõ ràng, việc phân loại nào được gán số nào không quan trọng.

Và lý do chúng tôi muốn làm điều này là vì đến một lúc nào đó, chúng tôi sẽ phải sử dụng

các danh mục này dưới dạng chỉ số mảng.

Và tương tự như vậy, nếu chúng ta có trạng thái S lớn thì chúng ta sẽ biểu diễn chúng bằng mã bằng cách sử dụng

số nguyên từ 0 đến S lớn trừ 1.

Đối với các giá trị liên tục, việc lưu trữ chúng trong một vectơ là hợp lý.

Mặc dù nếu bạn có thứ gì đó giống như hình ảnh thì nó sẽ là một tenxơ ba chiều.

Vì vậy, một cách ngắn gọn, nếu bạn có các giá trị liên tục, bạn có thể coi chúng như một tensor với một

hoặc nhiều kích thước.

Bây giờ bạn đã biết cách biểu diễn các trạng thái và hành động trong mã, đã đến lúc nói về

chính sách.

Khi tôi mới bắt đầu tìm hiểu về học tăng cường, tôi nhận thấy các chính sách có vẻ hơi kỳ quặc.

ý tưởng.

Thực ra, tôi thấy tất cả các phương pháp học tăng cường có phần kỳ quặc và xa lạ, nhưng

bạn sẽ quen với nó.

Ý tưởng về một chính sách có ý nghĩa ở mức độ cao, nhưng nó trở nên mơ hồ khi

bạn bắt đầu nghĩ về cách biểu diễn nó bằng toán học hoặc bằng mã.

Chính sách là những gì tác nhân sử dụng để xác định hành động nào cần thực hiện trong một trạng thái nhất định.

Điều quan trọng cần ghi nhớ là chính sách mang lại một hành động chỉ sử dụng trạng thái hiện tại.

Nó không sử dụng bất kỳ sự kết hợp nào giữa trạng thái hiện tại và trạng thái trước đó, và nó không

sử dụng bất kỳ thông tin nào về phần thưởng.

Về mặt kỹ thuật, như tôi đã đề cập trước đó, trạng thái có thể được tạo thành từ nhiều quan sát,

và điều đó cũng có thể bao gồm phần thưởng, mặc dù điều đó không bình thường.

Nhưng nói đúng ra, chính sách sẽ mang lại một hành động chỉ sử dụng trạng thái hiện tại.

Cách đơn giản nhất để nghĩ về một chính sách là nó là một ánh xạ từ điển hoặc một hàm

trả về một hành động cho một trạng thái.

Đây là một chức năng như vậy.

Như bạn có thể thấy, đầu vào duy nhất là trạng thái s và nó trả về một hành động a trong đó trạng thái

s là chìa khóa của từ điển và hành động a là giá trị.

Câu hỏi thực sự là, làm thế nào chúng ta có thể biểu diễn điều này về mặt toán học?

Đây là lý do tại sao trước tiên nên nói về cách chúng ta mã hóa các trạng thái và hành động.

Vì vậy, hãy tưởng tượng một lần nữa chúng ta đang ở trong thế giới lưới.

Nhân viên hỗ trợ của bạn hiện có một từ điển thể hiện hành động cần thực hiện với trạng thái nhất định như bạn có thể thấy ở đây.

Vì vậy, ví dụ, nếu chúng ta ở bên trái trạng thái mục tiêu, thì hành động thích hợp là di chuyển sang phải.

Và nói rõ hơn, tỉ số bên trái là 0-2.

Nếu chúng ta đang ở trạng thái ban đầu thì hành động thích hợp là tiến lên.

Và để cho rõ ràng, đó là trạng thái về 0.

Bây giờ, từ trạng thái ban đầu, việc di chuyển sang phải cũng hợp lệ vì chúng ta vẫn có thể đạt được mục tiêu từ thời điểm đó.

Bạn có thể thấy rằng, mặc dù tôi đã mã hóa các trạng thái ở đây một cách rõ ràng dưới dạng bộ dữ liệu, nhưng chúng ta có thể đạt được hiệu quả cao hơn

bằng cách mã hóa chúng dưới dạng số nguyên tương ứng với các bộ dữ liệu và sử dụng các số nguyên đó để lập chỉ mục cho một mảng.

Như bạn có thể nhớ lại từ các nghiên cứu khoa học máy tính của mình, việc lập chỉ mục mảng nhanh hơn lập chỉ mục từ điển.

Suy nghĩ về các chính sách như ánh xạ từ điển có phần hạn chế.

Có hai lý do cho việc này.

Đầu tiên, điều này sẽ không hoạt động nếu bạn có không gian trạng thái vô hạn.

Bạn sẽ cần một từ điển có kích thước vô hạn mà không thể có được.

Thứ hai là nó không cho phép tác nhân của chúng tôi khám phá môi trường của nó.

Hãy coi việc đào tạo người đại diện của bạn giống như dạy một đứa trẻ.

Lúc đầu, một đứa bé không biết gì cả.

Nó phải thử những điều mới để tìm ra cách thế giới vận hành và xây dựng trực giác của mình.

Một tác nhân học tăng cường cũng theo cách tương tự.

Nếu nó có một chính sách cố định và lúc nào cũng chỉ làm một việc thì nó không thể có được những trải nghiệm mới.

Vì vậy, việc các chính sách mang tính ngẫu nhiên là điều hợp lý.

Stochastic chỉ là một từ ưa thích để chỉ sự ngẫu nhiên.

Nói cách khác, một cách tổng quát hơn để biểu diễn các chính sách là biểu diễn chúng dưới dạng xác suất.

Việc biểu diễn các chính sách dưới dạng xác suất thực sự giải quyết được cả hai vấn đề tôi đặt ra ở trên.

Hãy xem làm thế nào.

Đầu tiên, nó giải quyết vấn đề ngẫu nhiên này.

Cách phổ biến để giải quyết vấn đề này trong học tăng cường là cho phép tác nhân khám phá là cho nó một cơ hội nhỏ để thực hiện một hành động ngẫu nhiên.

Vì vậy, đây là một hàm Python có thể thực hiện được điều này.

Đầu tiên chúng tôi tạo ra một số ngẫu nhiên.

Nếu con số này nhỏ hơn một số epsilon nhỏ nào đó, giả sử là 0,1, thì nó sẽ chọn một hành động ngẫu nhiên từ không gian hành động.

Nếu không, chúng tôi sẽ thực hiện một hành động từ chính sách cố định, ánh xạ từ điển của chúng tôi.

Phương pháp này được gọi là epsilon tham lam, và bạn sẽ tìm hiểu sau trong phần này tại sao nó hữu ích và tầm quan trọng của việc khám phá.

Vậy còn không gian trạng thái liên tục thì sao?

Trên thực tế, việc coi các chính sách mang tính xác suất dễ dàng phù hợp với không gian trạng thái liên tục hoặc vô hạn.

Hãy tưởng tượng trạng thái của bạn dưới dạng một vectơ s.

Bây giờ hãy tưởng tượng chúng ta có một số tham số chính sách w.

Hình dạng của w là chiều của không gian trạng thái theo kích thước của không gian hành động.

Hiện tại, chúng ta giả định rằng không gian hành động vẫn mang tính phân loại.

Vậy chúng ta phải làm gì khi muốn xuất ra các xác suất cho một tập hợp các danh mục?

Trên thực tế, điều này cũng giống như việc phân loại.

Chúng ta có thể sử dụng hàm softmax.

Vì vậy, bây giờ chính sách của chúng ta là softmax của w được chấm bằng trạng thái s.

Như bạn có thể thấy, điều này cho phép chúng tôi giới thiệu thêm một chút ký hiệu.

Trong học tăng cường, người ta thường biểu thị chính sách bằng ký hiệu pi, đừng nhầm lẫn với số pi.

Đối với bất kỳ trạng thái nào, chúng ta có thể tính toán phân bố xác suất trên không gian tác dụng, pi của một s cho trước.

Sau đó, để quyết định hành động nào sẽ thực hiện trong môi trường, chúng ta có thể chỉ cần lấy mẫu từ bản phân phối này.

Điều này cho phép chúng tôi khám phá nếu cần thiết, nhưng chúng tôi vẫn có thể xử lý chính sách này một cách xác định nếu muốn, chỉ bằng cách sử dụng argmax.

Cũng lưu ý rằng không cần thiết phải sử dụng mô hình tuyến tính như chúng tôi đang làm ở đây.

Trên thực tế, chúng ta có thể sử dụng bất kỳ công cụ xấp xỉ hàm nào, chẳng hạn như mạng nơ-ron.

Tại thời điểm này, bạn có thể tự hỏi, làm thế nào một tác nhân thông minh có thể biết phải làm gì chỉ bằng trạng thái hiện tại?

Đây là vấn đề chúng tôi đã mô tả trước đây.

Chỉ cần nhìn vào hình ảnh tĩnh của con đường, làm sao tôi có thể biết được hành động đúng là gì?

Nếu bạn có xu hướng suy nghĩ về mô hình học tập có giám sát, bạn có thể nhấn mạnh rằng cần phải có mục tiêu ở đây,

để tác nhân học cách liên kết trạng thái này với hành động này.

Nhưng trên thực tế, một đặc vụ hoàn toàn có thể học cách lập kế hoạch cho tương lai bằng cách sử dụng kinh nghiệm thu thập được khi chơi nhiều tập.

Ngay cả khi không có mục tiêu rõ ràng cho một trạng thái nhất định, tác nhân vẫn có thể tìm hiểu hành động nào cần thực hiện để tối đa hóa phần thưởng trong tương lai.

Đây là nội dung chúng ta sẽ tìm hiểu trong các bài giảng sắp tới.