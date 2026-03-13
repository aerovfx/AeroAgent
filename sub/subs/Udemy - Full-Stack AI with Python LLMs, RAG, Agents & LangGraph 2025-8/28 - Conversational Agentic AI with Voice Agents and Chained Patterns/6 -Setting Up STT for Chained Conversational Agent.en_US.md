# 6 -Thiết lập STT cho Chained Conversational Agent.en US

---

Được rồi các bạn, vậy bây giờ

mà chúng ta biết về xiềng xích

kiến trúc, chúng ta hãy

mã đặc vụ đầu tiên của chúng tôi.

Vì vậy điều đầu tiên chúng ta sẽ làm

để thiết lập trong video này là

stt, đó là lời nói thành văn bản.

Vì thế bằng cách nào đó tôi phải viết mã

một cái gì đó đưa người dùng

lời nói, đó là âm thanh

và đưa ra văn bản.

Được rồi, vậy hãy xem nào

làm thế nào chúng ta có thể làm điều đó.

Được rồi, vậy hãy để tôi nhanh chóng

mở mã python của chúng tôi.

Vì vậy, đây là mã python của chúng tôi.

Hãy để tôi đóng tất cả lại

những ứng dụng này.

Điều này đang chạy từ

phần trước của chúng tôi.

Vì vậy, hãy chỉ nói một đại lý giọng nói.

Được rồi.

Và hãy tạo ra

một tệp PY chính.

Vậy bước đầu tiên của tôi là gì?

Vậy hãy để tôi tạo ra

một chức năng chính

Tôi chỉ thích làm

mọi thứ theo cách này.

Bước đầu tiên là bằng cách nào đó có được

quyền truy cập vào người dùng, bạn

biết đấy, hệ thống âm thanh và bạn có

về cơ bản để có được điều này.

Vậy làm thế nào để làm điều đó

là thứ được gọi là sr,

nhận dạng giọng nói.

Có một gói hàng, vậy hãy để tôi

chỉ cần tìm kiếm lời nói

gói công nhận python.

Vậy đây là gói

mà chúng ta sẽ sử dụng.

Vì vậy, đó là một nhận dạng giọng nói.

Đúng như tên gọi, về cơ bản nó

chuyển đổi lời nói của bạn thành văn bản.

Vì vậy hãy sao chép lệnh

và cài đặt nó ở đây.

Vậy hãy để tôi chỉ

cài đặt thứ này.

Vì vậy tôi sẽ làm

một pip nhanh chóng, đóng băng

và yêu cầu nội dung Tx.

Đẹp.

Vậy bây giờ chúng ta có thể làm gì để

sử dụng cái này, nó rất đơn giản.

Được rồi nếu chúng ta cứ giữ

cuộn xuống, có

một mã mẫu là tốt.

Mã mẫu đó ở đâu?

Mã mẫu ở đâu?

Được rồi, vì lý do nào đó

mã mẫu là, tôi không thể

để tìm, nhưng dù sao đi nữa.

Được rồi, vậy bây giờ

quá trình cài đặt của chúng tôi đã hoàn tất.

Hãy để tôi nhanh chóng

làm một đường chuyền ở đây.

Vậy điều chúng ta sắp làm là

chúng ta sẽ nói nhập khẩu

nhận dạng giọng nói là sr.

Vì vậy đây là bài phát biểu của chúng tôi

gói công nhận

Những gì chúng ta sẽ làm là

nội dung số một, hãy

tạo nhận dạng giọng nói

đó là công cụ nhận dạng dấu chấm SR nên

về cơ bản đây là những gì

người nhận ra, đây là những gì

về cơ bản là phát biểu,

lời nói đến nhắn tin.

Vì thế tôi chỉ đang lưu giữ nó

trong biến R.

Vì vậy, đây là một công nhận.

Được rồi, để tôi phóng to

trong mã cho bạn để

bạn có thể nhìn thấy nó rõ ràng.

Bây giờ điều chúng ta phải làm là

chúng ta phải có quyền truy cập

tới micrô của người dùng.

Vì thế tôi chỉ có thể nói, này Mr.

Trình nhận dạng giọng nói, bạn có thể

vui lòng truy cập của người dùng

micro làm nguồn.

Vì vậy, dòng này về cơ bản mất

đây là quyền truy cập mic.

Được rồi, bây giờ tôi có thể điều chỉnh

điều đặc biệt này

đối với tiếng ồn xung quanh

có nghĩa là khử tiếng ồn.

Vì vậy tôi sẽ chỉ nói điều chỉnh môi trường xung quanh

tiếng ồn và tôi sẽ chỉ

nói đây là nguồn.

Hãy xem dòng này sẽ làm gì,

về cơ bản đây là môi trường xung quanh bạn

tiếng ồn đang cắt

tắt tiếng ồn xung quanh.

Bây giờ khi nào chúng ta muốn

để bắt đầu công nhận?

Nếu người dùng tạm dừng trong hai giây

sau đó chỉ cần bắt đầu công nhận.

Vì vậy, nếu người dùng dừng lại trong hai

giây đó là nơi

chúng ta sẽ bắt đầu

Bây giờ điều tôi có thể làm là tôi có thể

lấy âm thanh, tôi có thể lấy

âm thanh đó là R

Này, bạn có thể vui lòng lắng nghe được không?

Được rồi, chỉ cần ghi nguồn.

Vì vậy, về cơ bản điều này mang lại

cho tôi âm thanh, đúng không?

Vì vậy, hãy để tôi chỉ in ở đây.

Tôi sẽ chỉ nói nói điều gì đó.

Được rồi, tôi chỉ nói vậy thôi

gửi tới người dùng rằng này người dùng,

làm ơn nói gì đó đi

Bây giờ tôi đang nghe nó,

thì tôi có thể làm được nếu anh ấy đợi

trong hai giây.

Nếu chúng ta không nói gì

trong hai giây tôi chỉ có thể

nói âm thanh xử lý in.

Vì vậy, về cơ bản đây là những gì

bài phát biểu STT của bạn thành văn bản.

Vì vậy điều tôi có thể làm là tôi chỉ có thể

nói STT bằng R chấm nhận dạng.

Bạn có thể thấy bạn có

rất nhiều nhà cung cấp.

Có một cái Google.

Được rồi, R chấm ở đâu

sự công nhận của Google.

Vì vậy bạn chỉ cần nói R

nhận ra Google

và chỉ truyền âm thanh.

Thế thôi.

Vì vậy bây giờ bạn chỉ có thể nói print.

Được rồi và tôi chỉ có thể nói sử dụng nói

và tôi chỉ có thể in stt.

Thế thôi.

Vậy hãy xem liệu chúng ta có thể

để có được âm thanh của người dùng

và chúng tôi có thể xử lý

và in nó ra màn hình.

Vì vậy, đây là bước đầu tiên của chúng tôi.

Vì vậy, hãy để tôi chỉ gọi chính

hoạt động thật nhanh và để tôi

chỉ cần cố gắng chạy mã này.

Được rồi, CD vào giọng nói

đại lý và tôi sẽ đi

nói con trăn và tôi sẽ đi

để nói main py và enter.

Được rồi, vậy bạn có thể

thấy nó đang hoạt động.

Được rồi, vậy chuyện gì đã xảy ra?

Về cơ bản là có lỗi.

Nó báo không tìm thấy PI

âm thanh nên không tìm thấy PI

âm thanh Kiểm tra cài đặt.

Đây là một lỗi dự kiến.

Làm thế nào để giải quyết điều này?

Nếu bạn đến đó thì được thôi bạn

có thể thấy điều đó khi bạn cài đặt

để nó hết nhanh chóng.

Sẽ ổn thôi nếu tôi xuống đó,

thực sự có

đã đề cập rằng bạn sẽ nhận được

lỗi đặc biệt này.

Được rồi, bạn có thể thấy đây là tất cả

âm thanh nhận dạng giọng nói tốt.

Của tôi là osx nên tôi phải làm

cái này được rồi, tôi có

để làm việc này trước tiên tôi

cần cài đặt cổng âm thanh.

Vậy hãy để tôi mở

cửa sổ terminal phải không?

Vì vậy bạn có thể thấy tôi phải nói

brew cài đặt cổng âm thanh.

Vì vậy, đây là một lệnh tôi có

để thực hiện lệnh thứ hai.

Nó đang nói rằng bạn có

để cài đặt âm thanh PI bằng cách sử dụng

lệnh đặc biệt này.

Vì vậy, tôi sẽ chỉ sao chép nó.

Vì vậy, trong khi đó, việc này được thực hiện

bây giờ hãy quay lại đoạn mã,

cài đặt âm thanh nhận dạng giọng nói

và nhập để bạn có thể nhìn thấy.

Bây giờ nó đã được thực hiện.

Có lẽ nó sẽ hoạt động.

Vâng.

Vậy xin chào đại lý,

bạn đang làm gì?

Nhìn thấy?

Vậy xin chào đại lý,

bạn đang làm gì?

Vì vậy bạn có thể thấy chúng tôi

STT thành công

Bất kể tôi đang nói gì, tôi có thể

để chuyển đổi nó thành văn bản.