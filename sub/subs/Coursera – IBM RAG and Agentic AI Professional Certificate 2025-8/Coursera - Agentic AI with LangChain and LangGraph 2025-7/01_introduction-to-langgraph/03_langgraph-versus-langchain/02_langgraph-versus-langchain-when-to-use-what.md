# 02 langgraph-so với-langchain-khi-sử dụng-gì

---

LangChain và LangGraph đều là các khung nguồn mở được thiết kế để giúp các nhà phát triển xây dựng

các ứng dụng có mô hình ngôn ngữ lớn.

Vậy sự khác biệt là gì và tại sao lại sử dụng cái này hơn cái kia?

Chà, tôi nghĩ một nơi tốt để bắt đầu là xác định hai thứ này là gì.

Và hãy bắt đầu với LangChain.

Bây giờ chúng tôi đã thực hiện một video dành riêng cho LangChain và tôi đoán là có thể có một cửa sổ bật lên

ở đâu đó trong đầu tôi lúc này đang khuyến khích bạn xem video đó.

Nhưng đừng bấm vào, chưa đâu.

Hãy cho tôi một chút thời gian để tóm tắt về LangChain.

Sau đó, ở cuối video này, nếu bạn muốn biết thêm, bạn có thể quay lại và kiểm tra xem

một ra.

Được rồi.

Về cốt lõi, LangChain là một cách để xây dựng các ứng dụng hỗ trợ LLM bằng cách thực hiện một chuỗi

của các chức năng trong một chuỗi.

Vì vậy, giả sử chúng ta đang xây dựng một ứng dụng và điều đầu tiên nó cần làm là nó cần

để lấy một số dữ liệu từ một trang web.

Sau khi hoàn thành việc đó, chúng ta chuyển sang giai đoạn hai.

Và giai đoạn hai là tóm tắt dữ liệu mà chúng tôi đã truy xuất.

Và cuối cùng, chúng ta sẽ sử dụng bản tóm tắt này để làm điều gì đó.

Cụ thể, chúng tôi sẽ yêu cầu nó trả lời các câu hỏi của người dùng.

Vì vậy, quy trình làm việc ở đây là truy xuất, tóm tắt và trả lời.

Bây giờ chúng ta có thể sử dụng LangChain để giúp chúng ta thực hiện việc này.

Vì vậy, hãy bắt đầu với thành phần truy xuất.

Bây giờ thành phần truy xuất có thể bao gồm thành phần LangChain được gọi là trình tải tài liệu.

Giờ đây, trình tải tài liệu được sử dụng để tìm nạp và tải nội dung từ nhiều nguồn dữ liệu khác nhau.

Và nếu một số tài liệu đó có dung lượng lớn, chúng ta có thể chọn sử dụng bộ tách văn bản.

là một thành phần LangChain khác, dùng để chia văn bản thành các phần nhỏ hơn, có ý nghĩa về mặt ngữ nghĩa.

Được rồi, đó là lấy lại.

Bây giờ để tóm tắt, chúng ta sẽ sử dụng một chuỗi.

Và chuỗi sẽ điều phối quá trình tóm tắt.

Bây giờ điều đó có thể bao gồm việc xây dựng một thành phần nhắc nhở để hướng dẫn LLM thực hiện

tóm tắt.

Và nó cũng có thể chứa thành phần LLM để chuyển yêu cầu đó sang ngôn ngữ lớn

mẫu mà chúng ta lựa chọn.

Được rồi.

Và để trả lời, chúng tôi sẽ xây dựng một chuỗi khác.

Chuỗi này có thể bao gồm một thành phần bộ nhớ.

Vì vậy, đây là một thành phần khác của LangChain và được dùng để lưu trữ lịch sử hội thoại

trong bối cảnh.

Và chúng tôi sẽ đưa vào một thành phần nhắc nhở khác và một thành phần LLM khác để tạo ra

câu trả lời dựa trên bản tóm tắt và bối cảnh bản ghi.

Và điều thú vị ở đây là LLM mà chúng tôi sử dụng cho thành phần câu trả lời có thể hoàn toàn

mô hình ngôn ngữ lớn khác với mô hình chúng tôi sử dụng trong thành phần tóm tắt.

Kiến trúc mô-đun của LangChain cho phép chúng tôi xây dựng các quy trình công việc phức tạp bằng cách kết hợp các

thành phần cấp độ.

Được rồi, bây giờ hãy giới thiệu LangGraph.

LangGraph là một thư viện chuyên biệt trong hệ sinh thái LangChain, được thiết kế đặc biệt

để xây dựng các hệ thống đa tác nhân có trạng thái.

Nó có thể xử lý các quy trình công việc phức tạp, phi tuyến tính.

Vì vậy, hãy xem xét một tác nhân trợ lý quản lý nhiệm vụ.

Bây giờ, quy trình làm việc ở đây liên quan đến việc xử lý thông tin đầu vào của người dùng.

Vì vậy, hãy bắt đầu từ đó, xử lý đầu vào.

Và sau đó, trong quy trình làm việc này, chúng tôi sẽ cho phép thêm nhiệm vụ.

Chúng ta sẽ có thể hoàn thành các nhiệm vụ và chúng ta cũng sẽ có thể tóm tắt

nhiệm vụ.

Đây chính là kiểu kiến ​​trúc mà chúng tôi đang cố gắng xây dựng ở đây.

Bây giờ, LangGraph giúp chúng tôi tạo cấu trúc này dưới dạng cấu trúc biểu đồ trong đó mỗi hành động trong số này

được coi là một nút.

Vì vậy, hãy thêm nhiệm vụ, hoàn thành nhiệm vụ, tóm tắt, tất cả đều là nút.

Và sau đó là sự chuyển tiếp giữa những thứ này, được gọi là các cạnh.

Bây giờ, nút trung tâm là nút đầu vào của quá trình.

Vì vậy, đó là nơi đầu vào của người dùng xuất hiện.

Và điều đó sẽ sử dụng thành phần LLM để hiểu ý định của người dùng và định tuyến tới

nút hành động thích hợp.

Bây giờ, có một thành phần khác ở đây khá quan trọng đối với trạng thái này, trạng thái

thành phần.

Và thành phần trạng thái được sử dụng để duy trì danh sách nhiệm vụ, vượt qua tất cả các tương tác.

Vì vậy, nút thêm nhiệm vụ sẽ thêm các nhiệm vụ mới vào trạng thái.

Nút tác vụ hoàn chỉnh đánh dấu các tác vụ là đã hoàn thành.

Sau đó, nút tóm tắt sử dụng LLM để tạo ra cái nhìn tổng quan về các tác vụ hiện tại.

Tất cả các nút có thể truy cập và sửa đổi trạng thái, cho phép tương tác trạng thái theo ngữ cảnh.

Cấu trúc biểu đồ cho phép trợ lý xử lý các yêu cầu khác nhau của người dùng theo bất kỳ thứ tự nào,

luôn quay trở lại nút đầu vào của quy trình sau khi hành động hoàn tất.

Kiến trúc của LangGraph cho phép chúng ta tạo ra các tác nhân có trạng thái, linh hoạt có thể duy trì ngữ cảnh

qua các tương tác mở rộng.

Vì vậy, hãy so sánh trực tiếp LangChain và LangGraph trên một số khía cạnh.

Hãy bắt đầu với trọng tâm chính.

Bây giờ, trọng tâm chính của LangGraph là tạo và quản lý cái được gọi là đa tác nhân

hệ thống và quy trình công việc.

Trọng tâm của LangChain là cung cấp một lớp trừu tượng để xâu chuỗi các hoạt động LLM thành các hoạt động lớn

ứng dụng mô hình ngôn ngữ

Đó là sự khác biệt giữa hai.

Bây giờ, về cấu trúc, LangChain áp dụng, không có gì ngạc nhiên ở đây, cấu trúc chuỗi và cấu trúc đó

hoạt động như một DAG.

DAG là từ viết tắt của biểu đồ tuần hoàn có hướng, có nghĩa là các tác vụ được thực hiện theo một cách cụ thể

trật tự, luôn tiến về phía trước.

Vì vậy, ví dụ: chúng ta bắt đầu với nhiệm vụ số một, sau đó chúng ta sẽ có một nhánh cho nhiệm vụ có thể

nhiệm vụ số hai và nhiệm vụ thứ ba, sau đó chúng tôi sẽ quay lại nhiệm vụ trọng tâm số bốn.

Và quá trình này thật tuyệt vời khi bạn biết chính xác trình tự các bước cần thiết.

Mặt khác, cấu trúc biểu đồ của LangGraph hơi khác một chút vì nó

cho phép lặp lại và xem lại các trạng thái trước đó.

Vì vậy, chúng ta có thể có trạng thái A, trạng thái này có thể tiến và lùi với trạng thái B và trạng thái C.

Và điều này có lợi cho các hệ thống tương tác nơi bước tiếp theo có thể phụ thuộc vào việc phát triển

điều kiện hoặc đầu vào của người dùng.

Bây giờ, khi nói đến các thành phần, LangChain sử dụng rất nhiều thành phần và chúng tôi đã đề cập đến nhiều thành phần.

những cái này rồi.

Điều đó bao gồm bộ nhớ.

Có thành phần nhắc nhở là tốt.

Ngoài ra còn có thành phần LLM, đó là cách chúng tôi thực sự chuyển mọi thứ sang ngôn ngữ lớn

mô hình.

Và còn có thành phần tác nhân, tạo thành chuỗi giữa tất cả những thứ này.

Bây giờ, LangGraph sử dụng rất nhiều thành phần khác nhau.

Vì vậy, chúng ta có các nút, chúng ta cũng có các cạnh và chúng ta có các trạng thái.

Và đây đều là một phần của biểu đồ.

Và nói về trạng thái, điều đó mang lại cho chúng ta sự quản lý trạng thái rất tốt.

Và tôi nghĩ chúng ta có thể nói rằng LangChain có phần hạn chế về khả năng quản lý nhà nước.

Nó có thể chuyển tiếp thông tin qua chuỗi, nhưng nó không dễ dàng duy trì một trạng thái liên tục.

trạng thái qua nhiều lần chạy.

Điều đó nói lên rằng, LangChain có các thành phần bộ nhớ này có thể duy trì một số trạng thái trên

tương tác.

Tôi có thể nói rằng quản lý trạng thái của LangGraph mạnh mẽ hơn.

Và đó là vì trạng thái là thành phần cốt lõi mà tất cả các nút có thể truy cập và sửa đổi, cho phép

cho các hành vi phức tạp hơn, nhận biết ngữ cảnh.

Hãy nghĩ về các trường hợp sử dụng.

Chà, LangChain thực sự vượt trội, đặc biệt là ở các nhiệm vụ tuần tự, giống như một quá trình truy xuất

dữ liệu rồi xử lý rồi đưa ra kết quả.

Như đã nói, một lần nữa, LangChain có thể xử lý các nhiệm vụ không tuần tự ở một mức độ nào đó bằng

tính năng đại lý riêng.

Nhưng cỗ xe của LangGraph, đó thực sự là những kịch bản có tính chất phức tạp hơn nhiều

cho họ.

Các hệ thống phức tạp đòi hỏi sự tương tác và thích ứng liên tục.

Ví dụ: một trợ lý ảo cần duy trì bối cảnh trong các cuộc trò chuyện dài

và xử lý các loại yêu cầu khác nhau.

Đó là LangChain và LangGraph, hai framework mạnh mẽ để xây dựng các ứng dụng

sử dụng các mô hình ngôn ngữ lớn.

Được rồi, đó là tất cả những gì tôi có.

Bạn có thể xem video LangChain đó ngay bây giờ.