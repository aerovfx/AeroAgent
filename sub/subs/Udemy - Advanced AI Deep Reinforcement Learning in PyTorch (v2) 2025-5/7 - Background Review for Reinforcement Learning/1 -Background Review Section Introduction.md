# 1 -Phần ôn tập lý lịch Phần giới thiệu đã được dịch

---

Trong phần này của khóa học, chúng ta sẽ thảo luận về lý thuyết đằng sau việc học tăng cường.

Bài giảng này sẽ giới thiệu cho bạn về học tăng cường và chúng ta sẽ nói về

về nó một cách tổng quát mà không có bất kỳ phép toán hay thuật ngữ nào.

Một điều bạn phải chuẩn bị tinh thần khi học về học tăng cường

việc giám sát việc học tập khác nhau như thế nào.

Vì vậy, nếu bạn vừa mới đọc phần giới thiệu về học máy, nơi bạn đã học về các mô hình

chẳng hạn như các cụm vịnh ngây thơ và cụm camion, hoặc bạn đến từ nền tảng thống kê,

bạn sẽ ngạc nhiên về sự khác biệt giữa việc học tăng cường so với những gì bạn đã quen.

Vì vậy, hãy cố gắng dành chút thời gian để tiếp thu những khái niệm này và đừng cảm thấy sợ hãi trước những khái niệm mới này.

và cách suy nghĩ khác nhau.

Tôi muốn bắt đầu bằng việc nghĩ về việc học có giám sát.

Ví dụ: khi chúng ta nghĩ về một bộ phân loại hình ảnh, bạn có thể coi nó như một hàm tĩnh.

Tôi chuyển vào một hình ảnh và tôi nhận được một dự đoán. Ví dụ, nó cho tôi biết loại đối tượng trong ảnh là gì.

Không có khái niệm về thời gian. Tôi chuyển vào một hình ảnh khác, tôi nhận được một dự đoán khác.

Trình phân loại hình ảnh chỉ là một chức năng. Tôi cung cấp cho nó một đầu vào và nó tạo ra một đầu ra.

Vì vậy, tôi có ý nghĩa gì khi nói đến tĩnh và ý tôi là gì khi nói theo thời gian?

Bạn có thể nghĩ ngay đến mạng nơ-ron tái phát, là mạng nơ-ron có thể xử lý

trình tự. Đầu vào thay đổi theo thời gian. Tuy nhiên, đây không phải là lúc tôi đang nghĩ đến.

Nếu tôi chuyển một số giá cổ phiếu trong một khoảng thời gian nhất định và mô hình của tôi dự đoán liệu giá đó có

cổ phiếu sẽ tăng hoặc giảm vào ngày mai, đó vẫn là một hàm tĩnh.

Đây là ý tôi muốn nói về thời gian. Hãy tưởng tượng bạn đang xây dựng một mô phỏng xe tự lái.

Tại mỗi thời điểm, mạng lưới thần kinh của bạn có thể chụp ảnh nhanh màn hình và quyết định việc cần làm tiếp theo.

Nên đánh lái bên trái, nên đánh lái bên phải, tăng tốc hay phanh gấp?

Vì vậy, đây là sự khác biệt giữa học tập có giám sát và học tập tăng cường.

Học tập có giám sát chỉ là một chức năng. Bạn có thể gọi hàm này nhiều lần, nhưng nó vẫn chỉ là một

chức năng. Bạn truyền vào một hình ảnh và nó tạo ra một kết quả. Học tăng cường giống như một vòng lặp.

Nó tồn tại để đạt được mục tiêu nào đó. Ví dụ: đưa bạn đến đích mong muốn.

Bên trong vòng lặp, vâng, nó vẫn nhận một hình ảnh và tạo ra kết quả chỉ định cách thực hiện

điều khiển chiếc xe. Nhưng quan trọng là chương trình học tăng cường này có khái niệm về thời gian.

Nó không nghĩ đến hình ảnh này là gì, làm cách nào để chuyển hình ảnh này thành dự đoán đầu ra?

Thay vào đó, nó có khả năng lập kế hoạch cho tương lai.

Mặc dù tại thời điểm này, chiếc xe có thể chỉ nhìn thấy nó đang ở đâu trên đường,

nó biết rằng có một số chuỗi hành động mà nó phải thực hiện trong tương lai sẽ dẫn nó tới mục tiêu

mục tiêu. Được rồi, đó là điểm khác biệt chính giữa học tập có giám sát và học tập củng cố

học tập. Với việc học có giám sát, chúng ta không có khái niệm về mục tiêu, tương lai hay kế hoạch.

Chúng tôi chỉ lấy đầu vào và tạo ra đầu ra. Đó là một chức năng tĩnh. Với việc học tăng cường,

chúng ta có một kế hoạch và kế hoạch đó có thể được thực hiện trong tương lai để đạt được một số mục tiêu đã xác định trước.

Đây là một cách khác để suy nghĩ về việc học tăng cường. Hãy suy nghĩ về dữ liệu.

Với phương pháp học có giám sát, một lần nữa, hãy sử dụng phân loại hình ảnh làm ví dụ.

Chúng ta phải có nhãn cho mọi đầu vào trong tập huấn luyện của mình.

Vì vậy, nếu chúng ta có hình ảnh của một con chó, chúng ta phải có một mục khác chỉ rõ lớp chó.

Nếu chúng ta có hình ảnh của một con mèo, chúng ta phải có một mục khác xác định lớp mèo.

Nói cách khác, với mọi x, chúng ta phải có y.

Điều quan trọng cần nhớ là bộ dữ liệu nhãn phải do con người tạo ra.

Đôi khi học sinh có một ý tưởng thực sự buồn cười là chúng ta nên tự động hóa việc tạo ra

tập dữ liệu nhãn. Các bạn, nếu chúng ta đã có máy tính có thể dán nhãn dữ liệu một cách hoàn hảo,

thì điều đó có nghĩa là chúng ta đã giải quyết được vấn đề học máy. Máy tính có thể dán nhãn hoàn hảo

dữ liệu thực sự là những gì chúng tôi đang cố gắng xây dựng. Nếu những máy tính như vậy đã tồn tại thì chúng ta sẽ không

cần xây dựng chúng. Được rồi, hy vọng bạn tin rằng dữ liệu nhãn mác đến từ con người

và không phải một chiếc máy tính siêu thông minh nào đó.

Tại sao điều này lại quan trọng? Chà, hãy nghĩ lại về chiếc xe tự lái của chúng ta.

Chụp ảnh con đường này. Nếu chúng ta sử dụng phương pháp học có giám sát cho điểm dữ liệu này,

chúng ta sẽ cần phải cho nó một mục tiêu. Nhưng mục tiêu là gì? Tôi nên lái bên trái, tôi nên lái bên phải,

Tôi có nên tăng tốc, có nên ngắt quãng không? Trên thực tế, bạn có thể không thể đặt mục tiêu cho hình ảnh này.

Và thậm chí nếu có thể, làm sao bạn có thể dán nhãn cho từng khung hình mà chiếc xe sẽ gặp phải

dọc theo hành trình của nó? Hãy tưởng tượng nếu bạn có một chiếc máy ảnh tiêu chuẩn có thể chụp ảnh ở tốc độ 30 khung hình/giây,

và bạn có một giờ lái xe làm tập dữ liệu của mình. Một giờ là 3600 giây, nghĩa là bạn sẽ có

để gắn nhãn cho 108.000 hình ảnh chỉ từ một chuyến đi. Thay vào đó, học tăng cường học bằng cách sử dụng các mục tiêu thay vì

hơn các mục tiêu. Ví dụ: giả sử bạn muốn dạy một thuật toán học tăng cường để giải quyết

một mê cung. Trong kịch bản này, mục tiêu sẽ là tìm lối ra mê cung. Bạn không cần phải nói với thuật toán

điều đúng đắn cần làm là cho từng vị trí trong mê cung, vì đó sẽ là quá trình học có giám sát.

Thay vào đó, điều duy nhất mà thuật toán học tăng cường cần biết là mục tiêu là gì?

Từ đó, có thể tìm ra những việc cần làm ở từng vị trí của mê cung bằng cách học tăng cường.

Đó là sức mạnh của mô hình mới này.