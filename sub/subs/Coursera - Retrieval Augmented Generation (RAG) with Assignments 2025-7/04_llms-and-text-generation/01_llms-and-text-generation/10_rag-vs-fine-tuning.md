# 10 rag-vs-tinh chỉnh

---

Mặc dù RAG là một cách tiếp cận phổ biến và mạnh mẽ để cải thiện hiệu suất của LLM,

một kỹ thuật khác gọi là tinh chỉnh cũng thường được sử dụng.

Thay vì chỉ tăng cường lời nhắc,

tinh chỉnh đào tạo lại LLM có sẵn để cải thiện hiệu suất trong một bối cảnh cụ thể.

Chúng ta hãy xem xét kỹ hơn việc tinh chỉnh và vai trò của nó trong hệ thống RAG của bạn.

Ý tưởng cốt lõi của việc tinh chỉnh là đào tạo lại mô hình ngôn ngữ

với dữ liệu của riêng bạn để cập nhật các thông số nội bộ của nó.

Thông thường, việc này được thực hiện thông qua tinh chỉnh có giám sát hoặc SFT.

Nó được giám sát vì mô hình được đào tạo lại

bằng cách sử dụng tập dữ liệu được gắn nhãn từ miền mà mô hình đang được điều chỉnh.

Đặc biệt, việc tinh chỉnh hướng dẫn,

đề cập đến một cách tiếp cận trong đó tập dữ liệu bao gồm cả

một bộ hướng dẫn cho mô hình ngôn ngữ,

thường là một lời nhắc hoặc một câu hỏi,

cũng như một câu trả lời đúng nhất về sự thật được mong đợi.

Để tinh chỉnh mô hình, bạn cung cấp cho nó các hướng dẫn đầu vào

và xem kết quả đầu ra gần với câu trả lời đúng từ tập dữ liệu của bạn đến mức nào.

Sau đó, bạn sử dụng các kết quả này để điều chỉnh các tham số bên trong của mô hình

để phù hợp hơn với câu trả lời đúng.

Quá trình này rất giống với cách đào tạo mô hình ngôn ngữ ban đầu,

nhưng tập dữ liệu được sử dụng được lấy từ một miền cụ thể

mô hình đang được tinh chỉnh để chuyên môn hóa.

Giả sử bạn muốn tinh chỉnh một mô hình để hoạt động trong lĩnh vực chăm sóc sức khỏe.

Để bắt đầu, bạn sẽ chọn một mô hình ngôn ngữ có mục đích chung.

Nếu bạn hỏi mô hình này về một tập hợp triệu chứng cụ thể,

nói đau khớp, nổi mẩn da, nhạy cảm với ánh nắng mặt trời,

mô hình ngôn ngữ có thể cung cấp cho bạn câu trả lời chung chung với giọng điệu chung chung.

Điều này là do mô hình có sẵn không chuyên về dữ liệu y tế.

Nếu bạn sử dụng điều chỉnh lệnh trên cùng mô hình đó,

đào tạo nó về rất nhiều hướng dẫn và phản hồi trong lĩnh vực y tế,

về cơ bản, mô hình trở thành chuyên gia hơn nhiều trong việc trả lời loại câu hỏi đó.

Bây giờ, nếu bạn đưa ra lời nhắc tương tự,

nó có thể phản hồi chính xác hơn, chi tiết hơn,

và theo phong cách phù hợp hơn với lĩnh vực y tế.

Tinh chỉnh có thể hoạt động tốt trong những trường hợp như thế này,

nơi bạn muốn mô hình chuyên biệt hóa trong một lĩnh vực cụ thể,

như cung cấp chẩn đoán y tế ban đầu hoặc tóm tắt tóm tắt pháp lý.

Mặc dù hiệu suất của mô hình sẽ cải thiện trong lĩnh vực đó,

tinh chỉnh thực sự có thể làm giảm hiệu suất trong các lĩnh vực khác.

Quá trình tinh chỉnh chỉ tối ưu hóa hiệu suất của mô hình trong miền mục tiêu,

điều đó có nghĩa là đôi khi những điều chỉnh được thực hiện đối với các tham số bên trong của mô hình

sẽ dẫn đến hiệu suất thấp hơn với các loại yêu cầu khác.

Miễn là mô hình sẽ chỉ được sử dụng trong miền chuyên dụng của nó,

tuy nhiên, sự đánh đổi này thường đáng giá.

Một trường hợp cụ thể, điều này đúng là dành cho các mô hình nhỏ được sử dụng bên trong các hệ thống đại lý.

Nếu bạn biết trước công việc duy nhất của người mẫu là xác định

liệu lời nhắc có yêu cầu truy xuất từ cơ sở dữ liệu vectơ hay không,

bạn sẽ rất vui khi sử dụng một mẫu máy nhỏ, nhẹ

và tinh chỉnh kỹ lưỡng mô hình đó để chỉ thực hiện tốt nhiệm vụ duy nhất đó.

Điều đáng chú ý là việc tinh chỉnh thường không phải là cách tuyệt vời để dạy thông tin mới cho LLM.

Cách một mô hình được điều chỉnh bằng cách tinh chỉnh có xu hướng có tác động lớn hơn

về cách mô hình phản ứng với các lời nhắc, như từ ngữ nó sử dụng, phong cách hoặc cấu trúc,

và tác động ít rõ rệt hơn đến những thông tin mà mô hình biết.

Điểm cuối cùng này đề cập đến một số ưu và nhược điểm của RAG so với việc tinh chỉnh.

Vì vậy, hãy nói về thời điểm sử dụng từng cái một.

Nói tóm lại, sự đồng thuận hiện nay là RAG là người giỏi nhất trong việc đưa kiến thức vào

và tinh chỉnh là tốt nhất khi điều chỉnh tên miền.

Nếu bạn cần LLM có quyền truy cập vào thông tin mới,

thế hệ tăng cường truy xuất là giải pháp tốt nhất.

Bạn có thể đưa thông tin đó vào lời nhắc

và LLM sẵn có sẽ có thể kết hợp thông tin mới đó vào phản hồi của mình.

Mặt khác, nếu bạn muốn LLM của mình chuyên về một nhiệm vụ hoặc lĩnh vực nhất định,

tinh chỉnh là con đường để đi.

Đặc biệt nếu LLM của bạn sẽ xử lý một nhiệm vụ riêng biệt,

như lời nhắc định tuyến trong hệ thống RAG của bạn,

hoặc chỉ phản hồi một loại lời nhắc nhất định, việc tinh chỉnh sẽ có ý nghĩa hơn rất nhiều.

Tinh chỉnh và RAG cũng có thể được sử dụng cùng nhau.

Đặc biệt, bạn có thể tinh chỉnh một mô hình cụ thể

để kết hợp thông tin được truy xuất vào phản hồi cuối cùng của nó.

Nói cách khác, bạn đang giúp mô hình chuyên môn hóa vai trò của nó trong hệ thống RAG.

Khi quyết định sử dụng tinh chỉnh hay RAG, lựa chọn tốt nhất có thể là cả hai.

Mỗi cách tiếp cận cải thiện hiệu suất của mô hình theo những cách khác nhau,

và có những lợi ích khi sử dụng cả hai cùng lúc.

Nếu bạn muốn kết hợp tinh chỉnh vào hệ thống RAG của riêng mình,

Tôi khuyên bạn nên tham gia một khóa học riêng về tinh chỉnh

và khám phá cách tinh chỉnh mô hình ngôn ngữ của riêng bạn.

Tinh chỉnh là một chủ đề phức tạp,

và không thể trình bày đầy đủ nó trong khóa học này.

Điều đó có nghĩa là, bạn thường có thể tìm thấy các mô hình đã được tinh chỉnh cho phù hợp với mình

và thích ứng với một nhiệm vụ hoặc lĩnh vực cụ thể.

Nếu bạn cho rằng hệ thống của mình cần một mô hình được tinh chỉnh,

nhiều kho lưu trữ trực tuyến của các mô hình đã được tinh chỉnh trước đó có sẵn,

và bạn có thể sử dụng một trong những thứ đó mà không cần tự mình tinh chỉnh.

Tinh chỉnh và RAG đôi khi được mô tả là những lựa chọn thay thế cạnh tranh,

nhưng chúng được xem chính xác hơn là những công cụ bổ sung.

Thêm các mô hình được tinh chỉnh vào quy trình RAG của bạn,

hoặc thậm chí tinh chỉnh LLM cốt lõi tạo ra phản hồi cuối cùng của bạn,

có thể giúp cải thiện hiệu suất hệ thống của bạn.

Mặc dù bạn sẽ không đi sâu vào các kỹ thuật tinh chỉnh trong khóa học này,

nó chắc chắn đáng để khám phá khi bạn tiếp tục xây dựng các kỹ năng AI tổng quát của mình

và tìm cách tối ưu hóa hệ thống RAG của bạn.