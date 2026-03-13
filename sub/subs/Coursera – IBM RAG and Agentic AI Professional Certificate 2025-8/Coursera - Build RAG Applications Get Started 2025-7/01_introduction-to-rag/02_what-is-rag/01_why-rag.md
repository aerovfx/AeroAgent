# 01 tại sao-rag

---

Các mô hình ngôn ngữ lớn, chúng có ở khắp mọi nơi.

Họ hiểu được một số điều đúng một cách đáng ngạc nhiên và những điều khác lại rất sai một cách thú vị.

Tên tôi là Marina Danilevsky.

Tôi là nhà khoa học nghiên cứu cấp cao tại IBM Research,

và tôi muốn kể cho bạn nghe về một khuôn khổ

để giúp các mô hình ngôn ngữ lớn chính xác hơn và hiệu quả hơn

cập nhật, Thế hệ tăng cường truy xuất,

hoặc RAG.

Chúng ta hãy nói về phần thế hệ trong một phút.

Vì vậy, hãy quên việc truy xuất tăng cường.

Vậy thế hệ này đề cập đến các mô hình ngôn ngữ lớn,

hoặc LLM, tạo ra văn bản phản hồi

cho một truy vấn của người dùng được gọi là lời nhắc.

Những mô hình này có thể có một số hành vi không mong muốn.

Tôi muốn kể cho bạn một giai thoại để minh họa điều này.

Các con tôi gần đây đã hỏi tôi câu hỏi này,

trong hệ mặt trời của chúng ta, hành tinh nào có nhiều

mặt trăng?

Và câu trả lời của tôi là, ồ, thật tuyệt vời khi bạn

hỏi tôi câu hỏi này.

Tôi yêu không gian khi tôi bằng tuổi bạn.

Tất nhiên, đó là chuyện của 30 năm trước.

Nhưng tôi biết điều này.

Tôi đọc một bài báo và bài báo nói rằng đó là Sao Mộc và 88 mặt trăng.

Vì vậy, đó là câu trả lời.

Bây giờ, thực ra, có một vài điều sai trong câu trả lời của tôi.

Trước hết, tôi không có nguồn nào để hỗ trợ những gì tôi đang nói.

Vì vậy, mặc dù tôi đã tự tin nói nhưng tôi đã đọc một bài báo,

Tôi biết câu trả lời, tôi không tìm nguồn cung ứng

nó.

Vì vậy, đó là ngoài đỉnh đầu của tôi.

Ngoài ra, tôi thực sự đã không theo kịp điều này trong một thời gian.

Và câu trả lời của tôi đã lỗi thời.

Vì vậy, chúng tôi có hai vấn đề ở đây.

Một là không có nguồn.

Và vấn đề thứ hai là tôi đã lỗi thời.

Và trên thực tế, đây là hai hành vi thường xảy ra

được coi là có vấn đề khi tương tác

với các mô hình ngôn ngữ lớn.

Chúng là những thách thức LLM.

Bây giờ, điều gì sẽ xảy ra nếu tôi đánh bại

và đầu tiên đi tìm câu trả lời

trên một nguồn có uy tín như NASA?

Ồ, vậy thì tôi đã có thể nói, à, được rồi,

vậy câu trả lời là Sao Thổ với 146 mặt trăng.

Và trên thực tế, điều này liên tục thay đổi bởi vì các nhà khoa học

tiếp tục khám phá ngày càng nhiều mặt trăng.

Vì vậy, bây giờ tôi đã đưa ra câu trả lời của mình dựa trên điều gì đó đáng tin cậy hơn.

Tôi không hề bị ảo giác hay bịa ra một câu trả lời.

Ồ, nhân tiện, tôi không hề tiết lộ thông tin cá nhân

khoảng bao lâu rồi kể từ khi

Tôi bị ám ảnh bởi không gian.

Được rồi, vậy điều này có liên quan gì đến các mô hình ngôn ngữ lớn?

Chà, một mô hình ngôn ngữ lớn sẽ trả lời câu hỏi này như thế nào?

Giả sử tôi có một người dùng hỏi câu hỏi này về mặt trăng.

Một mô hình ngôn ngữ lớn sẽ tự tin nói: OK, tôi đã được đào tạo.

Và từ những gì tôi biết về các thông số của mình trong quá trình đào tạo,

câu trả lời là Sao Mộc.

Câu trả lời là sai, nhưng bạn biết đấy, chúng tôi không biết.

Mô hình ngôn ngữ lớn rất tự tin vào những gì nó trả lời.

Bây giờ, điều gì sẽ xảy ra khi bạn thêm phần tăng cường truy xuất này vào đây?

Điều đó có nghĩa là gì?

Điều đó có nghĩa là bây giờ, thay vì chỉ dựa vào những gì LLM biết,

chúng tôi đang thêm một nội dung

cửa hàng.

Điều này có thể được mở giống như internet.

Điều này có thể được đóng lại giống như một số bộ sưu tập tài liệu,

bộ sưu tập các chính sách, bất cứ điều gì.

Tuy nhiên, vấn đề bây giờ là LLM trước tiên sẽ hoạt động và

nói chuyện với cửa hàng nội dung và nói,

này, bạn có thể lấy từ tôi thông tin liên quan đến truy vấn của người dùng không

là?

Và bây giờ, với câu trả lời tăng cường cho chú chó tha mồi này, nó không còn là Sao Mộc nữa.

Chúng ta biết rằng đó là Sao Thổ.

Cái này trông như thế nào?

Chà, trước tiên, người dùng sẽ nhắc LLM bằng câu hỏi của họ.

Họ nói đây chính là câu hỏi của tôi.

Và ban đầu, nếu chúng ta chỉ nói chuyện với một mô hình sinh sản,

mô hình tổng quát nói,

ồ, được rồi, tôi biết câu trả lời.

Đây rồi.

Đây là phản hồi của tôi.

Nhưng bây giờ, trong khung RAM, mô hình tổng quát

thực ra có một hướng dẫn nói rằng,

không, không, không.

Đầu tiên, hãy đi và lấy nội dung có liên quan.

Kết hợp điều đó với câu hỏi của người dùng và chỉ sau đó tạo ra câu trả lời.

Vì vậy, lời nhắc bây giờ có ba phần, hướng dẫn thanh toán

chú ý đến nội dung được truy xuất

cùng với câu hỏi của người dùng.

Bây giờ hãy đưa ra phản hồi.

Và trên thực tế, bây giờ bạn có thể đưa ra bằng chứng giải thích tại sao

phản ứng là những gì nó được.

Vì vậy bây giờ, hy vọng bạn có thể thấy, RAD giúp ích như thế nào cho

hai thử thách LLM mà tôi đã gặp phải

đã đề cập trước đây?

Vì vậy, trước hết, tôi sẽ bắt đầu với phần lỗi thời.

Bây giờ, thay vì phải đào tạo lại mô hình của bạn nếu mới

thông tin xuất hiện, như, này, chúng tôi

tìm thấy thêm một số mặt trăng.

Bây giờ nó lại là Sao Mộc.

Có lẽ nó sẽ lại là Sao Thổ trong tương lai.

Tất cả những gì bạn phải làm là tăng cường kho dữ liệu của mình bằng những

thông tin, thông tin cập nhật.

Vì vậy, lần sau khi người dùng đến và đặt câu hỏi, chúng tôi đã sẵn sàng.

Chúng tôi chỉ cần tiếp tục và truy xuất thông tin cập nhật nhất.

Vấn đề thứ hai, nguồn.

Chà, mô hình LLM hiện đang được hướng dẫn trả

chú ý đến dữ liệu nguồn chính trước

đưa ra phản hồi của mình, và trên thực tế, bây giờ có thể đưa ra bằng chứng.

Điều này làm cho nó ít có khả năng bị ảo giác hoặc rò rỉ

dữ liệu vì nó ít có khả năng

chỉ dựa vào thông tin đã học được trong quá trình đào tạo.

Nó cũng cho phép chúng ta làm cho mô hình có một hành vi

điều đó có thể rất tích cực, điều đó

là biết khi nào nên nói, tôi không biết.

Nếu câu hỏi của người dùng không thể được trả lời một cách đáng tin cậy dựa trên

trên kho dữ liệu của bạn, mô hình

nên nói, tôi không biết, thay vì bịa ra điều gì đó

điều đó đáng tin cậy và có thể gây hiểu lầm

người dùng.

Tuy nhiên, điều này cũng có thể có tác động tiêu cực,

bởi vì nếu chó tha mồi không đủ

thật tốt khi mang lại mô hình ngôn ngữ lớn tốt nhất,

thông tin nối đất chất lượng cao nhất,

thì có thể truy vấn của người dùng có thể trả lời được sẽ không nhận được câu trả lời.

Đây thực sự là lý do tại sao nhiều người, trong đó có nhiều người trong chúng ta

ở đây tại IBM, đang giải quyết vấn đề

ở cả hai bên.

Cả hai chúng tôi đều đang nỗ lực cải thiện chú chó săn mồi để mang lại cho

mô hình ngôn ngữ lớn tốt nhất

dữ liệu chất lượng làm căn cứ cho phản ứng của mình, và cả

phần sinh sản để LLM

cuối cùng có thể mang lại phản hồi phong phú nhất, tốt nhất cho người dùng

khi nó tạo ra câu trả lời.

Cảm ơn bạn đã tìm hiểu thêm về RAG.