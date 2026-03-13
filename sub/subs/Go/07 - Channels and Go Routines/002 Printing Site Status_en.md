# 002 Trạng thái trang in vi

---

Giảng viên: Ở phần trước chúng ta đã bắt đầu

tập hợp một chương trình nhỏ để xem danh sách

của các URL khác nhau và thực hiện yêu cầu HTTP cho từng URL.

Mục đích chỉ là để xác minh

tên miền có phản hồi lưu lượng truy cập hay không.

Và về lý thuyết, nếu facebook.com hoặc amazon.com ngừng hoạt động,

chương trình của chúng ta sẽ in ra một số thông báo có nội dung:

Này, có vẻ như amazon.com sắp ngừng hoạt động

và không phản ứng với giao thông.

Bây giờ chúng tôi đã tạo phần URL ngay tại đây.

Chúng tôi đang lặp lại lát cắt đó

và bây giờ chúng ta sẽ viết một hàm nhỏ để

lấy liên kết này và thực hiện một yêu cầu thực tế để xem

địa chỉ cụ thể đó có phản hồi lưu lượng truy cập hay không.

Vì vậy, bên dưới chức năng chính của chúng tôi,

hãy kết hợp một chức năng khác.

Chúng ta sẽ gọi cái này, còn việc kiểm tra liên kết thì sao?

Vì vậy, nó sẽ lấy một liên kết, là một chuỗi,

và nó sẽ gửi một yêu cầu HTTP tới nó

và quyết định có liên kết hay không

hoặc URL thực sự đang phản hồi lưu lượng truy cập.

Vì vậy trước tiên chúng ta sẽ bắt đầu bên trong

ở đây bằng cách nhận được liên kết,

mà hãy nhớ về cơ bản là URL của chúng tôi,

và chúng tôi sẽ đưa ra yêu cầu GIT thực tế cho nó.

Vì vậy, chúng tôi đã thực hiện việc này trước đó vài phần.

Hãy nhớ đó là http dot git,

và sau đó chúng tôi chuyển đến địa chỉ mà chúng tôi muốn

để thực hiện yêu cầu.

Sau đó, chúng ta nhận lại hai giá trị từ việc gọi hàm này.

Đầu tiên là một cấu trúc đại diện cho thực tế

phản hồi đã quay trở lại.

Và thứ hai là một thông báo lỗi,

nếu xảy ra hoặc nếu xảy ra lỗi.

Trong trường hợp này, chúng tôi không thực sự quan tâm

về đối tượng phản hồi quay trở lại.

Chúng tôi chỉ quan tâm đến giá trị lỗi trả về.

Bởi vì tất cả những gì chúng tôi đang cố gắng làm ở đây là quyết định

liệu trang web có phản hồi lưu lượng truy cập hay không.

Vì vậy chúng ta sẽ chỉ thực sự xem xét

lỗi quay trở lại và

chúng tôi không quan tâm đến phản hồi chút nào.

Về cơ bản, nếu giá trị lỗi này ở đây,

nếu có giá trị thực ở đây, nếu nó không bằng 0,

thì điều đó có nghĩa là, được rồi

chúng tôi có thể gặp sự cố với trang web này

và chúng ta cần in ra một thông báo lỗi thích hợp.

Vì vậy, chúng tôi sẽ thêm vào một kiểm tra nhỏ ở đây.

Chúng tôi sẽ nói, nếu có lỗi

không phải là không,

thì điều đó có nghĩa là phải có điều gì đó không ổn

với trang web cụ thể này được đại diện bởi liên kết ngay tại đây.

Trong trường hợp đó, chúng tôi sẽ in ra dòng in có định dạng chấm,

và chúng tôi sẽ nói liên kết

cộng với chuỗi của chúng tôi có thể bị hỏng.

Và bạn biết những gì chúng ta thực sự không phải sử dụng

nối chuỗi ở đây.

Chúng ta chỉ có thể tách hai thành các đối số riêng biệt

và điều đó sẽ in ra chuỗi chính xác cho chúng ta.

Và ngay sau khi in

đưa ra một thông điệp cảnh báo nhỏ ở đây nói rằng,

Này, có vẻ như đã xảy ra sự cố với miền này,

chúng tôi sẽ đưa vào một tuyên bố trả lại để đảm bảo

rằng chúng ta không làm bất cứ điều gì khác bên trong chức năng này.

Sau đó, sau câu lệnh if,

giả định rằng không có lỗi,

vì vậy giả sử lỗi là không,

chúng tôi sẽ in ra một thông báo có nội dung:

Này, có vẻ như trang web này ổn đấy,

và nó thực sự phản ứng với giao thông.

Vì vậy, giả sử định dạng dòng in dấu chấm, liên kết và

đã lên.

Vậy hoặc có điều gì đó không ổn,

và chúng tôi giả định rằng trang web đã ngừng hoạt động,

nếu không thì chúng ta cho rằng mọi thứ đều ổn.

Và một lần nữa, chúng ta không thực sự cần phản hồi đến

quay lại từ yêu cầu xác minh hoặc đưa ra giả định về

liệu trang web có hoạt động và phản hồi lưu lượng truy cập hay không.

Được rồi, đây là chức năng liên kết kiểm tra của chúng tôi.

Nó trông khá tốt.

Bây giờ tất cả những gì chúng ta phải làm là đảm bảo rằng chúng ta gọi nó

kiểm tra chức năng liên kết từ trong vòng lặp for của chúng tôi.

Vì vậy, bên trong đây chúng ta sẽ gọi liên kết kiểm tra,

và chuyển vào liên kết của chúng tôi.

Được rồi, cái này trông khá ổn.

Vì vậy, tại thời điểm này, chúng tôi sẽ đưa ra một yêu cầu

cho mỗi URL mà chúng tôi liệt kê ở đây.

Chúng tôi sẽ thực hiện yêu cầu, có lẽ chúng tôi sẽ in

ra một số phản hồi rồi thoát khỏi chương trình.

Không có gì khác, chỉ cần chạy qua tất cả các liên kết khác nhau này

in ra trạng thái và thế là xong.

Vì vậy, hãy chuyển sang thiết bị đầu cuối của chúng tôi.

Chúng tôi sẽ chạy chương trình này và chúng tôi chỉ

sẽ quan sát hành vi và xem điều gì sẽ xảy ra.

Vì vậy, tôi sẽ quay trở lại thiết bị đầu cuối của mình.

Tôi sẽ chuyển sang thư mục kênh của mình,

và sau đó chúng ta sẽ chạy, go run main dot go, chương trình của chúng ta.

Và vì thế khi chúng tôi làm vậy,

chúng tôi thấy tất cả các thông báo trạng thái này bắt đầu được in lên.

Bây giờ có một cái gì đó thú vị ở đây.

Bạn sẽ nhận thấy rằng thứ tự

trong đó chúng tôi đang đưa ra yêu cầu là thứ tự

trong đó chúng tôi đã liệt kê tất cả các URL này bên trong

của lát chuỗi của chúng tôi ngay tại đây.

Và đó thực sự là một điều rất quan trọng.

Chúng ta hãy nghỉ ngơi ngay bây giờ

và chúng ta sẽ quay lại và nói chuyện một chút

về chính xác cách chương trình của chúng tôi đang được thực hiện ngay bây giờ

và loại vấn đề chúng tôi có thể gặp phải

vào việc xem xét nó được thực hiện như thế nào.

Vì vậy, hãy nghỉ ngơi nhanh chóng và chúng ta sẽ quay lại và làm một chút

phân tích chính xác về cách chương trình của chúng tôi đang chạy.