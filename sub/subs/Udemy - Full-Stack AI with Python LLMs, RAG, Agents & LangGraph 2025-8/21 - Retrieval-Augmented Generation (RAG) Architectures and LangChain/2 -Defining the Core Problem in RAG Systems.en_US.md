# 2 -Xác định vấn đề cốt lõi trong RAG Systems.en US

---

Được rồi, vậy trước tiên hãy hiểu

phát biểu vấn đề.

Ý tôi là, tuyên bố vấn đề là gì

RAG đang cố giải quyết phải không?

Vì vậy, hãy tưởng tượng rằng bạn

làm việc với một doanh nghiệp lớn

doanh nghiệp hay bất kỳ loại hình kinh doanh nào.

Và trong kinh doanh, bạn làm gì

có là bạn có rất nhiều dữ liệu.

Bạn có rất nhiều dữ liệu trong biểu mẫu

của tài liệu, ở dạng tệp PDF.

Có thể nó nằm trong cơ sở dữ liệu của bạn

hoặc bất kỳ định dạng nào, phải không?

Vì vậy, chỉ để đơn giản,

hãy lấy một ví dụ

rằng bạn có tất cả dữ liệu

ở dạng tệp PDF.

Vậy là có kinh doanh phải không?

Có lẽ đó là một công việc kinh doanh hợp pháp,

một doanh nghiệp luật sư, phải không?

Và họ có rất nhiều

của những tài liệu này.

Điều đó thực sự tuyệt vời.

Bây giờ họ muốn làm gì?

Hãy để chúng tôi nói rằng doanh nghiệp nói rằng,

này, chúng ta có rất nhiều dữ liệu phải không?

Rất nhiều dữ liệu văn bản.

Và rất khó để đọc chúng.

Rất khó để đi được chúng,

đi qua từng từ một.

Điều đó rất khó khăn đối với một con người

để xem nội dung là gì

có sẵn trong tập tin nào.

Vì vậy, đó là rất nhiều quá trình thủ công.

Điều họ muốn ở bạn là

đó, này, bạn có thể bằng cách nào đó

xây dựng cho chúng tôi một đặc vụ AI?

Bởi vì bây giờ AI đã có, phải không?

Bạn có thể trò chuyện với GPT, bạn có thể

trò chuyện với các mô hình LLM này.

Vậy hãy nói rằng

có một mô hình LLM.

Vì vậy, tôi sẽ chỉ lấy một ví dụ.

Hãy nói OpenAI.

Và về cơ bản điều họ muốn là,

này, chúng ta có rất nhiều người dùng phải không?

Chúng tôi có rất nhiều nhân viên.

Chúng tôi thực sự không muốn nhân viên của mình

để xem qua các tập tin này từng cái một

một vì nó tốn thời gian.

Họ, về cơ bản họ có thể hỏi

Trò chuyện GPT về điều gì đó, phải không?

Họ có thể nói, này, bạn có thể không, vì

Ví dụ: truy vấn của người dùng có thể được, bạn có thể

cho tôi biết về số vụ án nhé?

Giả sử là 32.

Vậy có vụ án số 32, được chứ?

Về một số trường hợp.

Tôi đã viết sai chính tả rất nhiều thứ.

Trường hợp số 32.

Vậy bây giờ xem nhé, Chat GPT không biết

trường hợp số 32 là gì phải không?

Dữ liệu công khai của ChatGPT không có

bối cảnh về điều này.

Vậy điều họ phải làm là

về cơ bản là Chat GPT.

Bạn phải bằng cách nào đó nói với Chat GPT

này, tôi có bộ hồ sơ này,

Tôi có sẵn rất nhiều tập tin

từ những tập tin có sẵn này phải không?

Từ những thứ có sẵn

các tập tin, bạn phải tìm kiếm cái đó

là nội dung có liên quan.

Nội dung liên quan đó ở đâu

truy vấn cụ thể này, Chat GPT

hoặc tôi thực sự nên nói LLM.

Được rồi, tôi không nên nói ChatGPT.

LLM phải đủ thông minh

để đọc tất cả các tập tin

để thực sự hiểu được bối cảnh.

Và về cơ bản người dùng đã hỏi những gì

có thể trả lời nó ở định dạng tốt hơn

này, tôi biết về trường hợp số 32.

Nó ở giữa đảng này và đảng này.

Đúng vậy, và hiện tại

trạng thái là thế này.

Và tôi đã nhận được thông tin này

từ tập tin cụ thể này.

Ý tôi là, chúng ta hãy nói ở đó

bạn biết đấy, có 1.000 tập tin.

Có 1.000 tập tin.

Và trò chuyện gì, LLM của bạn có gì

xong, thứ nhất, nó thực sự đã

đã cho bạn câu trả lời thích hợp

về điều bạn đã hỏi.

Ngoài ra nó còn mang lại cho bạn

số trang có liên quan

từ đây tôi hiểu rồi

trong trường hợp người dùng quan tâm,

anh ấy có thể đi qua trang này.

Vì vậy, đây là một vấn đề điển hình.

Vấn đề là, số một,

LLM, đúng rồi, LLM thì không

có bối cảnh về dữ liệu của bạn.

Được rồi?

Vì thế ở đây tôi muốn nhấn mạnh

về một điều đó là về

đó là dữ liệu của bạn.

Nó được huấn luyện trên dữ liệu

có sẵn trên Internet một cách công khai,

nhưng nó không có bối cảnh về

dữ liệu riêng tư của bạn, đó là

ở dạng tập tin, số một.

Điều thứ hai là vấn đề

đó là giả sử nếu bạn có

1.000 file, bạn không thể đưa hết

1.000 tệp này làm bối cảnh,

như một lời nhắc hệ thống tới LLM,

bởi vì có một bối cảnh

cửa sổ.

Bạn chỉ có thể cho ăn, bạn biết đấy,

một cửa sổ ngữ cảnh hạn chế.

Vì vậy không thể nào bạn

bạn biết đấy, chỉ có thể đọc tất cả

1000 tập tin này và cung cấp tất cả

ngay lập tức đến LLM và sau đó

xử lý truy vấn của người dùng.

Ý tôi là, nếu bạn đang làm điều này, bạn

về cơ bản họ đang làm việc đó cho mọi người

truy vấn, mỗi khi người dùng hỏi một

câu hỏi, bạn phải cung cấp tất cả

1000 tệp vào LLM và xử lý

nó, về mặt kỹ thuật thì không

có thể.

Và thậm chí nếu có thể, nó

sẽ rất tốn kém.

Vì vậy đây là vấn đề điển hình mà

chúng ta sẽ giải quyết bằng giẻ rách.