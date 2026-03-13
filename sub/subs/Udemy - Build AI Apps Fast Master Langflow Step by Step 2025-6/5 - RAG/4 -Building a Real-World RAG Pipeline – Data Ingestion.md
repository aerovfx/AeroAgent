# 4 -Xây dựng đường ống RAG trong thế giới thực – Nhập dữ liệu được dịch

---

Bây giờ, đã đến lúc tạo ra thứ gì đó thiết thực hơn hoặc có thể là quy trình làm việc phức tạp hơn,

sẽ cho phép chúng tôi nhập câu hỏi của người dùng và trả lời cụ thể cho truy vấn đó.

Chúng ta sẽ bắt đầu bằng cách tạo phần nhập dữ liệu, giống như chúng ta đã làm trong video trước.

Trong trường hợp này, chúng tôi sẽ sử dụng thành phần tệp, cho phép chúng tôi nhập một hoặc nhiều tệp

để xử lý chúng và lưu trữ tất cả thông tin đó.

Khi chúng tôi đã thêm thành phần này, chúng tôi sẽ chỉ định rằng chúng tôi muốn chọn một tệp.

Trong trường hợp của tôi, tôi đã thêm tệp này chứa tài liệu về một thành phần của nguồn

mã.

Tôi sẽ chỉ định rằng tôi muốn chọn tệp này để chạy một số thử nghiệm.

Bạn có thể kéo và thả bất kỳ tài liệu PDF hoặc bất kỳ tệp word nào bạn muốn.

Trong trường hợp của tôi, tôi sẽ chọn tài liệu PDF này.

Hãy nhớ rằng để thử nghiệm, tôi khuyên bạn nên thêm một tài liệu nhẹ.

Vì chúng có kích thước tệp lớn hơn hoặc bạn muốn càng nhiều tài liệu nên quá trình này càng dài

sẽ lấy và bạn sẽ sử dụng càng nhiều token.

Vì vậy, nếu nó chỉ để thử nghiệm, tôi khuyên bạn nên bắt đầu với một tệp nhỏ.

Khi chúng tôi đã thêm thành phần này, chúng tôi chỉ muốn trích xuất cột văn bản.

Lưu ý rằng tôi chạy thành phần này.

Nếu kiểm tra kết quả thì nó hiển thị đường dẫn file và văn bản nên chúng ta chỉ quan tâm

trong cột văn bản.

Vì vậy, như chúng tôi đã trình bày trong video trước, chúng tôi sẽ cho biết rằng chúng tôi muốn thêm một

thành phần hoạt động khung dữ liệu.

Hãy kết nối khung dữ liệu giữa cả hai thành phần.

Hãy chỉ định rằng thao tác là chọn các cột và cột mà chúng ta quan tâm

được gọi là văn bản.

Hãy chạy thành phần này để xác minh rằng mọi thứ đều hoạt động chính xác và xác nhận rằng chúng tôi đang thu được

chỉ có cột chúng tôi thực sự quan tâm.

Khi chúng ta có cột này, bước tiếp theo là chia thông tin thành các đoạn văn bản.

Điều này có thể dễ dàng đạt được với thành phần văn bản phân tách.

Hãy kết nối nút khung dữ liệu với nút văn bản hoặc khung dữ liệu được phân tách.

Sau khi thực hiện việc này, chúng tôi kiểm tra lại quy trình làm việc để đảm bảo mọi thứ hoạt động chính xác.

Ở đây, chúng tôi có các đoạn văn bản và mọi thứ đều hoạt động khi cần thiết.

Bước tiếp theo là tạo một tài khoản trên dịch vụ mà chúng tôi quan tâm và lưu trữ

thông tin vectơ.

Điều này nhằm tăng thêm tính hiện thực cho ví dụ này.

Chúng tôi có thể thực hiện việc này với thành phần DVD cục bộ mà chúng tôi đã thấy trước đây, nhưng để làm cho nó hiệu quả hơn một chút

nâng cao, chúng tôi sẽ sử dụng một vectơ được lưu trữ có tên là QDrand, bạn có thể xem tại đây.

Ở đây, chúng tôi đang ở trên trang web QDrand, như bạn có thể thấy trên màn hình.

Bây giờ hãy cho biết rằng chúng tôi muốn bắt đầu quá trình đăng ký.

Trong trường hợp của tôi, tôi sẽ chỉ định rằng tôi muốn thêm địa chỉ email mới.

Tôi đã nhận được mã xác minh nên tôi nhấp vào tiếp tục.

Với điều này, chúng tôi hiện đã đăng nhập vào bảng điều khiển QDrand.

Lưu ý rằng ở đây chúng tôi có thông báo, chào mừng bạn đến với QDrand Cloud.

Một điều bạn có thể làm nhanh chóng trên trang web này là tạo một cụm dễ dàng để bắt đầu

hoặc làm các xét nghiệm cần thiết.

Trong trường hợp của tôi, chúng tôi có thể đặt tên demo cho cụm này.

Dưới đây là các tính năng của cụm sẽ được tạo.

Mình nên làm rõ rằng đây là cluster miễn phí nên bạn cũng có thể tạo ra để sử dụng miễn phí

cho những cuộc biểu tình này.

Cũng có thể thay đổi nhà cung cấp.

Trong trường hợp của tôi, tôi sẽ giữ nguyên nhà cung cấp mặc định và chọn một địa điểm gần tôi hơn, trong trường hợp này

trường hợp, Hoa Kỳ.

Trong thông tin này, chúng tôi sẽ tạo cụm miễn phí.

Việc này có thể mất vài giây.

Trong khi cụm đang được tạo, cửa sổ này sẽ xuất hiện.

Tôi khuyên bạn nên sao chép khóa API của mình ngay lập tức vì chúng tôi sẽ sử dụng nó sau, vì vậy hãy lưu nó vào một

nơi an toàn.

Khi bạn đã sao chép và dán nó, bạn có thể đóng cửa sổ này.

Sau vài giây, bạn sẽ thấy cụm của chúng tôi hiện đã khỏe mạnh, điều đó có nghĩa là chúng tôi đã sẵn sàng

để tiếp tục.

Bây giờ, hãy quay lại Lancthlo và định cấu hình thành phần QDrand.

Chúng tôi chỉ ra rằng tên bộ sưu tập là tên chúng tôi đã thêm trước đó, đó là tên

mo.

Đối với phần truy vấn tìm kiếm, hiện tại nó không liên quan vì phần này sẽ được sử dụng khi chúng tôi

thực hiện tìm kiếm.

Và chúng ta cần cấu hình trong phần điều khiển là loại bỏ thuộc tính hoặc giá trị máy chủ này,

vì việc rời khỏi nó có thể gây ra lỗi.

Chúng tôi cũng cần thêm khóa API.

Tôi đã sao chép khóa API từ trang web chính và cuối cùng, điều chỉnh nó để thêm URL

của cụm bạn muốn.

Vì vậy, hãy quay trở lại QDrand.

Hãy cuộn xuống một chút và ở đây chúng ta có thể xem cách sử dụng API.

Đây là điểm cuối, đó là điều thực sự quan trọng đối với chúng tôi.

Chúng tôi sẽ sao chép nó.

Hãy quay lại Lancthlo và đó là giá trị chúng ta cần thêm dưới dạng URL.

Bạn cũng có thể thêm trường này để nó sẽ hiển thị như một phần của giao diện đồ họa.

Chúng tôi đóng cấu hình đó và bây giờ chúng tôi đã thiết lập với URL tên bộ sưu tập và

Khóa API.

Với dữ liệu này được định cấu hình, chúng tôi sẽ chỉ định rằng chúng tôi muốn kết nối đầu ra từ

bộ chia văn bản thành thành phần QDrand.

Bây giờ, hãy kết nối khung dữ liệu để nhập dữ liệu.

Chúng ta cũng hãy thêm thành phần cho phép chúng ta lấy thông tin vectơ, nghĩa là chúng ta

sẽ thêm thành phần nhúng openAI, chịu trách nhiệm vector hóa kết quả thu được

thông tin.

Chúng ta sẽ để các tham số mặc định và cuối cùng, chúng ta chỉ cần kiểm tra xem mọi thứ

hoạt động chính xác

Hãy bắt đầu chạy luồng này.

Bạn có thể nhận thấy rằng, sau vài giây, quá trình trích xuất thông tin đã kết thúc,

dữ liệu đã được lưu chính xác và chúng tôi sẽ quay lại QDrand.

Chúng ta hãy chuyển đến phần hiển thị số liệu.

Nhóc, bạn có thể thấy rằng dữ liệu đã được chèn chính xác như một phần của chúng

cơ sở dữ liệu.

Bạn cũng có thể quay lại phần tổng quan, ở đó, ở phía bên phải, bạn có một số thao tác nhanh,

chẳng hạn như truy cập vào cụm.

Chúng ta nhấn vào tùy chọn để truy cập vào cluster.

Nhóc, chúng ta cần nhập khóa API mà bạn đã lấy được trước đó.

Tôi dán khóa API, áp dụng các thay đổi và với điều này, bạn có thể thấy rằng chúng tôi đã có

một số đoạn và điểm được tạo chính xác như một phần của bộ sưu tập này.

Nếu chúng tôi phân tích dữ liệu chi tiết hơn, bạn có thể thấy rằng chúng tôi đã có thông tin cụ thể

từ tài liệu chúng tôi đã thêm trước đó.

Chúng tôi có một số điểm lưu trữ tất cả thông tin này, cho phép chúng tôi xác nhận rằng

việc lưu trữ từ các tệp PDF là chính xác.