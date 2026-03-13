# 03 chiến lược lấy mẫu llm

---

Một phần quan trọng khi làm việc với LLM là hiểu và kiểm soát tính ngẫu nhiên cốt lõi

về cách họ vận hành.

Trong video này, chúng ta hãy xem API LLM điển hình và khám phá các tùy chọn khác nhau

họ cung cấp để kiểm soát cách LLM của bạn chọn mã thông báo tiếp theo.

Mỗi mã thông báo mà một mô hình ngôn ngữ lớn thêm vào khi bạn hoàn thành đều là một lựa chọn ngẫu nhiên có trọng số.

Nếu bạn sử dụng mô hình ngôn ngữ lớn nguồn mở, bạn có thể thấy lựa chọn này được thực hiện như thế nào.

Các mô hình này sẽ cho bạn thấy xác suất mã thông báo được tạo ở mỗi bước, được sử dụng để

chọn mã thông báo tiếp theo.

Ví dụ: đối với dấu nhắc, bầu trời là như thế này, phân bố xác suất trông như thế này

thích.

Màu xanh lam có 50% khả năng xuất hiện tiếp theo, màu sáng có xác suất 25% và các màu khác

mã thông báo có 10% trở xuống, nhanh chóng giảm xuống dưới 1%.

Đây là hình ảnh trực quan của bản phân phối đó.

Khi đường cong có phần nhọn cao ở phía bên trái, bạn có thể nói người mẫu đã tự tin

theo lựa chọn của mình, chỉ với một hoặc có thể một vài mã thông báo khác có cơ hội thực sự

đang được chọn.

Mặt khác, sự phân bổ phẳng hơn như thế này có thể được hiểu là sự không chắc chắn.

Mô hình có nhiều hướng khả thi, nó có thể được hoàn thiện tiếp theo nhưng chưa rõ ràng

người chiến thắng.

Giải mã và kiểm soát đường cong phân phối này là một phần quan trọng trong cách bạn điều chỉnh LLM của mình

hành vi.

Vì vậy, hãy xem xét một vài chiến lược để làm điều này.

Một cách tiếp cận đơn giản là hướng dẫn LLM không thực sự đưa ra lựa chọn ngẫu nhiên và

chỉ cần luôn chọn mã thông báo có xác suất cao nhất.

Điều này được gọi là giải mã tham lam.

Ưu điểm chính của giải mã tham lam là nó làm cho LLM mang tính quyết định.

Nếu bạn cung cấp cho mô hình của mình cùng một lời nhắc, nó sẽ luôn tạo ra cùng một phản hồi.

Nhược điểm chính của việc giải mã tham lam là nó có thể dẫn đến văn bản có thể đoán trước được.

Những người chuyên nghiệp cuối cùng có thể cảm thấy chung chung hoặc thậm chí cứng nhắc.

Một vấn đề khác với giải mã tham lam là LLM đôi khi sẽ gặp khó khăn khi tạo ra

cùng một chuỗi từ lặp đi lặp lại.

LLM không thực sự quan tâm liệu việc hoàn thành tổng thể có hợp lý hay không.

LLM chỉ tiếp tục chọn mã thông báo tiếp theo có khả năng cao nhất và khi mô hình rơi vào tình trạng

một vòng lặp lặp đi lặp lại, không có cơ chế nào để thoát ra khỏi nó.

Bất chấp những hạn chế tiềm tàng này, việc giải mã tham lam có thể có ý nghĩa trong những trường hợp

mong muốn có được đầu ra mang tính xác định và có thể dự đoán cao, chẳng hạn như hoàn thành mã hoặc thậm chí

như một cài đặt tạm thời để gỡ lỗi hệ thống của bạn.

Trong hầu hết các trường hợp, bạn không muốn loại bỏ hoàn toàn tính ngẫu nhiên.

Bạn chỉ muốn kiểm soát nó.

Tham số được sử dụng rộng rãi nhất để kiểm soát tính ngẫu nhiên của LLM được gọi là nhiệt độ.

Bạn có thể hình dung nhiệt độ giống như một chiếc đồng hồ làm thay đổi hình dạng của phân bố xác suất.

được tạo bởi LLM của bạn.

Nhiệt độ mặc định là 1 chỉ cung cấp cho bạn phân phối ban đầu.

Nhiệt độ thấp hơn dẫn đến sự phân bổ có nhiều đột biến hơn, chỉ với những token có khả năng xảy ra cao nhất

có bất kỳ cơ hội nào được tạo ra.

Thứ tự của các mã thông báo không thay đổi, nhưng xác suất được chọn của chúng thì có.

Việc đặt nhiệt độ xuống hết mức 0 sẽ đặt mô hình thực hiện giải mã tham lam,

chỉ có một mã thông báo có khả năng xảy ra cao nhất có xác suất 100%.

Tăng nhiệt độ lên một chút, ví dụ trong khoảng từ 1,1 đến 1,3, sẽ làm phẳng nhiệt độ.

phân phối xác suất, mang lại cho các mã thông báo không chắc chắn có thêm một chút cơ hội được chọn.

Điều này dẫn đến văn bản nghe có vẻ đa dạng hơn và đôi khi thú vị hơn hoặc thậm chí sáng tạo hơn.

Đặt nhiệt độ quá cao sẽ dẫn đến phân bố xác suất rất phẳng.

Tất cả các token sẽ có cơ hội được chọn như nhau, ngay cả khi chúng không đạt được điều đó

nhiều ý nghĩa.

Dù bạn đặt LLM ở nhiệt độ nào thì đường cong phân phối đó vẫn sẽ có

đuôi dài chạy ra bên phải.

Chứa đầy những mã thông báo vô nghĩa, LLM của bạn có rất ít khả năng được lựa chọn.

Để giúp kiểm soát điều này, một số kỹ thuật lấy mẫu bổ sung được sử dụng.

Lấy mẫu Top k là đơn giản nhất và giới hạn LLM trong việc chọn từ k mã thông báo có khả năng xảy ra cao nhất.

Ví dụ: bạn có thể vừa đặt nhiệt độ là 1,1 nhưng cũng giới hạn LLM trong việc chọn

từ 5 token tiếp theo có nhiều khả năng xảy ra nhất.

Một cách tiếp cận tương tự được gọi là lấy mẫu p hàng đầu, giới hạn LLM trong việc chọn mã thông báo có

xác suất tích lũy giảm xuống dưới một ngưỡng nào đó.

Ví dụ: bạn có thể đặt p cao nhất là 85%.

Bạn sẽ bắt đầu từ phía bên trái của phân phối này và tiếp tục cộng các xác suất

của mỗi mã thông báo cho đến khi tổng số lớn hơn 85%.

Top p có xu hướng phản ứng nhanh hơn hoặc năng động hơn trong hai cách tiếp cận.

Trong top k, LLM luôn chọn từ cùng một nhóm mã thông báo, bất kể hình dạng của

sự phân phối.

Với p hàng đầu, nếu LLM khá chắc chắn, nghĩa là một số mã thông báo có xác suất rất cao,

LLM sẽ giới hạn các lựa chọn của mình ở một số mã thông báo có khả năng xảy ra nhất.

Thay vào đó, nếu LLM không chắc chắn hơn, nghĩa là phân phối không đổi, không có điều tốt nhất rõ ràng.

lựa chọn, LLM được phép chọn từ nhóm mã thông báo tiềm năng lớn hơn nhiều.

Một số kỹ thuật cũng nhắm vào xác suất của các từ riêng lẻ thay vì tổng thể

hình dạng của sự phân bố.

Ví dụ: các mô hình ngôn ngữ lớn có thể có xu hướng sử dụng nhiều lần cùng một từ

hoặc cụm từ có thể nghe không tự nhiên.

Nhiều LLM cho phép bạn áp dụng hình phạt lặp lại, điều này làm giảm xác suất

của những từ đã xuất hiện trong phần hoàn thành.

Điều này có thể làm cho văn bản thu được có âm thanh tự nhiên và đa dạng hơn.

Hầu hết LLM cũng cho phép bạn tăng hoặc giảm xác suất của các mã thông báo cụ thể, thường là

được gọi là xu hướng logit.

Sự thiên vị này sẽ điều chỉnh vĩnh viễn xác suất được chọn tăng hoặc giảm của các mã thông báo đó.

Nếu bạn biết bạn không muốn hệ thống RAG của mình tạo ra ngôn từ tục tĩu, bạn có thể thiên vị một số

lời nói xuống.

Mặt khác, nếu hệ thống RAG của bạn là một bộ phân loại được thiết kế để xuất ra một trong số ít

các danh mục, bạn có thể tăng xác suất của các danh mục đó để đảm bảo LLM luôn

lựa chọn giữa chúng.

Đây là lệnh gọi API kết hợp nhiều kỹ thuật bạn đã thấy trong video này.

Đây là sự kết hợp khá hợp lý, có mục đích chung của các thông số, nhiệt độ

0,8, p cao nhất là 0,9 và hình phạt lặp lại là 1,2.

LLM này sẽ thận trọng hơn một chút trong việc lựa chọn mã thông báo của nó, tránh việc chọn từ

phần cuối của đợt phân phối và phạt nhẹ các mã thông báo lặp lại.

Bằng cách thử nghiệm từng tham số, bạn có thể điều chỉnh hành vi của LLM cho

bối cảnh của ứng dụng của bạn.

Có rất nhiều kỹ thuật sẵn có để kiểm soát tính ngẫu nhiên vốn có trong

LLM và video này chỉ đề cập đến một số lựa chọn phổ biến nhất.

Nói chung, tôi khuyên bạn nên đặt nhiệt độ và mức p phù hợp nhất với nhu cầu của bạn.

Nếu bạn đang tạo mã hoặc trả lời các câu hỏi thực tế, nhiệt độ thấp hơn và nhiệt độ thấp hơn

top p có ý nghĩa.

Nếu bạn đang hoạt động trong một lĩnh vực sáng tạo hơn, nhiệt độ cao hơn và p cao hơn có thể mang lại

LLM của bạn có giai điệu thú vị và mang tính khám phá hơn.

Sau đó, hãy xem xét đưa ra các hình phạt lặp lại, sai lệch logit hoặc các hình thức lấy mẫu khác.

các kỹ thuật bạn nghiên cứu để giải quyết các vấn đề cụ thể mà bạn xác định về cách thức hoạt động của LLM của bạn.

Cuối cùng, hiểu rằng có nhiều cách để điều chỉnh các lựa chọn ngẫu nhiên của LLM và

lặp đi lặp lại các cài đặt phù hợp với dự án của bạn sẽ mang lại cho bạn hiệu suất

bạn cần.