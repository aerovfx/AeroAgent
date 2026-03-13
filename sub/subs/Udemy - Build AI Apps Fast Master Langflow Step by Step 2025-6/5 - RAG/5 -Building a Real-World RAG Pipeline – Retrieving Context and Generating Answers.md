# 5 -Xây dựng quy trình RAG trong thế giới thực – Truy xuất bối cảnh và tạo ra các câu trả lời đã được dịch

---

Khi chúng tôi đã xác nhận rằng thông tin đang được lưu chính xác trong cơ sở dữ liệu vectơ,

chúng ta sẽ tạo quy trình làm việc cho phép chúng ta nhập câu hỏi để mô hình AA

có thể trả lời bằng cách sử dụng thông tin cụ thể.

Hãy đi vào langflow và tạo một quy trình làm việc trong cùng tài liệu về quy trình mà chúng tôi hiện đang thực hiện

có lên và.

Với mục đích thử nghiệm, chúng tôi có thể bắt đầu bằng cách thêm trường văn bản để nhập một câu hỏi cụ thể.

Ví dụ: làm cách nào để thêm kiểu vào điều khiển?

Tài liệu PDF chỉ chứa thông tin về một điều khiển.

Vì vậy, câu trả lời chúng tôi nhận được sẽ phải cụ thể cho điều khiển này, vì đó là

thông tin chúng tôi đang truy xuất.

Sau khi chúng tôi xác định được văn bản hoặc câu hỏi đầu vào của người dùng, bước tiếp theo là thêm

Thành phần QDrand cho phép chúng ta lấy thông tin từ cơ sở dữ liệu vector liên quan

đến hoặc có liên quan đến truy vấn chúng tôi đang thực hiện.

Chúng ta vào phần lưu trữ vector, hoặc chúng ta có thể sao chép thành phần QDrand đã

đã định cấu hình thông tin đăng nhập của chúng tôi, cùng với tất cả dữ liệu tên bộ sưu tập, URL, v.v.

Bây giờ chúng ta sẽ kết nối tin nhắn với truy vấn tìm kiếm, đây là văn bản mà QDrand sẽ

tìm kiếm theo vectơ.

Vì vậy, chúng tôi kết nối trực tiếp câu hỏi để lấy được thông tin phù hợp nhất và cung cấp

bối cảnh mà mô hình AA sẽ trả lời.

Chúng ta cũng phải kết nối một thành phần kiểu nhúng.

Tiếp theo chúng ta kết nối thành phần openAI.

Và chúng tôi sẽ kiểm tra xem điều này có hoạt động chính xác không.

Sau vài giây, chúng ta có thể thấy nó hoạt động bình thường.

Hãy xem lại kết quả tìm kiếm và bạn sẽ thấy chúng tôi đã nhận được thông tin chính xác

chẳng hạn như tên bộ sưu tập, ID và văn bản, đó là những gì chúng ta thực sự cần.

Tôi sẽ đóng thông tin này và sau đó chỉ trích xuất cột văn bản, vì đây là thông tin

chúng tôi thực sự cần.

Làm thế nào chúng ta có thể đạt được điều này?

Ví dụ, chúng ta có thể sử dụng một thành phần phân tích cú pháp cho phép bạn định dạng thông tin từ

khung dữ liệu hoặc đối tượng dữ liệu để trích xuất các thuộc tính mà bạn quan tâm và thậm chí

thao tác với văn bản, đây sẽ là đầu ra của thành phần đó.

Nhóc ơi, chúng ta sẽ kết nối khung dữ liệu với trình phân tích cú pháp và giữ nguyên mẫu hiện tại.

Bạn có thể sửa đổi những thuộc tính này để bao gồm nhiều thuộc tính hơn như chúng tôi đã làm trong các video trước.

Khi chúng ta chỉ có thuộc tính này, tức là văn bản có thông tin được trích xuất, chúng ta

sẽ kiểm tra thành phần để xem nó trả về cái gì.

Bạn có thể thấy ở đây chúng tôi đã trích xuất thông tin từ từng đoạn văn bản mà chúng tôi thu được

để trả lời câu hỏi hoặc câu hỏi được đưa ra trước đó.

Vì vậy, khi chúng tôi có thông tin này từ trình phân tích cú pháp, bước tiếp theo là thêm thành phần nhắc nhở,

vì chúng ta sẽ định dạng câu hỏi của mình cho mô hình AA theo hai cách.

Đầu tiên, những gì thu được từ cơ sở dữ liệu sẽ đóng vai trò là bối cảnh để mô hình AA có thể hiểu được

thông tin đó nói về cái gì và tạo ra phản hồi được tối ưu hóa cho người dùng theo

đến câu hỏi.

Tiếp theo, mô hình AA cần biết nên trả lời câu hỏi nào dựa trên bối cảnh

thông tin.

Đó là lý do tại sao chúng tôi sử dụng thành phần nhắc nhở.

Vì vậy, những gì tôi làm là tuân theo truy vấn hoặc lời nhắc mà tôi đã tạo trước đó, trong đó

bối cảnh được chỉ định và nó cho biết, dựa trên bối cảnh trước đó, hãy trả lời câu hỏi

tùy theo khả năng của bạn.

Ở đây chúng tôi nêu câu hỏi và mô hình AA sẽ phản hồi hoặc tạo ra câu trả lời dựa trên

về thông tin trước đó.

Chúng tôi lưu các thay đổi và bối cảnh sẽ là những gì chúng tôi nhận được từ cơ sở dữ liệu vectơ.

Sau đó, chúng tôi kết nối phản hồi của trình phân tích cú pháp với thông tin đầu vào được nhắc và sau đó chúng tôi cần liên kết

câu hỏi đầu vào hoặc câu hỏi ban đầu kèm theo ghi chú.

Điều này sẽ được kết nối với câu hỏi.

Điều này có nghĩa là câu hỏi ban đầu của người dùng sẽ được liên kết với lời nhắc này, vì vậy nó sẽ

là câu hỏi mà người dùng đang hỏi.

Khi có tất cả thông tin này, chúng tôi có thể kết nối một thành phần openAI để tạo ra kết quả cuối cùng

câu trả lời.

Bây giờ chúng ta sẽ kết nối dấu nhắc, nghĩa là đầu ra từ dấu nhắc, tương ứng

cho câu hỏi cuối cùng mà chúng tôi muốn tạo bằng đầu vào openAI.

Chúng ta có thể thay đổi thông báo hệ thống nếu muốn.

Hãy sửa đổi tên mẫu máy thành GPT mini cho mẫu máy của chúng tôi.

Chúng tôi để nguyên khóa và điều này sẽ tạo ra phản hồi.

Với tất cả thông tin này đã sẵn sàng, thay vì kiểm tra, tôi sẽ xóa phần nhập văn bản, thành phần

và thay thế nó.

Hãy nhớ rằng nếu muốn, chúng ta có thể nhanh chóng trao đổi các thành phần.

Tôi sẽ thay đổi nó thành đầu vào trò chuyện để người dùng có thể trực tiếp hỏi bất kỳ câu hỏi nào họ muốn.

Hãy kết nối đầu vào trò chuyện với thành phần lời nhắc và dán phần này.

Hãy kéo hoặc thêm thành phần đầu ra trò chuyện để hiển thị phản hồi từ mô hình AI.

Bây giờ chúng ta hãy bắt đầu trò chơi và đặt một câu hỏi thật cụ thể.

Tài liệu PDF tôi đã thêm là tài liệu bạn nhìn thấy trên màn hình.

Thành phần đang được phân tích được gọi là thanh tiến trình.

Bạn có thể thấy rằng trong cấu hình, có một phần dành riêng để giải thích cách

để định cấu hình dịch vụ này trong lớp có tên startup.cs.

Đây là mã cụ thể cho biết cách thêm các dòng này để thành phần hoạt động chính xác.

Bây giờ hãy thêm một câu hỏi liên quan cụ thể đến phần này.

Làm cách nào tôi có thể định cấu hình thành phần trong startup.cs?

Chúng tôi sẽ gửi câu hỏi này.

Hãy nhớ rằng, chúng tôi không cung cấp thêm bất kỳ thông tin nào trong cuộc trò chuyện về câu trả lời sẽ như thế nào,

chúng tôi cũng không chỉ ra nó nói về thành phần nào.

Chúng tôi vừa hỏi cách định cấu hình tệp để sử dụng thành phần.

Với điều này, bạn có thể thấy rằng mô hình đã lấy được thông tin từ tài liệu

và bây giờ chúng tôi đã có câu trả lời thỏa đáng chỉ liên quan đến thành phần được đề cập trong

tài liệu.

Nếu chúng ta đặt câu hỏi mà mô hình không có ngữ cảnh hoàn chỉnh thì nó sẽ không

thực sự biết chúng ta đang đề cập đến thành phần nào, công nghệ gì hoặc ngôn ngữ lập trình nào

chúng tôi đang sử dụng.

Nhưng bằng cách cung cấp bối cảnh, nó biết chính xác phải làm gì.

Ở đây chúng ta có dòng tương tự như chúng ta đã thấy trước đó, services.addSinfusionLacer và dòng này

chứng minh rằng mã đang hoạt động chính xác vì nó trả về thông tin chúng tôi yêu cầu.

Bạn cũng có thể thấy rằng ngay cả bên trong đầu ra của cơ sở dữ liệu vector, có một số dòng

mã hiển thị cách định cấu hình lớp có tên startup.

Bằng cách này, chúng tôi đã xác minh rằng quy trình hoạt động chính xác và chúng tôi có thể tạo quy trình để chèn

thông tin mới vào cơ sở dữ liệu bên ngoài cũng như truy vấn dữ liệu từ cơ sở dữ liệu để tạo ra

một phản hồi cho người dùng dựa trên bối cảnh cụ thể của câu hỏi của họ.