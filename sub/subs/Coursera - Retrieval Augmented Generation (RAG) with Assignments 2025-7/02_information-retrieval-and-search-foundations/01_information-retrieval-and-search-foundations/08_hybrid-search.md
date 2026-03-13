# 08 kết hợp tìm kiếm

---

Đó là phần kết thúc chuyến tham quan của chúng tôi về các kỹ thuật tìm kiếm và lọc khác nhau được sử dụng bên trong

của một chú chó tha mồi.

Vì vậy, hãy xem cách chúng có thể được sử dụng cùng nhau như một phần của kỹ thuật tìm kiếm kết hợp

để tận dụng những thế mạnh khác nhau của họ.

Để bắt đầu, hãy xem lại cách hoạt động của từng kỹ thuật và những lợi ích chính của nó.

Lọc siêu dữ liệu sử dụng các tiêu chí cứng nhắc được lưu trữ trong siêu dữ liệu tài liệu để thu hẹp tìm kiếm

kết quả.

Nó nhanh chóng, dễ thực hiện và dễ diễn giải.

Bản thân nó có thể không phải là một kỹ thuật tìm kiếm tuyệt vời nhưng nó cung cấp một bộ lọc có-không nghiêm ngặt

mà cả hai cách tiếp cận khác đều không thể mang lại.

Điểm tìm kiếm từ khóa và xếp hạng tài liệu dựa trên việc có cùng từ khóa được tìm thấy trong

lời nhắc.

Tìm kiếm từ khóa vẫn khá nhanh và dễ thực hiện, thậm chí nó còn có thể thực hiện một cách xuất sắc

công việc tìm kiếm tài liệu liên quan.

Nó hoạt động đặc biệt tốt trong trường hợp lời nhắc và tài liệu chứa kỹ thuật

từ khóa hoặc tên sản phẩm, vì kết quả sẽ chứa những từ chính xác đó.

Tuy nhiên, tìm kiếm từ khóa phụ thuộc vào kết quả khớp chính xác và do đó không thể truy xuất tài liệu bằng

nghĩa giống nhau nhưng từ ngữ khác nhau.

Điểm tìm kiếm ngữ nghĩa và xếp hạng tài liệu dựa trên ý nghĩa tương tự với lời nhắc.

Tài liệu và lời nhắc được nhúng dưới dạng vectơ có vị trí trong không gian thể hiện ý nghĩa của chúng.

Việc tìm kiếm các tài liệu giống nhất với lời nhắc chỉ có nghĩa là bạn cần tìm tài liệu có

nhúng vectơ gần nhất với vectơ của lời nhắc.

Tìm kiếm ngữ nghĩa chậm hơn và tốn nhiều công sức tính toán hơn tìm kiếm từ khóa, nhưng nó cung cấp

tính linh hoạt mà không có kỹ thuật tìm kiếm nào khác có được.

Với cả ba cách tiếp cận đều có điểm mạnh tương đối, đây là cách chúng thường được áp dụng

được kết hợp thành một đường ống tìm kiếm kết hợp.

Đầu tiên, như mọi khi, người truy tìm sẽ nhận được lời nhắc.

Sau đó, trình truy xuất sẽ thực hiện cả tìm kiếm từ khóa và tìm kiếm ngữ nghĩa bằng cách sử dụng dấu nhắc đó.

Kết quả là hai danh sách tài liệu được xếp hạng, một danh sách được tính điểm và xếp hạng bằng từ khóa

tìm kiếm và một cách khác sử dụng tìm kiếm ngữ nghĩa.

Nếu bạn thích, hãy tưởng tượng mỗi kỹ thuật tìm kiếm trả về 50 tài liệu, với nhiều tài liệu

xuất hiện ở cả hai bảng xếp hạng, nhưng có lẽ theo thứ tự khác nhau.

Tiếp theo, cả hai danh sách này đều được lọc bằng bộ lọc siêu dữ liệu để xóa các tài liệu

không liên quan.

Ví dụ: bộ lọc có thể xóa các tài liệu không liên quan đến công việc của họ.

Trong ví dụ này, danh sách tìm kiếm từ khóa còn lại 35 tài liệu và ngữ nghĩa

chỉ tìm kiếm 30.

Bây giờ, hai danh sách xếp hạng này cần được kết hợp để tạo thành một bảng xếp hạng duy nhất.

Một thuật toán thường được sử dụng để kết hợp các thứ hạng này được gọi là hợp nhất thứ hạng đối ứng.

Thuật toán này thưởng cho các tài liệu được xếp hạng cao trong một trong hai danh sách, đồng thời cho phép

bạn có thể kiểm soát xem có nên tăng cường trọng số cho từ khóa hay xếp hạng theo ngữ nghĩa hay không.

Đây là công thức cho phản ứng tổng hợp thứ hạng đối ứng.

Các tài liệu ghi điểm dựa trên thứ hạng của chúng trong mỗi danh sách.

K là một siêu tham số, nhưng hiện tại, hãy giả vờ như nó bằng 0.

Trong trường hợp đó, mỗi tài liệu sẽ ghi điểm bằng tỷ lệ nghịch với thứ hạng của chúng.

Vì vậy, người đứng đầu được một điểm, người đứng thứ hai được nửa điểm, v.v.

Tài liệu lấy điểm từ mỗi danh sách xếp hạng và tổng điểm của chúng được sử dụng để tính toán

một thứ hạng cuối cùng.

Trong trường hợp chó tha mồi của bạn, đó chỉ là hai thứ hạng, thứ hạng từ khóa và ngữ nghĩa của chúng.

xếp hạng.

Nếu một tài liệu xuất hiện ở vị trí thứ hai trong một danh sách và thứ 10 trong một danh sách khác, nó sẽ được tính trên 1 điểm

2 hoặc nửa điểm tính từ xếp hạng đầu tiên và 1 trên 10 hoặc 0,1 điểm tính từ xếp hạng thứ hai,

với tổng số điểm là 0,6.

Những điểm số này sau đó được sử dụng để xếp hạng lại tất cả các tài liệu.

Hãy quay lại tham số K đó.

K được sử dụng để kiểm soát tác động của các tài liệu được xếp hạng cao nhất.

Khi K bằng 0, tài liệu được xếp hạng cao nhất trong bất kỳ danh sách nào sẽ ngay lập tức lên đầu

thứ hạng chung.

Even if it's only highly ranked once.

Ví dụ: tài liệu được xếp hạng cao nhất sẽ được 1 điểm và tài liệu được xếp hạng thứ 10 sẽ có điểm

1 phần mười.

Đó là sự khác biệt gấp 10 lần.

Tăng K lên khoảng 50 sẽ cân bằng mọi thứ.

Bây giờ, tài liệu được xếp hạng cao nhất đạt 1 trên 50 điểm và tài liệu được xếp hạng thứ 10 đạt điểm

1 trên 60, đây là một sự khác biệt khiêm tốn hơn nhiều về điểm số.

Nó vẫn trả tiền để được xếp hạng đầu tiên, nhưng không đến mức thống trị bảng xếp hạng

trên bất kỳ danh sách nào khác.

Lưu ý rằng RRF chỉ quan tâm đến thứ hạng của tài liệu trong mỗi danh sách chứ không quan tâm đến điểm số

đã dẫn tới những thứ hạng đó.

Ngay cả khi tài liệu được xếp hạng cao nhất đạt điểm cao hơn đáng kể so với tài liệu thứ hai, thì thông tin đó vẫn

không được xem xét.

Bên trong công cụ truy xuất, tìm kiếm kết hợp thường có siêu tham số thứ hai gọi là beta, siêu tham số này

cho phép bạn đánh giá thứ hạng được tạo ra bởi tìm kiếm ngữ nghĩa hoặc từ khóa.

Ví dụ: bạn có thể đặt beta thành 0,8, gán 80% tầm quan trọng hoặc trọng số cho thứ hạng

được cung cấp bởi tìm kiếm ngữ nghĩa và chỉ 20% vào thứ hạng được cung cấp bởi tìm kiếm từ khóa.

Tỷ lệ tìm kiếm theo từ khóa được chia theo tỷ lệ 70-30, 70% theo ngữ nghĩa, 30% theo từ khóa thường là điểm khởi đầu tốt và bạn

có thể điều chỉnh điều này cho hệ thống cụ thể của bạn để xem cái gì hoạt động tốt nhất.

Đối với các ứng dụng mà việc kết hợp từ chính xác thực sự quan trọng nhưng bạn muốn có một số ngữ nghĩa

sự giống nhau, bạn sẽ muốn đánh giá kết quả tìm kiếm từ khóa nhiều hơn ngữ nghĩa

kết quả tìm kiếm.

Trong các trường hợp khác khi sự tương đồng về ngữ nghĩa quan trọng hơn và từ khóa ít quan trọng hơn,

bạn sẽ muốn đánh giá kết quả tìm kiếm vectơ nhiều hơn kết quả tìm kiếm từ khóa.

Tại thời điểm này, chú chó tha mồi của bạn thực sự đã sẵn sàng trả lại kết quả.

Tùy thuộc vào số lượng tài liệu được yêu cầu ban đầu, thường được gọi là top K,

hầu hết các tài liệu K tương tự từ bảng xếp hạng kết hợp cuối cùng này đều được trả về bởi chó săn.

Tìm kiếm kết hợp cho phép người truy tìm tận dụng các lợi ích khác nhau của tìm kiếm từ khóa,

tìm kiếm ngữ nghĩa và lọc siêu dữ liệu cung cấp.

Tìm kiếm từ khóa cung cấp kết quả khớp từ chính xác, tìm kiếm ngữ nghĩa cho phép kết hợp từ khóa mờ hơn

dựa trên ý nghĩa và tính năng lọc siêu dữ liệu lọc tài liệu bằng các tiêu chí nghiêm ngặt.

Ngoài ra còn có nhiều cơ hội để thay đổi cách thức hoạt động của hệ thống hybrid này, cho dù đó là điều chỉnh

các tham số của thuật toán BM25, chọn siêu dữ liệu nào để lọc hoặc thay đổi

trọng số của từ khóa so với tìm kiếm ngữ nghĩa trong bước tổng hợp thứ hạng đối ứng.

Cách tiếp cận kết hợp này cho phép bạn phát huy điểm mạnh của từng cách tiếp cận và điều chỉnh hệ thống.

hiệu suất đối với dữ liệu trong cơ sở kiến thức của bạn hoặc nhu cầu của dự án tổng thể của bạn.

Tuy nhiên, để thực hiện việc điều chỉnh đó, bạn cần có cách đo lường hiệu quả hoạt động của chó săn,

vì vậy hãy cùng tôi xem video tiếp theo để xem chó tha mồi được đánh giá như thế nào.