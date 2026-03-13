# 04 - Python để xử lý trước dữ liệu với Pandas và Matplotlib

---

- [Giảng viên] Chúng ta đã tìm hiểu trước đây

Sự phổ biến của Python như một ngôn ngữ

để xử lý trước và phân tích dữ liệu,

phần lớn là do tính dễ đọc và dễ học của nó.

Trong bài học này,

chúng ta sẽ đi sâu vào hai thư viện Python mạnh mẽ

giúp hợp lý hóa đáng kể quá trình xử lý trước dữ liệu,

Gấu trúc và Matplotlib.

Pandas là một thư viện mạnh mẽ được thiết kế đặc biệt

để thao tác và phân tích dữ liệu.

Nó giới thiệu các cấu trúc dữ liệu, như chuỗi và khung dữ liệu,

giúp đơn giản hóa việc xử lý dữ liệu.

Cho dù bạn cần phân tích, hợp nhất, định hình lại,

or aggregate data, Pandas has you covered.

Trước khi bắt đầu sử dụng Pandas, chúng ta cần cài đặt nó,

và bạn có thể thực hiện việc này bằng lệnh pip install pandas.

Và một khi nó được cài đặt,

chúng tôi nhập nó bằng cách sử dụng import pandas as pd.

Hãy coi pd như một lối tắt cho Pandas để

không phải lúc nào chúng ta cũng phải gõ tên đầy đủ.

Đây là quy ước chung để đơn giản hóa mã của chúng tôi.

Khung dữ liệu là cấu trúc dữ liệu chính trong Pandas.

Hãy nghĩ về khung dữ liệu Pandas tương tự như một bảng

trong cơ sở dữ liệu hoặc bảng tính.

Chúng ta có thể tạo khung dữ liệu từ từ điển,

Tệp CSV, tệp Excel, v.v.

Và sự linh hoạt này cho phép chúng tôi

để dễ dàng tải dữ liệu từ nhiều nguồn khác nhau.

Trong ví dụ này, để tải dữ liệu,

chúng tôi đang đọc tệp dữ liệu đầu vào Telecom_dataset.csv,

và lưu trữ nội dung của tập tin đó

vào khung dữ liệu có tên là df,

sử dụng hàm pandas.read_csv.

Bây giờ, khi chúng ta có khung dữ liệu,

chúng ta có thể thực hiện nhiều hoạt động khác nhau.

Chúng ta có thể xem các hàng trên cùng hoặc dưới cùng bằng cách sử dụng đầu và đuôi.

Chúng ta có thể lấy thông tin về khung dữ liệu bằng cách sử dụng .info.

Để có được bản tóm tắt thống kê nhanh chóng, chúng tôi sử dụng mô tả.

Indexing and slicing help us

truy cập các phần cụ thể trong dữ liệu của chúng tôi.

Vì vậy, chúng ta hãy xem xét một vài ví dụ.

Ví dụ này hiển thị câu lệnh df.head

trong một ô mã Python.

Các hàng từ 0 đến 4 được hiển thị,

đó là năm hàng đầu tiên của khung dữ liệu.

Sau khi tải tập dữ liệu, đây thường là bước đầu tiên

để đảm bảo bạn đã tải dữ liệu.

Ví dụ này hiển thị câu lệnh df.tail

trong một ô mã Python.

Hàng 7038 đến 7042 được hiển thị,

đó là năm hàng cuối cùng của khung dữ liệu.

Ví dụ này hiển thị câu lệnh df.info.

DF.info hiển thị cột, số lượng không rỗng,

và kiểu dữ liệu cho từng đối tượng trong khung dữ liệu.

Làm sạch dữ liệu là một bước quan trọng trong quá trình tiền xử lý.

Các giá trị bị thiếu là phổ biến

và Pandas cung cấp các phương pháp để xử lý chúng.

Chúng ta có thể xác định các giá trị còn thiếu bằng cách sử dụng isnull,

điền chúng bằng cách sử dụng fillna hoặc fillna, N-A,

hoặc thả chúng xuống bằng cách sử dụng dropna.

Sự chuyển đổi bao gồm

thay đổi định dạng hoặc cấu trúc của dữ liệu.

Chúng ta có thể đổi tên các cột bằng cách sử dụng đổi tên,

thay đổi kiểu dữ liệu bằng astype,

và áp dụng các hàm tùy chỉnh cho dữ liệu của chúng tôi bằng cách sử dụng apply.

Metplotlib là một thư viện toàn diện

để tạo ra một loạt các hình ảnh trực quan.

Metplotlib hoạt động với Pandas,

cho phép chúng tôi tạo hoạt ảnh tĩnh

và các sơ đồ tương tác để trực quan hóa dữ liệu của chúng tôi.

Tương tự như Pandas, trước tiên chúng ta cần cài đặt Matplotlib,

sử dụng pip cài đặt matplotlib.

Sau đó chúng tôi nhập nó,

sử dụng import matplotlib.plyplot làm plt cốt truyện,

và điều này cũng sẽ cho phép chúng ta sử dụng các chức năng vẽ đồ thị của nó.

Matplotlib cho phép chúng ta tạo nhiều loại đồ thị khác nhau.

Biểu đồ đường, biểu đồ thanh và biểu đồ

là một số loại cốt truyện cơ bản mà chúng ta có thể tạo.

Tùy chỉnh là chìa khóa để làm cho âm mưu của chúng tôi có nhiều thông tin

và hấp dẫn trực quan.

Chúng ta có thể thêm tiêu đề và nhãn bằng cách sử dụng tiêu đề,

xlabel và ylabel.

Chúng tôi cũng có thể tùy chỉnh màu sắc và kiểu dáng để phù hợp với nhu cầu của mình.

Khi cốt truyện của chúng ta đã sẵn sàng, chúng ta có thể lưu nó bằng cách sử dụng savefig.

Seaborn là một thư viện trực quan mạnh mẽ khác

được xây dựng trên Matplotlib.

Nó cung cấp một giao diện cấp cao để vẽ hấp dẫn

và đồ họa thống kê thông tin.

Các kiểu và bảng màu mặc định của Seaborn

đặc biệt hữu ích

để làm cho hình ảnh trực quan của bạn hấp dẫn hơn

và dễ diễn giải hơn.

Ví dụ này cho thấy một biểu đồ phân tán

nhiệm kỳ và tháng trên trục X

và tổng doanh thu trên trục Y.

Vì vậy, hãy tiếp tục và thử cái này.

Và khi bạn đã sẵn sàng,

hãy cùng tôi xem video tiếp theo để xem giải pháp nhé.