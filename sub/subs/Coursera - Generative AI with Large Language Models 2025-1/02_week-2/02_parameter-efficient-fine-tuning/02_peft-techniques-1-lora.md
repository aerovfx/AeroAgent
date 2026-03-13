# 02 peft-kỹ thuật-1-lora

---

Thích ứng cấp thấp,

hay gọi tắt là LoRA,

là một tham số hiệu quả

kỹ thuật tinh chỉnh

rơi vào

thể loại tái tham số hóa.

Chúng ta hãy xem

vào cách nó hoạt động.

Như một lời nhắc nhở nhanh chóng,

đây là sơ đồ của

máy biến áp

kiến trúc đó

bạn đã thấy trước đó trong khóa học.

Dấu nhắc đầu vào là

biến thành token,

sau đó được chuyển đổi thành

nhúng vectơ và truyền

vào bộ mã hóa và/hoặc bộ giải mã

các bộ phận của máy biến áp.

Trong cả hai thành phần này,

có hai loại

của mạng lưới thần kinh;

sự tự chú ý và

các mạng tiếp liệu.

Trọng lượng của các mạng này

được học trong quá trình đào tạo trước.

Sau khi nhúng

vectơ được tạo ra,

chúng được đưa vào

lớp tự chú ý nơi

một loạt trọng số được áp dụng

để tính toán

điểm chú ý.

Trong quá trình tinh chỉnh hoàn toàn,

mọi tham số trong này

các lớp được cập nhật.

LoRA là một chiến lược

làm giảm số lượng

các thông số cần huấn luyện

trong quá trình tinh chỉnh bằng cách đóng băng

tất cả các mô hình ban đầu

các tham số và sau đó

tiêm một cặp

ma trận phân rã xếp hạng

bên cạnh trọng lượng ban đầu.

Kích thước của

ma trận nhỏ hơn

được thiết lập sao cho sản phẩm của họ

là một ma trận với

kích thước giống nhau

như trọng lượng

họ đang sửa đổi.

Sau đó bạn giữ

trọng lượng ban đầu của

LLM bị đóng băng và đào tạo

các ma trận nhỏ hơn bằng cách sử dụng

cùng được giám sát

quá trình học tập

bạn đã thấy vào đầu tuần này.

Để suy luận, hai cấp thấp

ma trận được nhân

cùng nhau để tạo ra một ma trận với

kích thước tương tự như

trọng lượng đông lạnh.

Sau đó bạn thêm phần này vào

trọng lượng ban đầu và

thay thế chúng trong mô hình

với những giá trị được cập nhật này.

Bây giờ bạn có LoRA

mô hình tinh chỉnh

điều đó có thể thực hiện

nhiệm vụ cụ thể của bạn.

Bởi vì mô hình này có

cùng một số lượng

các thông số như ban đầu,

có rất ít hoặc không có tác động

về độ trễ suy luận.

Các nhà nghiên cứu có

nhận thấy rằng việc áp dụng

LoRA chỉ

các lớp tự chú ý của

mô hình thường đủ để

tinh chỉnh cho một nhiệm vụ và

đạt được hiệu quả đạt được.

Tuy nhiên, về nguyên tắc,

bạn cũng có thể sử dụng LoRA trên

các thành phần khác như

các lớp chuyển tiếp nguồn cấp dữ liệu.

Nhưng vì hầu hết

các thông số của

LLM đang ở trong

lớp chú ý,

bạn nhận được khoản tiết kiệm lớn nhất trong

các tham số có thể huấn luyện bằng cách áp dụng

LoRA cho các ma trận trọng số này.

Chúng ta hãy nhìn vào một

ví dụ thực tế sử dụng

máy biến áp

kiến trúc được mô tả trong

sự chú ý là

Tất cả những gì bạn cần là giấy.

Bài báo chỉ rõ rằng

trọng lượng máy biến áp

có kích thước 512 x 64.

Điều này có nghĩa là

mỗi ma trận trọng số

có 32.768 tham số có thể huấn luyện được.

Nếu bạn sử dụng LoRA như

phương pháp tinh chỉnh bằng

cấp bậc bằng tám,

thay vào đó bạn sẽ tập luyện

hai cấp bậc nhỏ

ma trận phân rã

có chiều nhỏ là tám.

Điều này có nghĩa là Ma trận A sẽ

có kích thước 8 x 64,

kết quả là 512

tổng tham số.

Ma trận B sẽ có

kích thước 512 x 8,

hoặc 4.096 tham số có thể huấn luyện.

Bằng cách cập nhật trọng số của

những ma trận cấp thấp mới này

thay vì trọng lượng ban đầu,

bạn sẽ được đào tạo 4,608

thông số thay vì

32.768 và giảm 86%.

Vì LoRA cho phép

bạn đáng kể

giảm số lượng

các thông số có thể huấn luyện được,

bạn có thể thường xuyên biểu diễn

phương pháp này

tham số hiệu quả

tinh chỉnh với

một GPU duy nhất và tránh

sự cần thiết của một hệ thống phân phối

cụm GPU.

Kể từ khi phân rã thứ hạng

ma trận nhỏ,

bạn có thể tinh chỉnh một cách khác

thiết lập cho từng nhiệm vụ và sau đó

chuyển chúng ra

tại thời điểm suy luận

bằng cách cập nhật trọng số.

Giả sử bạn huấn luyện một cặp

Ma trận LoRA cho

một nhiệm vụ cụ thể;

hãy gọi nó là Nhiệm vụ A.

Để thực hiện suy luận

về nhiệm vụ này,

bạn sẽ nhân chúng lên

ma trận với nhau và

sau đó thêm ma trận kết quả

về trọng lượng đông lạnh ban đầu.

Sau đó bạn lấy cái mới này

ma trận trọng số tổng hợp

và thay thế trọng lượng ban đầu

nơi chúng xuất hiện trong mô hình của bạn.

Sau đó bạn có thể sử dụng mô hình này để

thực hiện suy luận về Nhiệm vụ A.

Nếu thay vào đó, bạn

muốn thực hiện

một nhiệm vụ khác, chẳng hạn như Nhiệm vụ B,

bạn chỉ cần lấy

LoRA ma trận cho bạn

được đào tạo cho nhiệm vụ này,

tính toán sản phẩm của họ,

và sau đó thêm ma trận này vào

trọng lượng ban đầu và

cập nhật lại mô hình.

Bộ nhớ cần thiết để lưu trữ

những ma trận LoRA này

là rất nhỏ.

Vì vậy, về nguyên tắc, bạn có thể sử dụng

LoRA để đào tạo cho nhiều nhiệm vụ.

Thay đổi trọng lượng

khi bạn cần sử dụng chúng,

và tránh phải lưu trữ

nhiều kích thước đầy đủ

phiên bản LLM.

Những mô hình này tốt như thế nào?

Hãy sử dụng ROUGE

số liệu bạn đã tìm hiểu về

đầu tuần này để

so sánh hiệu suất của

một mô hình tinh chỉnh LoRA để

vừa là mô hình cơ sở ban đầu

và một phiên bản tinh chỉnh đầy đủ.

Hãy tập trung vào việc tinh chỉnh

FLAN-T5 dành cho

tóm tắt đối thoại,

mà bạn đã khám phá

đầu tuần.

Chỉ để nhắc nhở bạn,

mô hình cơ sở FLAN-T5

đã có một bộ ban đầu

thực hiện tinh chỉnh đầy đủ

sử dụng một kích thước lớn

tập dữ liệu lệnh.

Đầu tiên, hãy thiết lập một

điểm cơ bản cho

mô hình cơ sở FLAN-T5 và

dữ liệu tóm tắt

thiết lập mà chúng ta đã thảo luận trước đó.

Đây là điểm số ROUGE

cho mô hình cơ sở trong đó

một con số cao hơn cho thấy

hiệu suất tốt hơn.

Bạn nên tập trung vào

điểm ROUGE 1

cho cuộc thảo luận này,

nhưng bạn có thể sử dụng bất kỳ

những điểm số này để so sánh.

Như bạn có thể thấy,

điểm số khá thấp.

Tiếp theo, nhìn vào điểm số

cho một mô hình đã có

tinh chỉnh đầy đủ bổ sung

về tóm tắt đối thoại.

Hãy nhớ rằng, mặc dù FLAN-T5

là một người mẫu có năng lực,

nó vẫn có thể hưởng lợi từ

tinh chỉnh bổ sung

về các nhiệm vụ cụ thể.

Với đầy đủ tinh chỉnh,

bạn cập nhật mọi cách trong

mô hình trong thời gian

học tập có giám sát.

Bạn có thể thấy rằng điều này dẫn đến

điểm ROUGE 1 cao hơn nhiều

tăng trên cơ sở

Mẫu FLAN-T5 bằng 0,19.

Vòng bổ sung của

tinh chỉnh đã được cải thiện rất nhiều

hiệu suất của mô hình

về nhiệm vụ tóm tắt.

Bây giờ chúng ta hãy lấy một

nhìn vào điểm số

cho mô hình tinh chỉnh LoRA.

Bạn có thể thấy điều đó

quá trình này cũng

dẫn đến một sự việc lớn

tăng hiệu suất.

Điểm số ROUGE 1

đã tăng từ

đường cơ sở là 0,17.

Điều này thấp hơn một chút so với

tinh chỉnh đầy đủ, nhưng không nhiều.

Tuy nhiên, sử dụng LoRA cho

tinh chỉnh được đào tạo một

số lượng nhỏ hơn nhiều

thông số hơn tinh chỉnh đầy đủ

sử dụng đáng kể

ít tính toán hơn,

vì vậy sự đánh đổi nhỏ này trong

hiệu suất có thể

cũng có giá trị nó.

Có thể bạn đang thắc mắc

làm thế nào để lựa chọn

thứ hạng của ma trận LoRA.

Đây là một câu hỏi hay và

vẫn còn hoạt động

lĩnh vực nghiên cứu.

Về nguyên tắc,

thứ hạng nhỏ hơn,

số càng nhỏ

của các tham số có thể huấn luyện được,

và càng lớn thì

tiết kiệm về tính toán.

Tuy nhiên, có một số vấn đề

liên quan đến mô hình

hiệu suất để xem xét.

Trong bài báo đó

LoRA được đề xuất đầu tiên,

các nhà nghiên cứu tại

Microsoft đã khám phá

sự lựa chọn khác nhau như thế nào

thứ hạng đã ảnh hưởng đến

hiệu suất mô hình

về các nhiệm vụ tạo ngôn ngữ.

Bạn có thể xem bản tóm tắt của

kết quả trong bảng ở đây.

Bảng thể hiện thứ hạng của

ma trận LoRA trong

cột đầu tiên,

sự mất mát cuối cùng

giá trị của mô hình,

và điểm số cho

số liệu khác nhau,

bao gồm BLEU và ROUGE.

Các giá trị in đậm cho biết

điểm số tốt nhất đó là

đạt được cho từng chỉ số.

Các tác giả đã tìm thấy một cao nguyên ở

giá trị tổn thất cho

hạng lớn hơn 16.

Nói cách khác, sử dụng

ma trận LoRA lớn hơn thì không

cải thiện hiệu suất.

Điều đáng nói ở đây là

xếp hạng trong khoảng 4-32 lon

cung cấp cho bạn một điều tốt

đánh đổi giữa việc giảm

các thông số có thể huấn luyện được và

bảo toàn hiệu suất.

Tối ưu hóa việc lựa chọn thứ hạng là

một lĩnh vực nghiên cứu đang diễn ra và

thực tiễn tốt nhất có thể phát triển như

nhiều học viên thích hơn

bạn sử dụng LoRA.

LoRA mạnh mẽ

phương pháp tinh chỉnh

đó đạt được hiệu suất tuyệt vời.

Những nguyên tắc đằng sau

phương pháp này là

hữu ích không chỉ

để đào tạo LLM,

nhưng đối với các mô hình trong các lĩnh vực khác.

Phương pháp đường dẫn cuối cùng

rằng bạn sẽ khám phá điều này

tuần không thay đổi

LLM hoàn toàn và thay vào đó

tập trung vào đào tạo

văn bản đầu vào của bạn.

Hãy tham gia cùng tôi trong phần tiếp theo

video để tìm hiểu thêm.