# 01 phần giới thiệu thao tác và phương thức nhập liệu

---

[ÂM NHẠC]

Xin chào và chào mừng trở lại với mô-đun tiếp theo

của khóa học này,

Giới thiệu các thao tác và phương thức nhập liệu.

Trong mô-đun trước, bạn đã hiểu

Tương tác giao diện người dùng và các loại của chúng.

Đến cuối mô-đun này bạn sẽ

có thể hiểu khác nhau

hành động đầu vào trong Studio.

Vậy chúng ta hãy bắt đầu, ở phần trước

bài học bạn đã học về đầu vào khác nhau

các hành động như nhấp chuột, gõ văn bản,

phím tắt, v.v.

Trong studio có những hoạt động cụ thể để

thực hiện các hành động này trên giao diện người dùng.

Các hoạt động là nhấp chuột,

gõ vào và gửi phím nóng.

Trước tiên hãy nói về hoạt động nhấp chuột.

[ÂM NHẠC]

Nó thực hiện hành động nhấp chuột

trên một phần tử giao diện người dùng được chỉ định cho

ví dụ: một nút, hộp kiểm radio

nút hoặc mũi tên thả xuống.

Hoạt động này có những đặc tính nhất định để

tùy chỉnh hành động được thực hiện bởi nó.

Chúng ta hãy xem xét một số

tính chất của hoạt động này.

Loại nhấp chuột đầu tiên, thuộc tính này chỉ định

loại hành động nhấp chuột sẽ được

được sử dụng khi mô phỏng sự kiện nhấp chuột.

Hành động click chuột có thể

nhấp chuột một lần, nhấp đúp chuột,

bấm lên hoặc bấm xuống.

Theo mặc định, một cú nhấp chuột được chọn.

Nút chuột thứ hai thuộc tính này

chỉ định nút chuột như bên trái,

nút phải hoặc nút giữa được sử dụng cho

hành động nhấp chuột.

Theo mặc định,

nút chuột trái được chọn.

Tiếp theo là hết thời gian, nó ghi rõ số tiền

thời gian tính bằng mili giây để chờ đợi

hoạt động sẽ chạy trước

một ngoại lệ được ném ra.

Giá trị thời gian chờ mặc định là 30.000

mili giây tương đương với

30 giây.

Tiếp theo, công cụ sửa đổi khóa, thuộc tính này

cho phép người dùng thêm một công cụ sửa đổi khóa.

Các tùy chọn có sẵn là Alt,

Phím Control, Shift và Window.

Hãy thảo luận về hoạt động Nhập vào.

[ÂM NHẠC]

Hoạt động Type Into gửi các lần nhấn phím tới

một phần tử giao diện người dùng, ví dụ như nhập

văn bản trong hộp nhập liệu hoặc tệp word.

Hoạt động này cũng có những tính chất nhất định

để tùy chỉnh hành động được thực hiện bởi nó.

Chúng ta hãy nhìn vào một số

tính chất của hoạt động này.

First activate selecting this

tùy chọn mang lại giao diện người dùng được chỉ định

phần tử ở tiền cảnh và

kích hoạt nó trước khi gõ văn bản.

Điều này rất hữu ích trong khi các hành động

được thực hiện trên nhiều ứng dụng.

Thứ hai được nhấp vào trước khi gõ

về việc chọn tùy chọn này

phần tử giao diện người dùng được chỉ định được nhấp vào

trước khi văn bản được viết.

Tiếp theo, độ trễ giữa các phím,

thuộc tính này chỉ định thời gian trễ trong

mili giây giữa

gõ phím liên tiếp.

Giá trị mặc định là 10 mili giây,

giá trị tối đa có thể là 1000 mili giây.

Tiếp theo là trường trống trên

chọn tùy chọn này,

tất cả nội dung hiện có trong thành phần giao diện người dùng

sẽ bị xóa trước khi văn bản của bạn được nhập vào.

Hãy thảo luận về hoạt động Gửi phím nóng.

Gửi hoạt động Hotkey gửi

phím tắt đến phần tử giao diện người dùng,

Hoạt động này cũng có những tính chất nhất định

để tùy chỉnh hành động được thực hiện bởi nó.

Chúng ta hãy nhìn vào một số

tính chất của hoạt động này.

Đầu tiên kích hoạt, bằng cách chọn tùy chọn này,

nó sẽ mang lại quy định

Phần tử giao diện người dùng ở nền trước và

kích hoạt nó trước khi viết.

Thứ hai, nhấp chuột trước khi gõ

khi chọn hộp kiểm này

phần tử Ui được chỉ định được nhấp vào

trước khi văn bản được viết.

Độ trễ tiếp theo giữa các phím,

điều này chỉ định thời gian trễ trong

mili giây giữa hai lần nhấn phím.

Giá trị mặc định là 10 mili giây và

giá trị tối đa là 1000 mili giây.

Tiếp theo là trường trống trên

chọn tùy chọn này,

tất cả nội dung hiện có trong thành phần giao diện người dùng

được xóa trước khi viết văn bản.

Xin lưu ý rằng tất cả đầu vào

hành động chia sẻ một số thuộc tính chung

đó là độ trễ đầu tiên,

thuộc tính này đặt độ trễ trước hoặc

sau khi nhấp chuột hoặc

gõ bất kỳ văn bản nào vào trường đầu vào.

Thứ hai là chờ đợi sẵn sàng

chọn thuộc tính này nó chờ

mục tiêu đã sẵn sàng

xác minh thẻ ứng dụng nhất định.

Trong video tiếp theo bạn sẽ làm quen

với các phương thức nhập có sẵn cho

các hoạt động đầu vào và

đó là tất cả cho video này.

Cảm ơn bạn đã xem.