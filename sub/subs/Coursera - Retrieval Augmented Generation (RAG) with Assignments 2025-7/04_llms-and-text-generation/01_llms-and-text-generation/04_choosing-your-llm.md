# 04 sự lựa chọn của bạn

---

Một quyết định quan trọng khi xây dựng ứng dụng RAG là bạn sẽ sử dụng LLM nào.

Có rất nhiều LLM có sẵn với các mức hiệu suất khác nhau, khả năng độc đáo,

và các hồ sơ chi phí khác nhau.

Việc chọn đúng thứ có thể có tác động lớn đến tốc độ, chất lượng và

ngân sách.

Vì vậy, hãy xem làm thế nào bạn có thể đưa ra lựa chọn phù hợp nhất với dự án của mình.

Hãy bắt đầu với một số khác biệt dễ dàng định lượng giữa các LLM.

Kích thước mô hình là số liệu được trích dẫn thường xuyên, thường được đo bằng bao nhiêu tỷ tham số

mô hình có.

Các mô hình nhỏ có thể có từ 1 đến 10 tỷ tham số, trong khi các mô hình lớn hơn có từ 100 đến

500 tỷ, có thể hơn nữa.

Các mô hình lớn hơn thường, nhưng không phải lúc nào cũng có nhiều khả năng hơn so với các mô hình nhỏ hơn,

nhưng chúng luôn đắt hơn để chạy.

Tất nhiên, chi phí là một yếu tố quan trọng.

Các nhà cung cấp LLM thường tính phí cố định cho mỗi triệu token, đôi khi

với các mức giá khác nhau cho mã thông báo đầu vào và đầu ra.

Nói chung, bạn có thể mong đợi các mẫu mới hơn, lớn hơn và có nhiều tính năng hơn sẽ có giá cao hơn.

Cửa sổ ngữ cảnh của mô hình cho bạn biết số lượng mã thông báo tối đa mà LLM có thể xử lý,

phân chia giữa cả lời nhắc và sự hoàn thành.

Mặc dù các giới hạn lớn mang lại sự linh hoạt hơn để có những lời nhắc và hoàn thành dài, nhưng bạn

vẫn trả tiền cho mỗi mã thông báo.

Thời gian nhận được mã thông báo đầu tiên và tốc độ, được biểu thị bằng mã thông báo trên giây, là một yếu tố quan trọng khác.

yếu tố.

Nếu hệ thống RAG của bạn phụ thuộc vào tương tác thời gian thực, bạn có thể sẵn sàng chấp nhận hiệu suất kém hơn

trong các lĩnh vực khác để có mô hình nhanh và có độ trễ thấp.

Ngày kết thúc đào tạo hoặc ngày kết thúc kiến thức của một mô hình sẽ cho bạn biết điểm cuối cùng

theo thời gian được biểu thị trong dữ liệu huấn luyện của mô hình.

Ngay cả trong hệ thống RAG, thời điểm cắt muộn hơn thường được coi là thích hợp hơn, đặc biệt là trong các bối cảnh

nơi người mẫu sẽ cần trả lời các câu hỏi về các sự kiện gần đây.

Mặc dù các số liệu có thể định lượng dễ dàng có thể giúp thu hẹp những mô hình mà bạn xem xét, nhưng thông thường

bạn quan tâm nhất đến chất lượng của một mô hình, điều này có thể khó định lượng hơn rất nhiều.

Chất lượng ở đây có nghĩa là mọi thứ từ khả năng suy luận của LLM thông qua các bài toán phức tạp,

để chỉ đơn giản là tạo ra văn bản dễ đọc.

Để giúp so sánh các mô hình trên tất cả các khía cạnh chất lượng khác nhau này, có một sự khác biệt đáng kinh ngạc.

một loạt các điểm chuẩn LLM có sẵn để cố gắng chấm điểm và so sánh các LLM.

Không có danh sách điểm chuẩn chính thức nào mà bạn có thể tham khảo, nhưng hãy hiểu rõ

nhiều tùy chọn có sẵn có thể giúp bạn chọn điểm chuẩn hiệu quả nhất

ý nghĩa cho dự án của bạn.

Điểm chuẩn có ba loại cấp cao, điểm chuẩn tự động, điểm chuẩn của con người và LLM

với tư cách là một thẩm phán.

Điểm chuẩn tự động chấm điểm LLM cho các nhiệm vụ có thể được đánh giá bằng mã.

Một dạng cổ điển cho loại điểm chuẩn này có thể là một bài kiểm tra trắc nghiệm trên một bài thi cụ thể.

lĩnh vực quan tâm hoặc một loạt các thách thức về toán học hoặc mã hóa trong đó các phản hồi của LLM

có thể được xác nhận dễ dàng bằng máy tính.

Một ví dụ điển hình về điểm chuẩn ở đây là MMLU hoặc Hiểu ngôn ngữ đa nhiệm lớn,

bao gồm 57 môn học từ STEM, nhân văn đến luật bằng phương pháp trắc nghiệm

các bài kiểm tra.

Điểm chuẩn máy tính kiểm tra LLM trên mọi thứ, từ các bài toán đến lý luận thông thường

câu hỏi.

Bạn sẽ thường xuyên thấy các nhà cung cấp LLM tiếp thị hiệu suất mô hình của họ dựa trên các điểm chuẩn này

và có thể tìm thấy thứ phù hợp với dự án của bạn.

Điểm chuẩn do con người đánh giá thường hoạt động bằng cách có hai LLM ẩn danh phản hồi

cùng một lời nhắc và yêu cầu người đánh giá chọn câu trả lời mà họ thích.

Những kết quả này được đưa vào cùng một thuật toán Elo được sử dụng để xếp hạng người chơi cờ, dẫn đến

bảng xếp hạng so sánh của LLM.

Một máy chủ phổ biến của loại hệ thống xếp hạng này được gọi là LLM Arena, có thứ hạng là một

trong số các tiêu chuẩn LLM được trích dẫn rộng rãi nhất.

Những thứ hạng do con người phân loại này nắm bắt các yếu tố chất lượng đa sắc thái giúp tự động hóa điểm chuẩn

không thể dễ dàng đo lường được.

Mặc dù các số liệu được tự động hóa và do con người phân loại thường giống nhau, nhưng khi điểm số của chúng khác nhau, điều đó

có thể làm nổi bật các sắc thái quan trọng trong hiệu suất của mô hình.

Điểm chuẩn LLM-với tư cách là thẩm phán sử dụng một LLM để đánh giá phản hồi của LLM khác đối với một bộ sưu tập

của câu hỏi kiểm tra.

Thẩm phán LLM có quyền truy cập vào một tập hợp các câu trả lời tham khảo và về cơ bản chỉ xác định cách thức

thường LLM được đánh giá sẽ đưa ra câu trả lời gần với câu trả lời đúng.

Điều này mang lại cho bạn tỷ lệ thắng có thể được sử dụng để so sánh LLM này với LLM khác.

Ưu điểm chính của LLM với tư cách là thẩm phán là đây là một cách tương đối rẻ và linh hoạt để đánh giá LLM.

Một nhược điểm của phương pháp này là thẩm phán cần phải được hiệu chỉnh cẩn thận vì

họ có xu hướng thích các câu trả lời từ nhóm mô hình ngôn ngữ của chính họ.

Ví dụ: các mô hình GPT từ OpenAI sẽ ưu tiên các mô hình GPT khác.

Những người mẫu Song Tử của Google sẽ thích những người mẫu Song Tử khác hơn.

Bằng cách hiệu chỉnh lại các mô hình có sẵn này, có thể giảm bớt sự thiên vị này.

Điểm chuẩn tốt có một vài phẩm chất.

Đầu tiên, chúng có liên quan đến dự án của bạn.

Nếu ứng dụng của bạn không bao giờ tạo mã, hãy so sánh LLM trên điểm chuẩn tạo mã

không giúp được gì nhiều

Tiếp theo, các điểm chuẩn cần phải khó khăn để thực hiện tốt công việc phân biệt giữa cao và

những mô hình có hiệu suất thấp.

Nếu mọi mô hình đều đạt điểm chuẩn tốt thì điều đó không hữu ích chút nào.

Điểm chuẩn phải có thể tái tạo được, nghĩa là bản thân điểm số không thay đổi đáng kể

giữa các lần chạy thử nghiệm và kết quả do nhà cung cấp mô hình trích dẫn phải được kiểm chứng.

Điểm chuẩn cũng phải phù hợp với hiệu suất trong thế giới thực.

Một LLM đạt điểm chuẩn lập trình tốt sẽ thực sự viết mã tốt trong thực tế.

Tại đây, bạn có thể cần phải đọc một số thông tin trên diễn đàn dành cho nhà phát triển để đảm bảo điểm chuẩn ở mức tốt

dấu hiệu của hiệu suất thực tế.

Một lý do khiến vấn đề này có thể phát sinh là ô nhiễm dữ liệu.

Các mô hình ngôn ngữ lớn được đào tạo trên hàng tỷ, nếu không muốn nói là hàng nghìn tỷ token được lấy từ

internet.

Có thể tập dữ liệu được điểm chuẩn sử dụng được bao gồm trong dữ liệu huấn luyện đó.

Trong trường hợp này, mô hình ngôn ngữ có thể hoạt động tốt hơn so với điểm chuẩn đó vì nó đã được nhìn thấy

các câu hỏi và câu trả lời chính xác trong quá trình đào tạo của mình.

Mặc dù điểm chuẩn có thể giúp bạn phân biệt giữa các mô hình nhưng chúng cũng chỉ nêu bật cách thức

toàn bộ lĩnh vực này đang phát triển nhanh chóng.

Đây là mẫu chung mà bạn sẽ thấy lặp lại trong hầu hết các đánh giá LLM.

Lúc đầu, điểm trung bình của mỗi môn khá thấp.

Sau đó, chỉ sau vài năm, việc các mô hình hoạt động ngang bằng với các chuyên gia về con người đã trở nên phổ biến.

Những điểm chuẩn này được gọi là bão hòa, nghĩa là chúng không còn giúp phân biệt giữa

các mô hình, vì hầu hết tất cả các mô hình tiên tiến đều đạt điểm gần tối đa.

Vào thời điểm đó, các tiêu chuẩn mới và thách thức hơn cần được đưa ra để đo lường một cách có ý nghĩa

cải thiện hiệu suất.

Tuy nhiên, những đánh giá mới đó sẽ nhanh chóng trở nên bão hòa và ngay cả những đánh giá mới hơn cũng sẽ

cần được giới thiệu.

Điều đáng rút ra ở đây là các mẫu ra mắt ngày nay thường tốt hơn đáng kể so với các mẫu

các mô hình thậm chí từ vài năm trước và bất kỳ mô hình nào bạn chọn hôm nay đều có thể sẽ

cần phải được thay thế khi các mô hình có khả năng hơn được giới thiệu nhanh chóng.

Chọn LLM phù hợp là một quyết định quan trọng nhưng tạm thời đối với cách bạn thiết kế

hệ thống giá đỡ.

Các yếu tố có thể định lượng dễ dàng như chi phí hoặc độ trễ có thể giúp thu hẹp lựa chọn của bạn và

nhiều số liệu chất lượng khác nhau có thể hướng bạn tới những mô hình tốt nhất phù hợp với trường hợp sử dụng của bạn.

Do tốc độ cải tiến của các mô hình, bạn nên lập kế hoạch hoán đổi dần dần

trong các mẫu mới được phát hành phù hợp với hệ thống giá đỡ của bạn.