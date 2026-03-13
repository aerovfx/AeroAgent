# 011 Vấn đề với con trỏ vi

---

Người hướng dẫn: Tại thời điểm này, chúng ta đã có một ý tưởng khá hay

về cách hoạt động của con trỏ trong Go.

Hãy nhớ rằng, Go là ngôn ngữ truyền theo giá trị.

Vì vậy, bất cứ khi nào chúng ta truyền một giá trị cho một hàm,

với tư cách là người nhận hoặc là một đối số,

dữ liệu đó được sao chép vào bộ nhớ.

Và do đó, chức năng theo mặc định

luôn luôn làm việc trên một bản sao cấu trúc dữ liệu của chúng tôi.

Chúng ta có thể giải quyết vấn đề này

và sửa đổi cấu trúc dữ liệu cơ bản thực tế

thông qua việc sử dụng con trỏ và địa chỉ bộ nhớ.

Bây giờ chúng ta sẽ bắt đầu nói về một chút

về một vấn đề lớn trong Di chuyển con trỏ.

Để tìm ra chính xác vấn đề này là gì và nó hoạt động như thế nào,

chúng ta sẽ thực hiện một dự án nhỏ khác

bên trong Sân chơi cờ vây.

Vì vậy tôi sẽ chuyển sang trình duyệt của mình

và tôi sẽ điều hướng đến play.golang.org.

Bây giờ khi đến đây, chúng ta sẽ thêm vào

chỉ cần một chút mã ở đây.

Và tin tôi đi, nó chỉ có vài dòng thôi.

Và trong vài dòng đó,

chúng ta sẽ hiểu rõ hơn về vấn đề lớn này là gì.

Vì vậy, hãy bắt đầu với nó.

Bên trong chức năng chính,

Tôi sẽ xóa câu lệnh in hiện có,

và sau đó tôi sẽ thay thế nó

với một tuyên bố về một lát cắt mới.

Vì vậy tôi sẽ tạo một biến có tên mySlice.

Tôi sẽ sử dụng cú pháp dấu hai chấm bằng,

và sau đó khai báo một lát kiểu chuỗi.

Và bên trong nó, chúng ta sẽ cung cấp cho nó văn bản

Xin chào, Có, Thế nào, Bạn.

Được rồi, đây là phần của chúng ta.

Nó có năm yếu tố bên trong nó.

Bây giờ tôi sẽ tạo một hàm riêng

cái đó lấy miếng đó

và cập nhật một trong các phần tử bên trong nó.

Vì vậy chúng ta sẽ nói func updateSlice.

Nó sẽ nhận một đối số mà chúng ta gọi là s, viết tắt của slice,

đó sẽ là kiểu lát của chuỗi.

Và sau đó bên trong đây, hãy tưởng tượng

mà chúng ta muốn thay thế phần tử đầu tiên bên trong slice.

Vì vậy tôi sẽ nói s ở 0,

đó là phần tử đầu tiên bên trong đó,

gửi cho nó tin nhắn Tạm biệt.

Vì vậy chỉ cần thay thế hoàn toàn văn bản

bên trong phần tử đầu tiên này.

Và bên dưới lát cắt ban đầu ngay tại đây,

hãy gọi hàm mới đó là

vì vậy chúng ta sẽ nói updateSlice và chuyển vào mySlice.

Và ngay sau đó,

chúng tôi sẽ đăng xuất giá trị của mySlice.

Vì vậy chúng ta sẽ nói fmt.Println mySlice, giống như vậy.

Bây giờ, đoạn mã này chúng ta có ở đây

trông cực kỳ giống với tất cả các mã

chúng ta đã viết cho đến nay xung quanh một cấu trúc.

Chúng tôi tuyên bố một giá trị mới,

trong trường hợp này là một lát cắt, trước đây là một cấu trúc,

sau đó chúng tôi chuyển giá trị đó cho một hàm,

chúng tôi sửa đổi giá trị và sau đó chúng tôi cố gắng in ra

cấu trúc dữ liệu cơ bản

sau khi nó được chuyển đến hàm.

Và như chúng ta vừa thấy hai phút trước,

giống như trong tất cả các video trước đây

mà chúng ta đã trải qua,

chúng tôi đã nói không ngừng nghỉ

rằng khi chúng ta làm việc với một cấu trúc

hoặc bất kỳ loại giá trị, bất kỳ loại biến nào,

và chúng tôi chuyển nó vào một hàm,

cấu trúc dữ liệu đó được sao chép

và bản sao được vận hành bên trong hàm.

Chúng tôi đã nói điều đó không ngừng nghỉ cho đến thời điểm này.

Vì vậy, hãy chạy mã này ngay tại đây,

và hãy xem điều gì xảy ra với câu lệnh nhật ký này.

Bây giờ, nếu slice hoạt động giống như cấu trúc,

khi chúng ta đăng xuất mySlice ngay tại đây,

chúng tôi mong đợi phần tử đầu tiên vẫn là Hi.

Vì vậy, hãy chạy cái này và xem điều gì sẽ xảy ra.

Vì vậy, khi chúng tôi chạy nó, thật đáng ngạc nhiên,

chúng ta thấy dòng chữ Tạm biệt ngay tại đây.

Vì vậy, mặc dù chúng ta không sử dụng con trỏ,

không có gì như thế, không có địa chỉ bộ nhớ nào cả,

có vẻ như với một lát cắt

khi chúng tôi sửa đổi nó bên trong hàm này,

nó thực sự đã sửa đổi giá trị ban đầu,

điều này hoàn toàn trái ngược với cách hoạt động của cấu trúc của chúng tôi.

Vì vậy, đây là vấn đề lớn mà tôi đang nói đến.

Đây là điều quan trọng, nó giống như vậy,

"Ồ, cách này không hoàn toàn hoạt động theo cách tương tự

với một cấu trúc như với một lát cắt."

Vì vậy chúng ta hãy nghỉ ngơi nhanh chóng.

Chúng ta sẽ quay lại trong phần tiếp theo,

và chúng ta sẽ tìm ra

chính xác tại sao mã này lại hoạt động khác

với một lát cắt hơn là với một cấu trúc.

Vì vậy, hãy nghỉ ngơi nhanh chóng và chúng ta sẽ nói về những gì đang diễn ra ở đây.