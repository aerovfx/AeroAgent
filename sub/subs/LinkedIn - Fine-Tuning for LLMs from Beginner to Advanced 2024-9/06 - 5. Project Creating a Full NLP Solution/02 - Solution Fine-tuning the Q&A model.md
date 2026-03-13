# 02 - Giải pháp Tinh chỉnh mô hình hỏi đáp

---

- [Giảng viên] Này, thử thách thứ hai thế nào rồi?

Trong thử thách thứ hai này,

Chúng tôi được yêu cầu tạo ra một câu hỏi trả lời,

mô hình tinh chỉnh sử dụng Flan-T5.

Điều này rất quan trọng

bởi vì rất nhiều thứ trong chatbot thực chất là những câu hỏi,

vì vậy đây là một phần rất quan trọng trong chatbot của chúng tôi.

Tuy nhiên, nếu bạn đang xây dựng một ứng dụng khác

ghi lại cách thực hiện hoặc hướng dẫn,

bạn vẫn sẽ cần phải thực hiện loại nhiệm vụ này.

Vì bạn là người mới làm quen với tập dữ liệu,

bộ dữ liệu SQuaD,

và bạn chưa quen với việc trả lời câu hỏi.

Tôi nghĩ rằng cách tiếp cận tốt nhất

là vẫn sử dụng phương pháp học chuyển tiếp.

Vì vậy chúng ta sẽ thực hiện LoRA trong thử thách tiếp theo

chỉ cần đi từng bước một.

Vì vậy, bắt đầu, hãy kết nối GPU,

tôi đây

và chúng tôi sẽ thực hiện cài đặt pip.

Hãy nhớ rằng chúng ta cũng phải cài đặt rouge-score

để xác nhận các câu trả lời.

Nó đây rồi.

Mọi thứ đã được cài đặt.

Như bạn đã biết, việc tiếp theo là thực hiện nhập khẩu

và vâng, bây giờ chúng ta sẽ sử dụng AutoModelForSeq2SeqLM

vì chúng tôi đã sử dụng tất cả khóa học

vì đây là Flan-T5.

Chúng ta đây rồi.

Và bây giờ chúng ta sẽ tải tập dữ liệu.

Tập dữ liệu SQuAD v2 này,

đó là một tập dữ liệu nguồn mở

có câu hỏi và câu trả lời

và nó rất, rất hữu ích.

Thế đấy.

Bây giờ chúng ta sẽ tải tokenizer

như chúng tôi vẫn luôn làm.

Thế là xong và chúng ta phải mã hóa dữ liệu của mình.

Vì vậy, thực sự tập dữ liệu SQuAD của nó khá lớn.

Vì vậy chúng ta sẽ thực hiện việc học chuyển giao

trên 25.000 ví dụ trên đoàn tàu

và 2.000 trên bộ xác thực.

Bạn muốn có kết quả tốt hơn, bạn biết phải làm gì,

chỉ cần sử dụng toàn bộ tập dữ liệu và chờ đợi nó.

Vì vậy, đây là lần đầu tiên chúng ta sẽ xử lý việc này.

Vì vậy tôi muốn bạn biết cách xử lý việc trả lời câu hỏi.

Hãy nhớ rằng trả lời câu hỏi,

thực ra tên đầy đủ của nó là,

trả lời câu hỏi theo ngữ cảnh.

Điều đó có nghĩa là chúng ta sẽ đưa ra một số bối cảnh

đến mô hình rồi đến câu hỏi,

và về cơ bản mô hình sẽ kiểm tra bối cảnh của nó

và dữ liệu huấn luyện của nó để trả lời nó.

Vì vậy, điều chúng ta cần làm là về đầu vào,

chúng ta cần cả câu hỏi và bối cảnh.

Vì vậy chúng ta sẽ sử dụng hàm zip từ Python,

điều đó sẽ thu hút hàng loạt câu hỏi

và hàng loạt bối cảnh

và lời nhắc mà chúng ta sắp tạo

sẽ là bối cảnh, sau đó là không gian,

sau đó là không gian đánh dấu nhiệm vụ và sau đó là câu hỏi.

Điều này rất quan trọng để mô hình hiểu được

rằng chúng tôi đang trả lời câu hỏi.

Được rồi? Rất, rất quan trọng.

Và về các câu trả lời, tập dữ liệu này có câu trả lời trống.

Vì vậy chúng ta phải kiểm tra,

nếu len của câu trả lời là tích cực, được thôi,

và nếu đúng như vậy thì chúng tôi sẽ đưa ra câu trả lời,

thực ra cái này nói, cái đó sẽ xóa nó,

chúng ta sẽ chỉ đặt phần tử đầu tiên,

nếu không, chúng ta sẽ phải đặt câu trả lời

như một chuỗi rỗng, được chứ?

Điều đó có nghĩa là người mẫu không biết.

Vậy chúng ta, bằng cách làm điều này, thủ thuật nhỏ này,

chúng tôi đang chèn câu trả lời Tôi không biết,

điều đó có nghĩa là người mẫu cũng sẽ biết

khi nó không biết,

nên nó không gây ảo giác.

Đây là một kỹ thuật rất phổ biến khi chúng tôi dạy các mô hình

tạo ra văn bản giống như các mô hình giải mã.

Đây cũng là một kỹ thuật mới dành cho bạn,

vì vậy đó là lý do tại sao tôi muốn bạn giải thích nó một cách đầy đủ.

Phần còn lại sẽ giống nhau.

Các đầu vào mô hình sẽ giống nhau.

Sau đó, các nhãn sẽ giống nhau

với mã thông báo mục tiêu.

Sau đó, từ nhãn, chúng tôi nhận được input_ids dưới dạng nhãn

và bộ giải mã_input_ids cũng chỉ là nhãn như trước.

Vì vậy, chúng tôi sẽ thực hiện ánh xạ và quá trình mã hóa sẽ diễn ra.

Như bạn có thể thấy, việc này sẽ diễn ra khá nhanh,

nhưng chúng tôi đã có những chi tiết nhỏ này ở dấu nhắc

điều đó mới đối với chúng tôi vì tập dữ liệu.

Đó là lý do tại sao tôi cũng giới thiệu bộ dữ liệu này với bạn

mang đến cho bạn thử thách này.

Làm cách nào để xử lý tập dữ liệu mới này?

Tôi không biết gì về nó.

Bây giờ đến việc chuyển đổi.

Việc chuyển đổi gần như giống nhau.

Hãy nhớ như mọi khi, chúng ta phải đặt bộ giải mã_input_ids

trong các cột vì đây là mô hình đoàn tàu,

nhưng tôi đã bổ sung thêm một chút để giúp ích cho việc đào tạo.

Tuy nhiên, đó là tùy chọn,

đó là bộ thu thập dữ liệu.

Có một lớp học (không rõ ràng)

được gọi là DataCollatorForSeq2Seq

Những gì nó làm là đảm bảo rằng đợt cuối cùng sẽ bị loại bỏ,

vì vậy tất cả các lô đều có cùng kích thước

và nó đảm bảo rằng việc mã hóa,

sẽ phù hợp nếu bất kỳ câu nào dài hơn dự kiến.

Điều này về cơ bản là ổn định việc đào tạo

và làm cho nó nhanh hơn.

Tuy nhiên, nếu bạn muốn đặt colator

và không hỏi gì như chúng ta vẫn làm, điều đó thật tuyệt vời,

đây là tùy chọn.

Tôi chỉ đang cho bạn xem một cái gì đó

điều đó tăng tốc độ đào tạo một chút.

Vì vậy, bây giờ hãy tạo hàng chục tập dữ liệu hàng.

Chúng ta đây rồi.

Chúng tôi tải mô hình

và lưu ý rằng tôi sẽ sử dụng flan-t5-base

chỉ vì mục đích không mất mãi mãi.

Tại sao tôi nói điều này?

Bối cảnh và các câu hỏi trong bộ dữ liệu SQuAD

có thể khá dài.

Điều này có nghĩa là lượng dữ liệu

mà chúng tôi phải xử lý trên mỗi thế hệ

sẽ mất nhiều thời gian,

điều đó có nghĩa là nếu chúng ta sử dụng flan-t5-large chẳng hạn,

điều đó thật hoàn hảo,

nhưng chúng ta đang nói về khoảng 30 phút mỗi kỷ nguyên

và vì chúng tôi chỉ làm việc đó vì mục đích giáo dục,

chúng tôi sẽ sử dụng flan-t5-base

điều này sẽ cho phép chúng tôi thực hiện các kỷ nguyên ngắn hơn.

Nhưng nếu bạn muốn xây dựng một chatbot có giá trị sản xuất,

chỉ cần đặt flan-t5-large hoặc cực lớn,

hãy chờ đợi và nó sẽ siêu ổn thôi.

Chúng ta đây rồi.

Chúng tôi có mô hình của chúng tôi.

Như bạn đã biết, ba lớp đầu tiên,

đó là phần nhúng, bộ mã hóa, bộ giải mã,

chúng tôi đặt chúng là không thể đào tạo được

và bây giờ chúng ta sẽ huấn luyện lớp dày đặc cuối cùng.

Chúng tôi đã sẵn sàng cho việc đào tạo.

Vì vậy bây giờ chúng tôi biên dịch mô hình.

Điều tương tự như trước đây.

Điều này luôn luôn giống nhau.

Và bây giờ chúng tôi đào tạo mô hình cho ba kỷ nguyên.

Hãy để tôi kéo cái này lên.

Và chúng ta bắt đầu.

Như bạn đã biết, việc này có thể mất một thời gian.

Tuyệt vời.

Chúng ta thấy rằng mô hình đã hoàn thành quá trình huấn luyện.

Trong trường hợp của tôi mất 35 phút,

đối với bạn, có thể mất nhiều thời gian hơn,

nhưng đó là điều được mong đợi.

Hãy nhớ rằng tập dữ liệu rất lớn.

Điều quan trọng là không chỉ mất mát

và việc mất xác nhận giảm dần theo từng thời kỳ,

mà còn giá trị tổn thất cũng rất, rất thấp,

có nghĩa là nó đã được đào tạo rất tốt.

Nếu chúng ta cần lưu mô hình như trước,

model.save_pretrain

và điều đó sẽ lưu mô hình như trước.

Vậy bây giờ chúng ta đi đây,

chúng tôi có mô hình, hoàn hảo.

Cuối cùng chúng ta sẽ đánh giá mô hình

với rouge_scorer.

Vì vậy, chúng tôi tạo ra một hàm trả lời sẽ thực hiện việc này,

điều tương tự như mọi khi,

tạo ra trong trường hợp này câu trả lời

cho câu hỏi và sau đó giải mã nó.

Và trong trường hợp của chúng ta, hãy nhớ rằng chúng ta sẽ thực hiện rouge_scorer.

Chúng ta sẽ lấy 1, 2 và L

rồi ghi điểm.

Và điều chúng ta cần làm là lấy một ví dụ,

chỉ là một ví dụ.

Hãy nhớ rằng, bạn có thể làm điều đó trên toàn bộ tập dữ liệu xác thực

và sau đó chúng tôi giải mã câu trả lời thực sự

dưới dạng văn bản tham chiếu

và chúng tôi chuyển điều đó bằng câu trả lời đã được tạo

bằng mô hình tới rouge_scorer.

Vì vậy, chúng tôi chạy cái này và việc này sẽ mất một chút thời gian

bởi vì nó cần phải tạo ra nhiều thế hệ hơn,

nhưng đừng lo lắng, nó được mong đợi.

Và chúng ta bắt đầu.

Trong trường hợp này, chúng ta có thể thấy rằng câu hỏi mà chúng ta nhận được,

à, câu trả lời cho câu hỏi mà chúng tôi nhận được chỉ là Pháp.

Vì vậy, câu trả lời thực tế là Pháp.

Vì vậy, nó đúng.

Vì vậy, rouge1 có độ chính xác một,

rouge2, tất nhiên là bằng 0,

vì đó chỉ là một từ.

Nhưng nếu chúng ta có một câu hỏi ngẫu nhiên khác,

thì chúng ta sẽ nhận được rouge_scores.

Điều chúng tôi có thể chắc chắn là chúng tôi đã thành công

chuyển giao đã học mô hình flan-t5-base

để trả lời câu hỏi,

và điều đó sẽ cực kỳ quan trọng

khi nào chúng ta sẽ áp dụng nó vào chatbot của mình.