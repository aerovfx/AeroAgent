# 04 - Demo Tích hợp mọi thứ vào giải pháp của chúng tôi

---

- [Người hướng dẫn] Trong bản demo cuối cùng này, tôi sẽ cho bạn thấy

cách tạo một chatbot

sử dụng ba mô hình mà chúng tôi đã đào tạo.

Vì vậy, trước tiên, hãy kết nối với GPU.

Và chúng tôi ở đó,

mặc dù chúng tôi không thực sự cần GPU cho việc này,

nó chỉ để làm cho nó chạy nhanh hơn.

Chúng tôi sẽ thực hiện cài đặt pip như trước đây,

bao gồm cả Flask, vì Flask sẽ là framework

mà chúng tôi sẽ sử dụng cho chatbot của mình.

Vì vậy, bây giờ đến phần quan trọng.

Chatbot của chúng tôi sẽ chạy trên một quy trình riêng trong Colab.

Lý do làm điều này chỉ là vì lợi ích

cũng có thể đưa ra yêu cầu

vào cuộc trò chuyện trong cùng một Colab.

Nếu bạn không muốn làm điều đó,

bạn không cần phải viết một tập tin riêng biệt mới.

Được rồi?

Vì vậy, trong tập lệnh này sẽ tải chatbot của chúng ta,

chúng tôi sẽ thực hiện việc nhập khẩu.

Sau đó, hãy lưu ý rằng chúng ta sẽ tải mô hình tình cảm.

Tình cảm_model là một trong đó đã được tinh chỉnh

chính xác giống như cách bạn đã làm với tập dữ liệu SS2,

nhưng trong thời gian dài hơn.

Để tóm tắt và qa_model,

thay vì sử dụng những cái chúng tôi đã đào tạo

có rất ít dữ liệu,

để có kết quả tốt hơn, chúng tôi sẽ sử dụng flan-t5-large.

Tuy nhiên, nếu bạn muốn sử dụng mô hình của mình, bạn chỉ cần vào đây

và chỉ cần đặt my_model_directory.

Và thế là xong. Nó chỉ hoạt động.

Và bạn đã tải mô hình của mình. Vì vậy, nó thật dễ dàng.

Và cuối cùng, để trả lời chung chung,

chúng ta sẽ sử dụng mô hình chỉ dành cho bộ giải mã tạo văn bản.

Trong trường hợp này, chúng tôi sẽ sử dụng GPT-2

đó là một mô hình nguồn mở.

Đối với ứng dụng của chúng tôi, chúng tôi sẽ lưu trữ tất cả các bản tóm tắt

của các cuộc trò chuyện và lịch sử cuộc trò chuyện.

Vì vậy, khi chúng ta muốn tóm tắt một cuộc trò chuyện,

điều chúng ta cần làm là tập hợp tất cả lại với nhau trong một dấu nhắc,

đặt Tóm tắt,

và như mọi khi, chuyển nó qua công cụ mã thông báo,

tóm tắt_model.generate,

và sau đó chúng tôi giải mã, thế là xong.

Nếu chúng ta muốn tóm tắt một tin nhắn

bởi vì chúng tôi được yêu cầu làm như vậy trong chatbot của mình,

đó là quá trình tương tự,

nhưng thay vì tham gia toàn bộ cuộc trò chuyện

chỉ trên văn bản,

nếu chúng tôi có câu hỏi,

thì dấu nhắc phải là dấu nhiệm vụ câu hỏi, dấu hai chấm,

câu hỏi, câu trả lời bằng dấu hai chấm và sau đó chúng ta để lại một khoảng trống

và đó là nơi mô hình sẽ tạo ra câu trả lời,

sau đó tạo và giải mã như trước.

Để tạo phản hồi ngẫu nhiên trên một tin nhắn,

đầu tiên chúng ta sẽ phân tích cảm xúc

với mô hình phân tích tình cảm.

Nếu nó âm tính,

thì chúng ta sẽ làm rõ mô hình bộ giải mã của mình,

này, người dùng đang tức giận và đây là tin nhắn của họ.

Còn không thì chỉ cần gửi tin nhắn.

Và sau đó chúng tôi gửi phản hồi trên generate_text.

Cuối cùng, để phân tích tình cảm,

chúng tôi sử dụng mô hình tình cảm.

Sau khi hoàn thành việc đó, hãy thiết lập các tuyến đường

mà chúng tôi sắp tạo trên chatbot của mình.

Lộ trình đầu tiên của chúng ta sẽ là thiết lập lại,

sẽ thiết lập lại mọi thứ.

Vì vậy, nó sẽ có được lịch sử cuộc trò chuyện,

tóm tắt nó, thêm nó vào bản tóm tắt cuộc trò chuyện

vì vậy chúng ta có lịch sử tóm tắt của cuộc trò chuyện.

Và sau đó lịch sử cuộc trò chuyện sẽ được đặt thành không.

Chúng ta sẽ có lời chào,

đó sẽ là thông điệp bắt đầu truyền thống,

và điểm cuối trò chuyện chung.

Điểm cuối trò chuyện về cơ bản sẽ nhận được một tin nhắn

được thêm vào lịch sử nói rằng điều này đến từ người dùng.

Và sau đó chúng tôi sẽ kiểm tra.

Nếu được yêu cầu tóm tắt,

sau đó chúng tôi sẽ trả lời

với hàm summary_text.

Nếu chúng tôi có một câu hỏi,

và tôi biết có lẽ có nhiều cách tốt hơn

để kiểm tra xem đó có phải là một câu hỏi hay không,

đây chỉ là một thứ rất thô sơ,

nhưng đây không phải là khóa học về chatbot,

đây là khóa học về cách tận dụng LLM cho chatbot.

Chúng ta sẽ sử dụng câu trả lời_question

và câu hỏi_câu trả lời LLM.

Nếu không, chúng ta sẽ tạo ra phản hồi

với mô hình chỉ có bộ giải mã.

Cuối cùng, chúng ta sẽ phân tích cảm xúc đề phòng,

và chúng tôi sẽ lưu trữ tất cả thông tin đó

vào lịch sử cuộc trò chuyện.

Và đó là chatbot của chúng tôi.

Lưu ý rằng nó tận dụng cả ba mô hình

mà chúng tôi đã tạo ra trong thử thách.

Vì vậy, khi tạo tập lệnh này, chúng ta phải chạy nó.

Và cách để chạy nó trên một quy trình riêng biệt là sử dụng nohup.

Vì vậy lệnh này sẽ khởi động chatbot

và nó sẽ xuất tất cả nhật ký vào Nohup.out.

Bây giờ, chatbot này cần tải xuống tất cả các mô hình,

tải tất cả các tensor,

vì vậy có thể mất khoảng hai đến ba phút để tải.

Được rồi, bây giờ đã trôi qua một chút thời gian, hãy kiểm tra

cách xác minh mô hình của chúng tôi đang chạy.

Có hai cách.

Đầu tiên là vào tệp nohup.out này,

nhấp đúp vào nó và kiểm tra nhật ký.

Vì vậy nếu chúng ta lấy cái này,

chúng ta có thể thấy các mô hình đang được tải xuống

và chúng ta có thể thấy rằng nó đã chạy ở cổng 5.000.

Vì vậy, tất cả đều tốt.

Cách khác là chạy lệnh sau,

lsof -i -P -n | grep LẮNG NGHE

sẽ kiểm tra tất cả các cổng nghe.

Và chúng ta có thể thấy ở đây chúng ta có một quy trình

thực sự lắng nghe trên 5.000.

Đó là chatbot của chúng tôi.

Vậy bây giờ điều chúng ta sẽ làm chỉ là để xác minh,

là chúng ta sẽ lấy được IP

từ tên máy chủ bằng thư viện socket,

và trên cảng 5.000

chúng tôi sẽ gửi yêu cầu nhận để chào hỏi.

Hãy nhớ rằng, điều này sẽ trả lại tin nhắn chào mừng.

Và thực sự, chúng tôi hiểu được nó.

Vậy là chatbot của chúng tôi đã hoạt động.

Bây giờ chúng ta sẽ gửi một tin nhắn để trò chuyện,

và nó sẽ là một câu hỏi.

Thủ đô của Pháp là gì?

Và phản ứng là nó đang suy nghĩ.

Chúng ta đến đó, câu trả lời là Paris.

Vì vậy, chúng tôi đã làm đúng.

Chúng ta cũng có thể hỏi, này, tóm tắt văn bản này,

và lưu ý rằng tôi đang chuyển toàn bộ văn bản về Bastille

và tại sao nó lại quan trọng.

Bây giờ là phần tóm tắt, tôi đặt nó ngắn gọn,

nên có lẽ phần tóm tắt sẽ ngắn.

Hãy xem nó.

Thế đấy.

Thật vậy, bản tóm tắt ngắn gọn nhưng vẫn có giá trị.

Bastille là một pháo đài ở Paris, Pháp.

Vậy là nó đã đúng.

Và cuối cùng, tôi có thể gửi tin nhắn bình thường

giống như tôi muốn xây dựng một ứng dụng,

và sau đó chúng ta sẽ thấy thế hệ.

Tất nhiên, mô hình chỉ dành cho bộ giải mã này

chưa được tinh chỉnh cho chatbot,

vì vậy chúng tôi không thực sự chắc chắn

rằng chúng ta sẽ nhận được những câu trả lời tuyệt vời.

Hãy xem. Tôi muốn xây dựng một ứng dụng.

Người khác trả lời: "Bạn muốn gì?"

Được rồi, đây có lẽ không phải là phản hồi tốt nhất

mà chúng ta có thể có được,

nhưng đó là vì OpenAI GPT-2 này thực sự đã được đào tạo

để hoàn thành văn bản tương tự hơn là tạo văn bản chatbot.

Nếu bạn quan tâm đến việc sử dụng tính năng tạo văn bản cho cuộc trò chuyện,

chúng tôi có một ứng dụng sắp xếp khóa học khác của tôi,

xây dựng và triển khai một chatbot từ đầu.

Và ở đó chúng ta sẽ thấy

cách định cấu hình mô hình Phi-3 của Microsoft,

đó là mô hình chỉ dành cho bộ giải mã tạo văn bản

có thể được cấu hình để trò chuyện.

Cuối cùng, nếu chúng ta chạy thiết lập lại,

toàn bộ cuộc trò chuyện nên được thiết lập lại,

và chúng ta sẽ có được bản tóm tắt cuối cùng

của toàn bộ cuộc trò chuyện.

Chúng ta đã nói về rất nhiều thứ,

nên tôi không biết điều đó sẽ xảy ra như thế nào.

Và tóm tắt là, "Bạn không thể xây dựng một ứng dụng

nếu bạn không biết mình muốn gì."

Được rồi, điều đó hoàn toàn chính xác.

(cười) Điều đó thật buồn cười.

Những điểm quan trọng của bản demo này là gì?

Ở đây chúng tôi đang kiểm tra xem chúng tôi thực sự có thể nói chuyện với chatbot của mình hay không.

Đây là giao diện yêu cầu.

Trong khóa học khác mà tôi đã đề cập,

thực ra chúng ta sẽ tạo ra một giao diện trực quan.

Nhưng điểm quan trọng là đây.

Giống như chúng ta có thể tạo ra một chatbot thực sự rất dễ dàng,

và ở đây chúng tôi sử dụng các chức năng này để tận dụng LLMS

mà chúng tôi đang tải ở đây.

Và để tận dụng LLM trong chatbot hoặc bất kỳ ứng dụng nào

luôn luôn là quá trình tương tự,

tokenizer model.generate và giải mã,

như chúng ta đã học trong suốt khóa học.