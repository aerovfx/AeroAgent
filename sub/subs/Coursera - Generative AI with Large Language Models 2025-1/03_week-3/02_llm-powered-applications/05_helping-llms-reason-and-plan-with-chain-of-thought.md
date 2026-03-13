# 05-lý-do-và-kế hoạch-với-chuỗi-tư duy

---

Như bạn đã thấy, đó là

điều quan trọng là LLM có thể

suy luận thông qua các bước đó

một ứng dụng phải mất,

để đáp ứng một yêu cầu của người dùng.

Thật không may, lý luận phức tạp

có thể là thách thức đối với LLM,

đặc biệt là đối với

những vấn đề liên quan

nhiều bước hoặc toán học.

Những vấn đề này tồn tại

ngay cả trong các mô hình lớn

cho thấy hiệu suất tốt

ở nhiều nhiệm vụ khác.

Đây là một ví dụ trong đó LLM

gặp khó khăn

hoàn thành nhiệm vụ.

Bạn đang yêu cầu mô hình giải quyết

nhiều bước đơn giản

vấn đề toán học,

để xác định có bao nhiêu

táo một quán cà phê

có sau khi sử dụng

một số để làm bữa trưa,

và sau đó mua thêm một số thứ nữa.

Lời nhắc của bạn bao gồm một

vấn đề ví dụ tương tự,

hoàn thành với giải pháp,

để giúp người mẫu hiểu

nhiệm vụ thông qua

suy luận một lần.

Nếu bạn thích, bạn có thể

tạm dừng video ở đây

một lúc và giải quyết

vấn đề của chính bạn.

Sau khi xử lý lời nhắc,

mô hình tạo ra

hoàn thành hiển thị ở đây,

nói rằng câu trả lời là 27.

Câu trả lời này sai,

như bạn đã phát hiện ra nếu

bạn giải quyết vấn đề.

Căn tin thực ra chỉ có

còn lại chín quả táo.

Các nhà nghiên cứu đã

tìm cách cải thiện

hiệu suất của

mô hình ngôn ngữ lớn

về nhiệm vụ lý luận,

giống như cái bạn vừa thấy.

Một chiến lược có

đã chứng minh một số thành công là

nhắc nhở người mẫu

suy nghĩ giống con người hơn,

bằng cách phá vỡ vấn đề

xuống thành các bước.

Ý tôi là gì khi nghĩ

giống con người hơn?

Vâng, đây là

vấn đề ví dụ một lần

từ lời nhắc trên

slide trước đó.

Nhiệm vụ ở đây là tính toán

có bao nhiêu quả bóng tennis Roger

có sau khi mua một số cái mới.

Một cách mà

con người có thể giải quyết

vấn đề này là như sau.

Bắt đầu bằng việc xác định

số lượng

quả bóng tennis Roger

có lúc đầu.

Sau đó lưu ý rằng Roger mua

hai lon bóng tennis.

Mỗi hộp chứa ba quả bóng,

vậy anh ấy có tổng cộng

sáu quả bóng tennis mới.

Tiếp theo, thêm 6 cái mới này

quả bóng về 5 ban đầu,

tổng cộng là 11 quả bóng.

Sau đó kết thúc bằng

nêu câu trả lời.

Những chất trung gian này

dạng tính toán

các bước suy luận đó

một con người có thể lấy,

và trình tự đầy đủ

các bước minh họa

chuỗi suy nghĩ đã đi

vào việc giải quyết vấn đề.

Yêu cầu người mẫu bắt chước

hành vi này được gọi là

chuỗi suy nghĩ nhắc nhở.

Nó hoạt động bằng cách bao gồm

một loạt

trung gian

bước suy luận vào

bất kỳ ví dụ nào bạn sử dụng cho

suy luận một hoặc vài lần.

Bằng cách cấu trúc các

ví dụ theo cách này,

về cơ bản bạn

dạy người mẫu cách

lý do thông qua nhiệm vụ

để đạt được một giải pháp.

Đây là vấn đề tương tự về táo

bạn đã xem một vài slide trước đây,

bây giờ được làm lại thành một chuỗi

của suy nghĩ nhắc nhở.

Câu chuyện của Roger

mua bóng tennis

vẫn được sử dụng làm

ví dụ một lần.

Nhưng lần này bạn bao gồm

lý luận trung gian

các bước trong văn bản giải pháp.

Các bước này về cơ bản là

tương đương với những cái

một con người có thể lấy,

mà bạn vừa thấy

một vài phút trước.

Sau đó bạn gửi cái này

chuỗi suy nghĩ

nhắc nhở lớn

mô hình ngôn ngữ,

tạo ra sự hoàn thành.

Chú ý rằng mô hình

bây giờ đã sản xuất

mạnh mẽ hơn và

phản hồi minh bạch

điều đó giải thích nó

các bước suy luận,

theo cấu trúc tương tự

như ví dụ một lần.

Mô hình bây giờ đã chính xác

xác định rằng chín

còn lại những quả táo.

Suy nghĩ thông qua

vấn đề đã giúp

người mẫu đến

câu trả lời đúng.

Một điều cần lưu ý là

trong khi dấu nhắc đầu vào là

được trình bày ở đây một cách cô đọng

định dạng để tiết kiệm không gian,

toàn bộ lời nhắc thực sự là

được bao gồm trong đầu ra.

Bạn có thể sử dụng chuỗi suy nghĩ

nhắc nhở để giúp đỡ LLM

cải thiện lý luận của họ về

các loại vấn đề khác nữa,

bên cạnh phép tính.

Đây là một ví dụ về một

bài toán vật lý đơn giản,

người mẫu đang ở đâu

được yêu cầu xác định xem

một chiếc nhẫn vàng sẽ chìm xuống

đáy bể bơi.

Chuỗi suy nghĩ

bao gồm lời nhắc

như ví dụ một lần ở đây,

chỉ cho người mẫu cách

giải quyết vấn đề này,

bằng lý luận rằng

một cặp sẽ chảy

bởi vì nó ít hơn

đậm đặc hơn nước.

Khi bạn vượt qua điều này

nhắc tới LLM,

nó tạo ra một điều tương tự

hoàn thiện có cấu trúc.

Mô hình xác định chính xác

mật độ của vàng,

mà nó đã học được từ

dữ liệu đào tạo của nó,

và sau đó là lý do

rằng chiếc nhẫn sẽ

chìm vì vàng nhiều

đậm đặc hơn nước.

Chuỗi suy nghĩ nhắc nhở

là một kỹ thuật mạnh mẽ

cải thiện khả năng của

mô hình của bạn để lý do

thông qua các vấn đề.

Mặc dù điều này có thể cải thiện đáng kể

hiệu suất của mô hình của bạn,

kỹ năng toán học hạn chế

LLM vẫn có thể gây ra

vấn đề nếu nhiệm vụ của bạn yêu cầu

tính toán chính xác,

như tổng doanh số bán hàng trên

một trang web thương mại điện tử,

tính thuế, hoặc

áp dụng giảm giá.

Trong video tiếp theo,

bạn sẽ khám phá

một kỹ thuật có thể giúp

bạn khắc phục được vấn đề này

bằng cách để LLM của bạn nói chuyện với

một chương trình đó là

giỏi toán hơn nhiều.

Chúng ta hãy tiếp tục và xem xét.