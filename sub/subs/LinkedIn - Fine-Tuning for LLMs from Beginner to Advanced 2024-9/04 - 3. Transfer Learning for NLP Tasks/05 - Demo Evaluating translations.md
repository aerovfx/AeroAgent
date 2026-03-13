# 05 - Demo Đánh giá bản dịch

---

- [Người hướng dẫn] Trong bản demo này, chúng ta sẽ mở rộng về

những gì chúng tôi đã làm trong bản demo trước

nơi chúng tôi đã chuyển giao việc học trên FlanT5

dịch từ tiếng Anh

sang tiếng Tây Ban Nha trên tập dữ liệu Opus 100.

Để làm được điều đó, chúng ta sẽ chuyển sang giai đoạn đánh giá

với điểm số ROUGE và BLEU.

Vì phần đầu của cuốn sổ cũng giống như vậy,

Tôi đã kết nối với GPU và chạy trước tất cả các bước.

Điều đó có nghĩa là cài đặt pip.

Sau đó tải FlanT5, tải tập dữ liệu,

thực hiện quá trình xử lý tương tự như chúng tôi đã làm

trước và tạo tập dữ liệu TensorFlow.

Cuối cùng, hãy chú ý lại, chúng ta đang thiết lập ba lớp đầu tiên

của mô hình là không thể đào tạo được,

thực hiện chuyển giao học tập một cách hiệu quả.

Với điều đó, hãy làm cho mô hình phù hợp,

vì vậy việc này có thể mất một lúc.

Trong khi đó, đây là cơ hội hoàn hảo

để lấy một ít nước và đi dạo.

Được rồi, hoàn hảo.

Bây giờ chúng ta có thể thấy rằng nó đã kết thúc,

GPU này mất 10 phút vào thời điểm này trong ngày,

hãy nhớ cho bạn nó có thể mất nhiều thời gian hơn.

Điều này phụ thuộc nhiều vào GPU bạn nhận được,

thời gian trong ngày

và chính xác bạn đang chạy trên máy nào.

Điều quan trọng là mô hình của chúng tôi đã học được

bởi vì một lần nữa, chúng ta có thể thấy điều đó ở mỗi thời điểm,

tổn thất giảm đi, vì vậy hãy tìm hiểu cách

để đánh giá bản dịch của chúng tôi.

Để làm được điều đó, chúng ta cần

để sử dụng gói điểm ROUGE

để khởi tạo cầu thủ ghi bàn ROUGE,

sẽ tính điểm ROUGE

và chúng ta cần lấy hàm BLEU của câu từ NLTK.

Đầu tiên chúng ta tạo chức năng dịch, giống như trước.

Cái này bạn đã quá quen rồi.

Chúng tôi thực hiện mô hình tạo trên ID đầu vào,

đã được token hóa và mã hóa,

và đầu ra được giải mã.

Điều này cũng giống như trước đây.

Để tính điểm, chúng ta luôn đi

để nói về một văn bản tham khảo và một giả thuyết.

Văn bản tham khảo về cơ bản là văn bản thực sự

mà chúng tôi đang tạo ra.

Trong trường hợp này, chúng tôi sẽ thực hiện dịch thuật,

nhưng một lần nữa, hãy nhớ đây là điều chung chung.

Đây có thể là một câu trả lời.

Nếu chúng ta đang trả lời câu hỏi thì đây có thể là một bản tóm tắt.

Nếu chúng ta đang thực hiện tóm tắt, v.v.

Giả thuyết sẽ là những gì chúng tôi tạo ra.

Đầu tiên, điều chúng ta cần làm

là để khởi tạo cầu thủ ghi bàn ROUGE

cho biết chúng ta muốn tính điểm nào.

Trong trường hợp này, chúng ta sẽ tính ROUGE một

của unigram, hai của bigram,

và ROUGE L, là mức trung bình của tất cả

về điểm số ROUGE, được thấy trong các slide.

Đối với điểm BLEU, chúng ta sẽ sử dụng phương pháp

cho chức năng làm mịn.

Điều này sẽ đảm bảo rằng tính toán của chúng tôi cũng hoạt động

cho những câu rất ngắn.

Chúng tôi tính toán điểm rouge chỉ

trong rouge.score, cực kỳ đơn giản.

Và sau đó đối với điểm BLEU, chúng tôi sử dụng phương pháp BLEU câu.

Và điều quan trọng là BLEU

cần từ tokenized, điều đó có nghĩa là

rằng nó được chia thành các từ thay vì các câu đầy đủ,

trước tiên chúng ta cần mã hóa chúng và sau đó chuyển chúng dưới dạng mã thông báo.

Vậy là chúng ta đã có chức năng của mình, chúng ta sẽ bắt đầu

để có được một lô ngẫu nhiên từ tập dữ liệu thử nghiệm.

Bạn có thể làm điều này trên tất cả các lô và tính trung bình.

Chúng tôi sẽ không làm điều đó chỉ vì lý do thời gian.

Thay đổi duy nhất là thay vì thực hiện dòng này, tiếp theo

của mỗi tập dữ liệu thử nghiệm sẽ dành cho lô trong tập dữ liệu thử nghiệm.

Và bạn làm việc theo từng đợt.

Chúng tôi thực hiện dịch thuật,

văn bản tham chiếu mà chúng ta biết về cơ bản là nhãn,

sau đó chúng tôi tính điểm và in ra.

Vì vậy, hãy chạy cái này,

và việc này có thể mất khoảng 2 đến 3 phút,

vì vậy đừng lo lắng nếu phải mất một chút thời gian.

Và chúng tôi đã có được nó.

Ví dụ: văn bản tham chiếu đầu tiên

đó là bản dịch là "Estaba khập khiễng,"

nghĩa là "Tôi đang dọn dẹp."

Và như bạn có thể thấy, đây là một bản dịch hoàn hảo.

Một lần nữa, đây là một tập dữ liệu ngẫu nhiên.

nếu bạn muốn làm điều đó trên tập dữ liệu thử nghiệm đầy đủ,

điều đó thật hoàn hảo.

Và nhân tiện, khi chúng tôi hiển thị điểm số,

chúng tôi đang hiển thị nó trên toàn bộ lô.

Điều đó có nghĩa là 64 dòng.

Và chúng ta có thể thấy rằng ROUGE 1 có độ chính xác là 1,

ROUGE 2 cũng như ROUGE L,

bởi vì chúng tôi đã có khả năng thu hồi hoàn hảo.

Điều đó có nghĩa là mỗi từ

trong bản dịch đã thực sự có mặt trong tài liệu tham khảo,

và điểm BLEU là 0,4, cực kỳ cao,

điều đó có nghĩa là ngược lại, trong tất cả

của các từ trong văn bản tham khảo,

hầu hết đều có trong bản dịch.

Vậy là chúng ta đã có một mô hình dịch thuật rất tốt. Vì vậy, đây là nó.

Chúng tôi đã thực hiện thành công việc học chuyển giao

và đánh giá bản dịch của chúng tôi

với ROUGE và BLEU.

Nhưng hãy nhớ rằng, dịch thuật chỉ là cái cớ để nói với bạn

làm thế nào để đánh giá bất kỳ trình tự nào để thực hiện nhiệm vụ theo trình tự.