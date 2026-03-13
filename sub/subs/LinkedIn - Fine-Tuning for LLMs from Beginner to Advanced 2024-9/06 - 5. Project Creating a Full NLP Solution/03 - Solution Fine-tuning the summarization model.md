# 03 - Giải pháp Tinh chỉnh mô hình tóm tắt

---

- [Giảng viên] Này, thử thách đó thế nào?

Trong thử thách cuối cùng này, ý bạn là

thực hiện tinh chỉnh LoRA để áp dụng tóm tắt

trên tập dữ liệu CNN DailyMail.

Điều rất quan trọng là có thể tóm tắt,

không chỉ bởi vì có thể trong chatbot của bạn

bạn được yêu cầu làm điều đó,

nhưng thông thường khi bạn triển khai chatbot,

at the end of the conversation we want to create a summary

của toàn bộ cuộc trò chuyện.

Ví dụ như sau này, người đại diện không cần phải làm việc đó,

hoặc chúng ta có một tin nhắn hay để nói về chuyện vừa xảy ra.

Trong bối cảnh đó, chúng ta hãy đi đến nó.

Vì vậy, chúng tôi sẽ kết nối với GPU của mình như mọi khi.

Hoàn hảo.

Và chúng ta sẽ thực hiện cài đặt pip như trước đây,

bao gồm cả điểm Rouge.

Nó đây rồi.

Vì vậy, bây giờ chúng ta đã ở đó, chúng ta sẽ tải tập dữ liệu,

và đó sẽ là tập dữ liệu CNN DailyMail,

và chúng tôi sẽ đưa ra một ví dụ.

Hoàn hảo.

Như bạn có thể nhớ,

ví dụ là chúng ta có bài viết và bài viết dài.

Rồi đến một lúc nào đó chúng ta có những điểm nổi bật,

đâu là phần tóm tắt và đâu là nội dung chúng tôi sẽ sử dụng.

Và cuối cùng chúng ta có một chỉ mục.

Vì vậy, đối với trường hợp tiền xử lý này,

chúng ta sẽ sử dụng đế Flan T5,

và CC mục tiêu chỉ là điểm nổi bật,

và đối với các bài viết chúng ta chỉ cần thêm nhiệm vụ mục tiêu của chúng,

trong trường hợp này, tóm tắt: và bài viết thực sự.

Sau đó, nó giống như trước đây,

chúng tôi chuyển mã thông báo để lấy đầu vào,

để lấy nhãn từ mục tiêu,

và sau đó ID đầu vào của bộ giải mã là ID trên ID đầu vào.

Hoàn hảo.

Chúng ta sẽ chỉ lấy 10.000 ví dụ,

bởi vì điều này có thể mất rất nhiều thời gian nếu không.

Mỗi bài viết đều dài.

Vậy hãy tưởng tượng nếu người kia mất 30 phút,

việc này có thể dễ dàng mất hàng giờ.

Và chúng ta sẽ chỉ lấy 500 ví dụ

cho tập dữ liệu thử nghiệm.

Sau đó, chúng ta sẽ chuyển đổi sang tập dữ liệu TensorFlow

as we have always done.

Và điều duy nhất tôi sẽ thay đổi ở đây,

Tôi sẽ đặt điều này là đúng để nó xáo trộn

và cuối cùng chúng ta có thể nhận được các đợt ngẫu nhiên

cho điểm số của Rouge.

Phải nói rằng, việc này sẽ không mất nhiều thời gian,

bởi vì chúng tôi đang chọn phần nhỏ

của tập dữ liệu thực tế.

Bộ dữ liệu CNN DailyMail đầy đủ, nếu bạn tò mò,

có hơn 300.000 bài viết, rất nhiều.

Và chúng ta bắt đầu.

Bây giờ chúng ta sẽ tải mô hình của mình.

Và một lần nữa, để làm cho việc này diễn ra siêu nhanh,

chúng ta sẽ sử dụng Flan T5 nhỏ.

Tuy nhiên, nếu bạn muốn sử dụng một cái lớn hơn, đừng lo lắng.

Bạn chỉ cần sử dụng, ví dụ: Flan T5 Large hoặc Extra Large,

và bạn sẽ có một mô hình tóm tắt rất tốt.

Thế đấy.

Bây giờ chúng ta sẽ triển khai lớp LoRA của mình,

giống như trước đây, giống hệt như trước đây.

Nếu chúng ta kiểm tra tóm tắt mô hình,

chúng ta có thể thấy nó có 76 triệu tham số,

và chúng tôi sẽ sử dụng LoRA trên bộ giải mã

và trên lớp dày đặc cuối cùng.

Và sau đó chúng ta có thể thấy rằng chúng ta sẽ chỉ tập luyện

16 triệu thông số.

Được rồi, nó nằm trong khoảng từ 20 đến 25% thông số.

Một lần nữa, chúng ta có thể đi sâu bao nhiêu tùy thích, như bạn biết đấy.

Sau đó, chúng ta cần biên dịch và chúng ta cần điều chỉnh,

giống như những gì chúng ta đã và đang làm bấy lâu nay.

Việc này sẽ không mất quá 10 phút

vì mô hình nhỏ và chúng tôi sử dụng tập dữ liệu nhỏ,

nhưng nếu bạn không có GPU, thời gian có thể lên tới 30 phút.

Được rồi, trong trường hợp đó, đã đến lúc đi dạo

và lấy một chút ánh sáng mặt trời.

Nếu không thì hãy đợi cho đến khi chuyện này kết thúc.

Hoàn hảo.

Chúng ta có thể thấy rằng mô hình đã được đào tạo,

it took almost six minutes in my machine.

Đối với bạn có thể mất 10, 15, và điều đó không sao cả.

Một lần nữa, chúng ta có thể xác minh tổn thất đã giảm,

vậy là tốt, mỗi thời đại.

Vì vậy bây giờ chúng ta lưu mô hình như trước và nó hoạt động.

Và bây giờ chúng ta sẽ đánh giá.

Và bây giờ, để đánh giá, chỉ cần tạo ra sự khác biệt,

chúng ta sẽ lấy một lô từ tập dữ liệu thử nghiệm

và những gì chúng ta sẽ nhận được là điểm BLEU trung bình.

Để làm được điều đó, chúng ta sẽ tính điểm BLEU

cho mỗi đầu vào của lô,

và sau đó chúng tôi sẽ trả về điểm BLEU trung bình.

Vì vậy, chúng tôi sẽ chạy nó.

Sẽ không mất nhiều hơn một hoặc hai phút,

và chúng ta sẽ nhận được điểm BLEU trung bình.

Hoàn hảo, mất khoảng 39 giây,

và trong trường hợp của chúng tôi, bạn có thể thấy rằng điểm BLEU của chúng tôi là 0,03,

điều đó thực sự tốt

Hoàn hảo.

Nếu bạn muốn những giá trị tốt hơn,

bạn biết bạn có thể sử dụng mô hình lớn hơn, nhiều dữ liệu hơn,

hoặc thậm chí ở đây, sẽ lâu hơn một chút,

nhưng bạn có thể đặt độ dài tối đa của câu trả lời được tạo,

điều đó có nghĩa là tóm tắt, có thể là 512 hoặc 1.024,

để mô hình có nhiều chỗ hơn để tạo bản tóm tắt.

Hãy nhớ rằng sau cùng, đó là cách BLEU hoạt động.

Nhìn chung, chúng tôi có một mô hình tóm tắt

để áp dụng cho chatbot của chúng tôi.