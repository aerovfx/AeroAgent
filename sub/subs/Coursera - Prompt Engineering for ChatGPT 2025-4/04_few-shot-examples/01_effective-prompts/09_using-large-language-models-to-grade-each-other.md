# 09 sử dụng-ngôn-lớn-mô hình-để-chấm-nhau

---

Chúng ta sẽ phải đối mặt với

vấn đề với lời nhắc của,

bản thân các mô hình ngôn ngữ lớn

sẽ di chuyển rất nhanh,

họ sẽ liên tục phát triển.

Và chúng ta đã thấy điều đó, chúng ta đã thấy

ChatGPT và GPT-4, chúng tôi đã thấy LLaMA và

Alpaca, chúng tôi đã thấy Vicuna và rất nhiều

những cái khác nhau liên tục xuất hiện.

Và một trong những điều chúng tôi muốn biết là,

khi chúng tôi phát triển danh mục lời nhắc,

các mẫu của chúng tôi, chúng tôi đã bỏ ra rất nhiều công sức vào

phát triển các lời nhắc phù hợp với chúng ta,

làm cách nào để chúng tôi đánh giá chúng và đảm bảo

rằng chúng được duy trì theo thời gian?

Bởi vì nếu chúng ta thay đổi

mô hình ngôn ngữ lớn,

điều đó có nghĩa là tất cả của chúng ta

lời nhắc sẽ bị phá vỡ?

Hoặc nếu chúng ta thay đổi dữ liệu

chúng tôi đang làm việc một chút,

điều đó có ảnh hưởng gì đến chúng ta không?

Vì vậy chúng ta cần những cách tốt hơn để

giúp đánh giá đầu ra.

Bây giờ, tất nhiên, có một cách,

rằng chúng ta sẽ làm điều này,

là chúng ta sẽ có con người

nhìn vào đầu ra trong nhiều trường hợp.

Nhưng chúng tôi muốn làm những điều có thể

có thể giúp chúng tôi mở rộng quy mô tốt hơn,

thực sự có thể đi và làm những việc lớn

phân tích tự động quy mô theo một cách nào đó.

Vậy chúng ta sẽ thực hiện việc này như thế nào?

Chà, một trong những điều thực sự thú vị

những thứ có mô hình ngôn ngữ lớn là

chúng ta thực sự có thể sử dụng chúng

để đánh giá bản thân.

Đây có thể là một trong những đầu vào mà chúng tôi sử dụng

để giúp xác định mức độ tốt của lời nhắc của chúng tôi

và mức độ bảo trì của chúng trong một thời gian

đã đến lúc, chúng ta có thể sử dụng một mô hình ngôn ngữ lớn

để chấm điểm chính nó hoặc kết quả đầu ra

của một mô hình ngôn ngữ lớn khác.

Vì vậy, chúng ta đã thấy những ví dụ

về điều này nơi chúng tôi có,

họ thực sự đã lấy

mô hình ngôn ngữ lớn và

họ đã dạy một mô hình ngôn ngữ lớn

về cơ bản là một mô hình ngôn ngữ lớn khác.

Nhưng chúng ta có thể làm điều gì đó tương tự, trong đó

chúng ta có thể lấy kết quả đầu ra từ một ngôn ngữ lớn

làm mẫu và thực sự đưa chúng trở lại

vào chính mô hình đó để chấm điểm chúng.

Hoặc chúng ta thực sự có thể đi và lấy một cái khác

mô hình ngôn ngữ lớn mà chúng tôi đang làm việc

với và có kết quả đầu ra của nó được xếp loại bởi, cho

ví dụ, một mô hình ngôn ngữ lớn tốt hơn,

có thể với nhiều thông số hơn có thể,

càng mạnh mẽ hơn.

Vì vậy, hãy xem một ví dụ về điều này và

cách chúng tôi có thể xây dựng lời nhắc để thực hiện việc đó.

Vì vậy, trong ví dụ này, tôi sẽ

dạy mô hình ngôn ngữ lớn,

trong trường hợp này là ChatGPT,

cách chấm điểm đầu ra của lời nhắc.

Tôi thực sự sẽ không cho nó xem

nhắc trong ví dụ của tôi, tôi sẽ chỉ

dạy nó quá trình chấm điểm, vì vậy

rằng nó có thể giúp tự động hóa nó cho tôi.

Và thế là

Tôi sẽ sử dụng một vài ví dụ ngắn.

Vì vậy, như đầu vào ở trên cùng,

Tôi đang nói, đây là ý kiến của tôi, và

đó là một chút văn bản về

Đại học Vanderbilt từ Wikipedia.

Nó xác định rằng Đại học Vanderbilt

được thành lập vào năm 1873.

Và tôi giải thích, đây là kết quả.

Đầu ra là, sau đây là danh sách

về các sự kiện, ngày tháng và kết quả,

Vanderbilt được thành lập vào năm 1873.

Và sau đó, lời giải thích là

đầu ra có văn bản không mong muốn khi bắt đầu và

chỉ nên bao gồm tên và ngày tháng.

Và thế là

Tôi cho nó điểm năm trên mười.

Vì vậy, đây là đầu ra được sản xuất.

Và sau đó tôi sẽ đưa ra lời giải thích mang tính con người

đầu ra có vấn đề gì,

tại sao nó không đạt được điểm tuyệt đối.

Sau đó tôi sẽ chấm điểm nó và

cho nó điểm năm trên mười.

Vì vậy tôi sẽ trải qua và

Tôi đang làm một vài trong số này bởi

đưa tay chỉ cho nó thấy điều tôi muốn.

Và sau đó tôi sẽ đưa ra một ví dụ khác

với cùng một đoạn văn bản.

Tôi đang nói đầu ra chỉ là 1873,

và ý nghĩa của việc này là,

nếu bây giờ bạn có thể cảm nhận được nó,

là tôi muốn một lời nhắc đang diễn ra

để trích xuất các sự kiện và

ngày mà các sự kiện diễn ra.

Và thế là xong, tôi muốn có một sự kiện

tên được phân tách bằng dấu phẩy và

sau đó là ngày của sự kiện đó.

Tôi không muốn bất kỳ văn bản nào khác,

Tôi không muốn một lời giải thích,

Tôi chỉ muốn tên các sự kiện và ngày tháng,

và tôi đang trình bày cách ChatGPT có thể

chấm điểm đầu ra để xem liệu

nó phù hợp với định dạng đó.

Tôi thậm chí còn không hiển thị lời nhắc

là, tôi không cho nó biết nhiệm vụ là gì,

Tôi đang đưa ra ví dụ để giúp bạn học hỏi.

Và sau đó tôi nói, giải thích, kết quả

đang thiếu thông tin quan trọng về

sự kiện đã xảy ra

vào ngày nhất định đó.

Và tôi cho nó điểm ba trên mười.

Và sau đó tôi có thêm một cái nữa với đầu vào,

cái đó giống nhau

đoạn văn về Vanderbilt.

Tôi cho xem dấu phẩy của Đại học Vanderbilt 1873,

đó là đầu ra lý tưởng cho

nhiệm vụ hư cấu của tôi.

Và sau đó tôi giải thích rằng

đầu ra chính xác.

Và sau đó tôi thực sự đã cắt nó đi,

vì có lỗi đánh máy ở đây.

Nó thực sự phải được đáp ứng

những kỳ vọng hay điều gì đó tương tự.

Và sau đó tôi cho điểm

của mười trên mười.

Điều thú vị là điều này thậm chí không

vấn đề là tôi đã phạm sai lầm ở đây trong

giải thích, bởi vì nó vẫn hoạt động.

Và thế là tôi đưa nó

một đầu vào hoàn toàn khác.

Tôi nói, đây là một đầu vào khác.

Một lần nữa, đó là về Vanderbilt,

và lịch sử của chương trình tiếng Anh

tại Vanderbilt trong văn bản sáng tạo.

Và vì vậy tôi cung cấp cho nó đầu vào này.

Một đoạn văn bản khác về điều đó, tôi nói

đầu ra là gì, và tôi cho nó biết đầu ra là gì

là những kẻ chạy trốn và những người nông dân miền Nam,

nửa đầu thế kỷ 20 và

thì Vanderbilt là thành viên sáng lập

của hội nghị Đông Nam, 1966.

Và về cơ bản đó là lời nhắc nhở cho

ChatGPT sau đó tiến hành chấm điểm đầu ra đó.

Và do đó nó cung cấp

một lời giải thích về đầu ra.

Nó thực sự đề cập đến một cái gì đó

rằng tôi đã không chấm điểm ở đó.

Nhưng điều thú vị là nó nói

có cách viết hoa không nhất quán,

và sau đó nó mang lại cho nó

điểm chín trên mười.

Vì vậy, với tư cách là một người dán nhãn và một con người

thực hiện nhiệm vụ này, tôi thực sự đã kết thúc

với điểm chín trên mười bởi vì lúc đó tôi

không nhất quán về cách viết hoa.

Nhưng bạn có thể thấy nó đã làm rất tốt.

Nó lấy loại chất

về những gì tôi muốn, và

nó thực hiện việc chấm điểm

nhiệm vụ mà tôi đã giao cho nó.

Và vì vậy, chúng ta thực sự có thể sử dụng ngôn ngữ lớn

mô hình để đánh giá đầu ra của lời nhắc.

Hiện nay có nhiều cách

bạn có khả năng có thể sử dụng điều này.

Một là, nếu bạn có một hệ thống nào đó

sẽ đi và đưa ra quyết định hoặc

tạo ra thông tin với số lượng lớn

mô hình ngôn ngữ như ChatGPT hoặc

một số mô hình khác mà bạn đang chạy,

bạn có thể muốn kiểm tra mô hình

chính nó hoặc mô hình khác tự kiểm tra.

Hoặc bạn có thể muốn làm điều này nhiều lần

lần, nơi bạn lấy đầu ra

bạn đang nhận được và bạn cho điểm nó

tiêu chí tương tự như những gì tôi đã làm ở đây.

Và bạn đã phát triển một lời nhắc với

tiêu chí chấm điểm, bạn có thể có

nhiều lời nhắc về tiêu chí chấm điểm,

và tất cả các bạn đều yêu cầu họ chấm điểm đầu ra.

Và sau đó, nếu điểm số thấp hơn một số

ngưỡng, à, có lẽ bạn muốn có

cái nhìn của con người về kết quả đầu ra đó, hoặc

có lẽ bạn chỉ muốn thử lại và

xem liệu bạn có thể nhận được gì không

tốt hơn nên được sản xuất.

Và như vậy,

điều này cung cấp cho bạn một loại công cụ bổ sung,

làm thế nào để chúng ta đi và đánh giá những gì

sắp ra mắt, hãy chắc chắn rằng nó trông đẹp,

và vẫn có sức mạnh và

sự phức tạp của các mô hình này.

Và đây là một cách để làm điều đó.

Hiện nay có rất nhiều cách

bạn có thể diễn đạt lời nhắc.

Bạn có thể muốn đi và

xem xét các phương pháp thay thế

mẫu để phát triển một số cách khác nhau.

Đây là một ví dụ sử dụng

vài ví dụ ngắn.

Và tôi có thể quay lại và

nói, chúng ta có thể nói hành động và

sử dụng mô hình tính cách,

hành động như một nhà phê bình nhanh chóng.

Thực hiện một, đưa ra kết quả

Tôi cho bạn điểm về mặt

nó phù hợp với mong đợi như thế nào

của người thiết kế nhanh chóng.

Tôi sẽ đưa cho bạn

ví dụ về gợi ý chấm điểm.

Và vì vậy chúng ta có thể đã đi và

đã làm điều gì đó như thế

Tôi đã thực hiện một lời nhắc tương đối đơn giản, nhưng

chúng ta có thể làm một việc phức tạp hơn nhiều

nhắc bằng cách sử dụng một số mẫu khác.

Một lần nữa, nó sẽ

tạo ra lời giải thích.

Và rồi ở phần cuối của nó,

nó cũng sẽ tạo ra một điểm cho nó.

Và vì vậy nó sẽ đi qua và

cho chúng tôi điểm tám trên mười.

Vì vậy, bạn nhận thấy chúng tôi có tám trên mười một

hiện tại, chúng tôi đã thay đổi lời nhắc một chút,

chúng tôi có chín trên mười.

Dù sao đi nữa, có vẻ như đó là một điều đẹp đẽ

kết quả đầu ra tốt dựa trên tiêu chí chấm điểm của chúng tôi

và những gì chúng tôi muốn.

Và vì vậy chúng ta có thể sử dụng loại này

công cụ trong hộp công cụ của chúng tôi.

Khi chúng ta cần đánh giá một lời nhắc và

đầu ra của lời nhắc,

chúng ta không cần phải luôn lùi lại

để con người nhìn vào nó.

Một điều chúng ta có thể làm là,

chúng ta có thể quay trở lại với việc có số lượng lớn

mô hình ngôn ngữ tự đánh giá đầu ra.

Và sau đó chúng ta có thể xây dựng những thứ khác nhau

các loại tự động hóa xung quanh đó, hoặc

chúng ta có thể sử dụng nó như một công cụ kích hoạt

để leo thang thành một con người.

Bây giờ, tất nhiên, nếu chúng ta có nhiều

những ví dụ thực sự hay về việc chấm điểm,

điều đó giúp chúng tôi rất nhiều.

Nhưng chúng ta không cần phải có nhiều.

Nếu bạn thấy trong ví dụ của tôi, tôi vừa

ba ví dụ về phân loại đầu ra và

nó đã làm rất tốt

tìm ra những gì tôi muốn.