# 16 -Các phương pháp bảo mật tốt nhất để chạy Docker Container một cách an toàn.en US

---

Được rồi, điều đó thật tuyệt.

Bây giờ chúng ta hãy xem một điều nữa.

Bây giờ có thêm một biện pháp bảo mật

lỗ hổng trong tập tin docker này.

Hãy để tôi chỉ cho bạn.

Vấn đề là tập tin docker này

chúng tôi đang chạy như NPM Start.

Vì vậy người dùng đang bắt đầu

hình ảnh docker này có

các đặc quyền của quản trị viên.

Điều đó có nghĩa là anh ta có thể xóa các tập tin.

Anh ấy có thể làm bất cứ điều gì trong hình ảnh này.

Vì vậy điều bạn có thể làm là bạn nên

không bao giờ chạy, bạn không bao giờ nên chạy

lệnh cuối cùng này với tư cách quản trị viên.

Vì vậy, những gì bạn có thể làm, bạn thực sự có thể

tạo người dùng trong hình ảnh docker.

Làm sao?

Sau khi tôi đã làm xong mọi việc,

Tôi chỉ có thể nói chạy, thêm, nhóm.

Được rồi, tôi có thể tạo một nhóm nếu bạn

được biết là thích các lệnh Linux.

Vậy hãy tạo một nhóm nhé?

Và tôi chỉ có thể nói, này,

ID nhóm là 1001 và bạn có thể

đặt tên nó giống như nút js.

Vì vậy, giả sử tôi đang tạo một nhóm.

Bây giờ điều tôi có thể làm là

Tôi có thể nói thêm người dùng.

Tôi muốn tạo một người dùng mới, được chứ?

Và sau đó tôi chỉ có thể nói, này, người dùng

ID và tôi có thể cấp ID cho người dùng này.

Giả sử 1001 và tôi có thể cộng nó,

và tôi có thể đặt tên cho nó

người dùng là nút js, phải không?

Chạy, không chạy.

Bây giờ hãy xem tôi có thể làm gì.

Tôi chỉ có thể nói người dùng

và tôi chỉ có thể nói nút js.

Bây giờ những gì nó làm về cơ bản là

những ứng dụng này, ứng dụng này

được chạy với tư cách người dùng này, không phải cái gì

bạn gọi chứ không phải người dùng root.

Ưu điểm của việc này là

bây giờ người dùng này không có quyền truy cập

đến quyền root.

Bạn hiểu điều đó chứ?

Bây giờ người dùng này không có quyền truy cập

đến quyền root.

Vì vậy, khởi động NPM này được chạy dưới dạng nút JS

người dùng không có đặc quyền quản trị viên.

Vì vậy điều này rất quan trọng

mà bạn nên ghi nhớ.

Vì vậy hãy luôn chạy ứng dụng cuối cùng

với tư cách là người dùng không phải root, bởi vì nếu

bạn đang chạy nó với tư cách là người dùng người dùng

root, người dùng, có thể có một số

lỗ hổng bảo mật, nghiêm trọng

lỗ hổng bảo mật có thể

đi lên.

Vâng, đây là một điều

mà tôi muốn cho bạn thấy.

Và vâng, còn một điều nữa là chúng tôi

còn thiếu mà chúng tôi phải đưa ra.

Bạn gọi là gì?

Vâng, có một cái, cổng.

Vì vậy chúng ta phải lộ port 8000

và chúng ta phải làm một việc nữa.

Bạn có biết rằng trong nguồn của chúng tôi

chúng tôi thực sự đang sử dụng cổng

từ một biến process.env.

Vì vậy bạn thậm chí có thể nói rằng, này,

Có một biến env.

Có một cổng biến env,

theo mặc định là 8000.

Bây giờ người dùng thậm chí có thể ghi đè lên nó.

Làm sao?

Hãy để tôi mở thiết bị đầu cuối.

Hãy xem tôi có thể làm gì.

Tôi chỉ có thể nói docker, chạy

tương tác D hoặc

giả sử dấu gạch nối tương tác P.

Này, bạn có thể lập sơ đồ cổng 3000 không?

đến 3000 của docker bên trong?

Nhưng cái thùng chứa đó, cái đó

ứng dụng cụ thể

sẽ không chạy trên 3.000, phải không?

Bởi vì theo mặc định chúng tôi

đã đặt nó ở mức 8.000.

Theo mặc định nếu không có

cổng nó chạy trên 8.000.

Vì vậy tôi có thể nói thiết lập một môi trường

Dấu gạch nối biến e đó là cổng

đến, hãy nói điều gì đó như 3000

và sau đó tôi chỉ có thể nói ts node.

Vì vậy, bây giờ bạn sẽ thấy rằng nó là

chạy trên cổng số 3000.

Vì vậy, bạn thậm chí có thể thiết lập môi trường

biến như thế này.

Bạn thậm chí có thể cho nhiều

dấu gạch nối môi trường e

như x bằng Y.

Dấu gạch nối e cái gì khác bằng

đến điều gì đó thế này.

Đúng vậy, vậy gạch nối e

gạch nối he, gạch nối e.

Bạn có thể làm điều đó.

Được rồi, vậy sử dụng dấu gạch nối này e

cờ, bạn có thể vượt qua

về các biến môi trường khi

bạn đang chạy vùng chứa của mình.

Hoặc nếu bạn có tệp env, bạn

thậm chí có thể làm một cái gì đó như dấu gạch nối

dấu gạch nối tệp ENV bằng, hãy

nói chấm gạch chéo chấm tệp ENV.

Vì vậy, về cơ bản điều này sẽ đọc

toàn bộ tập tin env và tải

những biến môi trường đó trước

đang chạy ứng dụng này.

Vâng, đây là một số

về những thứ bảo mật mà

bạn phải ghi nhớ.

Ổn thôi, hoàn toàn ổn thôi

không hiểu

những điều này vào thời điểm này.

Nhưng chỉ cần nhớ rằng

bạn có thể thay đổi người dùng.

Một khi bạn đã có kiến thức tốt

trong Linux và mọi thứ, sau đó

bạn sẽ hiểu thực tế

trường hợp sử dụng của việc thêm người dùng này.

Vì vậy, hãy kết thúc video này.

Và với điều này chúng tôi cũng có

đã kết thúc phần Dockerfile của chúng tôi.

Bây giờ các bạn đã biết cách tạo

hình ảnh Docker tùy chỉnh.

Bạn biết cách làm việc với tùy chỉnh

hình ảnh, cách xuất bản

những hình ảnh tùy chỉnh đó, cách thực hiện

xây dựng nhiều giai đoạn và cách thức

để dockerize ứng dụng của bạn.

Vậy xin chúc mừng

trên hành trình của bạn cho đến nay.

Tôi hy vọng bạn thích khóa học này

và sắp tới, trong

những phần sắp tới chúng ta sẽ đi

để bây giờ thăng tiến bản thân.

Chúng ta sắp lên cấp

lên trong docker.

Vậy hãy gặp bạn nhé

trong phần tiếp theo.

Cho đến lúc đó, tạm biệt và bảo trọng nhé.