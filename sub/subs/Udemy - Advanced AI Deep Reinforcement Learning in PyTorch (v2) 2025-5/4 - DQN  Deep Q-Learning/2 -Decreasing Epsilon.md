# 2 -Giảm dịch Epsilon

---

Được rồi, trong video này chúng ta sẽ xem xét phần đầu tiên trong số một vài sửa đổi về Q learning

mà chúng ta sắp làm để tiến tới học Q sâu.

Được rồi, và sự sửa đổi đó sẽ làm giảm epsilon.

Vì vậy, epsilon giảm hoặc phân rã.

Vì vậy, giảm dần, giảm epsilon.

Được rồi, hãy bắt đầu với trực giác đằng sau lý do tại sao chúng ta muốn làm điều này.

Vì vậy, trong quá trình học Q thông thường, chúng ta luôn sử dụng cùng một loại epsilon, phải không?

Vậy là bạn đã thấy điều đó.

Vì vậy, trong quá trình học Q thông thường, chúng tôi luôn sử dụng cùng một epsilon.

Vì vậy, ví dụ, epsilon bằng 0,1.

Được rồi, vậy vấn đề ở đây là gì?

Điều này có nghĩa là lúc đầu bạn đang thực hiện một loạt hành động mà bạn cho là tối ưu,

nhưng chúng tôi khởi tạo Q một cách ngẫu nhiên.

Vì vậy, bạn không thực sự thực hiện các hành động tối ưu.

Bạn chỉ đang thực hiện những hành động ngẫu nhiên một cách hiệu quả vì bạn vẫn đang cố gắng tìm hiểu sự thật

các giá trị Q.

Được rồi.

Được rồi, vậy chúng ta hãy viết nó ra.

Vì vậy lúc đầu bạn đang thực hiện các hành động.

Bạn cho là tối ưu nhưng về cơ bản thì chúng dựa trên những gì sai

Q.

Bạn thậm chí còn không biết Q.

Bạn đang cố gắng học Q vào thời điểm này.

Vì vậy, ví dụ, điều này có nghĩa là gì.

Vì vậy, nếu bạn đặt epsilon thành 0,1, điều này có nghĩa là chỉ khoảng 10% thời gian, bạn có thực sự

có cơ hội thực sự để học điều gì đó hữu ích để tìm hiểu thông tin hữu ích về Q.

Được rồi, vậy chúng ta xử lý vấn đề này như thế nào?

Vì vậy, một sửa đổi hữu ích mà chúng ta có thể thực hiện là giảm epsilon theo thời gian.

Được rồi, vậy là bạn bắt đầu với một giá trị lớn, chẳng hạn như một giá trị, vậy nên 100% thời gian bạn đang khám phá.

Và sau đó bạn giảm dần nó về 0 khi tác nhân tìm hiểu.

Vì vậy, lúc đầu, nó chỉ là thu thập thông tin.

Đây là những gì chúng tôi gọi là thăm dò.

Và cuối cùng, nó sử dụng thông tin đó để đưa ra quyết định tối ưu.

Và đó là những gì chúng ta gọi là bóc lột.

Được rồi, giải pháp là giảm epsilon theo thời gian.

Đây giống như chiếc xe cấp cứu thứ năm hiện nay.

Được rồi, ví dụ như vậy, hãy bắt đầu từ 1 và sau đó giảm xuống 0.

Được rồi, khi nó là một, chúng tôi đang thu thập thông tin, thu thập thông tin và chúng tôi gọi đây là khám phá.

Và khi chúng ta ở mức 0, chúng ta sẽ thực hiện những hành động tối ưu.

Vì vậy, chúng tôi đang đưa ra quyết định tối ưu.

Vì vậy quyết định tối ưu.

Chà, điều này giả định rằng đại diện của bạn đã học được vào thời điểm epsilon trở thành số 0.

Và điều này được gọi.

Và tất nhiên, những thứ đó.

Bạn chỉ cần kiểm tra nó.

Và sau đó bạn có thể thấy việc khám phá.

Và nếu bạn đã thực hiện các điều kiện tiên quyết, bạn biết rằng chúng tôi gọi đây là vấn đề nan giải về khám phá khai thác,

hoặc khám phá khai thác đánh đổi.

Và trên thực tế, nếu bạn tham gia khóa học củng cố tiên quyết, bạn đã có một nền tảng kiến thức tuyệt vời.

cơ hội để kiểm tra những gì tôi đang nói ở đây.

Vì vậy, ngay cả trước khi tìm hiểu về deep-key learning, bạn có thể đã kiểm tra khía cạnh này của deep-key learning.

Được rồi, và cụ thể những gì tôi đang đề cập đến là các phương pháp cướp.

Được rồi, cơ hội tốt để thử nghiệm là với bọn cướp.

Được rồi, vậy bạn thực sự có thể quay lại đoạn mã đó và triển khai một epsilon đang phân rã để xem nó hoạt động như thế nào theo cách riêng biệt.

Được rồi, và vì vậy tôi thích bài kiểm tra đó vì nó tách biệt vấn đề chọn hành động tốt nhất mà không cần phải xử lý các trạng thái hoặc chuyển đổi trạng thái.

Và vì vậy, đề phòng trường hợp bạn quên, về cơ bản thì có một tên cướp, hoặc vấn đề về tên cướp về cơ bản là, nếu bạn nói theo cách thực tế, thì bạn có rất nhiều máy đánh bạc.

Đúng vậy, hãy tin tưởng vào máy đánh bạc.

Vì vậy, bạn có một loạt máy đánh bạc và ý tưởng là tốc độ gió của các máy đánh bạc này là khác nhau.

Vì vậy, một trong số chúng có thể có tốc độ gió là 0,5, một trong số chúng có thể có tốc độ gió là 0,1, v.v.

Nhưng bạn không biết điều này bởi vì sẽ không ai nói với bạn rằng bạn chỉ cần chơi máy đánh bạc cho đến khi bạn tìm ra máy nào là tốt nhất.

Được rồi, và vì vậy trong tình huống này, không có trạng thái, đúng vậy, bạn chỉ đang chọn một hành động, phải, hành động một, hành động hai hoặc hành động ba, nhưng không có trạng thái, không có sự chuyển đổi trạng thái.

Vì vậy, nó giúp việc thử nghiệm dễ dàng hơn nhiều so với một MVP đầy đủ.

Và vì vậy tôi khuyên bạn nên thực hiện nếu bạn thực sự muốn hiểu việc giảm epsilon sẽ cải thiện cách hoạt động của thuật toán như thế nào.

Bạn sẽ thấy nó hội tụ nhanh hơn nhiều chỉ để kiểm tra nó và sau đó bạn sẽ có thể tự mình nhìn thấy nó.

Được rồi, và trong thực tế, có nhiều cách chúng ta có thể giảm epsilon, đúng vậy, trong thực tế,

nhiều cách để giảm epsilon.

Và vì vậy điều này không thực sự khoa học, đúng vậy, chúng ta không rút ra bất kỳ cách cụ thể nào để giảm epsilon từ những nguyên tắc đầu tiên.

Nó thực sự giống một heuristic hơn. Vì vậy, điều này có vẻ tốt, điều này có vẻ hiệu quả.

Vì vậy, chúng ta có thể làm điều gì đó như thế này, đúng vậy, chúng ta có thể thực hiện epsilon của bước thời gian T. Đây là alpha trên T, đúng không, hoặc chúng ta có thể phân rã theo cấp số nhân.

Vì vậy, chúng ta có thể làm epsilon của T bằng E mũ âm alpha T.

Và thế là T ngày càng lớn hơn. Điều này tiến gần đến số không.

Được rồi, nhưng đối với DQN, điều chúng tôi làm là giảm nó một cách tuyến tính.

Và sau đó, chúng tôi đặt một số giá trị tối thiểu, giá trị này vẫn ở giá trị tối thiểu đó.

Được rồi, đây là epsilon tối thiểu và đây là epsilon tối đa của chúng tôi.

Vì vậy, về cơ bản, cách nó hoạt động đối với chúng tôi là chúng tôi bắt đầu ở mức tối đa epsilon.

Giảm tuyến tính xuống epsilon min và sau đó chúng ta để nó ở mức epsilon min.

Và chúng ta cũng phải xác định có bao nhiêu bước.

Vì vậy, chúng ta sẽ gọi nó là T epsilon hoặc cái gì đó cần thiết để chuyển từ epsilon max sang epsilon min.

Được rồi, vậy hãy nghĩ xem bạn sẽ triển khai điều này như thế nào trong mã.

Và đây cũng là một bài tập hay khi chúng ta xem qua các bài giảng này, đừng chỉ sao chép trực tiếp mã học Q sâu mà hãy cố gắng xử lý mã học Q và tự mình triển khai từng tính năng này.

Vì vậy, tôi nghĩ đó sẽ là một bài tập hay để thực hiện trong khóa học này.

Và rõ ràng giải pháp sẽ là thuật toán DQN mà tôi sẽ chỉ cho bạn sau.