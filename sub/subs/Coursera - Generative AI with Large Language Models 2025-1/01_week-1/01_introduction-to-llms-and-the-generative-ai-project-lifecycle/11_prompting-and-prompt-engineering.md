# 11 kỹ thuật nhắc nhở và nhắc nhở

---

Được rồi, chỉ để nhắc nhở bạn về

một số thuật ngữ.

Văn bản bạn đưa vào

mô hình được gọi là lời nhắc,

hành động tạo ra văn bản

được gọi là suy luận,

và văn bản đầu ra là

được gọi là sự hoàn thành.

Toàn bộ số lượng văn bản hoặc

bộ nhớ có sẵn

để sử dụng cho lời nhắc là

gọi là cửa sổ ngữ cảnh.

Mặc dù ví dụ ở đây

cho thấy mô hình hoạt động tốt,

bạn sẽ thường xuyên gặp phải

tình huống trong đó mô hình

không tạo ra

kết quả là bạn

muốn ngay lần thử đầu tiên.

Bạn có thể phải

sửa lại ngôn ngữ

trong lời nhắc của bạn hoặc

theo cách đó

viết nhiều lần để có được

hình mẫu để ứng xử

theo cách mà bạn muốn.

Công việc này nhằm phát triển và cải thiện

lời nhắc được gọi là

kỹ thuật nhanh chóng.

Đây là một chủ đề lớn.

Nhưng một chiến lược mạnh mẽ để có được

mô hình để sản xuất

kết quả tốt hơn là

bao gồm các ví dụ về

nhiệm vụ mà bạn muốn

mô hình để thực hiện

bên trong lời nhắc.

Cung cấp các ví dụ bên trong

cửa sổ ngữ cảnh

được gọi là học tập trong ngữ cảnh.

Chúng ta hãy nhìn vào

thuật ngữ này có nghĩa là gì

Với trong bối cảnh

học tập, bạn có thể

giúp LLM tìm hiểu thêm

về nhiệm vụ đang

hỏi bằng cách bao gồm các ví dụ

hoặc dữ liệu bổ sung

trong lời nhắc.

Đây là một ví dụ cụ thể.

Trong lời nhắc hiển thị ở đây,

bạn yêu cầu người mẫu phân loại

tình cảm của một đánh giá.

Vì vậy liệu

đánh giá về bộ phim này

là tích cực hay tiêu cực,

lời nhắc bao gồm

của sự hướng dẫn,

"Phân loại đánh giá này,"

theo sau là một số bối cảnh,

trong trường hợp này là

chính văn bản đánh giá,

và hướng dẫn sản xuất

tình cảm ở phần cuối.

Phương pháp này, bao gồm cả

dữ liệu đầu vào trong dấu nhắc,

được gọi là suy luận zero-shot.

LLM lớn nhất là

giỏi một cách đáng ngạc nhiên về việc này,

nắm bắt nhiệm vụ được giao

hoàn thành và trở về

một câu trả lời hay.

Trong ví dụ này,

mô hình một cách chính xác

xác định

tình cảm càng tích cực.

Các mẫu nhỏ hơn, trên

mặt khác,

có thể đấu tranh với điều này.

Đây là một ví dụ về một

hoàn thành được tạo bởi GPT-2,

một phiên bản nhỏ hơn trước đó

của mô hình đó

hỗ trợ ChatGPT.

Như bạn có thể thấy, mô hình

không làm theo hướng dẫn.

Mặc dù nó tạo ra văn bản

với một số mối quan hệ

theo lời nhắc,

người mẫu không thể hình dung được

ra các chi tiết

của nhiệm vụ và không

xác định tình cảm.

Đây là nơi

cung cấp một ví dụ

trong lời nhắc có thể

cải thiện hiệu suất.

Ở đây bạn có thể thấy

rằng văn bản nhắc nhở

dài hơn và bây giờ bắt đầu bằng

một ví dụ hoàn chỉnh rằng

thể hiện các nhiệm vụ cần thực hiện

thực hiện theo mô hình.

Sau khi xác định rằng mô hình

nên phân loại đánh giá,

văn bản nhắc nhở bao gồm

một bài đánh giá mẫu.

Tôi yêu thích bộ phim này,

theo sau là hoàn thành

phân tích tình cảm.

Trong trường hợp này,

đánh giá là tích cực.

Tiếp theo, lời nhắc nêu rõ

hướng dẫn

một lần nữa và bao gồm

đánh giá đầu vào thực tế

rằng chúng tôi muốn

mô hình để phân tích.

Bạn vượt qua điều này mới lâu hơn

nhắc đến mô hình nhỏ hơn,

bây giờ có cơ hội tốt hơn

hiểu rõ nhiệm vụ bạn đang làm

chỉ định và định dạng của

câu trả lời mà bạn mong muốn.

Sự bao gồm của

một ví dụ duy nhất

được gọi là suy luận một lần,

trái ngược với zero-shot

nhắc bạn đã cung cấp trước đó.

Đôi khi một đơn

ví dụ sẽ không

đủ để người mẫu học hỏi

bạn muốn nó làm gì.

Vì vậy bạn có thể mở rộng

ý tưởng cho đi

một ví dụ duy nhất để

bao gồm nhiều ví dụ.

Điều này được gọi là

suy luận vài lần.

Ở đây, bạn đang làm việc với

thậm chí còn nhỏ hơn

mô hình thất bại

để thực hiện tốt

phân tích tình cảm

với suy luận một lần.

Thay vào đó, bạn sẽ thử

suy luận vài lần bởi

bao gồm một ví dụ thứ hai.

Lần này, một đánh giá tiêu cực,

bao gồm sự kết hợp của các ví dụ với

đầu ra khác nhau

lớp học có thể giúp đỡ

mô hình để hiểu

nó cần phải làm gì.

Bạn vượt qua cái mới

nhắc nhở mô hình.

Và lần này nó hiểu

hướng dẫn và

tạo ra một sự hoàn thành mà

xác định chính xác

tình cảm của

đánh giá là tiêu cực.

Tóm lại, bạn có thể thiết kế

lời nhắc của bạn để khuyến khích

làm mẫu để học bằng ví dụ.

Trong khi lớn nhất

người mẫu giỏi

suy luận không bắn

không có ví dụ,

mô hình nhỏ hơn có thể

hưởng lợi từ một lần hoặc

suy luận vài lần bao gồm

ví dụ về

hành vi mong muốn.

Nhưng hãy nhớ cửa sổ ngữ cảnh

bởi vì bạn có giới hạn

về số lượng

học tập theo ngữ cảnh

mà bạn có thể vượt qua

vào mô hình.

Nói chung, nếu bạn

thấy rằng mô hình của bạn

không hoạt động tốt khi, chẳng hạn,

bao gồm năm hoặc sáu ví dụ,

bạn nên thử tinh chỉnh

thay vào đó là mô hình của bạn.

Tinh chỉnh thực hiện

đào tạo bổ sung

trên mô hình sử dụng

dữ liệu mới để làm cho nó tốt hơn

có khả năng thực hiện nhiệm vụ mà bạn

muốn nó thực hiện.

Bạn sẽ khám phá việc tinh chỉnh trong

chi tiết trong tuần 2 của khóa học này.

Càng ngày càng lớn hơn

người mẫu đã được đào tạo

nó trở nên rõ ràng

khả năng đó

của các mô hình để thực hiện

nhiều nhiệm vụ

và họ tốt thế nào

thực hiện những nhiệm vụ đó

phụ thuộc mạnh mẽ vào

quy mô của mô hình.

Như bạn đã nghe trước đó

trong bài học,

mô hình với nhiều hơn nữa

các thông số có thể

nắm bắt thêm sự hiểu biết

của ngôn ngữ.

Các mô hình lớn nhất

tốt một cách đáng ngạc nhiên

tại suy luận không bắn

và có thể

suy luận và hoàn thành thành công

nhiều nhiệm vụ mà họ đã làm

không cụ thể

được đào tạo để biểu diễn.

Ngược lại, các mô hình nhỏ hơn

nói chung chỉ giỏi một

số lượng nhỏ nhiệm vụ.

Thông thường, những cái đó là

tương tự như nhiệm vụ đó

họ đã được đào tạo.

Bạn có thể phải thử

một vài mô hình để tìm ra

một cái phù hợp cho trường hợp sử dụng của bạn.

Khi bạn đã tìm thấy mô hình

điều đó đang có tác dụng với bạn,

có một vài cài đặt

bạn có thể thử nghiệm với

ảnh hưởng đến

cấu trúc và phong cách

trong số những sự hoàn thành đó

mô hình tạo ra.

Chúng ta hãy xem

tại một số trong số này

cài đặt cấu hình

trong video tiếp theo.