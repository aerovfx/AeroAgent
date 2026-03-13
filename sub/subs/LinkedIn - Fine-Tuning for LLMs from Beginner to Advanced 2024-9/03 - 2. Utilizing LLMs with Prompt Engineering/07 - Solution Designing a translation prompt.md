# 07 - Giải pháp Thiết kế lời nhắc dịch thuật

---

(nhạc sôi động)

- [Giảng viên] Vậy thử thách đó thế nào?

Bạn có thích nó không?

Hãy nhớ rằng nếu bạn không thể đi đến cuối cùng,

điều đó rất ổn vì điều quan trọng là phải nhận xét

rằng đó là một thử thách lâu dài

và một số bước, bạn sẽ thấy

rằng họ sẽ lặp lại chính mình trong suốt khóa học.

Vì vậy, khi bạn trải qua khóa học,

bạn sẽ quen dần với nó.

Để sau này bạn có thể quay lại và hoàn thành thử thách.

Ở đây tôi sẽ chỉ ra một giải pháp cho vấn đề.

Đó không phải là giải pháp, đó là một giải pháp.

Có nhiều giải pháp trong AI.

Vì vậy, trước tiên hãy kết nối qua GPU.

Chúng ta đã xong và hãy tiến hành cài đặt pip.

Nó đây rồi.

Hoàn hảo.

Bây giờ, điều chúng ta sắp làm, một lần nữa, như mọi khi,

chúng ta sẽ tải xuống mô hình.

Thế đấy.

Hoàn hảo.

Nhân tiện, trong trường hợp bạn không thích GPU mạnh mẽ,

bạn luôn có thể thay đổi lớn thành nhỏ

để có được phiên bản nhỏ hơn của FLAN-T5

và nó sẽ hoạt động thôi, được chứ?

Điều đó luôn luôn quan trọng.

Vì vậy, thử thách thực sự đầu tiên là tải xuống tập dữ liệu.

Chúng tôi sẽ sử dụng bộ dữ liệu CNN Daily Mail.

Vì vậy, nếu bạn tìm kiếm CNN Daily Mail Ôm Mặt,

về cơ bản bạn sẽ nhận được,

đây là tên của tập dữ liệu và cách tải nó

là với phương thức Load_dataset.

Vì vậy, hãy đưa ra một ví dụ.

Hoàn hảo.

Bây giờ tập dữ liệu đã được tải xuống

và chúng ta có thể thấy rằng nó có một bài viết

và sau đó nó có một thứ gọi là điểm nhấn,

đó là một bản tóm tắt, nhưng chúng tôi sẽ không làm điều đó.

Những gì chúng ta sẽ làm là chúng ta sẽ lấy bài viết

và chúng ta sẽ học tập trong tương lai

để làm cho mô hình T5 thực hiện dịch thuật,

đó là một nhiệm vụ khác với tập dữ liệu.

Đây là một ví dụ

của cái gọi là học tập đa phương thức,

đó là một chủ đề nâng cao,

nhưng tôi muốn đề cập đến nó.

Để tạo ra RAM GPU,

rất dễ tiếp cận với mọi người,

thay vì lấy toàn bộ bài viết,

điều đầu tiên tôi làm là tóm tắt bài báo,

đó là những gì chúng ta thấy ở phần bài viết.

Đây là bản tóm tắt của bài viết,

không phải là phần nổi bật, vì nó quá nhỏ.

Và ở đây chúng tôi có bản dịch chính xác

và chúng tôi đã làm tương tự với ba ví dụ.

Nếu bạn sử dụng phiên bản nhỏ,

có lẽ bạn có thể sử dụng nhiều ví dụ hơn nếu bạn muốn.

Nó siêu ổn.

Hãy chạy cái này và về cơ bản bạn có thể thấy nó

lời nhắc của chúng tôi sẽ có bài viết và sau đó là bản dịch của nó.

Bài viết và bản dịch là bài viết và bản dịch.

Đây sẽ là một vài kiểu bắn.

Vì vậy, bây giờ những gì chúng ta sẽ làm chỉ là thêm

ở cuối đó, dịch văn bản này

từ tiếng Anh sang tiếng Tây Ban Nha,

nên chúng ta nhận được nhiệm vụ thực tế 45 mà nó biết cách diễn giải,

một bài báo thực tế và bản dịch cho tất cả các cảnh quay.

Và sau đó chúng ta sẽ thêm một cái mới.

Vậy là chúng ta đã có lời nhắc bây giờ trông như thế này.

Bạn có thể thấy rằng nó phải dịch văn bản này

từ tiếng Anh sang tiếng Tây Ban Nha, văn bản và bản dịch.

Và sau đó chúng tôi nhận được một bài báo, một bài báo thử nghiệm,

và chúng tôi thêm nó vào dấu nhắc.

Vì vậy, lời nhắc của chúng tôi sẽ dịch văn bản này

từ tiếng Anh sang tiếng Tây Ban Nha, văn bản và dịch thuật.

Đây là một ví dụ, ví dụ thứ hai, ví dụ thứ ba.

Và cuối cùng, chúng ta có văn bản thực sự

mà chúng tôi muốn dịch về Chính quyền Palestine,

đó là một bài báo của CNN.

Và chúng tôi muốn bản dịch.

Vì vậy bây giờ chúng ta sẽ chạy nó qua mô hình

và chúng tôi chỉ đặt độ dài tối đa 500 để giới hạn

số lượng GPU mà bạn sẽ sử dụng.

Nếu bạn đặt nó lớn hơn,

nó sẽ tạo ra một bản dịch lớn hơn.

Đừng lo lắng.

Điều quan trọng là cái này sẽ được dịch,

vì vậy hãy làm cho nó chạy.

Và chúng ta bắt đầu.

Và chúng tôi nhận được bản dịch của chúng tôi.

(nói tiếng nước ngoài)

Và thế là xong.

Chúng tôi đã có được bản dịch tốt cho bài viết của mình,

nên chúng ta có thể thực hiện việc học đa phương thức này,

nhờ vào một vài kiểu bắn.

Điều này thật tuyệt vời.

Và chỉ cần show ra đây là bạn đã có bài viết

và bản dịch trong trường hợp bạn biết cả hai ngôn ngữ

và bạn muốn kiểm tra, nhưng tôi đã kiểm tra rồi

và nó thực sự hoạt động khá tốt.

Làm tốt lắm.

Bạn đã xem qua giải pháp này, toàn bộ chương này,

và hãy nhớ rằng, nếu bạn không có được giải pháp chính xác,

nó siêu ổn.

Có rất nhiều cách để đạt được kết quả tương tự.

Điều quan trọng là phải hiểu những gì chúng tôi đã làm,

lấy các chi tiết quan trọng

bởi vì điều đó sẽ được lặp lại

ở các chương sau.