# 02 từ-ý tưởng-đến-ai-xây dựng ứng dụng-với-ai-sáng tạo

---

Mới hôm nọ, tôi nhận thấy Gartner báo cáo rằng 80% doanh nghiệp sẽ có

đã sử dụng một số loại AI tổng quát thông qua các mô hình hoặc API vào năm 2026.

Và tôi không thể nói dối, với tư cách là một nhà phát triển, điều này khiến tôi hơi lo lắng bởi vì, vâng, tôi đã

đã sử dụng AI thông qua các đồng thí điểm khác nhau trong IDE của tôi và tôi cũng đã sử dụng ngôn ngữ lớn phổ biến

đã từng làm mô hình trực tuyến nhưng tôi chưa có kinh nghiệm thực sự xây dựng các ứng dụng sử dụng AI.

Chà, đây là trước khi tôi phát hiện ra việc bắt đầu với AI với tư cách là một nhà phát triển dễ dàng như thế nào.

Vì vậy hôm nay chúng tôi tập trung vào việc xây dựng các ứng dụng sử dụng GenAI.

Chúng ta sẽ nói về nơi bắt đầu, cách xây dựng các ứng dụng hỗ trợ AI này,

và chạy chúng ở đâu.

Và hôm nay bạn cũng sẽ tìm hiểu về một số công cụ và công nghệ nguồn mở khác nhau

điều đó có thể giúp tôi phát triển vòng lặp bên trong của việc xây dựng, chạy và thử nghiệm các ứng dụng

giờ đây với sức mạnh của AI trong tầm tay chúng ta.

Vì vậy, mặc dù có rất nhiều lựa chọn để chạy cục bộ một mô hình ngôn ngữ lớn

trên máy tính xách tay của tôi, hôm nay chúng ta sẽ nói về ba bước chính của AI

hành trình mà các nhà phát triển sẽ trải nghiệm khi đi từ một bằng chứng khái niệm đơn giản

thành một ứng dụng sản xuất.

Chủ yếu, đây là các giai đoạn lên ý tưởng và thử nghiệm, xây dựng và phát triển

và mặt hoạt động của sự vật.

Vì vậy, tôi có một câu hỏi cho bạn.

Làm thế nào để bạn bắt đầu xây dựng một ứng dụng sử dụng AI tổng quát?

Chà, bước đầu tiên là lên ý tưởng xoay quanh việc khám phá và chứng minh các khái niệm mà tôi có thể chia nhỏ

trong một vài bước đơn giản.

Vì vậy, trước tiên, hãy nhớ rằng trường hợp sử dụng của bạn là chuyên biệt, vì vậy bạn cần một mô hình chuyên dụng

điều đó cũng có thể thực hiện được công việc đó.

Bạn sẽ bắt đầu từ việc nghiên cứu và đánh giá các mô hình từ các kho phổ biến như Ôm

Face hoặc cộng đồng nguồn mở.

Và đó là một khởi đầu tuyệt vời.

Nhưng bạn cũng cần phải suy nghĩ về các yếu tố khác nhau chẳng hạn như kích thước mô hình, hay ví dụ:

ví dụ, hiệu suất của nó và hiểu điểm chuẩn thông qua điểm chuẩn phổ biến

những công cụ có sẵn ở đó là tốt.

Ví dụ: có một số quy tắc cơ bản khác nhau mà bạn cần hiểu.

Nói chung, việc tự lưu trữ một mô hình ngôn ngữ lớn sẽ rẻ hơn dịch vụ dựa trên đám mây.

Và các mô hình ngôn ngữ nhỏ, SLM, so với các mô hình ngôn ngữ lớn, LLM, thường sẽ hoạt động

tốt hơn với độ trễ thấp hơn và chúng chuyên dùng cho một nhiệm vụ cụ thể.

Bây giờ, bạn cũng nên hiểu về các kỹ thuật nhắc nhở khác nhau khi bạn thực sự

làm việc với mô hình.

Ví dụ: nhắc nhở bắn không.

Bây giờ đây là gì, về cơ bản là đặt một câu hỏi cho mô hình mà không có bất kỳ ví dụ nào về cách

để đáp lại.

Bây giờ, chúng ta cũng có thể thực hiện việc này hơi khác một chút với cái được gọi là nhắc nhở vài lần, trong đó

thực ra chúng tôi đang đưa ra một vài ví dụ khác nhau về cách phản ứng, hành vi mà bạn muốn

LLM cần có khi chúng tôi làm việc với AI và cả chuỗi suy nghĩ, thực ra là

yêu cầu người mẫu giải thích suy nghĩ, quy trình của nó từng bước một.

Vì vậy, xin chúc mừng, giờ đây bạn có thể đưa kỹ sư AI vào sơ yếu lý lịch của mình.

Nhưng nói một cách nghiêm túc, bạn cần hiểu những khả năng và hạn chế khác nhau

của các mô hình mà bạn đang làm việc cùng.

Và bạn có thể làm điều này và thử nghiệm dữ liệu của mình sớm để có thể hiểu bất kỳ

những thách thức tiềm ẩn có thể xuất hiện khi bạn trải qua hành trình AI.

Bây giờ chúng ta đã đánh giá các mô hình cho trường hợp sử dụng của mình, đã đến lúc xây dựng ứng dụng của chúng ta.

Bây giờ, giống như chúng ta có thể chạy cục bộ các cơ sở dữ liệu và các dịch vụ khác nhau trên máy của mình,

chúng tôi thực sự có thể làm điều tương tự với AI để thực sự phục vụ nó cục bộ từ máy của chúng tôi và có thể

để thực hiện các yêu cầu tới API của nó từ máy chủ cục bộ.

Ngoài ra, bạn còn nhận được lợi ích bổ sung khi biết rằng dữ liệu của mình được bảo mật và riêng tư tại cơ sở.

Điều đó thực sự quan trọng ngày nay.

Nhưng nếu bạn cũng muốn sử dụng dữ liệu đó với mô hình ngôn ngữ lớn của mình thì sao?

Vâng, có một vài phương pháp khác nhau để làm điều đó, bắt đầu với cái được gọi là truy xuất,

thế hệ tăng cường, hay RAG, nơi bạn thực sự sử dụng một mô hình ngôn ngữ lớn,

một mô hình nền tảng được đào tạo trước và bổ sung cho nó những dữ liệu chính xác và phù hợp.

Và điều này có thể giúp cung cấp phản hồi tốt hơn và chính xác hơn.

Nhưng điều bạn cũng có thể làm là tinh chỉnh mô hình.

Vì vậy, hãy lấy mô hình ngôn ngữ lớn và bao gồm dữ liệu với nó.

Vì vậy, chúng tôi thực sự đang xử lý thông tin này, cách chúng tôi muốn nó hoạt động, các phong cách khác nhau

và trực giác mà chúng ta muốn nó phản ứng, thực sự có trong chính mô hình đó.

Và do đó chúng ta có thể suy luận nó và có thể có dữ liệu theo miền cụ thể đó

mỗi khi chúng tôi thực sự làm việc với chính mô hình AI.

Bây giờ, đây chỉ là hai cách tiếp cận.

Còn nhiều nữa.

Nhưng tôi cũng muốn đề cập rằng việc có các công cụ và khuôn khổ phù hợp, chẳng hạn như

LangChain sẽ đơn giản hóa cuộc sống của bạn.

Họ sẽ cho phép bạn tập trung vào việc xây dựng các tính năng mới, chẳng hạn như

như các trường hợp sử dụng AI phổ biến như chatbot, tự động hóa quy trình CNTT, quản lý dữ liệu,

và nhiều hơn thế nữa bằng cách đơn giản hóa các lệnh gọi khác nhau mà bạn sẽ thực hiện thông qua mô hình.

Bây giờ, điều này có thể được thực hiện thông qua chuỗi lời nhắc và lệnh gọi mẫu để thực sự

thực hiện các nhiệm vụ phức tạp hơn.

Vì vậy, điều đó có nghĩa là bạn sẽ cần chia nhỏ vấn đề thành các bước nhỏ hơn, dễ quản lý hơn.

Và trong quá trình này, có thể đánh giá các luồng trong các lệnh gọi mô hình này,

bây giờ mà còn trong môi trường sản xuất, đưa chúng ta đến bước cuối cùng

vận hành các ứng dụng hỗ trợ AI này.

Vậy là cuối cùng, bạn đã có ứng dụng được hỗ trợ bởi AI hoặc một mô hình ngôn ngữ lớn,

và bạn muốn triển khai nó vào sản xuất để có thể mở rộng quy mô.

Và điều này thực sự nằm dưới sự bảo trợ của một thứ được gọi là hoạt động học máy,

hoặc MLOps.

Nhưng hãy để tôi tập trung vào các chủ đề quan trọng đối với bạn với tư cách là nhà phát triển.

Vì vậy, trước hết, cơ sở hạ tầng của bạn cần có khả năng xử lý việc triển khai mô hình hiệu quả

và nhân rộng.

Vì vậy, việc sử dụng các công nghệ như bộ chứa và bộ điều phối, chẳng hạn như Kubernetes,

sẽ giúp bạn làm điều này.

Có thể tự động mở rộng quy mô và cân bằng lưu lượng truy cập cho ứng dụng của bạn.

Và bạn cũng có thể sử dụng thời gian chạy sẵn sàng sản xuất, chẳng hạn như vLLM, để phân phát mô hình.

Và điều chúng tôi cũng đang thấy hiện nay là các tổ chức đang thực hiện

một cách tiếp cận kết hợp, cả với mô hình và cơ sở hạ tầng của họ.

Vì vậy, việc sử dụng dao Quân đội Thụy Sĩ nhiều mẫu này để tiếp cận các mẫu khác nhau cho các mục đích sử dụng khác nhau

trường hợp, cũng như sự kết hợp giữa cơ sở hạ tầng tại chỗ và đám mây để tận dụng tối đa

hết nguồn lực và ngân sách của bạn.

Vì vậy, với tất cả các ứng dụng mới được hỗ trợ bởi AI hiện có,

giả sử bạn có thứ gì đó đang được sản xuất, thì công việc vẫn chưa hoàn thành.

Bạn vẫn cần đo điểm chuẩn, giám sát và có thể xử lý các trường hợp ngoại lệ khác nhau

đang đến từ ứng dụng của bạn.

Và tương tự như cách chúng tôi có DevOps, chúng tôi cũng có MLOps để đảm bảo các mô hình

đi vào sản xuất một cách suôn sẻ.

Vì vậy, hãy lùi lại một bước, vì tôi nghĩ hôm nay chúng ta thực sự đã khám phá được rất nhiều điều.

Và một số đổi mới gần đây trong thế giới AI đã khiến chủ đề này trở nên thú vị hơn nhiều

có thể truy cập được đối với các nhà phát triển như bạn và tôi.

Và bạn có rất nhiều công cụ hiện có để trợ giúp bạn trong suốt quá trình.

Nhưng điều tôi muốn nhấn mạnh là mặc dù AI còn mới, nhưng thực ra nó chỉ là một thứ khác

công cụ mà bạn có thể thêm vào vành đai công cụ của mình.

Vì vậy, điều bạn có thể làm là sử dụng những công cụ này và sử dụng các bước quy trình khác nhau để

đi từ ý tưởng, xây dựng đến triển khai các ứng dụng này để tạo ra tác động thực sự

với công việc của bạn bằng cách sử dụng GenAI.