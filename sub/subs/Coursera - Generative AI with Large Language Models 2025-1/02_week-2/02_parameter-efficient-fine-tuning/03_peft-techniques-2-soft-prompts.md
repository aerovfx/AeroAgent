# 03 lời nhắc peft-kỹ thuật-2-mềm

---

Với LoRA, mục tiêu là tìm

một cách hiệu quả để cập nhật trọng số của

người mẫu mà không cần đào tạo

từng tham số một lần nữa.

Ngoài ra còn có các phương pháp bổ sung trong

PEFT nhằm mục đích cải thiện hiệu suất mô hình

mà không hề thay đổi trọng số.

Trong video này, bạn sẽ khám phá một giây

phương pháp tinh chỉnh tham số hiệu quả

gọi là điều chỉnh kịp thời.

Bây giờ, việc điều chỉnh lời nhắc có vẻ hơi ồn ào

giống như kỹ thuật nhanh chóng, nhưng

chúng khá khác nhau.

Với kỹ thuật nhanh chóng,

bạn làm việc bằng ngôn ngữ của bạn

nhắc để có được sự hoàn thành mà bạn muốn.

Điều này có thể đơn giản như cố gắng

các từ hoặc cụm từ khác nhau hoặc

phức tạp hơn, như bao gồm các ví dụ cho

Suy luận một hoặc ít lần.

Mục đích là giúp mô hình

hiểu bản chất của

nhiệm vụ bạn đang yêu cầu nó thực hiện và

để tạo ra sự hoàn thiện tốt hơn.

Tuy nhiên, có một số

những hạn chế đối với kỹ thuật nhanh chóng,

vì nó có thể đòi hỏi nhiều nỗ lực thủ công

để viết và thử các lời nhắc khác nhau.

Bạn cũng bị giới hạn bởi độ dài của

cửa sổ ngữ cảnh và vào cuối ngày,

bạn vẫn có thể không đạt được

hiệu suất bạn cần cho nhiệm vụ của mình.

Với việc điều chỉnh kịp thời, bạn có thể bổ sung thêm

mã thông báo có thể đào tạo theo lời nhắc của bạn và

để nó cho việc học có giám sát

quá trình xác định giá trị tối ưu của chúng.

Bộ mã thông báo có thể đào tạo

được gọi là dấu nhắc mềm và

nó được thêm vào trước các vectơ nhúng

đại diện cho văn bản đầu vào của bạn.

Các vectơ dấu nhắc mềm có cùng

chiều dài bằng các vectơ nhúng của

các mã thông báo ngôn ngữ.

Và bao gồm khoảng từ 20 đến

100 token ảo có thể đủ cho

hiệu suất tốt.

Các token đại diện cho tự nhiên

ngôn ngữ khó theo nghĩa là họ

mỗi cái tương ứng với một vị trí cố định

trong không gian vectơ nhúng.

Tuy nhiên, lời nhắc mềm không được sửa

từ rời rạc của ngôn ngữ tự nhiên.

Thay vào đó, bạn có thể coi chúng như

mã thông báo ảo có thể đảm nhận bất kỳ

giá trị trong khoảng thời gian liên tục

không gian nhúng đa chiều.

Và thông qua việc học có giám sát,

mô hình tìm hiểu các giá trị cho

những mã thông báo ảo này sẽ tối đa hóa

hiệu suất cho một nhiệm vụ nhất định.

Trong điều chỉnh hoàn toàn, dữ liệu huấn luyện

tập hợp bao gồm các lời nhắc đầu vào và

hoàn thành đầu ra hoặc nhãn.

Trọng số của mô hình ngôn ngữ lớn

được cập nhật trong quá trình học có giám sát.

Ngược lại với điều chỉnh kịp thời,

trọng số của mô hình ngôn ngữ lớn

bị đóng băng và

mô hình cơ bản không được cập nhật.

Thay vào đó, các vectơ nhúng của

lời nhắc mềm được cập nhật theo thời gian để

tối ưu hóa mô hình

hoàn thành lời nhắc.

Điều chỉnh kịp thời là một tham số rất quan trọng

chiến lược hiệu quả vì chỉ một số ít

các thông số đang được huấn luyện.

Ngược lại với hàng triệu đến hàng tỷ

của các thông số trong tinh chỉnh đầy đủ,

tương tự như những gì bạn đã thấy với LoRA.

Bạn có thể đào tạo một bộ khác

lời nhắc nhẹ nhàng cho từng nhiệm vụ và

sau đó dễ dàng trao đổi chúng

ra tại thời điểm suy luận.

Bạn có thể huấn luyện một bộ lời nhắc mềm cho

một nhiệm vụ và một tập hợp khác cho nhiệm vụ khác.

Để sử dụng chúng cho việc suy luận,

bạn thêm vào lời nhắc đầu vào của mình bằng

các mã thông báo đã học để chuyển sang mã thông báo khác

nhiệm vụ, bạn chỉ cần thay đổi dấu nhắc mềm.

Lời nhắc mềm rất nhỏ trên đĩa, vì vậy

kiểu tinh chỉnh này là

cực kỳ hiệu quả và linh hoạt.

Bạn sẽ nhận thấy LLM tương tự được sử dụng cho

mọi nhiệm vụ,

tất cả những gì bạn phải làm là tắt đi

các dấu nhắc mềm tại thời điểm suy luận.

Vậy điều chỉnh nhanh chóng hoạt động tốt như thế nào?

Trong bài báo gốc,

Khám phá phương pháp của Brian Lester và

cộng tác viên tại Google.

Các tác giả đã so sánh việc điều chỉnh kịp thời

đến một số phương pháp khác để

một loạt các kích cỡ mô hình.

Trong hình này từ bài báo, bạn có thể

xem kích thước Mô hình trên trục X và

điểm SuperGLUE trên trục Y.

Đây là tiêu chuẩn đánh giá

bạn đã biết về điều này trước đó

tuần chấm điểm hiệu suất của mô hình trên

một số nhiệm vụ ngôn ngữ khác nhau.

Đường màu đỏ thể hiện điểm của

các mô hình được tạo ra thông qua

tinh chỉnh đầy đủ trên một nhiệm vụ duy nhất.

Trong khi đường màu cam hiển thị điểm cho

mô hình được tạo bằng cách sử dụng

tinh chỉnh đa nhiệm.

Đường màu xanh thể hiện hiệu suất

điều chỉnh kịp thời và cuối cùng,

đường màu xanh hiển thị điểm cho

chỉ kỹ thuật nhanh chóng.

Như bạn có thể thấy, việc điều chỉnh kịp thời không

thực hiện cũng như tinh chỉnh đầy đủ cho

LLM nhỏ hơn.

Tuy nhiên, khi kích thước mô hình tăng lên thì

thực hiện việc điều chỉnh kịp thời.

Và một khi các mô hình có xung quanh

10 tỷ thông số,

điều chỉnh nhanh chóng có thể có hiệu quả

như tinh chỉnh đầy đủ và

cung cấp một sự gia tăng đáng kể trong hiệu suất

chỉ nhờ kỹ thuật nhanh chóng.

Một vấn đề tiềm năng cần xem xét là

khả năng diễn giải của ảo đã học

mã thông báo.

Hãy nhớ, bởi vì dấu nhắc mềm

mã thông báo có thể nhận bất kỳ giá trị nào trong

không gian vectơ nhúng liên tục.

Mã thông báo được đào tạo không tương ứng

đối với bất kỳ mã thông báo, từ hoặc

cụm từ trong từ vựng của LLM.

Tuy nhiên, một phân tích gần nhất

mã thông báo hàng xóm đến dấu nhắc mềm

vị trí cho thấy chúng hình thành

các cụm ngữ nghĩa chặt chẽ.

Nói cách khác, những từ gần nhất với

mã thông báo nhắc mềm có ý nghĩa tương tự.

Những từ được xác định thường có

một số ý nghĩa liên quan đến nhiệm vụ,

gợi ý rằng những lời nhắc

đang học từ giống như cách biểu đạt.

Bạn đã khám phá hai phương pháp PEFT trong phần này

bài học LoRA, sử dụng phân tách thứ hạng

ma trận để cập nhật mô hình

các thông số một cách hiệu quả.

Và điều chỉnh nhanh chóng, nơi có thể đào tạo

mã thông báo được thêm vào lời nhắc của bạn và

trọng lượng của mô hình không bị ảnh hưởng.

Cả hai phương pháp đều cho phép bạn xử lý tốt

điều chỉnh các mô hình có tiềm năng

cải thiện hiệu suất trong nhiệm vụ của bạn

trong khi sử dụng tính toán ít hơn nhiều so với đầy đủ

các phương pháp tinh chỉnh.

LoRA được sử dụng rộng rãi trong thực tế vì

về hiệu suất có thể so sánh với mức hoàn toàn tốt

điều chỉnh cho nhiều nhiệm vụ và tập dữ liệu,

và bạn sẽ dùng thử nó

chính bạn trong phòng thí nghiệm của tuần này.

Vậy xin chúc mừng bạn đã làm được

đến hết tuần thứ 2.

Hãy tóm tắt lại những gì bạn đã thấy trước đó

tuần sau, Mike đã hướng dẫn bạn cách

điều chỉnh mô hình nền tảng thông qua

một quá trình được gọi là tinh chỉnh lệnh.

Trên đường đi,

bạn đã thấy một số mẫu lời nhắc và

bộ dữ liệu đã được sử dụng

để huấn luyện mô hình FLAN-T5.

Bạn cũng đã thấy cách sử dụng đánh giá

số liệu và điểm chuẩn như ROUGE và

HELM để đo lường thành công

trong quá trình tinh chỉnh mô hình.

Tinh chỉnh hướng dẫn thực hành

đã tỏ ra rất hiệu quả và

hữu ích trên nhiều lĩnh vực tự nhiên

các trường hợp và nhiệm vụ sử dụng ngôn ngữ.

Chỉ với vài trăm ví dụ,

bạn có thể tinh chỉnh mô hình cho phù hợp với

nhiệm vụ cụ thể, điều này thực sự tuyệt vời.

Tiếp theo, bạn đã thấy tham số như thế nào

tinh chỉnh hiệu quả, hoặc PEFT,

có thể giảm khối lượng tính toán

cần thiết để tinh chỉnh một mô hình.

Bạn đã tìm hiểu về hai phương pháp bạn có thể

sử dụng cho LoRA này và Điều chỉnh nhanh chóng.

Nhân tiện, bạn cũng có thể kết hợp LoRA với

các kỹ thuật lượng tử hóa bạn đã học

khoảng tuần 1 trở đi

giảm dấu chân bộ nhớ của bạn.

Điều này được gọi là QLoRA trong thực tế,

PEFT được sử dụng nhiều để giảm thiểu

tài nguyên tính toán và bộ nhớ.

Và cuối cùng là giảm chi phí phạt

điều chỉnh, cho phép bạn tận dụng tối đa

ngân sách điện toán của bạn và

đẩy nhanh quá trình phát triển của bạn.