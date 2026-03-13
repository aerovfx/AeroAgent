# 13 -CodeGen để hoàn thành mã

---

Trong video này, tôi sẽ giới thiệu cho bạn một trong số rất nhiều kỹ năng được đào tạo trước.

các mô hình cơ sở mà bạn có thể sử dụng để tinh chỉnh và kiểm tra.

Nhân tiện, nếu bạn tham gia khóa học này chỉ vì bạn muốn tìm hiểu thêm về cách thức và

tại sao LLM hoạt động, sau đó là các mô hình mà chúng ta sẽ tập trung chủ yếu ở đây trong suốt phần này

khóa học là quá đủ cho mục đích của chúng tôi. Nhưng nếu bạn là nhà phát triển LLM hiện tại hoặc đầy tham vọng

đối với các ứng dụng triển khai thì có thể bạn sẽ thấy rằng các mô hình nhỏ mà chúng tôi sẽ sử dụng trong phần này

khóa học có thể không đủ tốt cho nhiều ứng dụng. May mắn thay, hầu hết các mô hình tôi sử dụng trong phần này

khóa học có sẵn trong các phiên bản lớn hơn với nhiều thông số hơn. Vì vậy tôi sử dụng các phiên bản nhỏ hơn

của các mô hình vì lợi ích của thời gian tính toán và thời gian nhập, v.v. Dù sao thì đó cũng là một

một chút sang một bên. Trong video này và các video tiếp theo, chúng ta sẽ sử dụng một mô hình có tên CodeGen, được phát triển

và được phát hành bởi Salesforce.

Như bạn có thể tưởng tượng, nó được thiết kế để tạo mã.

Ở đây bạn thấy ảnh chụp màn hình trang GitHub của họ,

và tôi bao gồm một phần điều này để bạn có thể thấy

nguồn của mô hình,

nhưng cũng một phần để nhấn mạnh rằng mô hình này đi kèm

với nhiều kích cỡ khác nhau hoặc các phiên bản khác nhau.

Vì vậy, trong video này và video tiếp theo,

chúng tôi sẽ sử dụng phiên bản nhỏ nhất mà họ cung cấp,

350 triệu tham số, đó là phiên bản này,

nhưng bạn có thể thấy rằng họ cũng đã phát hành, chẳng hạn,

một phiên bản 16 tỷ tham số của mô hình của họ.

Đó là hai bậc độ lớn,

nhiều thông số hơn những gì chúng tôi đang sử dụng trong video này.

Vì vậy nếu bạn quan tâm đến kết quả đầu ra chất lượng cao hơn,

sau đó chắc chắn đi cho một mô hình lớn hơn.

Nhưng những cái nhỏ hơn mà chúng ta sẽ sử dụng thì tuyệt vời,

Họ làm rất tốt, họ tạo ra mã thực sự.

Chỉ là nó chưa đủ lớn

thực sự hữu ích cho các ứng dụng.

May mắn thay, chúng ta cũng có thể tải xuống mô hình này

trực tiếp từ Ôm Mặt,

và điều đó thật tuyệt vì nó có nghĩa là

về cơ bản chúng ta có thể sử dụng cấu trúc mã giống nhau

như trong các video trước.

Nhân tiện, bạn có thể thấy rằng tập tin này

mà chúng tôi sẽ tải xuống, mô hình này, được gọi là mono,

có nghĩa là mô hình đã được đào tạo

trên một ngôn ngữ, đó là Python.

Họ cũng cung cấp một phiên bản đa ngôn ngữ

cũng đã được đào tạo về các ngôn ngữ mã hóa khác.

Vì vậy, lát nữa tôi sẽ chuyển sang Python,

nhưng trước tiên hãy để tôi nói cho bạn biết về mục tiêu của bản demo mã này.

Chúng ta sẽ bắt đầu bằng việc nhập và khám phá mô hình

để xem nó có kiểu kiến trúc gì.

sau đó tôi sẽ tạo ra một số đầu ra

dựa trên dòng mã đầu tiên ở đây.

Vì vậy, tôi đã nhập vào mô hình cho i trong phạm vi 10 dấu hai chấm,

và tất cả phần còn lại của mã này không đến từ tôi,

nó đến từ mô hình, nó được tạo ra bởi mô hình.

Bây giờ, mã này mà mô hình tạo ra

trông giống như mã Python,

có vẻ như nó nằm trong định nghĩa lớp,

nhưng nó không thực sự hợp lý theo nghĩa là

nó sẽ không tự chạy.

Vì vậy, điều tiếp theo tôi sẽ làm là chỉ cho bạn cách nhập mã

được đăng trên GitHub.

Ở đây chúng ta thấy ảnh chụp màn hình của một trong các kho lưu trữ GitHub của tôi.

Đây là từ cuốn sách tính toán của tôi.

Vì vậy cuốn sách này có rất nhiều mã Python

thể hiện các khái niệm tính toán

và đưa ra lời giải cho tất cả các bài tập trong sách.

Bây giờ, tất cả mã trong kho lưu trữ này

tập trung vào tính toán và trực quan hóa chức năng.

Và những gì chúng ta sẽ làm trong video tiếp theo

hãy tinh chỉnh mô hình gen mã này

trên mã Python tính toán

để mô hình tạo ra kết quả đầu ra

trông giống như mã Python tính toán.

Đó là những gì bạn thấy ở đây.

Bây giờ đây không phải là mã của tôi,

nhưng nó trông rất giống mã của tôi.

Bạn có thể thấy rằng vòng lặp for bây giờ trông hợp lý hơn,

và mã rõ ràng đang cố gắng làm điều gì đó

về tích phân hàm từng phần

giữa các điểm được chọn ngẫu nhiên,

và sau đó hình dung nó bằng cách sử dụng các màu sắc khác nhau.

Bây giờ, để rõ ràng,

chúng tôi không thực hiện việc tinh chỉnh này trong video này.

Bạn sẽ tự mình thực hiện việc tinh chỉnh

trong video tiếp theo, đó là một thử thách viết mã

dựa trên đoạn mã mà bây giờ tôi sẽ chỉ cho bạn.

Chỉ cần một vài thư viện mà chúng tôi cần cho video cụ thể này.

Đây là mô hình mà chúng tôi sẽ tải xuống.

Như tôi đã đề cập, đó là từ Salesforce.

Nó được gọi là Cogen, 350 triệu tham số và đơn ngữ nghĩa là nó chỉ được đào tạo trên Python.

Và đây là đường dẫn trực tiếp tới người mẫu này trên Ôm Mặt.

Được rồi, bây giờ chúng ta có thể xem qua mô hình này.

Và đây không phải là mô hình của OpenAI.

Vì vậy, một số tên cho một số bộ phận của mô hình

sẽ khác đi.

Và điều đó không sao cả vì lúc này bạn đã rất thoải mái

với việc xem xét và suy nghĩ về các thành phần khác nhau

của một mô hình ngôn ngữ lớn.

Vì vậy, hãy xem những gì chúng ta có thể thấy.

Vì vậy, chúng tôi có số nhúng mã thông báo từ là 51.000 mã thông báo cho 1.024.

1000 token vào năm 1024.

Vì vậy, 1024 là thứ nguyên nhúng.

Và bạn nhận thấy điều gì ở đây?

Bạn có thể nhận thấy rằng những gì còn thiếu

là một ma trận nhúng vị trí.

Vì vậy, họ không có điều đó trong mô hình này.

Họ có 20 khối máy biến áp,

bắt đầu với định mức lớp như bạn mong đợi.

Và sau đó chúng ta có phép chiếu QKV.

Đây là ba ma trận trọng số chú ý

được trộn lẫn với nhau hoặc nối với nhau thành một ma trận.

Bạn có thể thấy rằng mỗi thứ này, hoặc như bạn biết,

mỗi ma trận trọng số trong số ba ma trận này đều là hình vuông.

Đó là một nghìn một nghìn,

và chúng tôi nối chúng lại với nhau

để có được ma trận 3000 chiều.

Và đây là ma trận chiếu đầu ra.

Đó là ma trận trộn tuyến tính W zero.

Và sau đó chúng ta có lớp MLP

nơi chúng ta có đầu vào và đầu ra.

Và chúng tôi có bản mở rộng 4x khá điển hình này

của tính chiều.

Vì vậy, việc mở rộng đến bốn lần chiều

và sau đó co lại về chiều ban đầu.

Bây giờ những gì bạn không thấy ở đây là định mức lớp

ở đầu lớp MLP.

Tại sao họ đưa ra lựa chọn đó, tôi không thể nói,

nhưng nó là một ví dụ về sự khác biệt của LLM

được thiết kế bởi các công ty khác nhau,

các nhóm nghiên cứu khác nhau,

chúng có kiến trúc hơi khác nhau.

Cấu trúc tổng thể của một mô hình ngôn ngữ

và khối máy biến áp cũng vậy,

nhưng sẽ có rất nhiều loại mà bạn sẽ thấy.

Đúng vậy, một lý do khác khiến nó tuyệt vời

để có sự hiểu biết tốt về kiến trúc

nên bạn không thực sự bối rối

khi bạn thấy những khác biệt nhỏ

từ công ty này sang công ty khác.

Được rồi, ở đây tôi chỉ đang tạo một số mã thông báo ngẫu nhiên.

Ngoài ra còn có 50.000 token ở đây.

Và nếu tôi nhớ chính xác,

Tôi tin rằng mã thông báo này ban đầu được dựa trên

trên mã thông báo OpenAI GPT-2,

nhưng họ đã sửa đổi nó một chút,

nhưng bạn có thể muốn kiểm tra xem

nếu điều đó phù hợp với bạn.

Nhưng đây là điều bạn cần chú ý,

50.257 token trong tokenizer của họ.

Tuy nhiên, hãy nhìn vào chiều nhúng,

đó là 51.200.

Vậy điều này có nghĩa là gì?

Điều này có nghĩa là ma trận nhúng

thực tế là lớn hơn tokenizer,

hơn số lượng từ,

hoặc số lượng thẻ trong từ vựng.

Và điều đó có nghĩa là sẽ có một vài hàng

trong ma trận nhúng này không có kết nối với dữ liệu.

Họ không bao giờ nhìn thấy dữ liệu.

Chúng sẽ được sửa đổi ngẫu nhiên trong quá trình hỗ trợ phía sau,

nhưng chúng không tương ứng với bất kỳ mã thông báo nào.

Và tại sao họ làm điều đó?

Tôi nghi ngờ lý do họ làm điều đó

chỉ là để ma trận này phù hợp hiệu quả hơn

vào GPU vì một số lý do về thời gian tính toán.

Được rồi, vậy hãy xem nào.

Bây giờ điều tôi đang làm là tạo thêm mã

từ mô hình này giống như những gì tôi đã trình bày trong ảnh chụp màn hình.

Một lần nữa, đây là mô hình được đào tạo trước,

nhưng tôi chưa thực sự tinh chỉnh nó trên bất kỳ mã nào khác.

Vì vậy, những gì tôi đang làm là sử dụng model.generate,

Tôi đang nhập i trong phạm vi 10 dấu hai chấm,

và sau đó chúng ta xem những gì chúng ta nhận được.

Vì vậy chúng tôi hiểu điều này là hợp lý,

Và điều này dường như không thực sự hợp lý nữa.

Tôi đoán nó đang làm gì đó.

Nó rõ ràng trông giống như mã.

Có một số bình luận tiếng Hàn trong đó.

Vì vậy, rõ ràng là nó đang tạo ra thứ gì đó trông giống như mã.

Và ở đây nó đang cố gắng xác định một hàm

và vâng, có lẽ cũng có một lớp học bằng tiếng Tây Ban Nha.

Vì vậy, nó biết nhiều ngôn ngữ khác nhau của con người,

nhưng vâng, mã không nhất thiết phải hợp lý.

Trên thực tế, chúng ta có thể kiểm tra điều này.

Hãy thử cái này.

Tôi thực sự chỉ cần sao chép và dán mã này vào đây

và chạy nó và xem điều gì sẽ xảy ra.

Nó không chạy.

Bây giờ, đây không phải là lời chỉ trích Salesforce

hoặc mô hình của họ.

Tôi đoán là tôi không nói điều này với sự tự tin 100%,

nhưng tôi đoán rằng nếu bạn chạy chính xác

cùng mã này, nhưng sử dụng mô hình tham số 16 tỷ

chứ không phải mô hình tham số 350 triệu,

rằng bạn sẽ nhận được mã hợp lý hơn

và chính xác hơn theo nghĩa thực tế là nó sẽ như vậy,

rằng nó thực sự sẽ được biên dịch, nó sẽ là mã thực.

Được rồi, đó chỉ là phần giới thiệu ngắn gọn về mô hình đó.

Bạn sẽ làm việc với nó nhiều hơn trong video tiếp theo.

Điều tôi muốn làm bây giờ là chỉ cho bạn cách nhập tệp,

đặc biệt là các tệp sổ ghi chép từ bất kỳ kho lưu trữ Git công khai nào.

Vì vậy, ở đây chúng tôi đang sử dụng của tôi.

Như tôi đã đề cập trong các slide,

đây là từ cuốn sách tính toán của tôi

Vì vậy, tất cả mã ở đây về cơ bản là tải xuống cái này,

vì vậy hãy nhân bản mã này, tải xuống tất cả các tệp mã,

và sau đó tôi duyệt qua tất cả các thư mục

và tất cả các tập tin,

và tôi đang kiểm tra các tệp kết thúc bằng .ipynb,

Tất nhiên, đây là tệp sổ ghi chép Python.

Được rồi, việc tôi làm là đọc trong tập tin này,

và sau đó tôi kiểm tra từng ô.

Vì vậy tôi đang lặp qua tất cả các ô

và kiểm tra xem đó có phải là ô mã hay không.

Và đó là vì có rất nhiều loại tế bào khác

mà bạn có thể có.

Ví dụ, cái này ở đây là markdown.

Không có mã trong ô đầu tiên ở đây.

Vì vậy, chúng tôi không muốn token hóa điều đó.

Vì vậy, nếu ô mã hiện tại này hoặc nếu ô hiện tại này là mã,

thì về cơ bản tôi sẽ nối tất cả mã đó vào,

thu thập tất cả mã đó và sau đó mã hóa nó.

Được rồi, và xuyên suốt toàn bộ kho lưu trữ đó,

chúng tôi thấy rằng có 160.000 token,

nhưng chỉ có 3.000 trong số đó thực sự là độc nhất.

Điều đó khá thú vị khi nghĩ về mã,

rằng rất nhiều mã là dư thừa.

Bạn không viết nhiều mã rất đa dạng

cách mà bạn có rất nhiều từ và mã thông báo

khi bạn viết bằng ngôn ngữ tự nhiên.

Nếu bạn là người mới học LLM,

thì bạn có thể nghĩ rằng về cơ bản tất cả các mẫu đều có sẵn

giống như ChatGPT, nhưng điều đó thực sự không đúng.

Rất nhiều cá nhân, nhóm nghiên cứu ở các trường đại học,

Các tổ chức AI phi lợi nhuận và các công ty vì lợi nhuận

đã phát triển các mô hình ngôn ngữ được thiết kế tùy chỉnh

cho các mục đích cụ thể hoặc đã được đào tạo

chỉ trên các tập dữ liệu cụ thể.

Vì vậy, nó chắc chắn đáng để xem xét trực tuyến.

Thành thật mà nói, tôi thường khuyên bạn chỉ nên gắn bó

đến trang web Ôm Mặt,

nhưng bạn có thể nhìn xung quanh để tìm sự đa dạng của các mẫu mã

có sẵn và một số trong số chúng có thể rất phù hợp

cho bất kỳ ứng dụng nào bạn quan tâm.