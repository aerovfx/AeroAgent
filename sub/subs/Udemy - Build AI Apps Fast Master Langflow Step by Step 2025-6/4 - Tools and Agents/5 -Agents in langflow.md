# 5 -Đại lý trong langflow dịch

---

Khi chúng ta biết cách sử dụng các công cụ và tạo các công cụ tùy chỉnh trong Lightflow, đã đến lúc nói về

đại lý.

Ở đây, chúng tôi có một sơ đồ minh họa trực quan cách hoạt động của các tổng đài viên.

Bạn có thể thấy rằng chúng tôi có ba thành phần chính.

Đầu tiên là hướng dẫn từ người dùng của tôi được liên kết với một đại lý.

Mọi thứ bạn nhìn thấy ở trung tâm đều tương ứng với một tác nhân.

Vậy một đại lý bao gồm những gì?

Bạn có thể thấy rằng nó bao gồm một mô hình AIA, ALAM và thêm vào đó là một mô hình thú vị

Tính năng của một tác nhân là khả năng truy cập các công cụ khác nhau và thực hiện các nhiệm vụ khác nhau.

Trong ví dụ cụ thể này, chúng ta thấy rằng nó có thể thực hiện tìm kiếm trên web, lấy thông tin thời tiết,

truy cập tìm kiếm thông qua API, sử dụng thư viện toán học và truy xuất thông tin văn bản.

Ưu điểm của một tác nhân là nó có thể xác định những công cụ nào sẽ được sử dụng để đáp ứng nhu cầu của người dùng.

ý định.

Nếu người dùng muốn tìm kiếm thông tin về một chủ đề cụ thể, họ có thể sử dụng trình duyệt web

công cụ để tìm các chi tiết liên quan.

Ví dụ: nếu người dùng yêu cầu thông tin về thời tiết, API tương ứng có thể

được sử dụng để tìm kiếm dữ liệu liên quan đến chủ đề đó, v.v.

Vì ALAM có tất cả thông tin cần thiết để đáp ứng mục đích của người dùng nên nó tạo ra

một bản tóm tắt hoặc phản hồi cụ thể dựa trên mô hình AIA và đây là phản hồi

kết quả là đại lý AIA cung cấp.

Và đây là những gì được cung cấp cho người dùng, để họ có phiên bản tóm tắt về

yêu cầu ban đầu rằng đại lý hiện tại này hoạt động.

Và chúng ta cũng có thể mô phỏng hoặc triển khai hành vi này trong langflow.

Tôi lại quay trở lại langflow.

Làm thế nào để chúng tôi tạo ra một đại lý?

Nó thực sự rất đơn giản.

Nhóc, chúng ta có một phần gọi là tác nhân, nơi chúng ta tìm thấy thành phần tác nhân mà chúng ta có thể kéo,

thả và định cấu hình để mô phỏng hành vi mà chúng ta đã thấy trước đó.

Như chúng ta đã thấy trong hình, có một số tính năng như cần chỉ định nhà cung cấp cho

mô hình AIA

Bạn có thể sử dụng bất kỳ cái nào có sẵn, thực ra đây là một danh sách khá dài.

Trong trường hợp của tôi, tôi sẽ sử dụng các mô hình Open AIA.

Chúng tôi có tùy chọn để chọn một trong các mô hình cụ thể cho dịch vụ trong ngày.

Chúng ta phải chỉ định khóa vì nó cần thiết để kết nối với mô hình AIA và sử dụng nó để

thực hiện hoặc nhập một lệnh để bằng cách sử dụng các công cụ, nó tạo ra phản hồi cho

chúng tôi.

Tiếp theo, bạn sẽ thấy phần có tiêu đề hướng dẫn đại lý.

Ở đây, chúng ta có thể xác định một nhiệm vụ cụ thể.

Chúng tôi có thể mô tả chi tiết các đại lý như chúng tôi muốn và đó là điều chúng tôi sẽ

làm trong các tình huống nâng cao hơn sau này.

Trong trường hợp cụ thể này, vì đây chỉ là bản demo nên tôi tin vào hướng dẫn mặc định.

Điều tiếp theo là ở đây chúng ta có một phần hoặc thuộc tính được gọi là công cụ.

Ở đây, phần mô tả cho chúng ta biết rằng đây là những công cụ chúng ta có thể kết nối và tác nhân sẽ

thể sử dụng chúng để thực hiện các nhiệm vụ khác nhau.

Chúng ta có thể lấy những công cụ này ở đâu?

Chúng ta có thể lấy các công cụ như chúng ta đã thấy trước đây trong phần được gọi là công cụ hoặc trong các gói

phần.

Nếu chúng ta kéo một trong các công cụ, giả sử máy tính này, đây là một trong những công cụ đơn giản nhất

các thành phần, bạn sẽ thấy chế độ cấu hình xuất hiện ở trên cùng được gọi là chế độ công cụ.

Bởi vì một điều bạn có thể nhận thấy là chúng ta không thể kết nối trực tiếp máy tính

đối với tài sản công cụ của đại lý.

Vì vậy, để tính năng này hoạt động chính xác, bạn phải kích hoạt chế độ này.

Bằng cách đó, đầu ra này được kích hoạt và bây giờ chúng ta có thể kết nối thành phần này với

thành phần loại tác nhân mà bạn nhìn thấy hay đúng hơn là làm cho thành phần này hoạt động như một công cụ cho tác nhân.

Điều bạn có thể nhận thấy là khi bạn bật chế độ công cụ, thuộc tính có tên

biểu thức tự động trở nên vô hình.

Điều này xảy ra bởi vì khi một tác nhân đang vận hành hoặc xác định nên sử dụng công cụ nào thì thường

chính tác nhân tạo ra các hướng dẫn và thiết lập các tham số cấu hình của

thành phần để hoàn thành các thông tin cần thiết, sử dụng phản hồi và xử lý của thành phần

nó để tạo ra phản hồi cho người dùng.

Làm thế nào chúng ta có thể thấy điều này trong thực tế?

Chúng ta có thể thêm đầu vào ở đây như một phần của thành phần này.

Tôi sẽ vào.

Trên thực tế, tôi sẽ thêm đầu vào trò chuyện để đầu vào này sẽ đóng vai trò là đầu vào của tổng đài viên.

Tôi cũng sẽ kết nối đầu ra trò chuyện để chúng ta có thể xem quá trình thực thi trong sân chơi.

Lưu ý rằng bạn không cần phải định cấu hình bất cứ điều gì khác và bạn không cần đặt bất kỳ đầu vào nào

văn bản hoặc.

Hãy bắt đầu với sân chơi.

Tôi ở đây, điều thú vị nhất về các đặc vụ là chúng ta có thể giao tiếp với họ

một cách tự nhiên, đưa ra cho chúng ta những hướng dẫn phức tạp theo ý muốn của chúng ta và chính người đại diện sẽ thực hiện điều đó

thông tin để xử lý nó, sử dụng các công cụ cần thiết và hoàn thành các tham số cần thiết

để sử dụng thành phần một cách thích hợp.

Sau đó xử lý đầu ra để cung cấp cho chúng tôi phản hồi.

Ví dụ, ở đây chúng tôi đang yêu cầu nó tính toán công thức toán học này.

Hãy chuyển thông tin đến thành phần.

Và để nhanh chóng đọc cuốn sách, những gì đang diễn ra đằng sau hậu trường, bạn có thể thấy rằng chúng ta có

phần này cho biết rằng nó đã kết thúc và nó cho chúng ta biết đầu vào hiện tại là gì khi

đầu vào của đại lý là gì.

Tiếp theo, bạn có thể thấy thành phần hoặc chức năng được gọi là biểu thức đánh giá đã được thực thi.

Chúng tôi có đầu vào được cung cấp cho thành phần này và thành phần công cụ hoặc loại công cụ

trả về thông tin có kết quả là 16.

Bằng cách này, kết quả này được mô hình AI thu được và nó cung cấp cho chúng ta kết quả đầu ra

ở định dạng văn bản cho biết kết quả của phép tính này.

Chúng tôi có nó được hiển thị ở đây trên màn hình.

Bây giờ, điều bạn nên biết là khi chúng ta sử dụng tác nhân theo một loạt các bước khác nhau

diễn ra, chẳng hạn như tra cứu các phương pháp từ các thành phần khác nhau mà chúng tôi

cần sử dụng, tạo yêu cầu sử dụng các thành phần này và thiết lập bước tiếp theo

để, ví dụ, có được câu trả lời cuối cùng.

Tức là, một số bước sẽ được thực hiện mà bạn nên ghi nhớ vì nó có thể gây ra tình trạng cao hơn

mức tiêu thụ mã thông báo do các tác vụ khác nhau được thực hiện trong quá trình xử lý này.

Trên thực tế, như một phần trong phản hồi của nhân viên, nếu chúng ta đi tới phần được gọi là nhật ký, bạn có thể

xem tất cả các bước được thực hiện để có được thông tin đó.

Vì vậy, đây là nơi bạn có thể gỡ lỗi hoặc trích xuất thông tin để xác minh xem tác nhân có hoạt động chính xác hay không,

bằng cách sử dụng các công cụ cần thiết.

Một tùy chọn khác mà bạn có thể cân nhắc khi sử dụng một thành phần làm công cụ là thiết lập phần

gọi là hành động.

Cái này dùng để làm gì?

Nếu bạn muốn mô tả chi tiết hơn về tác nhân để nó hiểu được chức năng của

mỗi công cụ được liên kết, tại đây bạn có thể sửa đổi, ví dụ: tên của hàm có sẵn

trong thành phần cụ thể này, chẳng hạn như tính toán hoặc biểu thức.

Mặc dù vậy, nó đã có một cái tên khá mô tả, đó là biểu thức đánh giá.

Ở đây chúng tôi tìm thấy mô tả cho biết chức năng cụ thể của thành phần này.

Tại sao điều quan trọng là phải có một mô tả tốt?

Khi một tác nhân phân tích thành phần nào sẽ sử dụng để thực hiện một hành động cụ thể, nó sẽ thu thập

và xử lý tất cả các thông tin có sẵn, và dựa trên đó, chọn ra thông tin phù hợp nhất

công cụ để thực hiện hướng dẫn của người dùng.

Đây là lý do tại sao điều quan trọng là phải có thông tin chính xác hoặc dữ liệu cụ thể để

đại lý có thể sử dụng nó để hoàn thành hành động của mình.

Như chúng ta thấy trong biểu đồ MASHOR, có thể có một số công cụ được kết nối với một tác nhân.

Vì vậy, những gì chúng ta có thể làm là quay lại phần công cụ và thêm một thành phần khác, ví dụ:

Thành phần Wicked Pedia và kích hoạt lại nó như một công cụ.

Một số thông số có sẵn để chúng ta cấu hình.

Trong một số trường hợp, có thể đặt các tham số mà chúng tôi biết người dùng sẽ nhập hoặc chúng tôi

muốn đặt trước, ví dụ, giới hạn ở bốn kết quả.

Ví dụ: nếu chúng tôi có API trả phí, bạn nên giới hạn số lượng kết quả để tránh

tiêu dùng tín dụng quá mức.

Trong trường hợp này, có thể điều chỉnh ngôn ngữ và số lượng kết quả.

Bây giờ, vì chúng tôi đã kích hoạt nút chỉ định thành phần này làm công cụ nên chúng tôi kết nối nó với

đại lý và tự động chúng tôi có một công cụ để tính toán và một công cụ khác để tham khảo

Pedia độc ác.

Vì vậy, nếu chúng ta quay lại sân chơi, hãy bắt đầu một phiên mới và tôi sẽ sao chép và dán

ở đây, lời nhắc mà tôi đã viết trước đó, trong đó nói rằng, hãy điều tra cuộc đời của Bill Gates

và sau đó tạo ra một bài hát vui nhộn bằng cách sử dụng thông tin đó.

Chúng tôi gửi lời nhắc hoặc hướng dẫn này và bạn có thể quan sát các bước mà tổng đài viên đang thực hiện.

Bạn có thể thấy rằng đầu tiên một chức năng gọi là tìm nạp nội dung được thực thi, thuộc về

đến thành phần Wicked Pedia.

Nó trả về một tập hợp các kết quả liên quan đến Bill Gates.

Tiếp theo, bạn có thể quan sát thấy mô hình AIA tương tự đang xử lý thông tin thu được

từ Wicked Pedia để tạo ra một bài hát khá thú vị.

Đây là cách chúng ta có thể sử dụng một số công cụ trong một tác nhân.