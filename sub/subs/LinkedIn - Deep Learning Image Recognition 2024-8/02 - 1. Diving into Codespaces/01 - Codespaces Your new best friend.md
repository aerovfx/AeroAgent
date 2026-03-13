# 01 - Codespaces Người bạn thân mới của bạn

---

- Xin chào, tôi có một tin tuyệt vời cho bạn đây.

Trong khóa học này, chúng ta sẽ sử dụng GitHub Codespaces,

vì vậy sẽ không có vấn đề gì nếu bạn đang sử dụng Windows,

Mac, Linux hoặc bất kỳ loại hệ thống nào khác.

Cơ sở mã của chúng tôi sẽ giống nhau đối với tất cả chúng ta,

vì vậy không cần thiết lập hoặc thực hiện

bất kỳ loại cài đặt nào khác.

Vì vậy, hãy xem qua kho lưu trữ của chúng tôi ở đây.

Đây là kho lưu trữ GitHub của chúng tôi cho khóa học này,

và tôi sẽ xem xét nội dung của kho lưu trữ GitHub này,

và sau đó tôi sẽ hướng dẫn bạn

cách bạn có thể mở Codespaces của riêng mình.

Trước hết, kho lưu trữ GitHub này

bao gồm các thư mục khác nhau.

Vì vậy, hãy bắt đầu với cái từ trên xuống, devcontainer.

Vì vậy, devcontainer này chứa một số cài đặt

cho môi trường phát triển và vùng chứa của chúng tôi,

và nó cũng có một mã khóa rất quan trọng ở đây,

đang cài đặt tất cả các thư viện Python cần thiết.

Vậy là chúng ta có một file văn bản có tên là require.txt.

Điều này bao gồm tất cả các thư viện

chúng tôi sẽ sử dụng cho khóa học này.

Và như bạn thấy trong GitHub Codespaces,

chúng tôi đã tự động cài đặt nó ngay

trước khi môi trường Codespace của bạn sẵn sàng sử dụng.

Tiếp theo chúng ta sẽ đến GitHub

và GitHub có quy trình làm việc riêng ở đây như bạn thấy.

Bạn có thể nhấp vào nó và xem nó liên quan đến điều gì,

và sau đó bạn có thể thấy các cài đặt khác nhau

và những người chủ ở đây,

nhưng chúng tôi sẽ không giải quyết vấn đề đó trong khóa học của mình.

Vì vậy, đây chỉ là thông tin chung của bạn.

Tiếp theo, tôi sẽ chuyển sang cài đặt vscode.

Vì vậy, cài đặt vscode này có mọi thứ

chẳng hạn như fontSize, chẳng hạn như fontFamily,

và thậm chí cả cài đặt màu sắc

mà chúng tôi sẽ sử dụng cho khóa học này.

Bây giờ sau thông tin cơ bản này,

hãy cùng tập trung vào phần cốt lõi của khóa học,

đó là tệp mã và tệp đầu ra của chúng tôi.

Vì vậy đây là những điều rất, rất quan trọng

và đây là chủ đề chính của khóa học của chúng tôi.

Vì vậy, hãy để tôi bắt đầu với, thực sự bây giờ hãy bỏ qua,

đầu ra và đi qua thư mục nguồn

và sau đó chúng ta sẽ truy cập thư mục đầu ra tiếp theo.

Vâng, trong thư mục nguồn,

nói cách khác, tất cả mã nguồn của chúng tôi,

tất cả các tệp tập lệnh Python mà chúng tôi sẽ làm việc

trong khóa học này và tất cả các tệp Python của chúng tôi

được đặt tên gọn gàng,

bắt đầu từ tên chương, gạch dưới,

phần, gạch dưới, bắt đầu hoặc kết thúc.

Vậy tất cả những gì đòi hỏi là chúng ta bắt đầu với tệp bắt đầu

và chúng tôi đi đến phần cuối cùng của tập tin,

điều đó có nghĩa là bạn có thể theo dõi ở giữa phần đầu

và tự mình kết thúc việc xem tôi làm việc với mã.

Hoặc bạn có thể mở lại 02_01_end và liên hệ lại với chúng tôi.

Vì vậy, bạn có sự linh hoạt ở đây

và toàn bộ khóa học thực sự diễn ra theo định dạng này.

Nó bắt đầu bằng sự bắt đầu và kết thúc bằng sự kết thúc,

để bạn có thể theo dõi một cách có hệ thống.

Bây giờ chúng tôi thực sự có các chương cũng như các thử thách,

và những thách thức này sẽ chi tiết hơn

khi chúng ta đến những phần đó.

Bây giờ hãy lưu ý rằng chúng ta đã bỏ qua thư mục đầu ra.

Vì vậy, cuối cùng nhưng không kém phần quan trọng, hãy xem qua thư mục đầu ra

và chúng ta sẽ thấy rằng chúng ta có rất nhiều mô hình ở đây,

mà chúng tôi sẽ giải thích rất chi tiết

cũng như chúng tôi có tất cả kết quả đầu ra

mà chúng tôi đã tạo ra trong mã của mình

được lưu trong phần lô.

Lý do là trong Codespaces,

các lô không tự động bật lên một cửa sổ mới

giống như máy tính để bàn Visual Studio Code.

Vì vậy, như một giải pháp thay thế, chúng tôi đang sử dụng cốt truyện

chức năng lưu để lưu tất cả các ô

mà chúng tôi đã sản xuất trong khóa học này

dưới phần lô.

Điều này cũng mang lại cho chúng ta một lợi thế lớn

trong trường hợp bạn muốn xem lại các ô

mà chúng tôi đã thực hiện mà không cần chạy lại mã.

Vì vậy, bạn luôn có thể đi

và xem kết quả ở phần đồ thị.

Vẻ đẹp của những mẫu này bây giờ là

rằng chúng tôi đã lưu chúng ở đây, chúng tôi có thể quay lại

và tái sử dụng chúng nhiều lần

và chúng tôi có thể cải thiện chúng và có thể đổi tên chúng.

Như bạn có thể thấy, chúng ta có một mô hình đơn giản,

chúng tôi có một mô hình nâng cao, chúng tôi có một mô hình cộng nâng cao,

và chúng tôi có một mô hình tiên tiến, v.v.

Vì vậy tất cả chúng ta sẽ giải thích những gì đòi hỏi,

sự khác biệt là gì,

và các lớp học sâu tạo nên các lớp đó.

Được rồi, vậy là đủ về kho lưu trữ của chúng tôi.

Hãy tiếp tục và tạo không gian mã của riêng chúng ta.

Vì vậy hãy quay lại trang chủ của kho lưu trữ này

và tìm nút màu xanh lá cây có nội dung Mã

với một mũi tên xuống trên đó.

Vì vậy, hãy tiếp tục và nhấp vào nó.

Chà, nếu bạn đã có Codespace thì bạn đã bắt đầu

trước đây, bạn sẽ thấy điều này ở đây.

Nếu bạn chưa bắt đầu bất kỳ Codespace nào,

bạn sẽ thấy dấu cộng ở đây.

Thực ra, bạn sẽ thấy dấu cộng này

bất kể bạn có Codespace hay không.

Nhưng nếu bạn muốn có thêm

hoặc Codespace đầu tiên của bạn,

sau đó bạn chỉ cần nhấp vào dấu cộng này

và sau đó nó sẽ mở ra một Codespace mới.

Còn nếu tôi muốn mở Codespace cũ của mình thì sao?

Chà, tôi có thể làm điều đó bằng cách tìm ba dấu chấm này

rồi mở trình duyệt

để tôi có thể tiếp tục trên Codespaces

mà tôi đã tạo rồi.

Tôi không phải tạo lại nó mỗi lần.

Một tùy chọn khác mà bạn có thể sử dụng là như sau.

Bạn cũng có thể nhấp vào ba dấu chấm

và nhấp vào Mở bằng Visual Studio Code.

Vậy điều này xảy ra là nó thực sự mở nó ra

trong Mã Visual Studio

và nó hỏi bạn một vài câu hỏi.

Thứ nhất, nếu bạn không có Visual Studio Code,

sau đó nó thực sự sẽ nhắc bạn và hướng dẫn bạn

làm thế nào bạn có thể cài đặt nó trong máy tính của riêng bạn.

Và đó là một quá trình rất nhanh chóng.

Tôi thực sự rất khuyến khích bạn

để có Visual Studio Code cục bộ trong thiết bị của bạn.

Bất kể bạn đang sử dụng Windows, Linux, Mac,

bất cứ điều gì bạn có thể nghĩ ra,

đã cài đặt Visual Studio Code cục bộ.

Tuy nhiên, đối với lớp học này, bạn không cần nó.

Bạn có thể theo dõi 100% cùng với Codespaces

mà tôi đã cho bạn xem, nhưng về lâu dài,

thật tốt khi cài đặt Visual Studio Code.

Và tôi muốn nói thêm một điều nữa tại sao tôi lại giới thiệu nó.

Có một số lợi thế

mà chúng tôi không có trong Codespaces

mà Visual Studio Code cục bộ có.

Ví dụ: nó hiện lên các số liệu có cốt truyện hiển thị

trong các tệp Python mà không cần

lưu chúng vào tệp Notebook Jupyter

trong Mã Visual Studio cục bộ.

Nhưng chúng tôi không thể làm điều tương tự trong Codespaces.

Vì vậy, đó là lý do lớn số một.

Tại thời điểm ghi âm này,

Thật không may, trong Codespaces không có chức năng

để sử dụng GPU chưa.

Vì vậy đây là một lý do khác mà tôi khuyên bạn nên

có Mã Visual Studio

cũng được cài đặt cục bộ cho các dự án khác của bạn.

Bây giờ tôi đã mở Codespaces của mình

trong Visual Studio Code và tôi có thể thấy Codespace của mình

Bánh quế mờ ở đây.

Tuyệt vời, nó đã mở ra.

Bây giờ đây là điểm mấu chốt ở đây.

Bởi vì nó mở ra trong Visual Studio Code,

không có nghĩa là tôi đang chạy nó

trong Mã Visual Studio địa phương của tôi.

Tôi vẫn đang ở trong GitHub Codespaces,

và cách nhanh nhất để kiểm tra

đó là phía dưới bên trái.

Tôi có thể thấy Codespaces được viết ở đây.

Vì vậy, đây là Codespaces của tôi

và tôi có thể chạy bất cứ thứ gì ở đây bằng cách nhấp vào

vào Tệp Chạy Python ngay trên hình tam giác này.

Hoặc tôi có thể đơn giản sử dụng thiết bị đầu cuối ở đây.

Vì vậy, một trong hai cách hoạt động.

Chúng ta hãy đợi một chút và xem nó hoạt động như thế nào.

Sẽ có một số cảnh báo như thường lệ.

Điều đó không sao cả, chẳng hạn như Tensor RT

và vân vân bất ngờ.

Được rồi, nó hoạt động mà không gặp vấn đề gì và nó đã tạo ra một âm mưu

và nó nói rằng nó đã lưu cốt truyện trong các ô đầu ra

và display_images.png.

Vì vậy, có điều đó.

Nó lại xuất hiện trong các ô đầu ra

và display_images.png,

và chúng ta có thể thấy những hình ảnh mà chúng ta sẽ làm việc.

Bây giờ đây là Codespaces cũ của chúng tôi.

Hãy nhớ rằng tôi cũng đã mở một cái mới,

Codespace hoàn toàn mới ở đây phải không?

Vậy là tab thứ hai này chính là nó.

Đó là Codespace hoàn toàn mới ngoài Fuzzy Waffle

mà tôi đã có trước đó đã mở ra.

Vì vậy, bây giờ hãy lưu ý rằng tôi đang giữ nó như một trình duyệt web.

Tôi không mở nó trong Visual Studio Code.

Nó ở trong trình duyệt web.

Vì vậy, tôi có thể làm những điều tương tự

mà tôi đã làm ở cái kia

rằng tôi cũng có thể làm điều đó ở đây.

Vì vậy, cái nào chúng ta đã chạy làm ví dụ ở đây chẳng hạn?

Trong phần này tôi tin rằng chúng tôi đã chạy 02_01.

Vì vậy, vì sự bình đẳng,

hãy tiếp tục và chạy 02_01 ở đây.

Và sau đó hãy chứng minh rằng chúng ta có thể sử dụng phiên bản web

cũng như phiên bản Visual Studio Code.

Và một lần nữa, những cảnh báo tương tự sẽ xuất hiện

ở trên này, không sao cả.

Một số cảnh báo có liên quan

vì chúng tôi đã tắt GPU do

vào Codespaces và đó là điều bình thường.

Được rồi, đây cũng là việc tải xuống dữ liệu từ các tài nguyên

cho cifar-10 mà chúng ta sẽ đề cập sau.

Và thật tuyệt, chúng ta có cùng một cốt truyện

được lưu vào cùng một thư mục,

và nó hoạt động giống như mong đợi trong trình duyệt web

cũng như Mã Visual Studio.

Vì vậy, đây là cách bạn sử dụng repo GitHub

và Không gian mã cho khóa học này.