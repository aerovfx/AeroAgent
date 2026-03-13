# 07 bộ mã hóa chéo và colbert

---

Các kỹ thuật tìm kiếm ngữ nghĩa mà bạn đã thấy cho đến nay đều sử dụng kiến ​​trúc cơ bản.

Mỗi tài liệu và lời nhắc được gán một vectơ duy nhất được so sánh để tìm tài liệu hoặc

các đoạn tương tự như lời nhắc. Mặc dù phương pháp này mang lại kết quả tuyệt vời,

thậm chí có thể truy xuất chất lượng cao hơn với các kiến trúc phức tạp hơn.

Chúng ta hãy xem xét hai trong số đó, bộ mã hóa chéo và Colbert, đồng thời xem xét ưu và nhược điểm của chúng.

Kiến trúc bạn đã thấy trong suốt khóa học này để hỗ trợ tìm kiếm ngữ nghĩa

được gọi là bộ mã hóa kép. Mỗi tài liệu được gán một vectơ ngữ nghĩa bằng mô hình nhúng.

Khi nhận được lời nhắc, nó cũng được nhúng vào một vectơ. Sau đó, một khoảng gần nhất

Thuật toán của hàng xóm được cơ sở dữ liệu vectơ sử dụng để xác định nhanh chóng các tài liệu

có vectơ gần với vectơ gợi ý. Thuật ngữ bộ mã hóa kép đề cập đến thực tế là

tài liệu và lời nhắc được nhúng riêng biệt. Điều này rất quan trọng vì nó có nghĩa là tất cả các tài liệu

có thể được nhúng trước và chỉ lời nhắc cần được nhúng sau khi nhận được,

tăng tốc đáng kể việc tìm kiếm. Tuy nhiên, nếu bạn sẵn sàng từ bỏ một phần tốc độ,

bạn có thể nhận được kết quả tìm kiếm chất lượng cao hơn nữa. Hãy bắt đầu với bộ mã hóa chéo có thể

cung cấp thứ hạng tài liệu chất lượng cao hơn đáng kể so với bộ mã hóa kép. Để chấm điểm một tài liệu,

một bộ mã hóa chéo nối tài liệu với dấu nhắc và sau đó chuyển văn bản kết hợp

về cơ bản là một mô hình nhúng chuyên dụng. Vì cả lời nhắc và tài liệu đều ở

đầu vào, điều này cho phép mô hình hiểu được các tương tác theo ngữ cảnh sâu sắc giữa lời nhắc

và ghi lại văn bản mà bộ mã hóa kép có thể bỏ sót. Bộ mã hóa chéo được thiết kế để trực tiếp

đưa ra điểm liên quan, thường là một số từ 0 đến 1. Bạn có thể coi điểm này là điểm

xác suất trùng khớp tích cực giữa lời nhắc và tài liệu. Đây là một bộ mã hóa chéo đang hoạt động.

Giả sử bạn có ba tài liệu trong cơ sở kiến thức và bạn nhận được lời nhắc,

những địa điểm ăn uống tuyệt vời ở New York. Bộ mã hóa chéo nối dấu nhắc vào phía trước mỗi dấu nhắc

tài liệu. Sau đó, mỗi cặp tài liệu nhắc sẽ được chuyển qua bộ mã hóa chéo để tạo ra một

xác suất trùng khớp giữa lời nhắc và tài liệu. Nếu đây là một bộ mã hóa chéo được đào tạo tốt,

bạn sẽ mong đợi tài liệu đầu tiên đạt điểm khá cao, chẳng hạn như 0,7 hoặc 70 phần trăm. Kể từ khi

tài liệu khá phù hợp với lời nhắc, sau đó bạn lặp lại quy trình này cho từng tài liệu

nối lời nhắc vào phía trước, chuyển cặp tài liệu lời nhắc thông qua bộ mã hóa chéo

kiến trúc và tạo ra một điểm số. Bộ mã hóa chéo hầu như sẽ luôn cung cấp khả năng tìm kiếm tốt hơn

kết quả khi so sánh với bộ mã hóa kép, được đo bằng các số liệu phổ biến như mức độ liên quan của tìm kiếm.

Vấn đề chính với các bộ mã hóa chéo là chúng có quy mô rất lớn. Cơ sở kiến thức của bạn có thể dễ dàng

có hàng triệu hoặc có thể là hàng tỷ tài liệu, nghĩa là với mỗi lời nhắc bạn cần phải

chạy hàng tỷ cặp dấu nhắc tài liệu thông qua bộ mã hóa chéo để tạo ra mỗi tài liệu

điểm số liên quan. Bạn cũng không thể thực hiện bất kỳ quá trình xử lý trước nào để tăng tốc mọi thứ vì các bộ mã hóa chéo chạy trên một

cặp tài liệu nhắc và bạn sẽ không có lời nhắc cho đến khi người dùng gửi nó. Bộ mã hóa chéo cũng vậy

không hiệu quả khi sử dụng làm kỹ thuật tìm kiếm mặc định, nhưng chất lượng của kết quả khiến chúng trở thành một công cụ tuyệt vời

công cụ để cải thiện kết quả của các kỹ thuật tìm kiếm khác, thứ mà bạn sẽ khám phá sau

trong khóa học này. Một số kỹ thuật cố gắng phân chia sự khác biệt giữa tốc độ của bộ mã hóa kép và

chất lượng của bộ mã hóa chéo. Vì vậy, hãy xem xét một kiến trúc cuối cùng đang trở nên phổ biến được gọi là

COBEAR. COBEAR là viết tắt của tương tác muộn theo ngữ cảnh qua BERT. Ý tưởng của COBEAR là

bạn vẫn tạo trước các vectơ tài liệu, giống như trong bộ mã hóa hai chiều, nhưng hãy cố gắng nắm bắt sâu hơn

tương tác giữa văn bản của lời nhắc và từng tài liệu, như bộ mã hóa chéo. Để bắt đầu, mỗi

Tài liệu trong cơ sở tri thức được nhúng nhưng thay vì tạo ra một vectơ ngữ nghĩa cho

toàn bộ tài liệu, bạn tạo một vectơ ngữ nghĩa cho mỗi mã thông báo trong tài liệu. Một tài liệu với

do đó một nghìn mã thông báo cần được chuyển đổi thành một nghìn vectơ dày đặc. Khi có lời nhắc xuất hiện,

nó được nhúng theo cách tương tự, tạo ra một vectơ dày đặc cho mỗi mã thông báo trong dấu nhắc. Bây giờ,

Ý tưởng đằng sau việc tính điểm trong COBEAR là mỗi mã thông báo trong lời nhắc sẽ cố gắng tìm ra điểm giống nhất của nó

mã thông báo trong tài liệu. Hãy xem một ví dụ để xem nó hoạt động như thế nào. Hãy sử dụng bốn tài liệu giống nhau

và lời nhắc từ trước, Những địa điểm ăn uống tuyệt vời ở New York, đồng thời xem tài liệu đầu tiên được chấm điểm như thế nào.

Đầu tiên, thuật toán tìm khoảng cách vectơ hay nói cách khác là điểm tương đồng giữa mỗi vectơ

cặp mã thông báo từ tài liệu và lời nhắc. Nếu lời nhắc có 10 thẻ và tài liệu có

một trăm, kết quả là một lưới gồm một nghìn cặp điểm tương đồng. Điều này tạo ra một lưới

về mức độ liên quan của từng mã thông báo tài liệu với mã thông báo nhắc nhở. Ví dụ: các token New và York từ

lời nhắc sẽ rất khớp với New York và City trong tài liệu, trong khi Eat sẽ khớp với

thuận lợi với Ẩm thực. Mỗi mã thông báo lời nhắc sẽ có mã thông báo tài liệu có giá trị cao nhất

điểm số liên quan. Những điểm tối đa này được cộng lại để có được một điểm phù hợp cho tổng thể

tài liệu. Đây được gọi là điểm sim tối đa. Lặp lại quá trình này cho mọi tài liệu trong

Cơ sở tri thức cho phép chấm điểm tất cả các tài liệu và truy xuất các tài liệu phù hợp nhất.

Colbert cung cấp cả khả năng mở rộng của bộ mã hóa kép và phần lớn khả năng tương tác phong phú

giữa lời nhắc và tài liệu được tìm thấy trong bộ mã hóa chéo. Trong khi yêu cầu tính toán

để chấm điểm cho mỗi cặp dấu nhắc tài liệu đòi hỏi tính toán nhiều hơn so với bộ mã hóa hai chiều,

nó vẫn khá nhanh và có thể sử dụng trong bối cảnh thời gian thực hoặc gần với thời gian thực

tìm kiếm là cần thiết. Hạn chế lớn nhất của kiến trúc Colbert là số lượng vectơ

bạn cần lưu trữ mức tăng tương ứng với số mã thông báo trong cả lời nhắc và tài liệu.

Nếu bạn có tài liệu 2000 mã thông báo, bạn sẽ cần lưu trữ 2000 vectơ. Trong bộ mã hóa kép,

bạn chỉ cần lưu trữ một vectơ dày đặc duy nhất. Mô hình bộ mã hóa kép tiêu chuẩn cung cấp một cách hợp lý

chất lượng tốt, tốc độ cao và yêu cầu không gian lưu trữ vector tối thiểu. Tập thuộc tính này

biến nó thành kiến trúc mặc định cho tìm kiếm ngữ nghĩa. Bộ mã hóa chéo cung cấp tiêu chuẩn vàng

khi nói đến chất lượng tìm kiếm, nhưng chúng chậm đến mức không thể sử dụng chúng làm mặc định

kỹ thuật tìm kiếm. Colbert cung cấp chất lượng gần như của một bộ mã hóa chéo, nhưng ở tốc độ cao hơn nhiều.

gần hơn với một bộ mã hóa kép. Và cái giá phải trả của sự đánh đổi này là nó yêu cầu lưu trữ các lệnh

dữ liệu vector có độ lớn lớn hơn. Cơ sở dữ liệu vectơ ngày càng hỗ trợ Colbert

hoặc các cách tiếp cận tương tự, đặc biệt đối với các dự án đòi hỏi độ chính xác và bối cảnh sâu sắc.

sự hiểu biết. Ví dụ, trong lĩnh vực pháp lý hoặc y tế, sự đánh đổi đáng kể

việc tăng dấu chân bộ nhớ lưu trữ vector cho chất lượng tìm kiếm có thể đáng giá. Bộ mã hóa chéo

quá tốn kém về mặt tính toán để có thể sử dụng riêng cho việc tìm kiếm, nhưng may mắn là chúng không cần

được. Hãy cùng tôi xem video tiếp theo và xem cách tích hợp các bộ mã hóa chéo vào sản xuất

hệ thống truy xuất mặc dù chúng kém hiệu quả đáng kể.