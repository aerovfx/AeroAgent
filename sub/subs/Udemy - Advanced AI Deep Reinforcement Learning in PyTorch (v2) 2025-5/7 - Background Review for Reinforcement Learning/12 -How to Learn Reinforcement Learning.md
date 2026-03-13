# 12 -Cách học Học tăng cường được dịch

---

Để kết thúc và tóm tắt phần này, tôi muốn thảo luận ở mức độ cao hơn về những gì cần phải học

tại việc học tăng cường thực sự.

Cá nhân tôi nghĩ sẽ khá khó để nắm bắt và hiểu được việc học tăng cường

nó ở mức độ trừu tượng chỉ từ một phần duy nhất của một khóa học.

Hãy bắt đầu bằng cách nhận ra rằng học tăng cường rất khác với học có giám sát.

và học tập không giám sát.

Ngày nay, khi bạn đang học học có giám sát và không giám sát, nhiều khóa học dành cho người mới bắt đầu

áp dụng phương pháp né tránh cách thực hiện các mô hình.

Đây không phải là một cách tiếp cận tốt vì nó không giúp bạn hiểu được máy thật.

học tập.

Giả sử cấu trúc của các khóa học như thế này.

Trước tiên, bạn thảo luận về trực giác đằng sau cách thức hoạt động của mô hình, chỉ một số hình ảnh và

một số ý tưởng mô tả.

Sau đó, bạn tìm hiểu cách sử dụng mô hình đó trong scikit-learn, không bao gồm việc tải dữ liệu hoặc

đang nhìn vào kết quả.

Vậy vấn đề với cách tiếp cận này là gì?

Chà, nó không chỉ khiến bạn mắc nhiều sai lầm và còn có những hiểu lầm nghiêm trọng về

nội dung, nhưng có lẽ vấn đề lớn nhất với phương pháp này là bạn sẽ không bao giờ

biết những hiểu lầm đó là gì.

Nói cách khác, bạn đang ở một nơi mà bạn không biết những gì bạn không biết.

Bạn không biết lỗi lầm của mình và do đó bạn không thể sửa chữa chúng.

Bạn tự tin rằng mình đã học được điều gì đó, nhưng đây chẳng qua là sự thiếu hiểu biết đầy may mắn.

Và một lần nữa, đây chỉ là những quan sát của tôi về các học sinh khác, vì vậy đừng coi đó là vấn đề cá nhân.

sự phán xét của bạn.

Đây không phải là vấn đề quá lớn nếu đó là mức độ bạn muốn đi.

Nếu bạn chỉ có ý định sử dụng API và không bao giờ muốn trở thành một chuyên gia thực sự,

điều đó hoàn toàn ổn, không ai phán xét bạn cả.

Nhưng nó sẽ trở thành vấn đề khi đến lúc ngừng sử dụng API.

Bước ngoặt này xuất hiện khi bạn muốn học cách học tăng cường.

Không có API cho việc học tăng cường, ít nhất là chưa.

Vậy người ta làm gì?

Vâng, bạn phải tự mình thực hiện các thuật toán đó.

Vấn đề là nếu bạn không có kinh nghiệm triển khai các thuật toán học máy, việc củng cố

học tập không phải là nơi tốt để bắt đầu.

Tôi cũng muốn bình luận về nhiều blog, hướng dẫn, v.v. hiện có trên mạng

đang cố gắng dạy bạn về học tăng cường.

Hãy xem chúng ta đã mất bao lâu trong phần này để chuyển từ con số không sang học Q với tốc độ

Tôi sẽ xem xét càng nhanh càng tốt.

Hãy so sánh điều đó với độ dài của một hướng dẫn blog thông thường.

Cần phải rõ ràng rằng một bài đăng blog ngắn sẽ không thể có đủ chi tiết

để đưa bạn đến mức mà bạn thực sự có thể tự mình thực hiện việc học tăng cường.

Lời khuyên tốt nhất tôi có thể đưa ra cho bạn nếu bạn thực sự muốn học tăng cường là

cái này.

Tôi khuyên bạn nên tham gia một khóa học đầy đủ hoặc nhiều khóa học về học tăng cường.

Tìm hiểu về học tăng cường dạng bảng cơ bản trước khi bạn chuyển sang các phương pháp gần đúng.

Điều đó sẽ làm cho việc hiểu các khái niệm dễ dàng hơn nhiều.

Trong phần này chúng ta dành phần lớn thời gian để thảo luận về các khái niệm với giả định rằng

chúng tôi đang sử dụng bảng Q chứ không phải mạng nơ-ron.

Bạn muốn tìm hiểu về các phương pháp cơ bản để học tăng cường, có thể được phân loại

số một, các phương pháp quy hoạch động, số hai, các phương pháp Monte Carlo, và số

ba, các phương pháp khác biệt về thời gian và đảm bảo dành thời gian cho việc thực hiện.

Sau đó, chuyển sang các phương pháp xấp xỉ với mô hình tuyến tính.

Khi bạn đã hoàn thành việc đó và bạn đã triển khai các thuật toán học tăng cường với tuyến tính

mô hình, hãy chuyển sang sử dụng học sâu để xấp xỉ hàm.

Tại thời điểm này, bạn sẽ rất thoải mái với các khái niệm, nhưng việc thực hiện vẫn còn khó khăn.

một vấn đề khác hoàn toàn

Không giống như học có giám sát, học tăng cường rất khó thực hiện đúng, ngay cả khi bạn

là một lập trình viên chuyên nghiệp.

Rất dễ đưa ra các lỗi tinh vi khó hoặc gần như không thể theo dõi

xuống.

Và tất nhiên bạn không cần phải tin lời tôi.

Đây là bài đăng của Andre Carpathi, có lẽ là một trong những phương pháp học tăng cường nổi tiếng nhất

các nhà nghiên cứu nói về mức độ khó khăn của nó.

Trong nhận xét này, một người dùng khác nói về việc họ đã dành cả năm để cố gắng đạt được

Q học cách làm việc với mạng lưới thần kinh để đạt được một lợi ích cụ thể.

Nhiều sinh viên tham gia khóa học của tôi cảm thấy thất vọng khi một bài tập kéo dài hơn vài phút.

Bây giờ tôi đang nói về việc bạn đang làm việc gì đó trong một năm.

Andre trả lời nhận xét này và nói rằng tôi đã mất sáu tuần để nhận được mức độ chính sách

đang làm việc.

Và hãy nhớ rằng, anh ấy là một trong những nhà nghiên cứu hàng đầu thế giới về học tăng cường.

Anh ấy có tất cả công nghệ hiện đại mà anh ấy cần theo yêu cầu và được bao quanh bởi

những nhà nghiên cứu khác cũng thông minh như anh ấy nên anh ấy có thể xin họ lời khuyên hoặc kiểm tra

mã của anh ấy bất cứ lúc nào.

Vì vậy, ý tưởng chính mà tôi muốn bạn ghi nhớ là, khi bạn học học tăng cường,

nhận ra rằng việc thực hiện là rất không hề đơn giản, ngay cả đối với các chuyên gia.

Bạn nên dành nhiều thời gian và công sức để cố gắng làm mọi việc đúng đắn.