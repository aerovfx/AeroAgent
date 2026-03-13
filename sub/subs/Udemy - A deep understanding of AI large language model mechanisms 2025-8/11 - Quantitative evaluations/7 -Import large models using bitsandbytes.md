# 7 -Nhập mô hình lớn bằng cách sử dụng bitandbyte được dịch

---

Đây sẽ là một video nhanh chóng và đơn giản.

Kết quả cuối cùng là rất nhiều mô hình rất lớn không thể được nhập vào Python và đưa vào

GPU đơn giản chỉ vì chúng quá lớn.

Ví dụ: một mô hình tham số 7 tỷ với độ chính xác tối đa sẽ ở khoảng 50

lên tới 60 gigabyte, trong khi GPU tốt nhất mà Kurt Colab hiện cung cấp là 40 gigabyte.

Vì vậy, có một nhóm đã phát triển một thư viện triển khai một phương pháp gọi là lượng tử hóa,

về cơ bản có nghĩa là giảm kích thước của ma trận trọng số theo cách cho phép

bạn nhập và chạy các mô hình rất lớn với dung lượng bộ nhớ nhỏ hơn.

Đây là một ví dụ.

Mình đã thử import model Zephyr 7B, 7 tỷ thông số.

Bạn có thể thấy rằng nó đã làm hỏng phiên Python của tôi vì tôi vừa hết RAM.

Vì vậy, đó là vấn đề.

Và một giải pháp là thư viện bit và byte.

Đây là ảnh chụp màn hình trang GitHub của họ.

Và bạn sẽ không ngạc nhiên khi biết rằng chúng giao tiếp rất ăn ý với việc ôm mặt.

Trên thực tế, càng làm việc với LLM, bạn sẽ càng thấy khuôn mặt ôm ấp đó có trong đó.

trung tâm của hầu hết mọi thứ liên quan đến nguồn mở và chia sẻ các mô hình và bộ dữ liệu AI.

Tôi thực sự, thực sự hy vọng rằng tổ chức đó không bị các nhà đầu tư tham lam lấn át, những người

biến nó thành cái ác và khai thác nó để kiếm lợi nhuận hàng quý.

Đây là hy vọng.

Nhưng dù sao đi nữa, ý tưởng là giảm độ chính xác về số của trọng số từ 32 bit xuống

đến một cái gì đó nhỏ hơn.

Bạn có thể giảm xuống còn 4 bit cho mỗi tham số và khi đó các mô hình này nhỏ hơn nhiều.

Bạn có thể tải chúng xuống Python.

Bạn có thể chạy chúng và vân vân.

Hiện tại có một số sự suy giảm hiệu suất nhỏ nhưng nó thực sự không tệ đối với hầu hết các ứng dụng.

Về mặt kỹ thuật, bạn có thể huấn luyện và tinh chỉnh các mô hình lượng tử hóa này, nhưng điều đó thực sự không

được khuyến nghị trừ khi cần thiết.

Trên thực tế, thư viện này ở đây khá thông minh.

Và có các cơ chế nội bộ để quay lại độ chính xác đầy đủ cho các thông số

thực sự rất quan trọng và cũng dành cho các phép tính nhân ma trận quan trọng.

Đúng vậy, có rất nhiều thủ thuật khoa học máy tính thông minh giúp giảm thiểu sự suy giảm

hiệu suất mà bạn có thể mong đợi từ độ chính xác giảm đi.

Bạn sẽ thấy một số thủ thuật đó trong video tiếp theo.

Đây là ảnh chụp màn hình bằng Python của tôi khi tải thành công mô hình tham số 7 tỷ này tại

Độ chính xác 4 bit.

Và đây chính xác là mô hình bị lỗi bởi phiên Python mà tôi đã trình chiếu một vài slide

trước đây.

Tôi sẽ chuyển sang Python ngay để cho bạn thấy mã trông như thế nào

kiểu như, mặc dù tôi sẽ không thực sự làm việc với mô hình này cho đến video tiếp theo.

Đây là dòng mã gặp sự cố khi cộng tác vì bạn sẽ hết RAM.

Bạn đã hết bộ nhớ, ít nhất là vào thời điểm tôi đang ghi lại điều này.

Được rồi, việc cần làm là cài đặt bit và byte thư viện này.

Vì vậy, những gì bạn phải làm là chạy dòng này để cài đặt thư viện.

Và sau khi cài đặt xong, bạn cần khởi động lại phiên của mình.

Vì vậy, bạn làm điều đó bằng cách nhấp vào thời gian chạy và sau đó khởi động lại phiên.

Điều đó thật tuyệt vời đối với tôi lúc này vì tôi không có phiên hoạt động nào.

Nhưng nếu bạn hiện đang chạy một cái gì đó, một phiên Python ở đây, thì đây sẽ là

có sẵn.

Khởi động lại phiên và sau đó bạn có thể nhận xét dòng này hoặc đơn giản là bỏ qua ô này.

Bạn không cần phải chạy cái này hai lần.

Bạn chỉ cần chạy nó một lần rồi khởi động lại phiên và thế là bạn đã thành công.

Vậy thì bạn có thể đi rồi.

Và sau đó bạn có thể nhập những mô hình lớn này.

Vậy cái này giống như dòng này ở đây.

Nhưng ở trên này tôi không có đầu vào nào khác ngoài tên model.

Và ở dưới đây tôi có một đầu vào khác cho biết cấu hình lượng tử hóa bằng biến này

ở đây.

Đây là một đối tượng từ thư viện bit và byte.

Bạn có thể thấy tôi đang nhập nó lên đây.

Và ở đây tôi viết tải vào cho bit bằng đúng.

Bạn cũng có thể tải phiên bản 8 bit sẽ chính xác hơn một chút nhưng cũng

lớn hơn một chút.

Vì vậy, nó tùy thuộc vào bạn.

Nhưng chắc chắn đối với khóa học này, bất cứ khi nào chúng ta làm việc với các mô hình lớn, phiên bản cấm sẽ

được rồi.

Được rồi, sau đó bạn cũng có thể đặt một số tùy chọn khác về cơ bản chỉ giúp duy trì

độ chính xác cho các mô hình có độ chính xác giảm này.

Được rồi, thế là xong.

Trong video tiếp theo, chúng ta sẽ làm việc với mô hình này và nghiên cứu nó một chút.

chi tiết hơn một chút.

Nếu bạn muốn tự mình khám phá mô hình này trong video này thì thật tuyệt.

Nhưng đừng lo lắng về điều đó.

Bạn sẽ có cơ hội trong video tiếp theo.

Có rất nhiều thông tin trực tuyến về thư viện bit và byte.

Đây là một tài liệu tham khảo về lượng tử hóa hoặc tham chiếu đến việc thiết lập đối tượng này khi ôm

khuôn mặt sử dụng mô hình khuôn mặt ôm.

Và đây là tham chiếu đến mô hình này mà chúng ta sẽ làm việc chi tiết hơn trong phần tiếp theo

video.

Càng làm việc với LLM, bạn sẽ càng thấy rằng đó là một lĩnh vực lớn và đang phát triển nhanh chóng.

lĩnh vực có nhiều thách thức, khó khăn nhưng cũng có nhiều giải pháp và nỗ lực thú vị

để làm cho các mô hình được phổ biến rộng rãi hơn và dễ tiếp cận hơn.