# 07 - Giải pháp Tinh chỉnh FLAN-T5 cho dịch thuật

---

(âm nhạc sôi động bắt đầu)

- [Giảng viên] Vậy thử thách đó thế nào?

Đây là lần đầu tiên bạn triển khai tinh chỉnh LoRA.

Vì vậy bây giờ tôi sẽ chỉ cho bạn giải pháp của tôi,

một lần nữa, hãy nhớ rằng, đó là một giải pháp,

nhưng điều quan trọng nhất cần nhớ

LoRA là một kỹ thuật tiên tiến.

Vì vậy, ngay cả khi bạn cần xem qua các bản demo,

hoặc vào các bài viết hoặc các slide,

điều đó thật tuyệt vời.

Đó là cách chúng ta học, được chứ?

Đừng nản lòng vì có rất nhiều mã

và đó là rất nhiều phần bên trong của mô hình.

Không có giao diện dễ dàng như Keras cung cấp

để đào tạo người mẫu.

Trước đây chúng tôi phải thực hiện rất nhiều lần theo dõi

và bây giờ nó đã được mô phỏng hoàn toàn, và nó rất đẹp, phải không?

Và chúng tôi có ETA và thanh tiến trình.

Trước đây không phải như vậy.

Với LoRA thì là vậy và sau này sẽ khá hơn.

Nhưng biết những gì đang diễn ra dưới mui xe

và việc bạn làm điều đó mang lại giá trị cực lớn.

Không dài dòng nữa, hãy để tôi kết nối với GPU.

Tôi đây.

Vì vậy, trước tiên, chúng ta thực hiện cài đặt pip tương tự

như trước đây.

Nó đây rồi, hoàn hảo.

Và bây giờ chúng ta sẽ tải bộ dữ liệu WMT16 tương tự

mà chúng tôi đã sử dụng từ lâu.

Nhân tiện, trong khi tải xuống,

mà bạn biết là nó tốn rất ít thời gian,

nếu bạn không muốn sử dụng tiếng Đức sang tiếng Anh

và bạn muốn sử dụng một nhóm ngôn ngữ khác,

nó siêu ổn.

WMT16 thực sự có rất nhiều cặp ngôn ngữ.

Vì vậy, bạn có thể thử bằng ngôn ngữ của riêng bạn

vì vậy bạn cũng có thể tự mình xác minh thủ công

rằng các bản dịch đều ổn.

Tôi chỉ muốn làm rõ điều đó để đề phòng thôi.

Nó đây rồi.

Bây giờ chúng tôi đã tải xuống,

chúng tôi luôn có cùng một định dạng,

và bây giờ chúng ta sẽ tải tokenizer của mình.

Việc mã hóa vẫn giống như trước đây.

Vì vậy, chúng tôi sẽ dịch tiếng Anh sang tiếng Đức.

Chúng tôi lấy phần tiếng Anh từ bản dịch

và sau đó là phần tiếng Đức.

Và sau đó các nhãn về cơ bản sẽ là mục tiêu,

đó là phần tiếng Đức được token hóa,

và ID đầu vào của bộ giải mã cũng sẽ là ID đầu vào.

Vì vậy, chúng tôi có được nó.

Chúng tôi sẽ sử dụng 20.000 hàng để thực hiện việc này nhanh chóng.

Và chúng tôi thực hiện chuyển đổi tương tự sang tập dữ liệu TF như trước.

Luôn nhớ kích thước lô bạn chơi xung quanh

với số lượng RAM GPU mà bạn có.

Nó đây rồi.

Vậy là chúng ta đã lập được bản đồ rồi.

Vì vậy, hãy tải mô hình của chúng tôi.

Và chỉ vì thời gian,

Mình đang dùng Flan T5 Small.

Tất nhiên, ở đây, nếu bạn muốn có kết quả siêu tốt hơn,

bạn có thể tinh chỉnh LoRA và Flan T5 Large,

hoặc cực lớn, nhưng sẽ mất nhiều thời gian hơn.

Vì vậy, đó là sự lựa chọn của bạn.

Nó đây rồi.

Đã tải mô hình.

Lớp LoRA vẫn giống như trước.

Hãy nhớ rằng chúng ta có hai ma trận trọng số A và B.

Chúng ta có kết quả ban đầu, kết quả LoRA,

đó là A nhân B trên đầu vào,

và sau đó chúng tôi cộng chúng lại.

Nếu chúng ta xem bản tóm tắt mô hình, chúng ta sẽ có cấu trúc tương tự,

đó là bộ mã hóa, bộ giải mã và phần đầu được nhúng.

Trong trường hợp này chúng ta chỉ có 76 triệu tham số.

Và điều chúng ta sắp làm là chúng ta sẽ làm

chuyển giao học tập trên ba lớp đầu tiên.

Vì vậy, chúng tôi đóng băng chúng và lớp cuối cùng sẽ là lớp LoRA.

Vậy sau khi làm điều đó, chúng ta sẽ tính,

như chúng tôi đã làm trong bản demo trước,

các tham số có thể huấn luyện và không thể huấn luyện.

Và chúng ta có thể thấy rằng chúng ta sẽ đào tạo

16 triệu tham số, chiếm khoảng 1/4

nếu tính toán của tôi đúng.

Một lần nữa, hãy nhớ nếu bạn muốn huấn luyện ít tham số hơn,

bạn chỉ cần đi sâu hơn với LoRA vào từng lớp.

Được rồi?

Ở đây chúng tôi có bản tóm tắt mô hình của chúng tôi,

trong đó cho thấy điều tương tự.

Chúng ta sẽ huấn luyện 16 triệu thông số,

và bây giờ chúng ta sẽ biên dịch và đào tạo

như chúng ta đã và đang làm bấy lâu nay.

Được rồi, hoàn hảo.

Vậy là chúng ta đã hoàn thành khóa đào tạo trong ba phút.

Tất nhiên điều này một phần là do LoRA

và bởi vì nó là mô hình nhỏ.

Vì vậy chúng ta có thể thấy rằng mỗi giai đoạn không khởi động

chỉ mất 40 giây

và sự mất mát đã giảm mỗi kỷ nguyên

cũng trên bộ xác nhận.

Vì vậy chúng tôi đã đào tạo điều này rất tốt

và bây giờ chúng ta sẽ đánh giá mô hình.

Vì vậy, có một số cách.

Như bạn đã biết, chúng ta có model.evaluate,

Tôi đã thể hiện điều này rồi,

nó sẽ cho bạn thấy sự mất xác thực trên tập dữ liệu thử nghiệm,

đó là 11, nhưng con số đó có thể không cho bạn biết nhiều điều.

Vì vậy điều chúng ta sắp làm là tính toán

điểm BLEU.

Hãy nhớ rằng điểm BLEU so sánh độ chính xác

của văn bản tham chiếu được mã hóa bằng các từ

và văn bản giả thuyết,

đó là một văn bản được tạo ra, cũng được mã hóa.

Vì vậy điều chúng ta sẽ làm là lấy một đợt,

chỉ để làm cho nó nhanh chóng,

nhưng bạn có thể làm điều đó trên tất cả các lô.

Một lần nữa, chúng ta nhận được đầu vào tại tham chiếu,

chúng tôi tạo ra đầu ra,

và sau đó chúng tôi tính điểm BLEU trên mỗi đầu vào.

Và cuối cùng chúng ta sẽ in điểm BLEU trung bình

trên bộ xác nhận này.

Trên thực tế, nó sẽ có một đợt

của bộ xác thực chứ không phải toàn bộ bộ xác thực

vì những gì tôi đã nói với bạn,

nhưng nếu bạn chạy nó bằng vòng lặp for ở đó,

nó sẽ nằm trên toàn bộ bộ xác thực

và phần còn lại của mã chỉ chạy.

Vì vậy, quá trình này có thể mất một hoặc hai phút, vì vậy đừng lo lắng.

Tuyệt vời.

Vì vậy, chúng tôi đã nhận được điểm BLEU trung bình trên bộ xác thực này,

là 0,11, một giá trị rất rất tốt.

Hãy nhớ rằng giá trị tuyệt vời là 0,3, 0,4,

và ở đây chúng tôi đang sử dụng chiếc T5 nhỏ, thậm chí không phải chiếc cơ sở.

Điều đó có nghĩa là công việc của chúng tôi thực sự tốt.

Và đây chính là giải pháp cho thách thức này.

Tôi thực sự hy vọng rằng bạn thích nó.

Và nếu bạn còn nghi ngờ, hãy nhớ những điều quan trọng

là việc xử lý dữ liệu

mà chúng ta đã làm suốt thời gian qua,

thì chúng tôi áp dụng LoRA giống như cách chúng tôi đã áp dụng trên cả hai bản demo,

và cuối cùng chúng tôi đang đánh giá bằng điểm BLEU này.

Bạn muốn sử dụng Rouge, bạn có thể sử dụng Rouge.

Không sao đâu.

Đây không phải là giải pháp duy nhất.

Được rồi?