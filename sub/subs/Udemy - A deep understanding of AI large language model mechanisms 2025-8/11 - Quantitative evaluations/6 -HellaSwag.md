# 6 -HellaSwag đã dịch

---

Tôi chắc rằng bạn đang tò mò về tên tiêu đề trong video này.

Helliswag là từ viết tắt và tôi sẽ giải thích ý nghĩa của nó ở phần cuối của phần này

video.

Và trước đó, tôi sẽ cho bạn biết nó là gì và hiển thị bản demo mã về cách sử dụng nó.

Helliswag là bài kiểm tra đánh giá điểm chuẩn mà mọi người sử dụng cho LLM.

Nó khác với các eVals dựa trên mã thông báo như Proplexity.

Thay vào đó, nó giống như đưa ra một bài kiểm tra trắc nghiệm LLM trong đó câu trả lời đúng

phụ thuộc vào việc hiểu đúng cú pháp và ngữ pháp cũng như có được kiến thức thế giới về

một loạt các chủ đề.

Tôi sẽ chỉ cho bạn cách triển khai nó trong bản demo Python và tại đây bạn có thể xem một ví dụ

của hai câu hỏi kiểm tra.

Vì vậy, ý tưởng là chúng tôi trình bày mô hình với phần đầu tiên của văn bản được gọi là

bối cảnh.

Vì vậy, bối cảnh ở đây là, một người đàn ông có râu là một cảnh nói vào máy quay và thực hiện

một vài khuôn mặt, người đàn ông.

Được rồi, đó là bối cảnh.

Sau đó, có bốn kết thúc ứng cử viên, một trong số đó là đúng.

Trong ví dụ này, tùy chọn D được in đậm.

Vì vậy, mô hình được cung cấp bối cảnh và sau đó là tất cả các phần kết thúc, sau đó bạn tính toán

xác suất của mô hình liên quan đến mỗi kết thúc.

Nếu mô hình có xác suất kết thúc đúng cao nhất thì chúng ta xem xét

làm mẫu để trả lời đúng câu hỏi đó.

Và đó chính là điều mà điểm nhấn màu xanh lam này biểu thị ở đây.

Và bây giờ trong ví dụ này, câu trả lời đúng lại là D, nhưng mô hình đã đoán ra đáp án A.

Vì vậy, nó đã sai về mặt kỹ thuật ở đây.

Vì vậy, đó là ý tưởng chung.

Bây giờ, làm thế nào để chúng ta định lượng chính xác sự lựa chọn của mô hình cho từng lựa chọn trong số bốn lựa chọn này?

Đó là những gì bạn sẽ thấy trong bản demo Python.

Vì vậy tôi sẽ sử dụng phương tiện GPT2 ở đây.

Tôi sẽ chỉ cho bạn cách nhập tập dữ liệu Helliswag và một mục mẫu trông như thế này.

Vì vậy, phần CTX là bối cảnh.

Những kết thúc là bốn lựa chọn khác nhau, bốn kết thúc khác nhau.

Và nhãn ở dưới đây là chỉ mục của phần kết thúc đúng.

Vậy lựa chọn nào trong bốn lựa chọn này thực sự phù hợp với bối cảnh ở đây.

Đây là một sơ đồ minh họa cách hoạt động của việc định lượng.

Vì vậy, đối với ví dụ cụ thể này, có 21 mã thông báo trong ngữ cảnh.

Và các đường màu xanh lam và đỏ ở đây tương ứng với nhật ký đầu ra cuối cùng của mô hình cho

mã thông báo sắp tới.

Bây giờ có bốn phần cuối trong mỗi mẫu, nhưng ở đây tôi chỉ hiển thị phần cuối đúng

màu xanh lam và một trong những kết thúc sai có màu đỏ.

Bạn có thể thấy rằng xác suất mã thông báo cho các kết thúc chính xác nằm trên tất cả những điều này

mã thông báo cao hơn xác suất cho các kết thúc không chính xác.

Bây giờ đây là xác suất softmax cho từng mã thông báo riêng lẻ.

Vì vậy, có một số thực sự sẽ lớn hơn một.

Và trên thực tế, trong định lượng thực, xác suất log được sử dụng chứ không phải xác suất thực tế.

các giá trị xác suất.

Tôi sẽ tìm hiểu chi tiết hơn khi chuyển sang viết mã, nhưng về cơ bản đó chỉ là để giảm bớt

nguy cơ của các vấn đề số.

Và ở đây tôi đang hiển thị tổng, nhưng bạn thực sự cần nhân, nhân xác suất.

Và bởi vì những xác suất này thực sự rất nhỏ nên tích của chúng thậm chí còn nhỏ hơn.

Vì vậy, chúng tôi tính tổng các nhật ký thay vì nhân xác suất.

Dù sao, hãy chuyển sang mã và xem xét.

Dưới đây là các thư viện mà chúng tôi sẽ sử dụng.

Ở đây tôi đang nhập phương tiện GPT2.

Không có lý do đặc biệt nào khiến chúng ta cần sử dụng phương tiện trung bình thay vì nhỏ ở đây chỉ để cung cấp

một chút đa dạng.

Và ở đây tôi đang tải tập dữ liệu Helliswag bằng cách sử dụng các tiện ích được cung cấp bởi ôm

face, bao gồm cả hàm tải tập dữ liệu này.

Sự phân chia này ở đây có nghĩa là tôi sẽ chỉ thực hiện bộ xác thực.

Ngoài ra còn có một bộ đào tạo.

Nó lớn hơn rất nhiều.

Mặt khác nó cũng giống như vậy.

Nhưng vì trong video này, tôi chỉ hiển thị một đoạn mã nhỏ để bạn hình dung

về cách thức hoạt động của nó.

Chúng tôi thực sự chỉ cần một phiên bản nhỏ của tập dữ liệu này.

Được rồi.

Và ở đây bạn sẽ thấy một mẫu từ tập dữ liệu này, đó là những gì tôi đã hiển thị trong ảnh chụp màn hình

trong các slide.

Nhân tiện, bạn thực sự có thể chỉ cần bao gồm điều này.

Được rồi.

Vì vậy, ở đây, vâng.

Ở đây chúng ta thấy một người đàn ông đang ngồi trên mái nhà.

Anh ta đó là bối cảnh A và bối cảnh B. Yếu tố này ở đây bối cảnh CTX chỉ là hai bối cảnh

A và bối cảnh B kết hợp với nhau.

Vì vậy, tất cả những gì chúng ta thực sự cần là khóa ngữ cảnh này, khóa kết thúc này, là bốn tùy chọn

kết thúc và khóa nhãn này, cho chúng ta biết kết thúc chính xác.

Được rồi.

Vì vậy chỉ cần chọn ngẫu nhiên một.

Tôi chọn mẫu số 224.

Ở đây chúng tôi nhận được câu trả lời chính xác.

Tôi đang đặt nó thành một số nguyên chỉ để thuận tiện vì nó thực sự được mã hóa dưới dạng một chuỗi trong

tập dữ liệu.

Được rồi.

Vì vậy, sau đó tôi lấy bối cảnh và mã hóa nó và sau đó tôi nhận được phần kết thúc.

Và vâng, ở đây tôi chỉ hiển thị câu trả lời đúng và ba trừ câu trả lời đúng là

về cơ bản chỉ là đảm bảo rằng chúng ta sẽ nhận được một câu trả lời sai.

Tất nhiên trong thực tế bạn đánh giá cả bốn.

Ở đây nhằm mục đích trình diễn, tôi chỉ hiển thị cho bạn một câu trả lời đúng và một câu trả lời sai

câu trả lời.

Được rồi.

Vì vậy, điều này chưa là gì với mô hình.

Đây chỉ là mã thông báo và hiển thị văn bản cho hai tùy chọn.

Tất nhiên, đây là nơi tôi đẩy mã thông báo vào mô hình trên GPU.

Và những gì tôi muốn lấy lại là nhật ký của họ.

Và sau đó tôi đang softmaxing hoặc log softmaxing các bản ghi.

Sau đó, tôi lặp lại và lấy logic cho từng mã thông báo sắp tới.

Vì vậy, điều này luôn có một chút khó khăn khi bạn làm việc với kiến trúc GPT trong đó

bạn đang cố gắng dự đoán mã thông báo tiếp theo theo trình tự.

Điều bạn thực sự muốn là các bản ghi trước mã thông báo trong chuỗi mã thông báo vì

Ý tưởng là khi mô hình đang xử lý từng mã thông báo, nó sẽ chuyển đổi mã thông báo đó thành

dự đoán cho token tiếp theo.

Vì vậy, bạn không muốn xử lý mã thông báo tiếp theo.

Bạn muốn kết quả cuối cùng của việc xử lý mã thông báo hiện tại và điều đó sẽ dự đoán

mã thông báo tiếp theo.

Được rồi.

Vì vậy, đây là toàn bộ chuỗi dấu nhắc đúng và toàn bộ chuỗi dấu nhắc sai

nhắc nhở.

Bây giờ cả hai lời nhắc đó, đúng và sai, lúc đầu đều giống hệt nhau.

Đó là bối cảnh.

Bối cảnh ban đầu hoàn toàn giống nhau đối với hai tùy chọn này và chúng chỉ khác nhau bởi

kết thúc này.

Vì vậy, chúng ta không cần tính toán bất kỳ nhật ký nào cho ngữ cảnh vì chúng sẽ chính xác

giống nhau.

Thay vào đó, chúng tôi xử lý hoặc tổng hợp nhật ký cho tất cả các mã thông báo ở hai phần cuối.

Vì vậy, trong trường hợp này, đó là đường màu xanh và đường màu đỏ.

Bây giờ bạn có thể thấy không phải trường hợp người mẫu luôn dự đoán đúng cái kết ở trên đâu

kết thúc sai.

Vì vậy, trong mã thông báo cụ thể này, mô hình thực sự đã dự đoán mã thông báo cho mã không chính xác.

Vì vậy, đó là mặc trên chéo.

Vì vậy, sẽ khá hợp lý khi bạn nhìn vào điều này, bạn sẽ nói rằng một người đàn ông mặc đồ sẽ đẹp hơn.

có khả năng hơn là một người đàn ông chéo, đặc biệt là vì điều này sai ngữ pháp.

Đáng lẽ phải nói một người đàn ông băng qua đường.

Trên thực tế, đây là một trong những hạn chế của bộ dữ liệu này mà tôi sẽ thảo luận khi chuyển đổi

quay lại các slide rằng tập dữ liệu này có một số lỗi chính tả và một số lỗi ngữ pháp kỳ lạ.

Vì vậy, không có gì ngạc nhiên khi mô hình này thực sự mang lại tính logic cao hơn cho việc đeo so với

chéo.

Tuy nhiên, khi chúng tôi xem xét tất cả các mã thông báo cho toàn bộ phần kết, chúng tôi thấy rằng

tổng số log sẽ cao hơn đối với kết thúc đúng và thấp hơn đối với kết thúc sai

kết thúc tổng thể khi chúng ta xem xét tất cả các mã thông báo cùng nhau.

Bây giờ tại sao tôi lại tổng hợp nhật ký softmax mà không chỉ xác suất softmax thông thường

nếu chúng ta muốn có được xác suất của toàn bộ phần kết?

Vì vậy chúng ta có thể hình dung được điều đó.

Tôi thực sự thích hình dung đó hơn.

Tôi nghĩ hình ảnh trực quan trông đẹp hơn.

Vì vậy, nếu tôi loại bỏ nhật ký đó ở đây và tôi chỉ có softmax, chúng ta sẽ thấy đó chính xác là

cùng một câu.

Mọi thứ đều giống nhau.

Chỉ là bây giờ đây là những xác suất thay vì xác suất log softmax.

Như tôi đã đề cập trong các slide, những con số này không tổng bằng một, chúng tổng bằng một số nào đó

hơn một.

Và đó là bởi vì mỗi một token riêng lẻ này đều đến từ một phân bố xác suất

trên tất cả 50.000 token cho chỉ số token này.

Vì vậy xác suất softmax không vượt quá vị trí mã thông báo này.

Vượt quá 50.000 token trong vocab được tính riêng cho từng cá nhân

mã thông báo.

Và đó là lý do tại sao những con số này không có tổng bằng một.

Tuy nhiên, khi chúng ta tìm xác suất chung của toàn bộ câu này, thì đó là

xác suất của mỗi mã thông báo này được chọn.

Bạn không tổng hợp các xác suất.

Bạn phải nhân xác suất lên.

Và những xác suất này có thể rất nhỏ.

Chúng có thể thực sự rất gần bằng không.

Và do đó, bạn nhân những số càng nhỏ, cực nhỏ mà thực sự gần bằng 0, thì tích

sẽ cực kỳ nhỏ đến mức về cơ bản bạn đang làm việc tại hoặc thậm chí có thể thấp hơn

độ chính xác của máy tính của bạn.

Vì vậy, việc nhân các xác suất rất nhỏ sẽ trở nên rất không ổn định về mặt số lượng.

Và đó là lý do tại sao việc tính tổng các nhật ký lại ổn định hơn nhiều về mặt số lượng.

Nên tôi phải nói là tôi thích, tôi chỉ thấy bằng trực quan, tôi nghĩ xác suất

có chút rõ ràng.

Nhưng về mặt toán học, đó thực sự không phải là điều tối ưu nên làm.

Điều tốt hơn nên làm là tính tổng các nhật ký thay vì nhân xác suất.

Vì vậy, đây là mô tả trực quan về cách hoạt động của phân tích Helliswag đối với một cặp.

Vì vậy, để có một câu trả lời đúng.

Và bây giờ đoạn mã ở dưới đây sẽ lặp qua tất cả bốn tùy chọn để về cơ bản

lặp lại phân tích mà không cần trực quan hóa và nhận được câu trả lời cho mô hình từ bốn điều đó

tùy chọn.

Vì vậy, ở đây tôi đang chọn một ví dụ khác từ ví dụ tập dữ liệu số 42 này, chọn hoàn toàn

một cách ngẫu nhiên.

Tôi không biết con số này có ý nghĩa gì.

Và hãy xem.

Vì vậy, ở đây tôi chỉ trích xuất ngữ cảnh, độ dài ngữ cảnh để chúng ta chỉ đi tới

tổng hợp các nhật ký hoặc xác suất softmax của nhật ký cho các phần cuối chứ không phải cho toàn bộ chuỗi.

Và ở đây tôi đang nhận được câu trả lời thực sự.

Vì vậy, đây là chỉ số của câu trả lời đúng.

Và sau đó hãy xem tất cả mã này.

Vì vậy, bên trong vòng lặp for ở đây, tất cả đoạn mã này bạn đã thấy trước đây.

Thực ra cái này bạn cũng đã từng thấy trước đây.

Đây thực sự chỉ là sao chép, sửa đổi một chút trong mã trước đó, cao hơn một chút

lên.

Tôi đã viết nó dưới dạng vòng lặp for và ở đây tôi viết nó dưới dạng hiểu danh sách.

Nhưng về cơ bản, tất cả mã này bạn đã thấy trước đây, tất cả những gì tôi đang làm là trích xuất

nhắc, mã hóa nó, đẩy nó qua mô hình và tính tổng trên tất cả

của xác suất log softmax.

Và sau đó là vòng lặp for, vì vậy sau khi tôi đã xem hết tất cả bốn phần cuối tùy chọn đó,

chúng ta có thể thấy liệu mô hình có đúng hay không.

Vì vậy, trong trường hợp này, phần kết thúc có khả năng ghi nhật ký lớn nhất, khả năng ghi nhật ký tổng hợp, bằng nhau

câu trả lời đúng và do đó mô hình đã đúng.

Vì vậy, chúng ta thực sự có thể nhìn vào những giá trị này.

Đó là những chiếc mũ trùm đầu có khả năng bằng gỗ.

Và hãy xem.

Vì vậy, câu trả lời là ba.

Được rồi, vậy là âm 175 cao hơn bất kỳ số nào trong số này.

Và hãy xem ví dụ.

Các chàng trai nói chuyện, cười đùa và trêu chọc nhau trước khi bắt đầu trò chơi beer pong, blah, blah,

bla.

Một trong những quả bóng bàn bị lật ngược khiến các thiếu niên khác phải lấy từng quả

đập tay khác.

Ý tôi là, vấn đề là điều đó cũng có thể đúng.

Nhưng hóa ra câu trả lời đúng theo bộ dữ liệu này là nằm trong một chiếc cốc.

Và một trong những chàng trai bắt đầu uống bia.

Bây giờ, để biết đây là câu trả lời đúng, bạn cần có kiến thức toàn cầu về

trò chơi beer pong.

Bạn cần biết trò chơi đó hoạt động như thế nào.

Mặt khác, không thực sự rõ ràng kết thúc nào trong số những kết thúc này sẽ đúng.

Vì vậy, đó là lý do tại sao đây là một phương pháp đánh giá thú vị vì nó không chỉ cho chúng ta biết về

khả năng của mô hình trong việc xử lý các mã thông báo riêng lẻ và chuỗi mã thông báo, nhưng cũng

về kiến thức thế giới của mô hình, sự hiểu biết của mô hình về nhiều vấn đề khác nhau

chủ đề về thế giới.

Trong slide này, tôi sẽ thảo luận về một số hạn chế của Helliswag.

Đầu tiên, nó yêu cầu hiệu suất cụ thể của miền trong thử nghiệm.

Vì vậy, giả sử bạn có một mô hình được tinh chỉnh để giúp bạn viết các bài đăng trên LinkedIn.

Và có thể đó là một mô hình tuyệt vời.

Và nó thậm chí còn tốt hơn GPT trò chuyện mới nhất, nhưng nó hoạt động kém trên Helliswag vì

bạn chưa đào tạo người mẫu của mình để biết về quảng cáo cạo râu dành cho nam giới và trò chơi ném bia và

các chủ đề bí truyền khác mà tập dữ liệu Helliswag bao gồm.

Và một vấn đề chung với các phương pháp eval là khi một tập huấn luyện được xuất bản và một

mô tả của đánh giá là kiến thức công cộng.

Các công ty phát triển LLM có thể bắt đầu tinh chỉnh các mô hình của họ về đào tạo và

tập phát triển và trên các văn bản khác tương tự như tập kiểm tra.

Vì vậy, ngay cả khi nhóm Helliswag giấu bộ thử nghiệm của họ, LLM vẫn có thể hoạt động tốt

chuẩn bị cho nó.

Điều này cũng giống như khi bạn ôn thi bằng cách vượt qua các bài thi trước đó trong kỳ thi.

cùng một chủ đề.

Bây giờ bạn có thể không biết chính xác các câu hỏi thi mà bạn sẽ gặp, nhưng nếu bạn học nhiều

trong các kỳ thi tương tự, bạn có thể làm tốt hơn.

Vì vậy, điều đó có nghĩa là các phương pháp đánh giá này thường ít biểu thị khả năng của mô hình thực tế hơn

sau một vài năm.

Và vâng, như bạn đã thấy, nếu bạn xem qua tập dữ liệu này, bạn sẽ tìm thấy một số lỗi chính tả, một số

lỗi ngữ pháp và một số câu dường như không có nhiều ý nghĩa.

Vì vậy, nó không phải là một tập dữ liệu siêu sạch.

Bây giờ có những nhóm khác đã cố gắng cải thiện việc đánh giá Helliswag và

mỗi năm đều có những đánh giá mới liên quan đến ý tưởng của Helliswag

được phát hành, nhưng Helliswag vẫn là một bài kiểm tra điểm chuẩn khá chuẩn.

Được rồi, chúng ta bắt đầu thôi.

Những cái kết khó hơn, bối cảnh dài hơn, những hoạt động khó khăn hơn cho những tình huống có đối thủ

nhiều thế hệ.

Tôi chắc chắn 99,99% rằng các tác giả đã quyết định đầu tiên rằng họ muốn gọi nó là Helliswag

và sau đó họ phải nghĩ ra một số từ có âm thanh lạ mắt phù hợp với các chữ cái đó.

Được rồi, bây giờ bạn đã quen thuộc với hai nhóm đánh giá định lượng, những nhóm dựa trên

xử lý các mã thông báo riêng lẻ và các mã thông báo dựa trên chuỗi xử lý mã thông báo.

Không có phương pháp nào là hoàn hảo vì ngôn ngữ phức tạp và cẩu thả và vì LLM đang được

phát triển nhanh hơn nhiều so với việc đánh giá các LLM đó.