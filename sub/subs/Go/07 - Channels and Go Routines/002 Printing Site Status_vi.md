# 002 Trạng thái trang in vi

---

Trong phần trước, chúng tôi đã bắt đầu tập hợp một chương trình nhỏ để xem danh sách các URL khác

nhau và thực hiện một yêu cầu HTTP cho từng URL.

Mục đích của công việc này chỉ là để xác minh xem miền đang phản hồi lưu lượng truy cập hay không.

Và vì vậy, trên lý thuyết, if Facebook. com hoặc Amazon. com đi xuống, chương trình của chúng tôi sẽ ở

ra một số thông báo đã biết, điều này có vẻ giống như Amazon. com có ​​thể không hoạt động và không thể phục hồi lượng truy cập đã lưu.

Bây giờ, chúng tôi đã tạo phần URL của mình ngay tại đây.

Chúng tôi đang lặp lại phần đó và bây giờ chúng tôi sẽ viết một hàm nhỏ để lấy liên kết này và đưa ra

một yêu cầu thực tế để xem công cụ địa chỉ dữ liệu có phản hồi lưu lượng truy cập hay không.

Vì vậy, bên dưới chức năng chính của chúng ta, hãy đặt một chức năng khác.

Chúng tôi sẽ gọi cái này.

Làm thế nào để kiểm tra liên kết?

Vì vậy, nó sẽ lấy một liên kết là một chuỗi và nó sẽ thực hiện một yêu cầu HTTP đến nó và quyết định xem liên kết

hoặc URL thực sự phản hồi lượng truy cập đã lưu hoặc không.

Vì vậy, trước tiên chúng ta sẽ bắt đầu từ bên trong đây bằng cách nhận liên kết, liên kết này cần phải nhớ về cơ sở URL của chúng

ta và chúng ta sẽ thực hiện một yêu cầu thực tế đối với nó.

Vì vậy, chúng tôi đã thực hiện điều này trước đó một vài phần trước đây, hãy nhớ đó là http, dấu chấm nhận và sau đó chúng tôi chuyển tiếp

địa chỉ mà chúng tôi muốn thực hiện yêu cầu.

Sau đó, chúng tôi nhận lại hai giá trị từ việc gọi hàm này.

Đầu tiên là một cấu trúc đại diện cho phản hồi thực tế đã quay trở lại và sau đó là thông báo lỗi if

một phản ứng đã xảy ra hoặc nếu một lỗi đã xảy ra.

Bây giờ, trong trường hợp này, chúng tôi không thực sự quan tâm đến đối tượng phản hồi quay lại.

Chúng tôi chỉ quan tâm đến việc khắc phục lỗi có giá trị bởi vì tất cả những gì chúng tôi đang cố gắng làm ở đây đều đã được quyết định xem xét

trang web có phản hồi lưu lượng truy cập hay không.

Vì vậy, chúng tôi sẽ chỉ thực sự xem xét lỗi quay trở lại và chúng tôi không quan tâm đến phản hồi

all.

Về cơ bản, nếu lỗi giá trị này xảy ra ngay tại đây, nếu có giá trị thực tế ở đây, nếu nó không phải là con số 0, thì điều đó có

nghĩa là, tốt, được rồi, chúng tôi có thể gặp sự cố với trang web này và chúng tôi cần trong ra

một thông báo thích hợp về lỗi.

Vì vậy, chúng tôi sẽ thêm vào một kiểm tra nhỏ ở đây.

Chúng tôi sẽ nói nếu lỗi không phải là số không thì điều đó có nghĩa là phải có điều gì đó không ổn với trang web cụ thể này

được đại diện bởi Liên kết ngay tại đây.

Trong trường hợp đó, chúng tôi sẽ ra định dạng, line in và chúng tôi sẽ nói liên kết.

Thêm vào đó, chuỗi của chúng tôi có thể bị lỗi và chúng tôi thực sự không thể sử dụng chuỗi kết nối ở đây.

Chúng tôi chỉ có thể phân tách hai thành phần riêng biệt và điều chỉnh thành chuỗi chính xác cho chúng ta.

Và ngay sau khi in ra một thông báo cảnh báo nhỏ ngay tại đây có nội dung: Này, có vẻ như có

điều gì không ổn với miền này.

Chúng tôi sẽ đưa ra một lệnh hoàn trả để đảm bảo rằng chúng tôi không làm bất cứ điều gì khác trong chức năng này.

Sau đó, sau lệnh if, giả sử rằng không có lỗi, vì vậy sử dụng lỗi là 0, chúng tôi sẽ ra một

thông báo có nội dung: Điều này, có vẻ như trang web này là OC và nó thực sự phản hồi với việc lưu trữ

lượng truy cập.

Vì vậy, chúng tôi sẽ nói liên kết dòng in dạng chấm và được up.

Vì vậy, hoặc đã xảy ra sự cố và chúng tôi giả định rằng trang web không hoạt động, nếu không, chúng tôi cho rằng

mọi thứ đều ổn.

Và một lần nữa, chúng tôi không thực sự cần phải phản hồi các từ yêu cầu để xác minh hoặc đưa ra giả định về công việc

trang web có hoạt động hay không và có phản hồi lưu lượng truy cập hay không.

Vì vậy, đây là chức năng kiểm tra liên kết tốt của chúng tôi.

Bây giờ tất cả những gì chúng ta phải làm là chắc chắn rằng chúng ta gọi hàm kiểm tra liên kết từ trong vòng lặp của chúng ta.

Vì vậy, trong đây, chúng tôi sẽ gọi kiểm tra liên kết và chuyển vào liên kết của chúng tôi.

Vì vậy, điều này trông khá tốt.

Vì vậy, tại thời điểm này, chúng tôi sẽ thực hiện một yêu cầu cho mỗi URL mà chúng tôi liệt kê ở đây.

Chúng tôi sẽ thực hiện yêu cầu, có thể chúng tôi sẽ đưa ra một số phản hồi và sau đó thoát khỏi chương trình.

Không có gì khác, chỉ một.

Chạy qua tất cả các liên kết khác nhau ở trạng thái và thế là xong.

Vì vậy, hãy chuyển sang thiết bị đầu cuối của chúng tôi.

Chúng tôi sẽ chạy chương trình này và chúng tôi sẽ chỉ quan sát hành động và xem điều gì sẽ xảy ra.

Vì vậy, tôi sẽ lại thiết bị đầu cuối của mình.

Tôi sẽ thay đổi kênh thư mục của mình và sau đó chúng tôi sẽ chạy, chạy, chạy, chính, đi theo chương trình của chúng tôi.

Và vì vậy khi chúng tôi làm như vậy, chúng tôi đã tìm thấy tất cả các trạng thái thông báo này bắt đầu được ra.

Bây giờ có một cái gì đó thú vị ở đây.

Bạn sẽ nhận thấy rằng thứ tự mà chúng tôi đang yêu cầu là thứ tự mà chúng tôi đã liệt kê tất cả các thứ tự

URL này nằm trong phần chuỗi của chúng tôi ngay tại đây.

Và đó thực sự là một điều rất quan trọng.

Hãy nghỉ ngơi ngay bây giờ, và chúng tôi sẽ quay lại và nói một chút về chính xác chương trình

Quá trình của chúng tôi đang được thực hiện như thế nào ngay bây giờ và loại sự cố nào chúng tôi có thể gặp phải khi xem xét cách

nó được thực thi.

Vì vậy, nhanh chóng nghỉ ngơi.

Chúng tôi sẽ quay lại và phân tích một chút về tính chính xác của chương trình mà chúng tôi đang chạy như thế nào.