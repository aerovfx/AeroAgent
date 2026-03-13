# 08 độ trễ so với chất lượng phản hồi

---

Một hành động cân bằng quan trọng khác mà bạn phải xem xét đối với ứng dụng RAG trong sản xuất

là thời gian cần thiết hoặc độ trễ của bất kỳ truy vấn nào so với chất lượng phản hồi.

Chỉ cần thêm một trình truy xuất vào hệ thống của bạn sẽ tăng thêm độ trễ. Và khi bạn thêm nhiều thành phần hơn vào

tăng chất lượng phản hồi, như sắp xếp lại hoặc xây dựng các hệ thống đại lý phức tạp hơn,

độ trễ có thể tăng lên. Vì vậy, chúng ta hãy xem xét kỹ hơn sự đánh đổi này và cách bạn có thể tìm ra giải pháp phù hợp

cân bằng cho hệ thống của bạn. Độ trễ quan trọng như thế nào đối với hệ thống của bạn phụ thuộc rất nhiều vào ngữ cảnh

trong đó nó sẽ được sử dụng. Khách hàng duyệt một trang web thương mại điện tử có rất ít

kiên nhẫn cho thời gian phản hồi chậm. Vì vậy, bạn có thể tối ưu hóa đề xuất mặt hàng của mình

dịch vụ có độ trễ rất thấp, có thể phải trả giá bằng việc không đề xuất dịch vụ hoàn hảo

mục từ danh mục của bạn. Mặt khác, một hệ thống RAG được thiết kế để giúp các bác sĩ chẩn đoán các bệnh hiếm gặp

tay, có thể sẽ được tối ưu hóa cho chất lượng phản hồi, ngay cả khi điều đó có nghĩa là phản hồi mất nhiều thời gian

sản xuất lâu hơn. Khi giải quyết độ trễ, một nguyên tắc dễ nhớ là hầu hết tất cả đều

là kết quả của việc chạy máy biến áp. Kết quả là, thủ phạm lớn nhất sẽ là quy mô lớn của bạn.

lời gọi mô hình ngôn ngữ Mặc dù việc truy xuất có thêm một chút độ trễ, đặc biệt, một số

kỹ thuật sắp xếp lại dựa trên máy biến áp, cơ sở dữ liệu hiện đại và đặc biệt là cơ sở dữ liệu vectơ,

rất nhanh và có quy mô tốt. Nếu bạn muốn giảm độ trễ, nơi tốt nhất để bắt đầu

là mô hình ngôn ngữ cốt lõi của bạn. Một cách tiếp cận hiệu quả ở đây là chỉ sử dụng mô hình ngôn ngữ nhỏ hơn.

LLM nhỏ hơn hoặc các mô hình lượng tử hóa sẽ luôn chạy nhanh hơn trên cùng một phần cứng, giả sử

cùng một bộ nhớ có sẵn. Một cách tiếp cận khác là sử dụng bộ định tuyến LLM nhỏ hơn, nhiệm vụ của nó là

để xem lời nhắc và quyết định xem LLM nhỏ hơn hay lớn hơn là công cụ phù hợp cho công việc.

Nếu một truy vấn yêu cầu lý luận phức tạp, nó có thể được chuyển đến một mô hình lớn hơn và mạnh mẽ hơn.

Trong khi đó, các truy vấn đơn giản có thể được chuyển đến các mô hình nhỏ hơn và nhanh hơn.

Điều này giúp giảm độ trễ cho các lời nhắc đơn giản hơn trong khi chỉ cho phép độ trễ tăng đối với

những lời nhắc phức tạp hơn yêu cầu nó. Đối với các hệ thống thường nhận được lời nhắc rất giống nhau,

bộ nhớ đệm cũng có thể giúp giảm độ trễ. Để làm điều này, bạn duy trì một bộ nhớ đệm của các dữ liệu được gửi thường xuyên.

lời nhắc và câu trả lời của họ. Khi nhận được lời nhắc mới, bạn nhanh chóng tính toán độ tương tự

điểm số giữa lời nhắc mới và điểm trong bộ đệm. Nếu bạn tìm thấy một kết quả đủ gần,

bạn có thể ngay lập tức trả về phản hồi được lưu trong bộ nhớ cache, hoàn toàn bỏ qua quá trình tạo tương đối chậm

quá trình. Với sự điều chỉnh cẩn thận, phương pháp này có thể cải thiện đáng kể độ trễ của hệ thống đối với nhiều lời nhắc.

Nếu bạn vẫn muốn sử dụng bộ nhớ đệm nhưng phản hồi được cá nhân hóa phần nào,

bạn vẫn có thể truy xuất các phản hồi được lưu trong bộ nhớ đệm nhưng sau đó cung cấp phản hồi được lưu trong bộ nhớ đệm và lời nhắc của người dùng

sang LLM nhỏ hơn và nhanh hơn để thực hiện những điều chỉnh nhỏ đối với phản hồi nhằm thực hiện

phù hợp hơn với lời nhắc. Khi bạn đã tối ưu hóa độ trễ của LLM cốt lõi của mình,

bước tiếp theo là giải quyết các thành phần dựa trên máy biến áp khác trong đường ống của bạn.

Đây có thể là trình ghi lại truy vấn, trình xếp hạng lại hoặc LLM của bộ định tuyến, v.v. Mỗi cái này

các thành phần đóng vai trò quan trọng nhưng chúng cũng làm tăng độ trễ. Lời khuyên của tôi ở đây là hãy đo lường

cả độ trễ mà mỗi thành phần đang thêm vào hệ thống của bạn và chất lượng phản hồi gia tăng mà chúng

cung cấp. Ví dụ: bạn có thể nhận ra rằng mình không nhận được nhiều lợi ích từ trình viết lại truy vấn của mình

và chọn loại bỏ thành phần đó. Mặc dù việc tạo ra thường là nguyên nhân gây ra độ trễ lớn nhất,

vẫn có nhiều cách để loại bỏ độ trễ do chó tha mồi của bạn gây ra. Một cách tiếp cận là sử dụng

các phần nhúng được lượng tử hóa nhị phân trong cơ sở dữ liệu vectơ của bạn. Điều này đơn giản hóa cơ bản

tính toán khoảng cách vector và giúp tăng tốc độ truy xuất. Phân chia cơ sở dữ liệu lớn hơn thành

các trường hợp riêng biệt, đặc biệt là khi chúng có kích thước khá lớn, cũng có thể giúp giảm độ trễ tìm kiếm.

Đây là những cách tiếp cận phổ biến để cải thiện độ trễ trong bất kỳ cơ sở dữ liệu nào và hầu hết cơ sở dữ liệu vectơ

nhà cung cấp bao gồm các công cụ để giúp bạn triển khai chúng. Hầu như luôn có độ trễ so với

sự cân bằng chất lượng trong hệ thống RAG của bạn. Để bắt đầu, bạn nên hiểu hệ thống của bạn có bao nhiêu độ trễ

có thể chịu đựng được. Nếu bạn cần giảm độ trễ, hãy bắt đầu bằng cách giải quyết LLM cốt lõi của bạn. Sau đó chuyển sang cái khác

các tính năng dựa trên máy biến áp hoặc LLM. Nếu độ trễ vẫn là một vấn đề, hãy đảm nhận các thành phần khác trong

đường ống. Với một hệ thống quan sát mạnh mẽ được áp dụng, bạn sẽ có thể thấy tác động của

những thay đổi của bạn và liên tục giảm độ trễ xuống mức mà dự án của bạn cần.