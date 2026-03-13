# 04 tạo ứng dụng tương tác đầu tiên của bạn

---

Trong video trước, bạn đã xây dựng ứng dụng Streamlit đầu tiên được hỗ trợ bởi GenAI.

Nó hiển thị một số văn bản, được gọi là mô hình GenAI và in kết quả đầu ra.

Nhưng thành thật mà nói, nó không thực sự mang tính tương tác.

Bạn có thể mở ứng dụng và thế là xong.

Hãy làm cho nó có tính tương tác.

Streamlit cung cấp cho bạn một tập hợp các phần tử Python tương tác được gọi là widget.

Những điều này cho phép bạn thêm quyền kiểm soát của người dùng vào ứng dụng của mình

mà không cần chạm vào HTML hoặc JavaScript.

Dưới đây là một số ứng dụng tiện dụng mà bạn có thể sử dụng cho ứng dụng GenAI.

st.textinput là một hộp văn bản cho lời nhắc.

st.button kích hoạt hành động.

st.selectbox thêm danh sách thả xuống để chọn mô hình.

st.slider điều chỉnh các giá trị như nhiệt độ.

st.checkbox tạo các nút bật tắt.

st.fileuploader tải lên tệp CSV hoặc tệp văn bản.

st.spinner hiển thị hình ảnh động đang tải khi chờ đợi thứ gì đó.

Ví dụ: đối với phản hồi từ LM.

Trong video này, chúng tôi sẽ sử dụng ba trong số chúng để nâng cấp ứng dụng của bạn.

Một hộp văn bản để nhập lời nhắc.

Một thanh trượt để kiểm soát tính sáng tạo của mô hình được gọi là nhiệt độ.

Và một vòng quay để hiển thị khi mô hình đang tạo văn bản.

Bạn sẽ học cách sử dụng nhiều tiện ích hơn trong suốt phần còn lại của khóa học.

Bạn có thể tiếp tục chỉnh sửa tệp bạn có từ video trước

hoặc tìm file giải pháp trong repo để làm theo.

Nếu bạn muốn thêm một hộp để gõ lời nhắc của riêng bạn,

bạn chỉ cần một dòng mã bổ sung.

userprompt bằng st.textinput để tạo một hộp cho người dùng nhập liệu.

Đối số đầu tiên của hàm này là một thông báo

cho người dùng biết cách tương tác với hộp.

Nhập lời nhắc của bạn.

Bạn cũng có thể thêm lời nhắc mặc định để điền vào hộp khi khởi động.

Ví dụ: giải thích AI tổng quát trong một câu.

Bây giờ, chỉ cần thay thế lời nhắc được mã hóa cứng trong lệnh gọi mô hình của bạn bằng lời nhắc gạch dưới của người dùng.

Khi chạy ứng dụng, bạn sẽ thấy hộp nhập liệu

và nó sẽ chạy mô hình ngay khi bạn nhấn enter.

Hãy kiểm tra nó bằng một cái gì đó đơn giản để đảm bảo nó hoạt động.

Hãy thử gõ, viết một câu chuyện về mèo rồi nhấn enter.

Streamlit sẽ lo phần còn lại.

Hay lắm, một câu chuyện về mèo.

Bạn cũng có thể để người dùng thử nghiệm mức độ sáng tạo

hoặc mô hình xác định bằng cách thêm tiện ích thanh trượt.

Để thêm một mã vào tập lệnh của bạn, hãy đặt mã này ở gần đầu ứng dụng của bạn

nơi bạn xác định đầu vào của người dùng.

Điều này tạo ra một thanh trượt từ 0 đến 1, với 0 là giá trị xác định nhất

và 1 là sáng tạo nhất.

Đối số giá trị đặt giá trị mặc định

và đối số bước kiểm soát giá trị tăng bao nhiêu

hoặc giảm khi người dùng di chuyển thanh trượt.

Bây giờ, chỉ cần cập nhật lệnh gọi mô hình của bạn để bao gồm giá trị nhiệt độ cụ thể.

Bạn vừa làm cho ứng dụng của mình trở nên năng động.

Người dùng hiện có thể điều chỉnh cảm giác của AI.

LLM có thể mất vài giây để phản hồi

và ứng dụng của bạn có thể bị treo trong thời gian đó.

Hãy khắc phục điều đó bằng cách thêm một công cụ quay vòng giúp người dùng của bạn hình dung được

cho họ biết mô hình đang chạy lệnh gọi API.

Bạn có thể thực hiện việc này bằng cách gói mã lệnh gọi API trong khối with st.spinner.

Bây giờ, thay vì tự hỏi liệu có thứ gì bị hỏng không,

người dùng nhìn thấy một hình ảnh động nhỏ hữu ích trong khi mô hình đang hoạt động.

Nếu bạn đang gọi mô hình nhiều lần với cùng một đầu vào

đặc biệt trong quá trình phát triển,

bạn có thể lưu trữ kết quả bằng cách sử dụng trình trang trí dữ liệu st.cache.

Nếu bạn chưa từng làm việc với người trang trí trước đây, đừng lo lắng.

Về cơ bản nó là một trình bao bọc giống như một câu lệnh with

rằng bạn có thể bố trí một chức năng để thay đổi hoặc nâng cao chức năng của nó

mà không sửa đổi chức năng ban đầu.

Vì vậy, điều đầu tiên bạn cần làm là chuyển lệnh gọi mô hình sang chức năng của chính nó

được đặt tên là getResponse.

Ứng dụng sẽ hoạt động giống hệt nhau.

Bạn chỉ cần di chuyển một số logic vào chức năng riêng của nó

sau đó đặt trình trang trí lên trên hàm getResponse như thế này.

dữ liệu st.cache là một công cụ trang trí Streamlit giúp cải thiện tốc độ ứng dụng

bằng cách lưu trữ kết quả của hàm hoặc phép tính trước đó.

Nó báo cho Streamlit biết, tôi đã từng thấy thông tin đầu vào này trước đây.

Chỉ cần trả về kết quả được lưu trong bộ nhớ cache thay vì chạy lại mã.

Nó đặc biệt hữu ích với các ứng dụng JNI

vì các cuộc gọi JNI tốn thời gian và tốn tiền.

Vì vậy, nếu bạn yêu cầu mô hình phân tích đi phân tích cùng một tập dữ liệu,

bạn có thể sử dụng dữ liệu st.cache để nhận được kết quả ngay lập tức.

Thay vì nhấn đi nhấn lại API.

Trong dự án Avalanche,

đây là điều bạn có thể muốn cân nhắc sử dụng

đối với bất kỳ chuyển đổi dữ liệu nào bạn cần thực hiện.

Hoặc có lẽ để phân tích tình cảm.

Chỉ trong vài dòng mã,

bạn đã nâng cấp từ bản demo tĩnh lên ứng dụng tương tác đầy đủ.

Bây giờ là lúc đưa dữ liệu vào.

Trong video tiếp theo,

bạn sẽ tìm hiểu cách tải dữ liệu lên ứng dụng của mình

và thực hiện các hoạt động được hỗ trợ bởi GenAI trên đó.

Tất cả trong khi nâng cao kỹ năng Streamlit của bạn.

Hẹn gặp bạn ở đó.