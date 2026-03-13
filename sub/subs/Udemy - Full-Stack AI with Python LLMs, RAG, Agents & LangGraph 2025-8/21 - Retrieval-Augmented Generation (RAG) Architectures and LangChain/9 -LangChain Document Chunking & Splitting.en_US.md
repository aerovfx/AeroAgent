# 9 -LangChain Chunking & Splitting.en US

---

Được rồi các bạn, vậy nên trong trường hợp đặc biệt này

video, hãy xem chúng ta có thể làm thế nào

thực hiện phân đoạn thông minh với LangChain.

Vì vậy tôi sẽ chỉ tìm kiếm LangChain.

Xem lại bộ chia văn bản LangChain.

Được rồi, nếu tôi tìm kiếm ở đây, bạn

có thể thấy rằng bạn có một cái gì đó

được gọi là bộ chia tài liệu.

Hoặc bạn có thể nói bộ chia văn bản.

Nếu bạn đọc cái này.

Việc chia nhỏ tài liệu thường

một bước xử lý trước quan trọng

cho nhiều ứng dụng.

Nó liên quan đến việc phá vỡ

văn bản lớn thành nhỏ hơn.

Phải?

Vì vậy, về cơ bản bạn có

một tài liệu, bạn muốn chia nó

vào các đoạn văn.

Vậy làm thế nào bạn có thể làm điều đó?

Nếu chúng tôi cuộn xuống, bạn có thể thấy chúng tôi

chỉ có thể sử dụng văn bản ký tự

bộ chia hoặc thậm chí bạn có một cái gì đó

được gọi là bộ chia văn bản đệ quy.

Được rồi, vậy là có một cái.

Vậy làm thế nào chúng ta có thể làm điều này?

Trước hết, xem nào, chúng ta cần làm pip,

cài đặt bộ chia văn bản LangChain.

Vì vậy, nó là một gói khác.

Vì vậy, hãy để tôi mở tích hợp của tôi

terminal, nhấn lệnh và nhập.

Sau đó pip, đóng băng theo yêu cầu.

Nhắn tin.

Vì vậy, bây giờ tôi có nó.

Vậy bây giờ điều tôi sắp làm,

Tôi chỉ định nói rằng này anh bạn,

từ chuỗi lang, được rồi,

từ chuỗi lang, bộ chia văn bản.

Tôi cần nhập đệ quy

bộ chia ký tự.

Thực sự, thực sự, thực sự tốt đẹp.

Bây giờ tôi chỉ cần, tôi sẽ chỉ

thêm một bình luận chia rẽ

những con chó thành những khối nhỏ hơn.

Được rồi, những phần nhỏ hơn.

Vậy điều chúng ta cần làm là tôi sẽ

chỉ cần nói tôi sẽ tạo

một ví dụ về bộ chia văn bản ở đây.

Vì vậy tôi sẽ chỉ nói văn bản

bạn biết đấy, bộ chia.

Được rồi, đây là của tôi

bộ chia văn bản đệ quy.

Chúng tôi chỉ có thể cung cấp cho nó một kích thước chunk.

Vì vậy tôi sẽ chỉ nói tại sao nó không

dù sao cũng khuyên tôi điều gì đó, vì vậy

Tôi sẽ chỉ nói kích thước chunk là 1000.

Vấn đề bây giờ là thế này.

Bạn thậm chí có thể đưa ra một cái gì đó

được gọi là sự chồng chéo.

Bây giờ sự chồng chéo này là gì?

Xem sự chồng chéo này thực sự là

điều thú vị.

Hãy để chúng tôi nói rằng bạn có

một đoạn văn, bạn có cái này

đoạn văn, bạn có đoạn này

và bạn có đoạn này.

Bây giờ về mặt kỹ thuật nếu tôi chỉ đọc cái này

đoạn văn và sau đó tôi đọc nó

đoạn văn và sau đó tôi đọc nó

đoạn văn, vấn đề là, bạn biết đấy,

Tôi mất bối cảnh vì về mặt kỹ thuật

có một số thông tin quan trọng

đây, đây là một số điều quan trọng

thông tin ở đây

Nhưng bạn không thể chỉ đọc một

đoạn văn và, và bạn biết đấy, mong đợi

rằng nó sẽ hiểu mọi thứ.

Vì vậy, về cơ bản những gì chúng tôi làm là nếu

Tôi lấy cái này, đây là lần đầu tiên của tôi

đoạn, nhưng ở đoạn thứ hai tôi

sẽ lấy một phần nhỏ từ

đoạn trước và toàn bộ đoạn này

khúc.

Điều này về cơ bản giúp tôi

để hiểu được nền tảng,

có một chút chồng chéo.

Tương tự, đoạn tiếp theo sẽ là đoạn này.

Vì vậy sự chồng chéo giúp tôi hiểu

một chút tóm tắt

từ đoạn trước.

Vì vậy, tôi đang cho nó một đoạn chồng lên nhau.

Bây giờ, khi bạn có bộ chia văn bản này

sẵn sàng, những gì bạn có thể làm, bạn có thể

về cơ bản chỉ cần nói thế thôi, này, Mr.

Bộ tách văn bản, bạn có thể vui lòng

chia tài liệu cho tôi?

Nó sẽ nói, chắc chắn rồi.

Vì vậy, bạn chỉ có thể chuyển tài liệu

dưới dạng tài liệu, và đổi lại, cái này

sẽ cung cấp cho bạn các khối.

Chúc mừng các bác nhé

bạn đã thực hiện xong việc phân chia của mình.

Vì vậy, khối này sẽ là khối nhỏ hơn

có kích thước 1000 với độ chồng chéo 400.

Vì vậy, chỉ với hai dòng, bây giờ

bạn đã chuyển đổi các trang của mình

thành các phần có thể quản lý được.

Bây giờ, bước tiếp theo là gì?

Bước tiếp theo thực sự là tạo ra

nhúng vector từ đoạn này.

Một lần nữa, bạn có thể làm điều đó một cách thủ công,

nhưng một lần nữa, LangChain mang lại cho bạn,

một công cụ cho việc đó.

Để chúng ta sắp thấy

trong bài giảng tiếp theo.