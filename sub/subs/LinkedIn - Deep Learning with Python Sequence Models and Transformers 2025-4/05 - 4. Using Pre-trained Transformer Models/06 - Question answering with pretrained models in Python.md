# 06 - Trả lời câu hỏi với các mô hình được đào tạo trước trong Python

---

- [Người hướng dẫn] Trong video này,

chúng ta sẽ sử dụng một mô hình được đào tạo trước

từ trung tâm Ôm Mặt để trả lời câu hỏi.

Có hai cách tiếp cận chính để trả lời câu hỏi.

Một là cách tiếp cận khai thác,

và cách khác là một cách tiếp cận trừu tượng.

Cách tiếp cận khai thác ngụ ý

rằng chúng ta sẽ trích xuất các phần cụ thể của văn bản

làm câu trả lời, trong khi cách tiếp cận trừu tượng đòi hỏi

rằng chúng tôi tạo ra những phản hồi mới dựa trên

về các khái niệm trong văn bản.

Trong hướng dẫn này, chúng ta sẽ tập trung

về phương pháp trả lời câu hỏi khai thác.

Hãy bắt đầu bằng cách chọn kernel của chúng ta.

Vì vậy, chúng tôi đã chọn ở đây,

sau đó chúng tôi giảm thiểu mức độ dài dòng của nhật ký của mình.

Điều tiếp theo chúng tôi làm bây giờ là chúng tôi muốn

để khởi tạo một đường dẫn để trả lời câu hỏi.

Để làm điều này, chúng tôi nhập hàm đường ống

từ gói máy biến áp.

Sử dụng chức năng đường ống,

chúng tôi tạo ra một quy trình mới gọi là người trả lời,

và chúng tôi chỉ định một nhiệm vụ, trả lời câu hỏi.

Vì vậy, hãy tiếp tục và chạy nó.

Vì vậy, bây giờ một đường dẫn mới đã được khởi tạo.

Điều tiếp theo chúng tôi muốn chúng tôi làm là chỉ định văn bản ngữ cảnh.

Đây là tài liệu nguồn, nguồn thông tin.

Ở đây, chúng ta có một số văn bản về sứ mệnh Apollo,

và chúng ta sẽ sử dụng nó và sẽ trả lời các câu hỏi

hoặc đặt câu hỏi và trả lời các câu hỏi dựa trên văn bản này.

Vì vậy hãy tiếp tục và chạy cái này ở đây.

Vì vậy, chúng tôi tạo văn bản ngữ cảnh,

thì chúng ta chỉ định một câu hỏi, phải không?

Vậy câu hỏi mà chúng tôi muốn hỏi ở đây là

mục tiêu chính của sứ mệnh Apollo của NASA là gì?

Vì vậy, chúng tôi đã tạo một biến có tên question_text dựa trên điều này.

Bây giờ chúng ta sẽ chuyển qua cả bối cảnh

và câu hỏi cho quy trình của chúng tôi,

và kết quả chúng ta sẽ gọi là câu trả lời.

Vì vậy, đường ống được gọi là câu trả lời.

Chúng tôi đã bỏ qua câu hỏi và bối cảnh.

Vậy chúng ta hãy tiếp tục chạy nó và xem kết quả là gì.

Vì vậy, dựa trên quy trình mà chúng tôi vừa xác định,

nó có thể trích xuất câu trả lời từ văn bản ngữ cảnh,

và câu trả lời là "đưa con người lên mặt trăng,

đưa họ trở về Trái đất an toàn," phải không?

Vậy đó chính là phản ứng khai thác.

Vì vậy, cách đường dẫn xử lý văn bản được trả về

như một cuốn từ điển.

Với mỗi câu trả lời, điểm số, điểm bắt đầu và kết thúc,

chúng ta có thể định dạng lại cái này.

Bằng cách đó, nó dễ dàng hơn một chút

để tiến về phía trước, vì vậy chúng ta hãy tiếp tục và làm điều đó.

Vì vậy, ở đây, chúng tôi có câu hỏi được liệt kê,

mục tiêu chính của sứ mệnh Apollo của NASA là gì?

Và sau đó chúng ta có thể nhận được câu trả lời mà nó đưa ra

cho chúng tôi trước đó ở đây và định dạng lại nó

vì vậy theo cách đó nó rõ ràng hơn đối với chúng tôi,

đưa con người lên mặt trăng

và đưa họ trở về Trái đất an toàn.

Và chúng tôi cũng chỉ định chính xác, một lần nữa, hãy nhớ,

đây là cách tiếp cận khai thác, phải không?

Vì vậy, chúng tôi có một số điểm cho chúng tôi biết sự tự tin.

Chúng tôi cũng có vị trí trong văn bản, các giá trị chỉ mục

hoặc các vị trí trong văn bản nơi câu trả lời đến.

Vì vậy đây là một cách tiếp cận đơn giản

để trả lời câu hỏi, cách tiếp cận khai thác.

Đối với một cách tiếp cận trừu tượng,

chúng ta sẽ phải xác định một mô hình được đào tạo trước

có thể trả lời các câu hỏi dựa trên

về ngữ cảnh bằng cách sử dụng cách tiếp cận trừu tượng.