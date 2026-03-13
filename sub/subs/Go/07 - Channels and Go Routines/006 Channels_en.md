# 006 Kênh vi

---

Người hướng dẫn: Bây giờ chúng ta có một ý tưởng hay hơn

về thói quen đi lại là gì,

hãy tích hợp chúng vào chương trình của chúng tôi

để chúng tôi có thể tìm nạp nhiều URL cùng một lúc.

Vì vậy, về cơ bản, mỗi lần

mà chúng tôi gọi là hàm checkLink,

chúng tôi muốn đảm bảo rằng chúng tôi tạo ra một thói quen đi lại hoàn toàn mới,

điều mà chúng ta có thể làm chỉ bằng cách sử dụng từ khóa go.

Vì vậy, tôi sẽ quay lại trình soạn thảo mã của mình.

Bên trong chức năng chính của chúng tôi,

Tôi sẽ tìm nơi chúng ta gọi là checkLink.

Vì vậy, ngay tại đây, chức năng này ngay tại đây,

chúng tôi muốn chắc chắn

được thực thi bên trong một quy trình hoàn toàn mới.

Trong quy trình đó, chúng tôi sẽ tìm nạp liên kết đã cho.

Thông lệ sẽ nói,

"Ồ, cái này trông giống như một loại mã chặn nào đó.

Tôi không thể làm gì khác

cho đến khi chức năng này hoàn thành."

Bộ lập lịch đi sẽ phát hiện ra điều đó

và sau đó chuyển việc thực thi sang một quy trình khác

cho đến khi cuối cùng mọi thứ nói lên,

"Được rồi, cuối cùng tôi đã lấy được tài nguyên của mình,

và bây giờ tôi sẽ in ra thứ gì đó cho người dùng."

Vì vậy tất cả những gì chúng ta phải làm để điều đó xảy ra

là đặt từ khóa go trước lệnh gọi hàm của chúng ta.

Hãy nhớ rằng chúng ta chỉ sử dụng từ khóa go

trước các lệnh gọi hàm.

Được rồi, vậy hãy lưu cái này lại.

Thành thật mà nói, đó thực sự là tất cả những gì chúng ta phải làm

để làm điều này xảy ra.

Vì vậy hãy lưu tập tin này,

và chúng ta sẽ chạy nó và xem điều gì sẽ xảy ra.

Vì vậy tôi sẽ chuyển sang thiết bị đầu cuối của mình,

và chúng ta sẽ đi chạy chính.

Bây giờ tôi sẽ chạy cái này, và chắc chắn rồi,

có vẻ như hoàn toàn không có gì thực sự được in ra.

Vì vậy, chương trình của chúng tôi chắc chắn đã hoạt động trước đây,

nhưng bây giờ nó không hoạt động nữa,

ngay khi chúng tôi bắt đầu giới thiệu các thói quen cờ vây.

Và đây chính là lỗi mà chúng ta đang nói đến

ở cuối phần cuối cùng.

Đây là một lỗi có liên quan rất chặt chẽ

với thực tế là chúng ta đang sinh ra những thói quen này.

Vì vậy, một lần nữa, khi chúng ta khởi động chương trình lần đầu tiên,

chúng ta có thói quen đi chính duy nhất này,

và sau đó bất cứ khi nào chúng tôi sử dụng từ khóa go đó,

chúng tôi đang tạo ra những thói quen cho trẻ em.

Vấn đề là thế này đây.

Đây là nơi mọi thứ bắt đầu trở nên thú vị.

Thói quen chính là thói quen duy nhất bên trong chương trình của chúng tôi

điều khiển khi chương trình của chúng tôi thoát hoặc thoát.

Vì vậy, khi chúng ta bắt đầu chương trình lần đầu tiên,

chúng tôi nhận được quy trình chính này được tạo theo mặc định.

Vì vậy, thói quen chính bắt đầu chạy.

Tại một thời điểm nào đó, khi chúng ta bắt đầu bước vào vòng lặp for,

nên chúng ta có thể tưởng tượng như có lẽ ngay ở đây,

thói quen chính của chúng tôi bắt đầu tạo ra

tất cả những đứa trẻ này đều đi theo thói quen.

Nó bắt đầu hình thành thói quen cho trẻ.

Chúng tôi tạo ra tổng cộng khoảng bốn hoặc năm,

và sau đó quy trình chính nói,

"Được rồi, có đoạn mã nào khác bên trong hàm chính này không?

để tôi chạy?

Giống như có việc gì khác để tôi làm không?"

Và tại thời điểm đó,

sau khi nó kết thúc vòng lặp for ngay tại đây,

thói quen chính là, "Ồ, tôi đoán là không còn gì khác nữa.

Tôi không còn việc gì để làm nữa.

Vậy bạn biết gì không?

Tôi đã hoàn tất và tôi sẽ thoát ra hoàn toàn."

Thói quen chính không quan tâm đến việc tất cả các thói quen của trẻ

vẫn chưa hoàn tất việc tìm nạp HTTP của họ,

hoặc các liên kết thực tế hoặc các URL thực tế

mà chúng tôi đang cố gắng tìm nạp ở đây.

Vì vậy, mặc dù những thói quen của trẻ

vẫn còn một số việc phải làm,

thói quen chính là: "Tôi không có việc gì khác để làm.

Tôi xong rồi.

Tôi đi đây.

Tôi sẽ thoát" và toàn bộ chương trình sẽ tự động thoát.

Vì vậy, rõ ràng việc triển khai rất đơn giản này

của việc nói, "Ồ, vâng, cứ đi và làm gì đó đi

bên trong các quy trình đi riêng biệt khác này,"

sẽ không dễ dàng như vậy đối với chúng ta.

Rõ ràng là phải có

một số lượng công việc bổ sung ở đây.

Vậy cách chúng ta sẽ làm điều này

là bằng cách sử dụng một cấu trúc khác trong Go được gọi là các kênh.

Các kênh được sử dụng để liên lạc

ở giữa các thói quen chạy khác nhau.

Chúng tôi sẽ sử dụng một kênh

để đảm bảo rằng thói quen chính được nhận thức

khi mỗi đứa trẻ này thực hiện các thói quen

đã hoàn thành mã của họ.

Vì vậy, về cơ bản chúng tôi sẽ tạo một kênh,

và kênh đó sẽ liên lạc

giữa tất cả các thói quen đi khác nhau này.

Giờ đây, các kênh là cách duy nhất chúng ta có

để giao tiếp giữa các thói quen đi.

Không có cách nào khác.

Chúng tôi chỉ liên lạc bằng cách sử dụng các kênh.

Vì vậy, chúng ta có thể nghĩ về một kênh

như là một cái gì đó như thế này.

Đó là loại thảo luận hoặc giao tiếp trung gian

giữa tất cả các thói quen chạy khác nhau này

trên máy cục bộ của chúng tôi.

Bạn có thể nghĩ về chính kênh đó

giống như nhắn tin văn bản hoặc giống như nhắn tin tức thời.

Vì vậy, chúng tôi có thể gửi một số dữ liệu vào một kênh

và điều đó sẽ tự động được gửi

đến bất kỳ quy trình chạy nào khác trên máy của chúng tôi

có quyền truy cập vào kênh đó.

Chúng ta có thể xử lý một kênh

giống như bất kỳ giá trị nào khác bên trong Go.

Vì vậy, về cơ bản chúng tôi tạo kênh theo cách tương tự

rằng chúng ta tạo một cấu trúc hoặc một lát cắt hoặc một int hoặc một chuỗi.

Vì vậy, chúng là những giá trị thực tế mà chúng ta có thể chuyển đi,

và trong trường hợp này,

chúng ta sẽ chuyển qua các bước đi khác nhau này.

Bây giờ, điều quan trọng nhất cần hiểu về kênh

là chúng được gõ, giống như mọi biến khác.

Vậy nên tôi không chỉ nói sự thật rằng,

này, giá trị này thuộc loại kênh.

Ý tôi muốn nói rằng thông tin

mà chúng tôi chuyển vào một kênh

hoặc dữ liệu mà chúng tôi cố gắng chia sẻ

giữa những thói quen khác nhau này

tất cả phải cùng loại.

Về cơ bản, khi chúng tôi tạo một kênh,

chúng tôi nói rằng hãy tạo một kênh có mục đích chia sẻ,

giả sử, hãy nhập chuỗi trong toàn bộ ứng dụng của chúng tôi.

Vì vậy chúng ta sẽ tạo một kênh kiểu chuỗi.

Khi chúng tôi tạo một kênh kiểu chuỗi,

điều đó có nghĩa là chúng tôi chỉ có thể gửi tin nhắn chuỗi

thông qua kênh này đến các hoạt động đi khác.

Vì vậy chúng ta không chỉ giới hạn trong việc giao tiếp

với các kênh kiểu chuỗi.

Chúng ta cũng có thể tạo một kênh chia sẻ số float

hoặc int hoặc Booleans hoặc structs hoặc bất cứ thứ gì khác,

nhưng chúng tôi không thể lấy một kênh được tạo bằng một chuỗi

và nói, đặt một số giá trị float vào nó.

Điều đó dẫn đến lỗi loại và hãy đi và nói:

"Này, kênh này nhằm mục đích chia sẻ thông tin

hoặc nổi hoặc bất cứ điều gì,

và bạn không thể đặt loại cụ thể này vào đây."

Được rồi, đó là một chút về các kênh,

nhưng rõ ràng là nó không thực sự giải đáp được cách chúng ta sử dụng chúng

để thực sự giao tiếp giữa các quy trình,

hoặc đi theo thói quen, xin lỗi.

Vì vậy chúng ta hãy tạm dừng nhanh chóng.

Chúng ta sẽ quay lại phần tiếp theo.

Chúng tôi sẽ tạo kênh đầu tiên của mình

và tìm ra cách sử dụng nó để giao tiếp

giữa tất cả các thói quen đi khác nhau này.

Vì vậy, hãy nghỉ ngơi nhanh chóng và tôi sẽ gặp bạn trong video tiếp theo.