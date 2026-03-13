# 7 -Tạo luồng đa tác nhân phân cấp trong dịch langflow

---

Một mô hình phổ biến khác khi sử dụng các tác nhân là mô hình đa tác nhân phân cấp trong đó

có một người quản lý, như bạn có thể thấy trên màn hình, người đó có nghĩa là đại lý nào sẽ

làm việc để hoàn thành một nhiệm vụ cụ thể.

Chúng tôi sẽ tạo một cái trong langflow.

Nhóc, chúng ta có canvas trong langflow.

Hãy tiến hành kéo và thả một tác nhân như một phần của khung vẽ này.

Chúng tôi định cấu hình nó khi cần và bây giờ tôi sẽ kết nối tác nhân này với công cụ máy tính.

Bằng cách này, tác nhân này sẽ chỉ được sử dụng khi chúng ta muốn thực hiện các phép tính toán học,

mặc dù chúng tôi có thể tích hợp bất kỳ công cụ nào khác mà chúng tôi yêu cầu để thực hiện các hoạt động liên quan khác.

Bây giờ, hãy sửa đổi các hướng dẫn của tác nhân này và điều gì đó bạn có thể làm để mô hình AI

biết tác nhân nên được sử dụng như thế nào để thêm một mô tả, ví dụ, chỉ ra rằng

nó là một tác nhân giải thích toán học.

Nhóc, chúng ta có một hướng dẫn ngắn gọn nói rằng hành vi của đặc vụ phải là cung cấp

hướng dẫn hoặc từng bước giải quyết vấn đề, giải thích chúng như thể đang nói chuyện với

một đứa trẻ mẫu giáo.

Hãy hoàn tất việc chỉnh sửa.

Bước tiếp theo là tạo một tác nhân thứ hai.

Để làm được điều này, chúng ta cần kéo thành phần tác nhân.

Hãy cấu hình lại và tác nhân này sẽ được kết nối với thành phần hoặc công cụ có tên

Wikipedia.

Chúng tôi biến thành phần này thành một công cụ, kết nối chúng và trong trường hợp cụ thể này, chúng tôi sửa đổi

hướng dẫn để chỉ ra rằng đại lý này là một đại lý tìm kiếm chuyên nghiệp.

Nhóc, chúng ta chỉ ra cách chúng ta muốn câu trả lời.

Ví dụ: yêu cầu một đoạn văn có thông tin tóm tắt được giải thích là

nếu nó được gửi đến một đứa trẻ mẫu giáo.

Chúng tôi đã chỉnh sửa xong và bây giờ chúng tôi có một cặp đặc vụ sẽ tạo nên phần dưới

của hệ thống phân cấp.

Bây giờ, chúng ta cần chỉ định người quản lý cho luồng này.

Chúng ta làm điều đó như thế nào?

Hãy kéo tác nhân thứ ba như một phần của quy trình.

Bạn sẽ nhận thấy rằng mỗi tác nhân có một nút không thể kết nối trực tiếp như một công cụ để

đại lý loại người quản lý này.

Những gì chúng ta sẽ làm là chuyển đổi các tác nhân này thành công cụ để tác nhân chính có thể tái sử dụng chúng

đồng thời, các tác nhân này sử dụng các công cụ có sẵn của mình để thực hiện các hoạt động khác nhau.

Khi chế độ công cụ được bật, bạn có thể thấy rằng chúng tôi có thể kết nối các tác nhân khác nhau với người quản lý

đại lý.

Tác nhân quản lý này sẽ chịu trách nhiệm quyết định cái nào sẽ được sử dụng để thực hiện các hoạt động khác nhau

nhiệm vụ.

Điều cần thiết là bạn phải đặt ra các hướng dẫn rõ ràng để nhân viên này biết cách thức hoạt động.

Thông thường, các tác nhân này cung cấp các hướng dẫn rõ ràng và phức tạp hơn một chút giống như những gì tôi đã đưa ra.

đang bước vào.

Chúng ta cần chỉ ra cho tác nhân rằng nó nên phối hợp một số tác nhân con để thực thi

hướng dẫn của người dùng cuối.

Chúng tôi muốn nó phân tích yêu cầu và theo khả năng sẵn có của

các tác nhân, tạo ra một luồng các bước để hoàn thành nhiệm vụ mà người dùng yêu cầu.

Nhóc ơi, chúng ta có một loạt hướng dẫn cụ thể hơn như phân tích ý định của người dùng và chọn

các đại lý có liên quan trong số những người khác.

Bây giờ chúng ta có một lời nhắc phức tạp hơn một chút.

Chúng tôi hoàn thành hướng dẫn và với điều này, bây giờ chúng tôi có luồng tác nhân hoặc đa tác nhân này

sẵn sàng nơi chúng tôi có người quản lý.

Hãy kiểm tra nó.

Đối với điều này, chúng tôi cần một đầu vào trò chuyện.

Hãy tiếp tục và không ăn.

Đầu vào trò chuyện này phải được kết nối trực tiếp với đầu vào của nhân viên quản lý và chúng tôi cũng kết nối

một đầu ra trò chuyện cho người quản lý để chúng tôi có thể giao tiếp qua sân chơi.

Hãy nhập một hướng dẫn.

Ví dụ: một công thức toán học hoặc một bài toán.

Hãy gửi một vấn đề thông qua trò chuyện.

Bạn có thể thấy rằng khi chúng tôi nhập hướng dẫn, chúng tôi đã có quyền truy cập vào một tác nhân.

Lưu ý rằng chúng ta gọi lại các công cụ của tác nhân.

Trong trường hợp này, họ chịu trách nhiệm giải các bài toán và ở đây chúng tôi nhận được một câu trả lời thỏa đáng

câu trả lời.

Bây giờ hãy thử một lời nhắc phức tạp hơn.

Cái này dành cho những người đang sử dụng tác nhân nghiên cứu của họ.

Nhóc con, từ nghiên cứu cho chúng ta biết rõ ràng rằng cần phải tiến hành tìm kiếm.

Với lời nhắc này, chúng tôi muốn thực hiện nghiên cứu về một nhân vật.

Điều này cho thấy rằng nó truy cập hoặc chọn một tác nhân mà trong trường hợp này là tác nhân nghiên cứu.

Ở đây chúng ta có tham số đầu vào và cuối cùng, phản hồi của chúng ta được tạo sau khi tìm kiếm

trên Wikipedia, phù hợp với truy vấn chúng tôi đã thực hiện.

Đó là cách chúng ta có thể tạo hệ thống phân cấp trong Lancthlo bằng cách sử dụng nhiều tác nhân và theo cách này

hệ thống phân cấp đa tác nhân trong Lancthlo được trực quan hóa.