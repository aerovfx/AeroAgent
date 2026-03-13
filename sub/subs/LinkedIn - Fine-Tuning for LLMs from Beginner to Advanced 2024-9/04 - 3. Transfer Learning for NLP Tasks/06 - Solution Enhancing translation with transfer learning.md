# 06 - Giải pháp nâng cao dịch thuật bằng học chuyển tiếp

---

(nhạc sôi động)

- [Giảng viên] Vậy thử thách đó thế nào?

Điều này khó khăn hơn một chút

hơn cái trước phải không?

Tôi biết nó đã lâu.

Tôi biết bạn phải xử lý tập dữ liệu mới này

bạn không biết, nhưng hãy thành thật đi,

AI một phần có nghĩa là xử lý các tập dữ liệu chưa biết,

và nó trông như thế nào,

và làm thế nào tôi có thể làm việc với điều này?

Đó là lý do tại sao tôi muốn bạn tạo một tập dữ liệu mới,

hoàn toàn mới, vì vậy chúng ta hãy xem lại giải pháp.

Hãy kết nối với GPU và tôi đây.

Và điều đầu tiên, như bạn biết, là cài đặt PIP.

Chúng ta đây rồi, hoàn hảo.

Vì vậy, điều đầu tiên là lấy tập dữ liệu,

trong trường hợp này là tập dữ liệu bản dịch WMT16,

và chúng tôi sẽ dịch tiếng Đức sang tiếng Anh.

Vì vậy, hãy tải tập dữ liệu của chúng tôi.

Xinh đẹp.

Và như bạn có thể thấy, ở đây chúng tôi có bản dịch,

Tiếng Đức-Anh, hoàn hảo.

Phần này bạn đã biết rồi flan-t5-base.

Chúng ta sẽ sử dụng TFAutoModelForSeq2SeqLM.

Và chúng ta bắt đầu.

Vì vậy đối với quá trình tiền xử lý,

điều duy nhất tôi sắp đề cập là thực sự khác biệt

đó là bây giờ chúng ta cần dịch tiếng Anh sang tiếng Đức.

Đầu tiên chúng ta lấy ví dụ tiếng Anh,

và sau đó là bản dịch sang tiếng Đức, và các mục tiêu.

Đó là một điểm thực sự quan trọng, được chứ?

Vì vậy, nó gần giống với tập dữ liệu trước đó, Opus 100,

nhưng hơi khác về định dạng,

bởi vì ở đây chúng ta cần làm điều này cho vòng lặp.

Sau đó, trên tokenizer, ý tưởng cũng tương tự

để lấy ID đầu vào, nhãn và ID đầu vào của bộ giải mã.

Và hãy nhớ, luôn cắt ngắn=True, đệm= max_length,

và return_tensors='tf', rất, rất quan trọng.

Tất cả phần còn lại vẫn giữ nguyên.

Thế là xong, chúng ta đã có bộ dữ liệu của mình.

Một lần nữa, chúng ta có được mô hình giống như trước đây.

Chúng ta sẽ thực hiện việc học chuyển giao.

Vì vậy, chúng tôi sẽ đóng băng ba lớp chính.

Chúng ta sẽ chỉ đào tạo lớp dày đặc.

Và chúng tôi chỉ đào tạo 24 triệu thông số.

Vì vậy bây giờ chúng ta tập luyện giống như trước đây.

Được rồi, ở đây chúng ta có thể thấy rằng mô hình đã được huấn luyện,

mọi thứ đều tốt

Phải mất một thời gian.

Bạn có thể thấy rằng, trong trường hợp của tôi, mất 11 phút.

Trong trường hợp của bạn, có thể mất một chút thời gian.

Vì vậy bây giờ hãy đánh giá mô hình này,

đó là những gì chúng tôi đã ở đây chờ đợi.

Một lần nữa, chúng ta sẽ tính toán,

trong trường hợp này, chỉ có điểm bleu,

nhưng bạn có thể ghi điểm rouge nếu bạn muốn.

Vì vậy, chúng tôi sẽ mã hóa lại tham chiếu

và giả thuyết và chạy câu bleu,

để có được điểm xanh.

Chúng tôi sẽ lấy một lô từ tập dữ liệu thử nghiệm,

generate the output,

và sau đó chúng ta sẽ có được tài liệu tham khảo và giả thuyết

bằng cách giải mã tham chiếu thực tế, do đó giá trị thực,

và đầu ra của việc tạo chế độ.

Chúng tôi tính toán bleu.

Và sau đó chúng ta sẽ làm điều đó trên mọi đầu vào,

và cuối cùng in ra điểm bleu trung bình.

Vì vậy, hãy chạy cái này.

Vì vậy, việc này có thể mất khoảng một đến hai phút,

tùy thuộc vào GPU của bạn, vì vậy đừng lo lắng.

Bạn có thể thấy rằng, trong trường hợp của tôi, mất 37 giây,

bởi vì tôi chỉ thực hiện một loạt dữ liệu.

Và ở đó chúng ta có điểm bleu trung bình

trên bộ xác nhận, là 0,12.

Hoàn hảo.

Vì vậy, chúng tôi có thể lấy một tập dữ liệu tiếng Đức một cách hiệu quả,

lấy flan-t5,

chuyển giao học tập để làm dịch từ tiếng Đức,

Nhân tiện, đây không phải là ngôn ngữ mẹ đẻ của mô hình đó,

và điều đó rất quan trọng cần đề cập,

bởi vì chúng tôi đang làm điều gì đó mới mẻ đối với mô hình,

việc này thường mất thời gian và khó khăn,

và sau đó chúng tôi có thể đánh giá nó bằng thước đo thực tế,

"Này, đây là mô hình của bạn hoạt động tốt như thế nào."

Tất nhiên, điểm càng cao thì càng tốt.

Vì vậy, bây giờ bạn thậm chí có thể so sánh các mô hình.

Và điều đó kết thúc thử thách này.