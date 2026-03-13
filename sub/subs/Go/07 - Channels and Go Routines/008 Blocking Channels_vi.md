# 008 Chặn kênh vi

---

Trong phần cuối cùng, chúng tôi đã tạo kênh đầu tiên của mình, chúng tôi tạo kênh, chúng tôi chuyển nó vào chức năng

check link link.

Sau đó, khi chúng tôi yêu cầu nhận được yêu cầu của chúng tôi thành công hoặc không thành công, sau đó chúng tôi sẽ gửi một chuỗi thông báo vào kênh, sau đó

sau đó quay lại bên trong hàm chính.

Chúng tôi đã lắng nghe một tin nhắn và in it ra khi chúng tôi nhận được một tin nhắn.

Chỉ có một vấn đề nhỏ.

Chúng tôi nhận thấy rằng khi chúng tôi chạy đoạn mã này, chúng tôi chỉ nhận được một bản cập nhật lệnh và sau đó là chương trình cài đặt ngay lập tức

tức thực thi hoặc ngay lập tức thoát ra, không thực hiện.

Vì vậy, chúng tôi hãy đi sâu vào vấn đề này và tìm hiểu chính xác những gì đang xảy ra hiện nay khi chúng tôi bắt đầu xem xét vấn đề này.

Đây chắc chắn là một trong những khái niệm sơ cấp nhất về kênh.

Vì vậy, hy vọng chúng tôi sẽ giải quyết vấn đề này thực sự khó khăn và nắm bắt rất tốt một số nguyên tắc cơ bản

của kênh.

Vì vậy, hay thực hiện ngay bây giờ.

Vì vậy, đây là sơ đồ chức năng của chúng tôi.

Đây là chức năng chính của chúng tôi và đây là chức năng kiểm tra liên kết của chúng tôi.

Vì vậy, chúng tôi hãy xem xét vấn đề này và tưởng tượng mọi dòng mã khi nó đang được thực thi.

Vì vậy, các thói quen chính bắt đầu.

Ngay sau khi chúng tôi tạo chương trình của mình, sau đó chúng tôi tạo phần chuỗi của mình, sau đó chúng tôi tạo kênh của mình, sau đó

chúng đi vào vòng lặp và chúng tôi tạo ra quy trình hoạt động đầu tiên của mình.

Chúng tôi chuyển liên kết và kênh kiểm tra liên kết chức năng.

Và vì vậy, về cơ bản chúng ta có thể tưởng tượng rằng thói quen đầu tiên của chúng ta sau đó sẽ trở thành thành trực tiếp.

Chúng tôi sẽ tưởng tượng rằng quy trình đầu tiên xuất hiện trực tiếp là phần tử đầu tiên bên trong chuỗi cắt cắt

string của chúng tôi.

Vì vậy, google. com.

Vì vậy, sau đó thói quen của chúng tôi là dậy thì.

Nó bắt đầu thực thi mã bên trong đây và ngay lập tức thực hiện một yêu cầu nhận.

Vì vậy, tại thời điểm đó, chúng tôi có thể tưởng tượng rằng quy trình cắm cờ này hiện đã bị tạm dừng như ngay tại đây.

Vì vậy, trên dòng mã đó ngay tại đó.

Bây giờ quy trình chính thức dậy và nó bắt đầu tạo các quy trình hoạt động khác trong chương trình của chúng tôi.

Vì vậy, một lần đi thường xuyên cho mọi liên kết khác.

Bây giờ, đây là điều thực sự quan trọng, rất quan trọng cần hiểu.

Sau khi chúng tôi tạo mọi quy trình đi lại, quy trình chính sau đó nói, được rồi, tôi sẽ ngồi

đây và chờ tin nhắn đến qua kênh.

Bất cứ khi nào chúng tôi chờ đợi một tin nhắn đến qua một kênh, đây là một cuộc gọi chặn, một dòng

mã chặn theo cách đúng mà chức năng nhận được của chúng ta ở đây cũng đã bị chặn.

Vì vậy, ngay khi thời gian chạy Go nhận thấy rằng chúng ta muốn nhận tin nhắn từ một kênh, nó sẽ nói: Ồ, quy trình

điều này đang chờ đợi điều gì sẽ xảy ra.

Hiện không có mã nào khác để chạy ngay bây giờ.

Chúng tôi chỉ cần tạm dừng và để nó hoạt động.

Vì vậy, thói quen chính được đưa vào giấc ngủ và nó nói, được rồi, bạn sẽ không thực hiện thói quen chính nữa.

Chúng tôi sẽ chờ đợi điều gì sẽ xảy ra.

Sau đó là một khoảng thời gian trôi qua.

Thời gian trôi.

Thời gian trôi.

Và cuối cùng là quy trình đi của chúng tôi, bất kỳ yêu cầu nào sẽ được giải quyết trước đó.

Và trong trường hợp này, đó là Google cho cá nhân tôi, vì đó là trang web tải nhanh nhất cho

bạn.

Bạn có thể đã nhận được một kết quả khác.

Bạn có thể đã tìm thấy một số kết quả khác nếu bạn có tốc độ kết nối khác với tốc độ của tôi.

Vì vậy, sau đó ngay lập tức quy trình đi đầu tiên giải quyết yêu cầu quy trình đi đánh thức lại và nó bắt đầu

thực thi lại phần mã hóa bên trong hàm này.

Vì vậy, cuối cùng nó sẽ gửi thông báo này ngay tại đây trong trường hợp không thành công hoặc

gửi thông báo ở bên dưới ngay bên dưới đây để chọn trường hợp thành công.

Vì vậy, về cơ bản, thói quen của con dê thức dậy và cuối cùng gửi tin nhắn vào kênh.

Bây giờ, khi tin nhắn này được gửi đi, thời gian chạy sẽ hiển thị, đã được rồi, có vẻ như chúng tôi đang nhận được một

data number trên kênh này.

Có bất kỳ công việc thường xuyên nào đang chờ đợi một số thông tin trên kênh này không?

Và thói quen nhắc nhở và nói, Ồ, đúng vậy.

Tôi đang chờ một số thông báo trên kênh này.

Và làm điều đó, thói quen chính thức dậy trở lại.

Nó đã nhận được giá trị mà chúng tôi đã gửi vào kênh.

Nó ở trong đó ra.

Và sau đó, thói quen nói chính, đó là nó.

Không có mã nào khác để tôi chạy.

Chúng tôi sẽ thoát khỏi toàn bộ chương trình.

Và bài học rút ra ở đây là việc nhận tin nhắn từ một kênh là một thứ bị chặn.

Đó là một dòng chặn mã hóa.

Chúng tôi phải đợi một thông báo được gửi đến trước thời gian chạy hoặc trước quá trình này

tiếp tục.

Chuyển dòng mã này ngay tại đây.

Và vì vậy trong thực tế, chúng ta có thể hình dung một sơ đồ giống như thế này.

Vì vậy, đây là một chút phức tạp, nhưng chúng ta hãy đi qua nó từng bước một.

Vì vậy, chương trình đầu tiên của chúng tôi bắt đầu ở đây ở phía bên tay trái.

Chúng tôi nhập quy trình chính, chúng tôi tạo các lát chuỗi của chúng tôi và sau đó chúng tôi nhập vào vòng lặp cho.

Sau đó, chúng tôi tạo ra một số thói quen khác nhau.

Vì vậy, lần đầu tiên là Google. com normal, sau đó là Facebook và sau đó là Amazon hoặc bất kỳ liên kết nào khác mà chúng tôi có.

Vì vậy, ngay sau khi kết thúc vòng lặp và về cơ bản, chúng tôi có thể tưởng tượng rằng vòng lặp được hoàn thành thành công

tại thời điểm Amazon hoặc bất kỳ kết nối cuối cùng nào.

Vì vậy, về cơ bản ở dòng này ngay tại đây, chúng tôi đã hoàn thành vòng lặp và chúng tôi đang chờ kênh

của chính mình.

Vì vậy, dòng này ngay tại đây có nghĩa là đại diện cho dòng mã này về cơ bản ngay tại đây.

Vì vậy, chúng tôi đang chờ đợi điều này.

Chúng tôi đang chờ một số dữ liệu đến qua kênh.

Vì vậy, sau đó tất cả các quy trình khác nhau của chúng tôi đang chạy và không có quy trình chính nào đang chạy tại

thời điểm đó.

Bây giờ, đó là một phóng đại sự thật ở đây.

Bạn biết đấy, quy trình chính đã bị tạm dừng trong quá trình thực thi.

Và thành thật mà nói, tất cả các quy trình khác cũng như chúng tôi đang chờ phản hồi từ yêu cầu HTTP của chúng tôi quay

trở lại.

Nhưng chúng ta có thể chỉ ở dạng sơ đồ, chúng ta có thể tưởng tượng nó xảy ra như thế này.

Vì vậy, cuối cùng vào một thời điểm nào đó, Google. com là người đầu tiên dậy và nói, Ồ, có vẻ như

như chúng tôi đã nhận được phản hồi.

Và như vậy, ngay sau khi chúng tôi nhận được phản hồi đó, quy trình của Google sẽ gửi dữ liệu vào

Kênh, quy trình chính sẽ được đánh giá lại, sau đó lấy giá trị đó, ra.

Nó thấy rằng không có mã nào khác để chạy trong hàm đó.

Và do đó, các thói quen chính thoát ra và các thói quen khác mà chúng ta có về cơ bản bị bỏ lại trong hư hỏng, và chúng không

bao giờ thực sự kết thúc.

Họ đã được chấm dứt hoàn toàn chỉ định.

Vì vậy, chúng tôi hãy xem xét vấn đề này ở mức độ tiếp theo ở đây và chúng tôi hãy thực hiện tìm kiếm và chỉ chơi một chút

về điều này một chút, về cơ bản.

Vì vậy, tôi sẽ tìm thấy dòng lệnh trong chúng tôi.

Tôi sẽ sao chép nó và tôi sẽ đặt một bản sao khác ngay bên dưới nó.

Vì vậy, hiện tại chúng tôi có hai vị trí mà chúng tôi đang chờ đợi tin nhắn qua kênh của chúng tôi.

Bây giờ tôi sẽ lưu tệp này và tôi muốn bạn tạm dừng ngay bây giờ, và tôi muốn bạn

nghĩ trong đầu, bạn mong đợi điều gì sẽ xảy ra vào thời điểm này?

Tôi chỉ muốn bạn suy đoán phổi tung.

Bạn nghĩ điều gì sẽ xảy ra vào lúc này khi chúng tôi chạy chương trình của mình?

Hy vọng rằng bạn đã có rất nhiều ý tưởng.

Bây giờ chúng ta hãy chuyển sang thiết bị đầu cuối của chúng ta và chúng ta sẽ chạy lại chương trình.

Hiện nay.

Lần này, chúng tôi đã nhận được hai bản cập nhật báo cáo dành riêng cho Google. com và StackOverflow.

Bây giờ một lần nữa, bạn có thể tìm thấy một thứ tự khác ở đây nếu các yêu cầu của bạn được giải quyết bằng một thứ tự khác

với tôi, điều này hoàn toàn ổn.

Vì vậy, bây giờ chúng tôi hãy xem những gì đang xảy ra ở dạng sơ đồ ở đây.

Vì vậy, hiện tại cơ bản ở đây là một sơ đồ giống nhau chỉ với một hoặc hai bước bổ sung.

Vì vậy, tôi sẽ chỉnh sửa dòng này ngay tại đây để thực hiện phù hợp với những gì tôi nhận được, đó là Stack Overflow.

Vì vậy, hiện tại chúng tôi có thể tưởng tượng rằng quy trình chính của chúng tôi bắt đầu, nó lặp lại thông tin qua phần chuỗi của chúng tôi

và bắt đầu một loạt các quy trình khác nhau.

Sau đó, thói quen chính của chúng tôi nói, Đã rồi, tôi đang nghe trên kênh.

Tôi đang chờ một số dữ liệu đến.

Sau đó, quy trình của Google cuối cùng cũng kết thúc.

Nó ra hoặc gửi một số dữ liệu vào kênh mà chương trình chính sau đó sẽ nhận được nó.

Vì vậy, quy trình chính nhận dữ liệu đó và đánh lại biểu thức, sau đó ra dữ liệu và sau đó chuyển đổi

sang code next line.

Và dòng mã tiếp theo ngay tại đây cũng cho biết hãy chờ đợi một số dữ liệu đến kênh của chúng tôi.

Và vì vậy chúng tôi lại đi vào một điều chính xác.

Sau đó, quy trình chính trở lại chế độ ngủ và thức dậy khi đối với tôi, Stack Overflow đã hoàn thành và gửi

một số dữ liệu vào kênh.

Sau đó, quy trình chính nhận dữ liệu đó, in it ra và sau đó nói rằng không có mã nào khác dành cho tôi

viết, vì vậy tôi sẽ thoát hoàn toàn.

Và vì vậy, chúng tôi có thể bắt đầu sắp xếp các dòng lệnh trong đây ngay tại đây và xem một số hành vi thú vị.

Vì vậy, đối với tôi, tôi có một danh sách năm liên kết ngay tại đây, năm liên kết.

Vì vậy, nếu tôi muốn, tôi có thể nói dán ra năm tin nhắn sẽ được nhận ở đây.

Đúng năm.

Vì vậy, hiện tại chúng tôi sẽ đợi năm tin nhắn trong kênh trước khi thoát khỏi chương trình này.

Vì vậy, tôi sẽ lưu cái này, tôi sẽ chạy nó.

Và bây giờ chúng tôi sẽ tìm thấy năm kết quả ở đây.

Vì vậy, một, hai, ba, bốn, năm.

Sau đó, không có mã nào nữa hoặc không có mã nào nữa để thực hiện việc này.

Và vì vậy chúng tôi đã thoát hoàn toàn.

Và hiện tại, chúng tôi có thể tìm thấy một số hành động thực sự kỳ lạ.

Nếu tôi cài đặt thêm một bản báo cáo ở đây.

Và đây là số sáu.

Nhưng bạn và tôi biết rằng chúng tôi sẽ chỉ tìm thấy tin nhắn được gửi đến kênh của chúng tôi vì chúng tôi

tôi chỉ tạo mới một quy trình hoạt động năm.

Vì vậy, hiện tại khi tôi lưu điều này và chạy mã của chúng tôi, chúng tôi sẽ tìm thấy thông báo năm.

Và sau đó chương trình của chúng tôi chỉ được treo bởi vì thói quen chính bây giờ chỉ là ngồi ở đó chờ ai gửi

một số thông tin vào kênh của chúng tôi.

Và về mặt cá nhân, tôi nghĩ đây là hành vi thực sự thú vị ở đây.

Vì vậy, như bạn có thể tưởng tượng, suy nghĩ thực sự kỹ năng về các kênh của chúng tôi và cách chúng được thiết lập bên trong

ứng dụng của chúng tôi bắt đầu trở nên rất quan trọng.

Tất nhiên, hiện tại, chúng tôi không thể muốn chương trình của mình được treo ở đây và chạy.

Vì vậy, chúng tôi nghỉ ngơi nhanh chóng.

Chúng tôi sẽ quay trở lại trong phần tiếp theo và chúng tôi sẽ tìm ra cách chúng tôi có thể có trong

ra tất cả các thông báo đến từ kênh của chúng ta mà không cần phải viết một loạt câu lệnh khác

nhau ở đây.

Bởi vì rõ ràng là chúng tôi không muốn xếp chồng lên nhau như một dòng lệnh như thế này,

đặc biệt nếu chúng tôi bắt đầu có một số URL khác nhau ở đây mà chúng tôi muốn có trong ra.

Vì vậy, nhanh chóng nghỉ ngơi.

Hãy quay lại phần tiếp theo và chúng tôi sẽ tìm hiểu cách chúng tôi có thể giải quyết vấn đề chặn kênh này

như thế nào.