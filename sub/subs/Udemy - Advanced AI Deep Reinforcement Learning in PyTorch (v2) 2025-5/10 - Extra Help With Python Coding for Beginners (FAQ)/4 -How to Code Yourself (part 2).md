# 4 -How to Code Yourself (phần 2) đã dịch

---

Đây là những gì được biết đến trong công nghệ phần mềm là phát triển dựa trên thử nghiệm hoặc TDD.

Trong quá trình phát triển dựa trên thử nghiệm, chúng tôi bắt đầu bằng cách viết các bài kiểm tra.

Bởi vì số một, mã của bạn phải luôn có các bài kiểm tra.

Và thứ hai, việc viết bài kiểm tra trước tiên buộc bạn phải suy nghĩ về cách bạn mong đợi API của mình

để làm việc và nó cho phép bạn đưa ra các quyết định thiết kế hợp lý mà không bị phân tâm bởi

chi tiết thực hiện.

Vì vậy, bạn thấy điều này áp dụng như thế nào cho mọi thuật toán học máy, không chỉ hồi quy tuyến tính.

Trong rất nhiều video viết mã cũ, rất tiếc là tôi đã quyết định chỉ viết mã trực tiếp.

Điều này giúp ích cho một số người nhưng không lý tưởng cho những người khác.

Ngoài ra, các video mã hóa sẽ xuất hiện mà không có cảnh báo.

Nói chung, các bài giảng xuất hiện theo cùng một khuôn mẫu.

Đầu tiên chúng tôi làm lý thuyết và sau đó chúng tôi thực hiện đoạn mã tương ứng.

Nó gần như luôn hoạt động theo cách này.

Vì vậy, sau bài giảng lý thuyết, bạn có thể khá chắc chắn rằng chúng ta sẽ áp dụng lý thuyết đó

sớm bằng mã, trừ khi nó đơn giản đến mức có thể coi là một bài tập.

Bây giờ để tránh đối xử với mọi người như trẻ mẫu giáo nên tôi không có video kể

bạn rằng đã đến lúc viết mã.

Tất cả các bạn đều là những người trưởng thành chủ động và độc lập nên khi học lý thuyết, bạn đã

biết rằng đã đến lúc bạn phải tự mình đưa nó vào mã.

Đôi khi bạn có thể gặp khó khăn và không biết mã viết là gì hoặc dữ liệu gì

thiết lập là.

Trong trường hợp đó, bạn có thể xem bài giảng về mã hóa tiếp theo, nhưng đừng xem hết

thông qua.

Hãy xem vừa đủ để bạn biết ý tưởng chung là gì và chúng tôi đang cố gắng thực hiện điều gì

hoàn thành và sau đó cố gắng tự mình hoàn thành phần còn lại.

Bây giờ, giả sử bạn đã xem vừa đủ để biết chúng tôi đang cố gắng làm gì.

Bạn biết lý thuyết nhưng vẫn không thể hoàn thành đoạn mã.

Tại thời điểm này, bạn có thể muốn xem lại lý thuyết bài giảng để chắc chắn rằng bạn thực sự hiểu

từng phần.

Nếu không, bạn có thể muốn thử tìm hiểu rõ hơn trên diễn đàn thảo luận.

Nếu không, bạn cũng có thể muốn xem xét các tài nguyên bên ngoài.

Đôi khi bạn có thể thiếu một số nền tảng khoa học máy tính quan trọng mà tôi cho rằng

mọi người đều đã biết rồi.

Điều đó hoàn toàn bình thường vì mỗi người đều có một nền tảng khác nhau.

Bạn nên tự nghiên cứu và điều này cũng hoàn toàn bình thường.

Đó không phải là một điều xấu, đó là một điều tốt.

Hỏi một sinh viên đại học xem đây có phải là việc họ làm không và họ sẽ nói với bạn rằng họ làm như vậy

nó mọi lúc.

Điều này xây dựng mức độ dẻo dai về tinh thần và khả năng chủ động, điều này rất quan trọng nếu bạn

muốn học thứ này.

Có rất nhiều điều để học và bản thân tôi vẫn đang học những điều mới mỗi ngày.

Vì vậy, giả sử bạn đã xem lại bài giảng lý thuyết.

Bạn đã xem một số tài liệu bên ngoài về lý thuyết mà vẫn chưa hiểu

bạn sẽ đặt nó vào mã như thế nào.

Tại thời điểm này, có một số bài tập tuyệt vời mà bạn có thể thực hiện.

Xem bài giảng về mã hóa hoặc xem mã đầy đủ trên GitHub.

Hãy xem qua nó và đảm bảo rằng bạn hiểu từng dòng.

Bước tiếp theo là không cần nhìn lại mã, hãy thử tự mình triển khai.

Bản thân điều này đã là một công cụ học tập tuyệt vời.

Nhiều thuật toán tôi đã học, lần đầu tiên tôi không hiểu chúng.

Tôi đã học được chúng bằng cách xem cách thực hiện của người khác và mổ xẻ nó.

Tôi nhìn vào từng phần và tự hỏi mình đã làm đúng phần nào và phần nào

có phải tôi đã sai không?

Điều này giúp bạn hiểu được những sai lầm bạn đang mắc phải trước đây.

Điều thú vị về việc triển khai là nó cũng hoạt động ngược lại.

Chúng ta đi từ lý thuyết đến code nhưng nghĩ theo hướng ngược lại, code thực sự có ích

chúng tôi cũng hiểu lý thuyết tốt hơn.

Tôi luôn nói rằng nếu bạn không thể triển khai mã thì bạn không hiểu lý thuyết.

Vì vậy, nếu bạn có thể học được 50% lý thuyết, hãy thử triển khai mã.

Hãy xem xét cách triển khai hiện có và cuối cùng làm cho nó hoạt động.

Khi đó bạn có thể yên tâm rằng giờ đây bạn đã biết hơn 50% lý thuyết.

Việc mã hóa tích cực giúp bạn hiểu nhiều lý thuyết hơn so với khi bạn mới học

lý thuyết của chính nó.

Vì vậy việc thực hiện giúp bạn hiểu được lý thuyết nhưng nó cũng giúp bạn hiểu được

trực giác là tốt.

Trực giác là một điều khó khăn.

Trên thực tế, tôi sẽ đi xa hơn khi nói rằng đó là một cái bẫy.

Trong nhiều hoặc thậm chí hầu hết các trường hợp, trực giác được xây dựng dựa trên kinh nghiệm.

Điều đó có nghĩa là rút ra lý thuyết từ những nguyên lý đầu tiên hay nói cách khác là rút ra lý thuyết

từ những sự thật bạn đã biết là đúng và từ việc thực hiện.

Trực giác thường muốn nghe trực giác từ những người có nhiều kinh nghiệm nhưng vấn đề

là trực giác này được xây dựng dựa trên nhận thức muộn màng.

Trực giác thường là điều đầu tiên và cũng là điều cuối cùng bạn muốn tập trung vào.

Bạn muốn có một chút trực giác ngay từ đầu để có ý tưởng tổng quát

về những gì bạn muốn đạt được.

Sau khi học lý thuyết và thực hiện, bạn có thể suy ngẫm chi tiết và tóm tắt

chúng ở mức độ cao.

Đây là trực giác thực sự được xây dựng dựa trên nhận thức sâu sắc và kinh nghiệm.

Sai lầm lớn nhất mà người mới bắt đầu mắc phải là họ đọc trực giác do người khác viết.

người thực sự có kinh nghiệm trong khi bản thân họ lại không có.

Từ góc nhìn của người ngoài, thật khó để nhận ra sự khác biệt.

Tại sao vậy?

Chà, nếu người mới bắt đầu có thể nảy ra những ý tưởng cấp cao giống như chuyên gia thì điều đó sẽ

Nghe có vẻ như họ cũng là chuyên gia trong khi thực tế không phải vậy.

Thật không may, có quá nhiều khóa học thực hiện điều này.

Họ muốn bạn cảm thấy hài lòng khi học được điều gì đó và họ muốn bạn không phải làm vậy.

làm điều gì đó quá khó khăn.

Và bởi vì bạn có thể lặp lại những trực giác cấp cao tương tự nên thực sự có vẻ như bạn đang

là một chuyên gia nên đây là lý do tại sao tôi gọi nó là một cái bẫy.

Biết trực giác không chỉ khiến bạn cảm thấy như bạn biết điều gì đó.

Nó cũng khiến bạn thực sự tự tin về sự thật này.

Và sau đó vì cái tôi của bạn muốn duy trì sự tự tin này nên bạn sẽ bắt đầu phát điên

những câu như lý thuyết và cách thực hiện không quan trọng vì bạn đã hiểu rồi

trực giác.

Nhưng như bạn biết điều này là hoàn toàn ngược lại.

Hãy tóm tắt bài giảng này vì có rất nhiều thông tin cần tiếp thu.

Hãy nhớ rằng bài giảng này nói về cách thức và lý do tại sao bạn nên tự mình viết mã.

Đầu tiên chúng tôi nói về lý do tại sao.

Điều này là do nó đảm bảo bạn đang suy nghĩ về các chi tiết và điền vào chỗ trống

sử dụng kỹ năng nhận dạng mẫu của riêng bạn.

Nó đảm bảo rằng bạn không chỉ cho rằng mình biết chuyện gì đang xảy ra mà còn thực sự biết chuyện gì đang xảy ra.

đang diễn ra.

Có một sự khác biệt lớn, đặc biệt nếu bạn là kiểu người thích thừa nhận bạn

biết mọi thứ.

Tiếp theo chúng tôi nói về cách làm.

Chúng ta đã nói về việc tất cả dữ liệu đều giống nhau như thế nào và việc đó là lĩnh vực hay ngành nào thực sự không quan trọng

tất cả dữ liệu của bạn đều được áp dụng từ cùng một thuật toán.

Tiếp theo, chúng tôi xem xét các giao diện của các thuật toán cũng giống nhau một cách thuận tiện.

Vì vậy, chúng tôi có một loại kịch bản kết hợp và kết hợp trong đó chúng tôi có thể nhập bất kỳ loại dữ liệu nào vào

bất kỳ loại mô hình.

Ví dụ: bạn có thể sử dụng hồi quy tuyến tính với dữ liệu tài chính hoặc bạn có thể sử dụng mạng nơ-ron

về dữ liệu sinh thái.

Tất cả dữ liệu đều giống nhau và tất cả các model đều có cùng giao diện.

Tiếp theo, chúng tôi đã nói về một chiến lược để thực sự áp dụng điều này.

Có thể bạn đã thấy rằng chúng ta luôn xen kẽ giữa lý thuyết và mã.

Đầu tiên chúng ta thảo luận về lý thuyết và sau đó chúng ta triển khai nó bằng mã.

Đôi khi bạn có thể phải quay lại và xem lại lý thuyết hoặc đôi khi bạn có thể phải

tra cứu mọi thứ trên internet.

Điều đó hoàn toàn bình thường.

Đây gần như là một ngày trong cuộc đời của một sinh viên đại học.

Chúng tôi đang cố gắng xây dựng cùng một mức độ dẻo dai về tinh thần và khả năng chủ động tham gia khóa học này.

Vì vậy, chiến lược sẽ dừng lại sau khi bạn học lý thuyết và cố gắng tự viết mã.

Đôi khi bạn cần thêm một chút chi tiết nên bạn có thể muốn xem một chút về

các bài giảng về mã hóa để xem điều gì đang diễn ra và sau đó thử tự mình thực hiện phần còn lại.

Nếu bạn không thể tự mình lấy được thì có thể thử xem toàn bộ hoặc xem

kết quả mong đợi và sau đó cố gắng thực hiện nó từ bộ nhớ.

Bản thân điều này đã là một công cụ học tập tuyệt vời vì nó cho phép bạn tự hỏi mình đã nhận được gì

đúng và mình đã sai ở điểm nào để bạn hiểu được lỗi mình mắc phải.

Cuối cùng, điều quan trọng là phải hiểu sự khác biệt giữa trực giác, lý thuyết và việc thực hiện.

và chúng củng cố lẫn nhau như thế nào.

Điều quan trọng là không rơi vào cái bẫy chỉ hiểu trực giác do ai đó viết ra

khác và sau đó cho rằng điều này tương đương với việc thực sự hiểu mọi thứ.

Trong nhiều trường hợp, không phải là chờ đợi ai đó nói với bạn những cụm từ hay để đánh lừa bạn.

bạn nghĩ rằng bạn hiểu trực giác nhưng đúng hơn là bạn nên tìm kiếm trực giác bằng cách làm việc

thông qua lý thuyết và thực hành.

Và cuối cùng, đừng quên khi đến lúc viết mã, bạn phải viết mã.