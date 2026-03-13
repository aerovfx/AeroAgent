# 5 -Bằng chứng việc sử dụng Jupyter Notebook cũng giống như không sử dụng nó đã được dịch

---

Trong bài giảng này, tôi sẽ nói về máy tính xách tay Jupiter.

Thỉnh thoảng, tôi nhận được câu hỏi kỳ lạ này từ các sinh viên hỏi tại sao tôi không làm những việc trong

Sổ tay sao Mộc.

Hãy để tôi giải thích tại sao tôi nghĩ điều này là lạ.

Thứ nhất, quan điểm của tôi là nó hoàn toàn không cần thiết và thực sự không thay đổi được gì cả

có sử dụng sổ ghi chép Jupiter hay không.

Hãy để tôi nhắc lại điều đó.

Sử dụng sổ ghi chép Jupiter cũng giống như việc không sử dụng sổ ghi chép Jupiter.

Không có sự khác biệt nào ngoài thực tế là nó trông khác.

Nói cách khác, màn hình có màu khác.

Rõ ràng, sự khác biệt như vậy là không đáng kể.

Trong bài giảng này, tôi sẽ chứng minh điều đó xảy ra như thế nào.

Một lý do chính khiến tôi không thích cuốn sổ tay Jupiter là vì nó khiến quá nhiều học sinh phải

không biết Python thực sự hoạt động như thế nào.

Nếu bạn chỉ cảm thấy thoải mái khi ở trong sổ ghi chép và khi bạn nhìn thấy mã Python trong tệp văn bản

hay bất cứ nơi nào khác và bạn cảm thấy sợ hãi hay bị đe dọa, điều đó là không tốt.

Mã Python trong tệp văn bản hoàn toàn giống với mã trong sổ ghi chép.

Thực sự không có gì đáng sợ về nó.

Các lập trình viên làm việc thực tế cuối cùng cần phải viết mã để triển khai

và chạy tự động.

Nói cách khác, mã cuối cùng của bạn sẽ nằm trong một tệp Python tự chạy mà không cần

Sổ tay sao Mộc.

Vì vậy, nếu bạn muốn có hy vọng sử dụng những kỹ năng này trong công việc thực tế, tốt hơn hết bạn nên

thoải mái khi viết mã Python bên ngoài sổ ghi chép Jupiter.

Bạn cũng nên biết rõ hơn rằng thực sự không có sự khác biệt nào giữa việc viết mã

trong sổ ghi chép Jupiter và viết mã bằng IPython hoặc bảng điều khiển.

Đây là một ví dụ tôi thích về cách bạn có thể sử dụng Python trong thế giới thực không trích dẫn.

Giả sử bạn viết một đoạn kịch bản gửi email cho sếp để thông báo rằng bạn sắp đến muộn

cho công việc.

Và giả sử bạn thực sự không muốn gửi email này theo cách thủ công nhưng bạn muốn nhận được

được gửi tự động vào mỗi sáng thứ Sáu để sếp không mắng bạn vì đã đến

đi làm muộn sau khi bạn thêm bữa tiệc quá vất vả vào tối thứ năm.

Vâng, điều đó rất đơn giản.

Tất cả những gì tôi phải làm là trên máy chủ của mình tạo ra cái gọi là cronap trong đó.

Tôi chỉ nhập mã khi tôi muốn lệnh này chạy và sau đó ở bên phải mã đó,

Tôi chỉ định lệnh mà tôi muốn chạy.

Đó chỉ là không gian Python và sau đó là tên tập lệnh.

Như bạn có thể thấy, đó đơn giản là cách bạn chạy tập lệnh Python này từ dòng lệnh.

Và bây giờ vào lúc 9h45 thứ Sáu hàng tuần, tập lệnh này sẽ gửi cùng một email cho sếp của bạn

để nói với anh ấy rằng bạn sẽ đến muộn.

Được rồi, chúng ta đừng đi chệch hướng ở đây.

Vấn đề ở đây là bạn thực sự không muốn sử dụng Jupyter Notebook cho việc gì đó

như thế này.

Tôi nghĩ một lợi thế có thể nhận thấy của Jupyter Notebook là bạn có thể xem kết quả của các bước trung gian.

tính toán.

Tuy nhiên, đây chỉ là lợi thế được cảm nhận chứ không phải lợi thế thực sự vì bạn có thể làm

điều tương tự cũng xảy ra ngay cả khi bạn không ở trong sổ ghi chép.

Đầu tiên, tôi chắc rằng bây giờ bạn đã thấy, tôi Python cũng in ra kết quả sau bạn

nhập một lệnh.

Tôi Python được gọi là REPL, viết tắt của vòng lặp in eval đọc và đó thường là những gì

tất cả đều làm được bất kể bạn đang sử dụng ngôn ngữ nào.

Vì vậy, cho dù đó là Python, Ruby, PHP hay bất kỳ ngôn ngữ nào khác.

Từ khóa ở đây là in.

Tại sao vậy?

Chà, một trong những mục tiêu và quy tắc viết và gỡ lỗi mã của tôi là khi nghi ngờ hãy in nó ra

ra ngoài.

Tôi không thể nói cho bạn biết tôi đã nhận được câu hỏi trong phần Hỏi đáp bao nhiêu lần trong khi lẽ ra nó có thể

dễ dàng trả lời bằng cách chèn câu lệnh in vào mã hiện có.

Dù sao đi nữa, mục đích của cuộc thảo luận dài dòng này về việc in ấn mọi thứ là gì?

Chà, nếu bạn nghĩ Jupyter Notebook là chương trình duy nhất giúp bạn làm điều này,

bạn cần mở rộng tầm nhìn của mình một chút.

Trên thực tế, bạn nên luôn luôn làm điều này.

Nếu bạn không sử dụng nhiều câu lệnh in trong khi viết mã thì bạn đang không làm được điều đó.

đúng rồi.

Hãy nhớ lập trình không phải là triết học.

Bạn không được phép chạy một chương trình trong đầu.

Điều đó giống như cố gắng thực hiện phép chia dài trong đầu khi bạn có một chiếc máy tính trong tay.

tay.

Vì vậy, chỉ bằng cách in mọi thứ ra, bạn có thể làm việc hiệu quả hơn.

Đừng cố đoán xem chương trình sẽ làm gì và hãy để chính chương trình đó nói cho bạn biết

nó đang làm gì vậy.

Điểm mấu chốt ở đây là bạn phải luôn in mọi thứ ra.

Việc Jupyter Notebook hiển thị cho bạn kết quả của từng khối mã không đơn giản là

một bất ngờ hạnh phúc.

Nhưng một bài học quan trọng khác ở đây là nếu bạn muốn sử dụng Jupyter Notebook, thì có

hoàn toàn không có gì ngăn cản bạn làm như vậy.

Nói cách khác, việc sử dụng Jupyter Notebook tương thích 100% với mọi thứ chúng tôi đã có

đang làm.

Trên thực tế, nếu bạn nhớ lại, mục tiêu của bạn trong các khóa học này không phải là chạy mã của tôi mà là viết mã của riêng bạn.

mã.

Và tất nhiên, vì đó là mã của bạn nên bạn có thể viết nó theo cách bạn muốn, kể cả Jupyter

Sổ tay.

Trong phần còn lại của bài giảng này, tôi sẽ chứng minh cho bạn thấy rằng bạn có thể lấy bất kỳ kịch bản nào từ

kho lưu trữ khóa học mà chúng tôi biết chạy trong bảng điều khiển vì đó là cách tôi luôn minh họa

nó.

Và nó cho bạn thấy rằng mã chính xác này chạy trong Jupyter Notebook.

Hãy bắt đầu.

Được rồi, giả sử tôi đang ở trong lớp thư mục có nhiều khối và tôi quan tâm đến mã bên trong phân loại

example.py.

Như bạn có thể thấy, những gì tôi có bây giờ là đoạn mã này bên trong trình soạn thảo văn bản.

Bây giờ nếu bạn chưa biết trình soạn thảo văn bản là gì thì đó chỉ là một chương trình hiển thị cho bạn

nội dung của tệp văn bản và cho phép bạn chỉnh sửa những nội dung đó.

Đây là chương trình lý tưởng để viết mã.

Thỉnh thoảng, nếu bạn đang viết bằng ngôn ngữ như Java hoặc Swift, bạn có thể muốn sử dụng

IDE, nhưng thậm chí sau đó nó hoàn toàn không bắt buộc.

Ngày nay tôi thích viết Java bằng trình soạn thảo văn bản đơn giản như Sublime Text hơn.

Trong mọi trường hợp, thông thường người ta không cần sử dụng IDE để viết mã Python.

Bây giờ về Notebook Jupyter.

Chà, hãy khởi động Notebook Jupyter.

Vì vậy, tôi sẽ truy cập Jupyter Notebook.

Được rồi, bây giờ tôi đã chạy Jupyter Notebook, vì vậy tôi sẽ bắt đầu một cuốn sổ mới.

Ngoài ra, hãy lưu ý rằng chúng tôi đã khởi động sổ ghi chép trong cùng thư mục với Python có liên quan.

tập tin, vì vậy đó là điều bạn muốn ghi nhớ cho tương lai.

Bây giờ, điều tôi sắp làm là chứng minh rằng mọi thứ trong này

Tệp Python hoạt động giống hệt nhau trong sổ ghi chép cũng như trong bảng điều khiển.

Vì vậy, hãy bắt đầu với việc nhập khẩu.

Trên thực tế, chúng ta cũng hãy lấy cái này.

Được rồi, dán nó vào.

Chạy nó.

Vì vậy, mọi thứ đều ổn cho đến nay.

Bây giờ hãy tải dữ liệu.

Được rồi.

Chúng tôi đã tải dữ liệu.

Bây giờ tôi không chắc nó thuộc loại gì nên tôi có thể kiểm tra nó bằng cách sử dụng hàm type.

Vì vậy, hãy để tôi thử điều đó.

Thật tuyệt, vì vậy tôi nhận được SKlearn.Utels.Bunch, đó là loại dữ liệu biến.

Trước đây, bạn nhớ lại rằng chúng tôi đã thực hiện ví dụ này trong IPython, nhưng như bạn có thể thấy, kết quả

giống nhau trong sổ ghi chép Jupyter.

Ngoài ra, nếu bạn muốn chạy tệp Python này trong bảng điều khiển, thì bạn cần có một tệp type.

Hãy nói.

Vì vậy, giả sử bạn muốn nhập ví dụ phân loại Python, sau đó bạn có thể thêm một số

print câu lệnh nếu bạn muốn hiển thị những dòng tương tự trong khi tệp này đang chạy.

Bây giờ tôi sẽ không đi sâu vào chi tiết phức tạp như vậy trong phần còn lại của ví dụ này vì bạn đã thấy nó rồi.

Vì vậy, chúng ta hãy đi qua từng dòng còn lại.

Giả sử tôi muốn kiểm tra các khóa trong biến dữ liệu.

Được rồi, có vẻ tốt cho đến nay.

Hãy kiểm tra hình dạng của thuộc tính dữ liệu.

Được rồi, có vẻ tốt cho đến nay.

Hãy kiểm tra các mục tiêu.

Được rồi, vẫn là những gì chúng ta mong đợi.

Những tên mục tiêu.

Có vẻ tốt.

Hình dạng mục tiêu.

Đây phải là 569.

Và hãy kiểm tra tên tính năng.

Được rồi, điều đó cũng tương tự.

Bây giờ hãy thực hiện phần chia bài kiểm tra tàu của chúng ta.

Được rồi, bây giờ hãy khởi tạo và điều chỉnh mô hình của chúng ta.

Được rồi, bây giờ chúng ta hãy kiểm tra điểm tàu ​​và điểm kiểm tra.

Được rồi, bây giờ hãy xem chúng ta có thể đưa ra những dự đoán mới như thế nào.

Vậy các bạn thấy nếu gán cho một biến thì nó không in ra kết quả.

Nhưng nếu bạn có một biểu thức thì nó sẽ in kết quả.

Vì vậy, có một số dự đoán và đây là một cách khác để tính toán độ chính xác của các dự đoán.

Vì vậy, chúng ta có thể sử dụng các câu trả lời tương tự trước đây.

Và chúng ta cũng có một ví dụ khác nơi chúng ta có thể sử dụng mạng lưới thần kinh để làm điều tương tự.

Vì vậy, hãy xây dựng mô hình, huấn luyện nó và in điểm tàu.

Và hãy in điểm kiểm tra nữa.

Được rồi, vậy là mọi thứ đều hoạt động theo cách tương tự mà không cần sử dụng sổ ghi chép.

Bây giờ, một điều khác mà tôi có thể làm là tôi có thể lấy toàn bộ thứ này và sao chép nó, dán vào và chạy nó.

Vì vậy, đó là một điều khả thi khác mà bạn có thể làm.

Nhưng nhược điểm của việc đó là bạn không thể nhìn thấy kết quả đầu ra trung gian.

Nhưng một lần nữa, đó chính là mục đích của các câu lệnh print.

Được rồi, vậy chúng ta có thể kết luận gì từ bài tập này?

Chà, chúng ta có thể thấy rằng mã này chạy giống hệt nhau trong sổ ghi chép Jupyter cũng như ở mọi nơi khác.

Đó là lý do tại sao tôi luôn nói mã Python là mã Python dù nó ở đâu.

Nếu bạn muốn sử dụng sổ ghi chép Jupyter để chạy mã khóa học, hoàn toàn không có gì ngăn cản bạn làm điều đó.