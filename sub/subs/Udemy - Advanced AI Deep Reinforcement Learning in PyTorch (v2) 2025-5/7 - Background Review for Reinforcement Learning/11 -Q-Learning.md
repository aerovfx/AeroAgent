# 11 -Q-Learning đã dịch

---

Cuối cùng, chúng ta đã sẵn sàng nghiên cứu thuật toán học tín hiệu nổi tiếng.

Hãy tóm tắt lại những gì chúng ta đã làm cho đến nay vì đó là một quá trình khá dài để có được

để gợi ý việc học.

Đầu tiên chúng tôi xác định tất cả các thuật ngữ có liên quan, chẳng hạn như tác nhân, môi trường, trạng thái, phần thưởng hành động

vân vân.

Việc học những định nghĩa này cho phép chúng tôi cấu trúc vấn đề của mình một cách toán học.

Cụ thể, chúng ta có thể mô hình hóa các vấn đề học tăng cường như MDP, quy trình quyết định Markov.

Tiếp theo, chúng tôi xem xét cách giải quyết MDP, nghĩa là có hai điều.

Đầu tiên, chúng ta giải quyết vấn đề dự đoán, tìm hàm giá trị cho một chính sách.

Thứ hai, chúng tôi giải quyết vấn đề kiểm soát, tìm ra chính sách tốt nhất trong một môi trường nhất định.

Chúng tôi biết rằng, nếu chúng tôi biết tất cả các xác suất trong MDP thì việc này khá dễ dàng.

Nhưng khi không biết xác suất, chúng ta có thể sử dụng các phương pháp lấy mẫu mà chúng ta gọi là

Monte Carlo.

Có một vấn đề lớn với Monte Carlo.

Nghĩa là, để tính lợi nhuận, chúng ta phải đợi cho đến khi một tập phim kết thúc.

Điều này là do lợi nhuận được định nghĩa là tổng của tất cả các phần thưởng trong tương lai.

Chúng tôi không thể biết tổng số phần thưởng trong tương lai cho đến khi chúng tôi thu thập được chúng.

Và do đó, chúng ta phải đạt đến trạng thái cuối trước khi tính toán kết quả trả về mẫu.

Tại sao đây là một vấn đề?

Chà, hãy tưởng tượng kịch bản mà bạn có những tập phim rất dài hoặc kịch bản có

không có trạng thái kết thúc.

Trong trường hợp sau, Monte Carlo không phải là một lựa chọn.

Trước đây, điều đó vẫn chưa lý tưởng, vì điều đó có nghĩa là đại lý của bạn phải chi rất nhiều

trong một thời gian dài hoạt động dưới mức tối ưu, mặc dù nó đã thu thập được rất nhiều dữ liệu từ

mà nó có thể cải thiện.

Câu trả lời cho vấn đề này là các phương pháp sai phân theo thời gian.

Nếu bạn nhớ lại, tôi đã nói trước đó rằng một trong những tính năng quan trọng nhất của việc hoàn trả là

rằng nó có thể được định nghĩa một cách đệ quy.

Lợi nhuận tại thời điểm t có thể được biểu diễn dưới dạng lợi nhuận tại thời điểm t cộng 1.

Bạn đã thấy điều này đã giúp chúng ta tạo ra và giải phương trình Bellmit như thế nào.

Bây giờ nó sẽ giúp chúng ta một lần nữa.

Một cách đơn giản để nghĩ về nó là thế này.

Các phương pháp Monte Carlo là một bài toán gần đúng về giá trị kỳ vọng.

Các phương pháp sai phân theo thời gian đơn giản là một phương pháp gần đúng với Monte Carlo.

Vì vậy, nói cách khác, chúng là một xấp xỉ của một xấp xỉ.

Tất cả chỉ là một mẹo nhỏ với phương pháp Monte Carlo.

Khi chúng tôi cập nhật Q hoặc V, đây là giá trị trung bình mẫu của tất cả các mẫu chúng tôi đã thu thập,

chúng tôi không phải thể hiện bản cập nhật dưới dạng trung bình mẫu.

Điều đó có nghĩa là chúng tôi phải giữ tất cả các mẫu xung quanh, việc này có thể chiếm nhiều bộ nhớ

và mất nhiều thời gian để tính toán.

Thay vào đó, chúng ta có thể biểu thị trung bình mẫu hiện tại theo trung bình mẫu trong quá khứ.

Chúng tôi lưu ý rằng điều này trông rất giống với việc giảm độ dốc.

Chà, tại sao không thử nghiệm lý thuyết này?

Hãy đặt sai số bình phương j của chúng ta là sai số bình phương giữa mục tiêu thực sự g và giá trị của tôi

đối với trạng thái s V của s.

Bây giờ, giả sử tôi muốn cập nhật V của s bằng mẫu g mới nhất mà tôi vừa thu thập.

Để thực hiện cập nhật, tôi sẽ sử dụng phương pháp giảm độ dốc.

Đặt V của s là giá trị cũ của V của s trừ đi tốc độ học nhân với gradient.

Vâng, độ dốc là gì?

Nếu chúng tôi đưa gradient này vào bản cập nhật giảm độ dốc của mình,

và bỏ qua cả hai, vì nó có thể được đưa vào tốc độ học tập,

chúng tôi lấy lại phương trình cập nhật chính xác mà chúng tôi sẽ sử dụng cho mức trung bình giảm dần theo cấp số nhân.

Là một lưu ý phụ, tôi muốn đề cập rằng cuối cùng không có sự khác biệt

liệu chúng ta có gọi những gì chúng ta đang làm là chuyển màu là chúng ta và giảm dần độ dốc hay không.

Vì có dấu cộng ở đây nên bạn có thể nghĩ nó là độ dốc của chúng tôi và.

Dấu cộng được sử dụng tự nhiên nếu bạn rút ra biểu thức này từ bản cập nhật trung bình mẫu.

Nhưng nếu bạn rút ra biểu thức này từ sai số bình phương, bạn sẽ nhận được dấu âm,

và bạn có thể coi đó là sự giảm dần độ dốc.

Tuy nhiên, cuối cùng thì đây chỉ là đại số cơ bản và bạn nên tự khẳng định rằng cả hai biểu thức đều tương đương nhau.

Vậy điều này có gì đáng chú ý?

Bây giờ chúng ta sẽ kết hợp hai ý tưởng này lại với nhau.

Ý tưởng số một là cập nhật hàm giá trị bằng cách sử dụng giá trị trung bình giảm dần theo cấp số nhân

giống như giảm độ dốc.

Ý tưởng số hai là lợi nhuận có thể được xác định theo cách đệ quy.

Vậy còn chuyện này thì sao?

Chúng ta sẽ tiếp tục sử dụng phương pháp giảm độ dốc, nhưng thay vì sử dụng toàn bộ lợi nhuận,

chúng ta sẽ ước tính lợi nhuận.

Chúng tôi thu thập phần thưởng tiếp theo r, nhưng thay vì chờ đợi để nhận bất kỳ phần thưởng nào trong tương lai,

chúng ta chỉ đơn giản đoán rằng chúng sẽ gần với V của s nguyên tố, giá trị của trạng thái nơi

chúng tôi đã hạ cánh.

Vì vậy, thay vì sử dụng g bằng r cộng gamma nhân phần thưởng tiếp theo cộng gamma bình phương

phần thưởng tiếp theo, v.v., chúng ta nhận ra rằng g chỉ bằng r cộng gamma nhân với

trở lại tiếp theo g prime.

Nhưng g prime có giá trị kỳ vọng V của s prime.

Vì vậy, thay vào đó chúng ta chỉ nói g xấp xỉ bằng r cộng gamma nhân V của s prime.

Bằng cách này, chúng ta chỉ phải đợi một bước trước khi cập nhật mô hình của mình.

Chúng ta không còn phải đợi đến cuối tập phim nữa.

Chúng ta gọi r cộng gamma nhân V của s prime là ước tính lợi nhuận đã được khởi động.

Nó cho phép chúng ta cập nhật V của s ngay sau khi nhận được phần thưởng r tiếp theo, thay vì

phải đợi cho đến khi chúng tôi thu thập được tất cả các phần thưởng trong tương lai.

Phương pháp này được gọi là phương pháp sai phân theo thời gian.

Đây là một số trích dẫn giả để bạn có thể khái niệm hóa cách thức hoạt động của nó.

Là một lưu ý phụ, điều này cũng sẽ cung cấp cho bạn một số thông tin chi tiết về những gì đang diễn ra bên trong chúng ta.

phát chức năng tập phim mà chúng ta chưa thực sự thảo luận.

Trong mã giả này, chúng ta không cần phải loại bỏ chức năng phát tập phim,

vì việc phát tập phim là một phần của vòng lặp này.

Chúng tôi có nhiều việc phải làm ở mỗi bước của tập phim và do đó chúng tôi không thể gói gọn nó hoặc

ủy thác nó cho một số chức năng khác.

Để bắt đầu, giả sử chúng ta được cung cấp một số môi trường và một số chính sách.

Chúng tôi khởi tạo hàm giá trị là ngẫu nhiên.

Sau đó, chúng tôi vào một vòng lặp phát một số tập được xác định trước.

Ngoài ra, bạn cũng có thể chạy vòng lặp cho đến khi thấy V của s hội tụ, hoặc theo cách khác

lời nói, ổn định trên một số giá trị và không đi chệch khỏi nó.

Bên trong vòng lặp, chúng ta bắt đầu phát một tập.

Điều đầu tiên chúng tôi làm là gọi ENV.reset, nó sẽ đặt lại môi trường và đưa chúng tôi trở lại

về trạng thái ban đầu và trả về trạng thái ban đầu đó.

Chúng ta sẽ gọi nó là s.

Tiếp theo, chúng ta khởi tạo cờ Boolean done thành false.

Cờ Boolean này sẽ được đặt thành true khi chúng tôi hoàn thành một tập.

Tiếp theo, chúng ta nhập một vòng lặp while hoàn thành khi done trở thành đúng.

Bên trong vòng lặp, chúng tôi lấy hành động từ chính sách của mình.

Sau đó chúng tôi thực hiện hành động trong môi trường bằng cách gọi ENV.step.

Điều này trả về ba điều.

Trạng thái tiếp theo là trạng thái nguyên tố, phần thưởng r và cờ hoàn thành tiếp theo.

Lưu ý rằng tôi đã thiết kế mã giả này tương tự như API phòng tập thể dục OpenAI, có

trở thành tiêu chuẩn trong vài năm qua.

Điều này thật dễ hiểu và nó sẽ giúp ích cho bạn trong tương lai nếu bạn bắt đầu sử dụng OpenAiGym.

Điều ngược lại cũng đúng.

Nếu bạn đã từng sử dụng OpenAI Gym trước đây thì điều này sẽ giúp mọi việc dễ hiểu hơn.

Tiếp theo chúng tôi thực hiện cập nhật lớn.

Bản cập nhật khác biệt tạm thời mà chúng ta đã thảo luận trong suốt bài giảng này.

Cuối cùng, và điều quan trọng là đừng quên.

Chúng ta phải cập nhật biến s cho lần lặp tiếp theo của vòng lặp.

Trạng thái tiếp theo hiện tại là trạng thái nguyên tố sẽ trở thành trạng thái hiện tại s trong lần lặp tiếp theo.

Cuối cùng, khi vòng lặp hoàn tất, VFS đã hội tụ.

Có một điều kỳ lạ về việc học theo sự khác biệt về thời gian.

Hãy xem xét kỹ cái gọi là cập nhật giảm độ dốc này.

Mục tiêu là r cộng gamma nhân VFS prime.

Dự đoán là VFS.

Nếu chúng ta liên hệ điều này với việc học có giám sát, chúng ta sẽ nhận thấy điều gì đó kỳ lạ.

Trong học có giám sát, chúng ta được cung cấp mục tiêu như một phần của tập dữ liệu.

Nhưng ở đây chúng tôi đang làm một điều đáng ngạc nhiên.

Chúng tôi đang dự đoán chính mục tiêu.

Một phần mục tiêu được trao, đó là phần thưởng r.

Nhưng phần còn lại, VFS prime, thực ra là một dự đoán mô hình.

Vì vậy, sẽ đúng hơn khi nói rằng những gì chúng ta đang làm không hoàn toàn là giảm độ dốc.

Thay vào đó, nó được gọi là bán gradient.

Nhưng đây chỉ là một cái tên.

Đó là nguyên tắc quan trọng.

Nguyên tắc là chúng tôi không biết mục tiêu thực sự, chúng tôi chỉ ước tính nó.

Và điều này làm cho nó rất khác với việc học có giám sát.

Được rồi, những gì chúng ta đã xem xét cho đến nay là vấn đề dự đoán.

Bây giờ cuối cùng cũng đến lúc tiết lộ lớn.

Chúng ta sẽ giải quyết vấn đề điều khiển bằng thuật toán q learning nổi tiếng.

Tại thời điểm này, chúng tôi đã dành rất nhiều thời gian để xây dựng các điều kiện tiên quyết cho việc học q, để bạn

hầu như không nên ngạc nhiên với những gì bạn nhìn thấy.

Tuy nhiên, chúng ta hãy có một cái nhìn.

Như trước đây, vì q học là một thuật toán điều khiển nên chúng ta quan tâm đến việc cập nhật q thay vì

hơn là cập nhật V.

Ở mức độ cao, chúng ta chủ yếu quan tâm đến phần trong cùng của vòng lặp.

Đó là nơi chúng tôi chọn một hành động và thực hiện một bước trong môi trường cũng như nơi chúng tôi cập nhật

bảng q.

Vì vậy đây là hai phần chúng ta sẽ tập trung vào ở đây.

Khi chúng ta chọn một hành động, một lần nữa, chúng ta sẽ sử dụng cách tiếp cận tham lam của Epsilon.

Vì vậy với xác suất Epsilon nhỏ, chúng ta sẽ chọn một hành động ngẫu nhiên.

Nếu không, chúng ta sẽ lấy argmax trên q với trạng thái s.

Khi chúng ta chọn hành động của mình, chúng ta sẽ thực hiện hành động đó trong môi trường.

Khi chúng tôi cập nhật q, chúng tôi làm một điều gì đó rất tinh tế nhưng quan trọng.

Nghĩa là, khi tính toán mục tiêu, chúng ta bỏ qua bất kỳ hành động nào chúng ta sẽ thực hiện tiếp theo.

Thay vào đó, chúng ta giả định rằng chúng ta sẽ thực hiện hành động tham lam và đạt giá trị lớn nhất trên q với điều kiện

số nguyên tố của bang.

Điều này có hai lợi thế.

Đầu tiên, điều đó có nghĩa là, để cập nhật q, chúng ta không phải đợi cho đến khi có được

hành động tiếp theo là số nguyên tố trong lần lặp tiếp theo của vòng lặp.

Thứ hai, nó khiến q phải học cái được gọi là thuật toán ngoài chính sách.

Điều này có nghĩa là tôi có thể tự do khám phá nhưng thuật toán của tôi sẽ cập nhật bảng q như thể tôi

đã hành động một cách tham lam.

Vì vậy, đây là cách học q khi chúng ta kết hợp tất cả lại với nhau.

May mắn thay, nó trông khá giống với mã giả của bài toán dự đoán.

Đầu tiên chúng ta được cung cấp một số đối tượng môi trường.

Sau đó chúng ta khởi tạo q với các giá trị ngẫu nhiên.

Sau đó, chúng tôi nhập một vòng lặp dành cho một số tập được xác định trước.

Theo tùy chọn, bạn có thể tiếp tục cho đến khi q hoặc chính sách hội tụ.

Tiếp theo nó giống như những gì chúng ta đã có trước đây.

Chúng tôi thiết lập lại môi trường và bắt đầu lại ở trạng thái ban đầu.

Chúng tôi khởi tạo cờ done thành false.

Sau đó, chúng tôi chỉ nhập một vòng lặp để thoát khỏi tập khi chúng tôi hoàn thành.

Tiếp theo chúng ta sử dụng epsilon tham lam để chọn một hành động.

Sau đó, chúng tôi thực hiện một bước trong môi trường.

Chúng tôi lấy lại số nguyên tố của bang, phần thưởng r và cờ hoàn thành.

Tiếp theo, chúng ta tạo mục tiêu cho bản cập nhật q, lấy giá trị tối đa trên q cho trạng thái nguyên tố s.

Tiếp theo, chúng tôi cập nhật q của s và a bằng cách sử dụng mục tiêu mà chúng tôi vừa tính toán.

Cuối cùng, chúng tôi cập nhật trạng thái hiện tại s thành trạng thái nguyên tố tiếp theo.

Cuối cùng, khi thoát khỏi vòng lặp, chúng ta đã tìm được chính sách tối ưu.

Hãy tóm tắt những gì chúng ta vừa làm vì nó khá dài.

Đầu tiên chúng tôi bắt đầu bằng việc lưu ý rằng Monte Carlo sẽ không hoạt động trong những tập phim dài vô tận.

Và vấn đề là chúng ta phải đợi cho đến khi một tập phim kết thúc mới có thể học được.

Thay vào đó, chúng tôi sử dụng thực tế là kết quả trả về có thể được xác định theo cách đệ quy.

Điều này cho phép chúng tôi ước tính lợi nhuận gần đúng bằng cách chỉ sử dụng phần thưởng tiếp theo và giá trị ở trạng thái tiếp theo.

Chúng tôi cũng biết được rằng học tăng cường cuối cùng bắt đầu giống như học có giám sát,

trong đó mục tiêu của chúng tôi không phải là mục tiêu thực sự mà là ước tính được thực hiện bởi mô hình của chính chúng tôi.

Về cơ bản, chúng tôi đang thực hiện giảm độ dốc trên bảng q.

Sử dụng phương pháp này, nó cho phép chúng tôi cập nhật bảng q của mình ở mỗi bước vì chúng tôi chỉ phải đợi

cho đến khi chúng tôi nhận được một phần thưởng duy nhất để thực hiện cập nhật.

Chúng tôi gọi cách tiếp cận này là học trực tuyến vì tác nhân học trong khi thu thập dữ liệu.