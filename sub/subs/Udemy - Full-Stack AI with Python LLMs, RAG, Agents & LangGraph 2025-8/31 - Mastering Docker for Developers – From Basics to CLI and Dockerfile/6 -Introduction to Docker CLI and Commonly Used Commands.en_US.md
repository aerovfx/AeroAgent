# 6 -Giới thiệu về Docker CLI và các lệnh thường dùng.en US

---

Này, chào mừng đến với một điều thú vị khác

video về khóa học docker.

Và trong video đặc biệt này,

hãy xem một số lệnh Docker CLI.

Trong phần cụ thể này, chúng tôi sẽ

xem Docker CLI như thế nào, sử dụng

giao diện dòng lệnh, bạn có thể

tương tác với động cơ docker.

Được rồi.

Động cơ docker này là

thực sự là một điều rất mát mẻ.

Và trong video cụ thể này, tôi sẽ

chỉ cho bạn xem một số thông tin nội bộ

những thứ của động cơ docker này.

Vì vậy, hãy bắt đầu

với video.

Vậy điều tôi đã nói với bạn

lúc đầu để chạy Docker,

bạn cần một cái gì đó được biết đến

như động cơ docker, phải không?

Động cơ docker này.

Bây giờ, công cụ docker này

chịu trách nhiệm về

xử lý các container này.

Bạn biết đấy, khi nào cần tạo

một thùng chứa, khi nào cần xóa

một thùng chứa, khi nào cần tạo

một hình ảnh, cách kéo một hình ảnh.

Vì vậy toàn bộ việc quản lý này

của container và hình ảnh được thực hiện

bởi công cụ docker này, phải không?

Bây giờ, một vẻ đẹp của docker này

động cơ, để tôi chỉ cho, bạn

biết đấy, có công cụ docker này.

Vì vậy chỉ cần giả sử rằng đây là

động cơ docker, phải không?

Đây là công cụ docker của bạn.

Vì vậy, một vẻ đẹp của công cụ docker này

là cái này, nó hiển thị một số API

mà bạn có thể giao tiếp.

Vì vậy, khi tôi nói docker, xin lỗi, hãy kiểm soát

D, tôi chỉ muốn đi lên từ đó.

Tôi chỉ muốn, bạn biết đấy, thoát ra ngoài

từ thùng chứa này.

Vâng.

Vì vậy, khi tôi nói docker, hãy chạy

tương tác, giả sử, và tôi nói

Ubuntu, vậy về cơ bản điều gì sẽ xảy ra?

Tại sao lại có mệnh lệnh kỳ diệu này, cái gì

lệnh kỳ diệu này làm gì?

Điều này về cơ bản nói với Docker

động cơ đó, này, tôi muốn.

Được rồi, điều tôi muốn làm, về cơ bản là tôi

muốn chạy một hình ảnh Ubuntu.

Điều này báo hiệu docker

động cơ, và động cơ docker này

nhận yêu cầu này.

Và những gì nó làm, về cơ bản là

chạy một container cho chúng tôi.

Với hình ảnh được chỉ định.

Với hình ảnh được chỉ định, phải không?

Và khi tôi đã như vậy.

Và không chỉ vậy, chúng ta thực sự có thể

làm rất nhiều thứ với cli.

Bây giờ, nếu tôi quay lại, bạn có thấy điều này không?

ui, giao diện người dùng tuyệt đẹp này được cung cấp bởi

Docker Desktop, làm sao nó biết cái nào

container đang chạy thì làm sao nó biết

có những hình ảnh gì, đó là

về cơ bản là tương tác giống nhau

Công cụ Docker và mang lại cho bạn rất nhiều

ui đẹp.

Hiểu rồi?

Nhưng bạn có nghĩ rằng giao diện người dùng này sẽ

có sẵn cho bạn ở khắp mọi nơi?

Bạn có nghĩ rằng khi, một khi bạn

trong một máy chủ gốc, trong thực tế

máy chủ, nơi bạn có SSH

thiết bị đầu cuối, bạn có nghĩ rằng bạn có thể

cài đặt giao diện người dùng Docker này ở mọi nơi?

Không, điều đó là không thể, phải không?

Giao diện người dùng Docker này tốt.

Đây là một công cụ rất hữu ích cho bạn

mục đích của nhà phát triển, nhưng bạn luôn

không có giao diện người dùng docker này

được cài đặt trên mọi máy.

Vì thế bạn phải học

về tất cả các lệnh dòng lệnh

để tương tác với công cụ Docker này.

Và bạn đã biết một

lệnh, đó là chạy Docker.

Bây giờ hãy để tôi chỉ cho bạn một số lệnh.

Được rồi, kiểm soát D.

Vì vậy, bạn có thể thấy rằng tôi

bên trong cỗ máy của chính tôi.

Vì vậy, một là nếu tôi chỉ nói docker, bạn

có thể thấy rằng sự giúp đỡ xuất hiện.

Đây là tất cả các lệnh

mà chúng ta có thể sử dụng.

Được rồi, đây là docker.

Vì vậy, bạn có các lệnh phổ biến

như chạy những gì chạy tạo ra

và chạy một container mới.

Chúng ta đã thấy điều này rồi phải không?

Docker exec PS ở đó.

Vì vậy, docker build là ở đó.

Vì vậy đây là tất cả các lệnh

mà chúng ta nên biết.

Vì vậy, hãy đề cập đến điểm chung

lệnh đầu tiên.

Được rồi, tôi sẽ quay

thiết lập một thiết bị đầu cuối mới để mọi thứ

là siêu rõ ràng với bạn.

Được rồi, một là Docker Docker ps.

Vì vậy, Docker PS về cơ bản

liệt kê tất cả các container.

Được rồi, tôi chỉ có thể nói Docker ps

Bạn có thể thấy rằng tôi không

có bất kỳ container nào đang chạy.

Bạn có thể thấy id vùng chứa.

Mọi thứ đang dần trở nên vô giá trị.

Tại sao?

Vì không có vùng chứa Docker

đang chạy và thoát.

Được rồi, được rồi, chỉ để chứng minh quan điểm của tôi,

hãy để tôi nói Docker chạy,

Ubuntu tương tác nhập.

Bạn có thể thấy rằng điều đặc biệt này

container đang chạy,

đó là ece, đại loại như thế.

Bây giờ nếu tôi chạy thì sao

lệnh tương tự một lần nữa?

Được rồi, tôi hiểu rồi.

Này, ACEE05 này đang chạy.

Bạn có thể thấy đây là điều tương tự

và Ubuntu và lệnh là thế này

đã tạo 7 giây trước và cập nhật cổng.

Và bạn biết nó có một cái tên độc đáo.

Vì vậy, nếu bạn so sánh kết quả đầu ra này

với kết quả đầu ra này, bạn thực sự sẽ

thấy rằng những điều này giống nhau.

Bạn có thể thấy, ID giống nhau.

Bạn có thể thấy ID giống nhau.

Bạn thậm chí có thể thấy tên giống nhau.

Về cơ bản thì cái này, giao diện người dùng này,

máy tính để bàn Docker này là

cũng tiêu thụ cùng một bộ

API để cung cấp cho bạn giao diện người dùng.

Được rồi, bây giờ chúng ta hãy quên đi

về máy tính để bàn Docker này.

Bạn có thể thấy bằng cách làm điều này

Docker ps, tôi đã có thể

để liệt kê tất cả các container,

tất cả các container đang chạy.

Nhưng nếu tôi nói Docker PS giúp đỡ

vì vậy bạn thực sự sẽ thấy đó là gì

tôi có thể làm gì khác với Docker ps này không?

Vì vậy tôi có thể nói Docker PS liệt kê tất cả

các thùng chứa và bạn chỉ có thể nói

Docker PS A hoặc gạch nối, gạch nối tất cả

để hiển thị tất cả các container.

Nhưng theo mặc định nó chỉ hiển thị

các container đang chạy.

Được rồi, được rồi, đây là,

đây là điều tôi muốn

Vì vậy tôi chỉ có thể nói Docker PS gạch nối A

để liệt kê tất cả các container, thậm chí

nếu họ đang ở trạng thái đã thoát.

Hoặc tôi có thể phù hợp với Docker ps,

dấu gạch nối, dấu gạch nối, tất cả.

Hiểu rồi, hiểu rồi.

Chỉ cần nhìn thấy điều đó.

Làm thế nào tôi có thể làm được điều này?

Thấy chưa, tôi chỉ đang đọc tài liệu

trước mặt bạn phải không?

Và bí danh.

Bạn có thể làm Docker container ls,

bạn có thể làm danh sách vùng chứa Docker.

Bạn thậm chí có thể làm Docker container ps.

Bạn có thể làm Docker ps.

Vì vậy, về cơ bản đây là các lệnh giống nhau.

Vậy Docker PS chỉ là cách viết tắt

để thực hiện Docker container ls.

Vì vậy, bạn có thể thấy tôi có thể nói Docker

container ls Điều tương tự.

Docker container LS A.

Hoặc tôi có thể nói docker, Docker,

container, container ps, Điều tương tự.

Hoặc tôi có thể trực tiếp làm Docker ps.

Thế thì sao.

Những gì nhóm đang làm là

về cơ bản vì niêm yết

thùng chứa là một thứ rất phổ biến

lệnh, họ đã viết tắt

đó là tâm lý của Docker.

Thật tuyệt vời.

Vì vậy, bây giờ bạn biết một lệnh.

Đó là cái gì vậy?

Một lệnh đó là Docker ps.

Phải?

Và để.

Để nhận được sự giúp đỡ, bạn chỉ cần

nói docker, Docker ps Dấu gạch nối,

gạch nối, gạch nối, giúp đỡ.

Được rồi, về cơ bản thì điều này

mang đến cho bạn sự giúp đỡ.

Vậy Docker ps là gì?

Docker PS có liệt kê

tất cả các thùng chứa.

Đẹp.

Bây giờ hãy làm lại Docker.

Vì vậy, Docker ps về cơ bản

để có được tất cả các thùng chứa

bạn đã xây dựng Docker.

Vì vậy chúng ta sẽ thấy một khi chúng ta bước vào

nội dung tập tin docker, phải không?

Bạn có hình ảnh Docker.

Bạn có thể nói hình ảnh Docker.

Ồ, điều đó có nghĩa là tôi có thể

nói hình ảnh Docker.

Đi vào.

Tôi có một hình ảnh được cài đặt

trên máy của tôi, Ubuntu.

Phải?

Hình ảnh Docker, dấu gạch nối, dấu gạch nối trợ giúp.

Được rồi, vậy tôi có thể nói Docker image ls.

Tôi có thể nói danh sách hình ảnh Docker.

Hình ảnh Docker.

Tôi có thể nói gạch nối, gạch nối tất cả

để hiển thị tất cả các hình ảnh.

Ẩn mặc định

những hình ảnh trung gian.

Tôi có thể nói gạch nối, gạch nối tiêu hóa.

Tôi có thể nói định dạng.

Tôi có thể nói chuỗi định dạng.

Tôi có thể nói im lặng.

Tôi có thể nói cây.

Vậy bạn có thể thấy điều đó

đây là những lệnh.

Vậy về cơ bản lệnh này là gì

có, điều này liệt kê tất cả các hình ảnh

mà bạn có trên máy của mình.

Vì vậy, nếu tôi chỉ thực hiện điều khiển D và tôi nói

docker, chạy tương tác và busybox.

Được rồi, vậy tôi chỉ muốn chạy hộp bận rộn.

Vì vậy, hãy bận hộp và nhập.

Nên không thể tìm thấy hình ảnh

bây giờ nó sẽ kéo.

Được rồi, hãy chờ kéo.

Kéo là xong.

Bây giờ nếu tôi làm docker, hình ảnh,

bạn có thể thấy tôi có hai hình ảnh

trên máy của tôi phải không?

Và cùng với kích thước của chúng,

thứ quá tuyệt vời phải không?

Những thứ tuyệt vời.

Vậy Docker image, Docker Image LS vậy

Docker image LS tương tự như vậy.

Về cơ bản đây là những bí danh.

Vì vậy bạn có thể, đây là cách bạn có thể

về cơ bản liệt kê các hình ảnh docker.

Được rồi, bây giờ chúng ta hãy đi sâu.

Bây giờ nếu tôi nói docker,

Tôi còn có gì nữa?

Chúng tôi có hình ảnh docker.

Chúng tôi đã thấy đăng nhập và đăng xuất docker.

Tôi sẽ cho bạn thấy sau một thời gian.

Bạn có thể làm phiên bản docker

để hiển thị docker gì

phiên bản bạn đang sử dụng.

Vì vậy tôi chỉ có thể nói docker

phiên bản và nhập.

Vậy là chúng ta đã thấy lệnh này

ngay từ đầu phải không?

Và bạn có thông tin docker.

Được rồi, hãy xem, cái gì

thông tin docker này?

Vì thế tôi chỉ có thể nói

thông tin docker và nhập.

Vì vậy, tôi có thông tin này.

Vì vậy, về cơ bản đây là

tất cả thông tin trên toàn hệ thống

về hệ thống của tôi và những gì tôi đang sử dụng.

Tôi có bao nhiêu hình ảnh, bao nhiêu

container dừng, bao nhiêu container chạy

container, tổng số container.

Bạn có thể thấy nó rất nhiều

về thông tin đang đến

trên máy cụ thể của tôi.

Phải.

Quá tốt, một khởi đầu tuyệt vời.

Phải?

Thứ tuyệt vời này.

Đẹp.

Và một điều nữa.

Bạn có thấy điều này không?

Cái đó, cái gì thế này?

Thứ UNIX này?

Bạn biết nó làm gì không?

Về cơ bản có một docker

socket đang chạy đang nghe

tới các lệnh này.

Vì vậy có thể ở một số nơi khác

video chúng tôi có thể đề cập đến điều đó.

Nhưng đúng vậy, trong video cụ thể này

bạn biết rằng những gì thực sự là một

công cụ docker và cách CLI trợ giúp

bạn tương tác với Docker này

quỷ, quá trình Docker này đang chạy

và quá trình docker này, Docker này

động cơ quản lý nội bộ tất cả điều này

mọi thứ.

Bây giờ tôi sẽ cho bạn thấy một điều.

Nếu tôi đi vào bảng điều khiển này,

bảng điều khiển docker, giao diện người dùng này

về cơ bản tôi đã cho bạn xem,

điều bạn sẽ nhận thấy là ở đây

nó báo công cụ Docker đang chạy.

Nếu tôi tạm dừng việc này thì sao?

Nếu tôi tạm dừng việc này bây giờ thì sao

bạn sẽ thấy rằng tôi thực sự

không thể chạy bất cứ thứ gì.

Docker chạy Ubuntu tương tác gạch nối.

Ồ, nó, nó, nó tự động

khởi động động cơ.

Hãy để tôi tắt động cơ.

Hãy để tôi tắt máy.

Được rồi, bây giờ nếu tôi làm điều này, nó sẽ

cho tôi một lỗi đó

động cơ docker không chạy.

Được rồi.

Tôi hy vọng nó không khởi động lại

nó tự động.

Ồ, nó đang bỏ cuộc, vậy là

nó sẽ mất một thời gian.

Nhưng vâng, bạn có thể thấy điều đó

không thể kết nối với daemon Docker.

Vì vậy, công cụ Docker không chạy

tại thời điểm đặc biệt này

và tôi không thể làm được gì cả.

Phải.

Vậy làm thế nào tôi có thể làm cho nó chạy?

Tôi chỉ có thể mở docker

nộp đơn lại hoặc tôi

có thể nói như systemctl.

Bắt đầu Docker ngay bây giờ.

Công cụ Docker đang chạy.

Bây giờ nếu tôi làm điều đó, bạn có thể thấy

động cơ docker đã hoạt động trở lại.

Vì vậy, công cụ docker này trong nội bộ

đang làm rất nhiều phép thuật.

Trình nền docker này chỉ là

một điều tuyệt vời phải không?

Và bạn nên biết tất cả các lệnh

công cụ dòng, dòng lệnh

để tương tác với công cụ docker này.

Vì vậy, điều này về cơ bản là về

một số điều cơ bản về docker cli.

Và trong video tiếp theo, chúng ta sẽ đi

để đi sâu vào docker

chạy lệnh mà chúng ta nên làm.

Điều đó chúng tôi đã làm cho đến nay.

Vậy là chúng ta hãy kết thúc video

và hẹn gặp lại các bạn ở video tiếp theo.

Vậy tạm biệt nhé các bạn.

Bảo trọng.