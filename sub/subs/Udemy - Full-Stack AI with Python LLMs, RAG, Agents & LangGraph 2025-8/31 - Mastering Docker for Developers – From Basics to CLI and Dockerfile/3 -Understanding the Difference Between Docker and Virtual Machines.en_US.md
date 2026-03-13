# 3 -Tìm hiểu sự khác biệt giữa Docker và Virtual Machines.en US

---

Vì vậy, xin chào mọi người, tôi hy vọng rằng

bạn đã có thể đến

với giải pháp để giải quyết

vấn đề môi trường phát triển.

Nếu không, đừng lo lắng.

Tôi ở đây để cung cấp cho bạn một hướng dẫn.

Vì vậy trong điều đặc biệt cuối cùng

video chúng tôi thấy đó có vấn đề gì

docker đang cố gắng giải quyết bây giờ?

Giải pháp.

Hãy bắt tay vào giải pháp.

Một giải pháp là tôi có thể

thực sự thiết lập một cái gì đó đã biết

như một máy ảo, phải không?

Có thể có một sự ảo hóa.

Vì vậy, với ảo hóa, điều tôi

có thể làm là tôi phải cài đặt một số

loại VMware hay loại VirtualBox

của một công cụ trên máy của tôi.

Và trên sự ảo hóa đặc biệt này

cấp độ, điều tôi có thể làm là tôi có thể có

Ubuntu, đang chạy, được chứ?

Tôi có thể có bất kỳ, bất kỳ hoạt động nào

hệ thống đang chạy và tất cả những thứ này

các công cụ khác có thể được cài đặt.

Thế nên tôi chỉ có thể nói tất cả những điều tương tự

Có thể cài đặt 10 công cụ +dev

trong máy ảo này.

Và sau đó điều tôi có thể làm là tôi

thực sự có thể chia sẻ ảo này

máy với nhà phát triển của tôi.

Và tôi cũng có thể sử dụng

máy ảo này đây.

Vậy điều đặc biệt này

giải quyết vấn đề của tôi

Điều đó đúng.

Điều đặc biệt này giải quyết được

vấn đề vì bây giờ tôi có một ảo

máy được thiết lập trên máy Mac của tôi.

Anh ấy có bộ máy ảo này

lên máy Windows của anh ấy.

Và mọi người đều có cùng một

Ubuntu, cùng hơn 10 công cụ và

mọi thứ sẽ đảm bảo

rằng có sự nhất quán,

mã hoạt động tốt, mã,

hành vi được mong đợi là ổn về mọi mặt

môi trường.

Nhược điểm của điều này đặc biệt

cách tiếp cận đó là ảo hóa

rất nặng và đắt tiền.

Bởi vì những máy ảo này

trong GBS, nó giống như

điên rồ, như 30gb và 40gb.

Vậy nên việc chia sẻ những chiếc máy này

không hề dễ dàng phải không?

Bạn không thể chỉ chọn nó

lên và chia sẻ nó bởi vì

tất nhiên là nó rất nặng.

Rất nặng và hơi nặng

điểm đặc biệt này

theo thời gian, sẽ là quá mức cần thiết nếu

bạn thực sự nghĩ về nó

Cuối cùng, mục tiêu cuối cùng của bạn

chỉ là để chạy một mã.

Một mật mã?

Mã là gì?

Mã chỉ là một tập tin văn bản.

Và chỉ để chạy một tập tin văn bản

bạn phải thực sự quay

lên toàn bộ máy ảo.

Và điều gì sẽ xảy ra nếu nhà phát triển cụ thể này

đang có một máy cấp thấp?

Giả sử anh ấy chỉ đang có

một máy có RAM 4GB.

Chạy ảo khó lắm

máy bên trong máy thực tế của chúng tôi

chỉ với 4GB RAM, phải không?

Tương tự, nó thực sự đang sử dụng rất nhiều

tài nguyên chỉ để chạy mã của bạn.

Đúng vậy, bạn có thể thực hiện ảo hóa

với VMware hoặc thứ gì đó tương tự.

Nhưng vấn đề duy nhất

là nó rất nặng.

Vì vậy tôi sẽ nói cho bạn biết điều này như thế nào

ảo hóa hoạt động tốt,

vậy chúng ta hãy đi sâu vào một chút.

Vậy hãy nói rằng đây là

lớp phần cứng của bạn, được chứ?

Vì vậy, đây là lớp phần cứng của bạn.

Vậy ý tôi là gì

bởi lớp phần cứng này?

Về cơ bản đây là của bạn,

máy thực tế của bạn nơi bạn

có ram, cpu của bạn, của bạn

bo mạch chủ, mọi thứ.

Nghĩ.

Bật, cấp độ phần cứng cụ thể này

bạn cài đặt một cái gì đó

được gọi là Hệ điều hành.

Vậy hãy nói rằng đây là

một hệ điều hành phải không?

Hệ điều hành này

có thể là bất cứ điều gì

Hệ điều hành này có thể

là Windows, đây có thể là Mac

os, đây có thể là Linux.

Vì vậy hãy nói rằng chúng ta có thể đi

giống như Windows.

Vì vậy, giả sử Windows này là

được cài đặt ở đây trên Windows.

Những gì bạn có thể làm là bạn có thể cài đặt

một loại VMware nào đó, phải không?

Một số loại

cơ chế ảo hóa.

Vậy hãy nói rằng điều này

là siêu giám sát của tôi, được chứ?

Vì vậy, điều này được gọi là hypervisor.

Vì vậy, hypervisor có thể được cài đặt.

Về cơ bản đây là

mức độ ảo hóa.

Và trình ảo hóa này là

kích thước rất, rất cao

và rất đói tài nguyên.

Được rồi, Rất đói tài nguyên.

Tôi sẽ nói với bạn điều đó sau.

Và trên bộ ảo hóa đặc biệt này,

những gì bạn có thể làm sau đó bạn có thể

có nhiều máy ảo.

Ví dụ, tôi có thể có

một máy ảo đang chạy,

giả sử Ubuntu, được chứ?

Vì vậy, chiếc máy này dành cho Ubuntu, tôi

có thể có một máy

đang chạy, giả sử một số Linux.

Tôi có thể có.

Sau đó, một máy đang chạy,

giả sử bạn gọi Windows là gì?

Tôi có thể có một chiếc máy

chạy một số hoạt động khác

hệ thống, có thể lại là Ubuntu.

Vậy bạn hiểu rằng tôi là gì

về cơ bản là làm, chỉ một giây thôi.

Chứng OCD của tôi đang ảnh hưởng đến điều này

điểm bởi vì tôi thực sự muốn điều đó.

Này, nếu điều này có thể được gia hạn, phải không?

Vâng.

Vì vậy bạn có thể thấy rằng những gì chúng tôi có

xong là chúng ta đã có mức độ phần cứng,

chúng tôi có cấp độ Windows,

là hệ điều hành thực tế của tôi.

Chúng tôi có một số hypervisor.

Và trên bộ ảo hóa này chúng ta có thể có

nhiều hệ điều hành, phải không?

Điều này có thể giống như VMware

hoặc một cái gì đó như thế.

Vậy điều xảy ra là đây là những điều rất

đắt tiền về kích thước.

Đây không phải là dễ dàng có thể chia sẻ.

Và mọi máy móc, bây giờ

điều này rất quan trọng.

Mọi máy đều có quyền truy cập

đến cấp độ hạt nhân.

Họ có quyền truy cập vào tất cả

các tài nguyên phần cứng.

Cái này nữa, cái này nữa, và cái này nữa.

Vì vậy, ảo hóa là tốt.

Vì vậy, về cơ bản đây là

ảo hóa.

Ảo hóa là tốt, nhưng sôi sục

đến cùng một vấn đề,

rằng thứ này rất đắt tiền.

Bây giờ giải pháp thứ hai cho cùng

vấn đề là dockerization.

Bây giờ dockerization là loại

chỉ ảo hóa, nhưng trong

một cách rất nhẹ nhàng.

Tôi sẽ cho bạn biết Docker hoạt động như thế nào.

Được rồi, về mặt Docker, vậy

nếu tôi chỉ sao chép tương tự

kiến trúc, vì vậy tôi sẽ chỉ cho bạn biết

đó là cách Docker giải quyết vấn đề này.

Vì vậy, về cơ bản Docker hoạt động

theo một nguyên tắc được gọi là đó

nó chia sẻ cùng một phần cứng

hoặc cấp độ hạt nhân.

Vậy hãy nói rằng điều này

là cấp độ hạt nhân của bạn.

Được rồi?

Vậy Docker làm gì thì Docker sử dụng

thứ được gọi là công cụ Docker.

Được rồi?

Đây là công cụ Docker mà bạn

phải cài đặt trên máy của bạn.

Và điều này rất nhẹ.

Đây không phải là rất

đắt tiền, không lớn lắm.

Được rồi?

Và công cụ Docker ở trên cùng

của công cụ Docker, bạn có thể chạy

một cái gì đó được gọi là container.

Được rồi, bạn có thể chạy một cái gì đó

được gọi là container.

Những vùng chứa này có thể là bất kỳ hình ảnh nào.

Ví dụ, điều này có thể

một thùng chứa Ubuntu.

Được rồi?

Đây có thể là một thùng chứa Ubuntu.

Điều này có thể giống như một thùng chứa Windows.

Đây có thể là một số container khác.

Điều duy nhất, sự khác biệt duy nhất

giữa hai sơ đồ này là

rằng ở đây họ đã có quyền truy cập

đến tất cả cấp độ ảo hóa

và họ có hạt nhân của riêng mình.

Nhưng ở đây kernel là shadcn.

Điều đó có nghĩa là nếu đây là Linux

kernel, nếu đây là Linux

kernel, bạn chỉ có thể chạy

Các thùng chứa Linux ở trên nó.

Nếu là nhân Windows,

bạn chỉ có thể chạy cửa sổ Windows

các thùng chứa ở trên đó.

Điều đó có nghĩa là thực tế

hạt nhân không phải là shadcn.

Nó sử dụng kernel của bạn,

hệ điều hành của bạn.

Phải?

Công cụ Docker là một cái gì đó

cái đó phải được cài đặt và sau đó

bạn có thể chạy bất kỳ container nào.

Vì vậy những thùng chứa này không

hệ điều hành hoàn chỉnh

trong kịch bản cụ thể này.

Những thứ này thực sự đã đầy

hệ điều hành bị thổi bay.

Đây là một hệ điều hành đầy đủ

giống như 5gb, 10gb.

Nhưng đây không phải là một bản đầy đủ

hệ điều hành.

Đây chỉ là một phần thôi phải không?

Nhiều tính năng còn thiếu,

nhưng đây chỉ là một lát cắt.

Đây là một môi trường của điều đó.

Và trong thế giới Docker nó

được biết đến như một hình ảnh.

Vì vậy đây là một điểm khác biệt

làm cho Docker rất nhẹ.

Và bởi vì Docker lúc này

điểm đặc biệt là rất

nhẹ, điều này làm cho dễ dàng

để chia sẻ những hình ảnh Docker này phải không?

Vì thế điều tôi có thể làm là tôi, bạn của tôi,

đồng phát triển của tôi có thể có những thứ này

ba thứ được cài đặt, đó là cái này

Công cụ Docker và tôi chỉ có thể

chia sẻ hình ảnh Docker này với anh ấy.

Tôi thậm chí có thể xuất bản những thứ này

Hình ảnh Docker trên Internet

để bất cứ ai cũng có thể sử dụng a.

Tôi có thể sử dụng hình ảnh Docker này

được nhân bản

về môi trường sản xuất.

Tôi có thể sử dụng hình ảnh Docker này

để tặng nó cho bạn tôi.

Tôi có thể sử dụng hình ảnh Docker này.

Tôi có thể sử dụng Docker này

hình ảnh, với chính tôi.

Vì vậy mọi người đều có cùng một môi trường

trong hình ảnh Docker cụ thể này.

Chúng ta có thể chạy MongoDB, chúng ta có thể

chạy Redis, chúng ta có thể có

không chạy, về cơ bản đã cài đặt.

Bạn có thể cài đặt postgres,

bạn có thể cài đặt Node js,

và chỉ với một cú nhấp chuột bạn

chỉ có thể khởi động nó và chạy.

Vì vậy đây chính là ưu điểm của Docker.

Docker nhẹ,

và vì nó nhẹ,

nó có thể được chạy ở bất cứ đâu.

Điều duy nhất là công cụ Docker

là thứ phải được cài đặt.

Vì vậy, nếu ai đó hỏi bạn điều đó,

lợi thế của Docker là gì

trên ảo hóa?

Nó rất nhẹ.

Sao nó nhẹ thế

bởi vì nó sử dụng kernel của bạn.

Nó không phải là một sự bùng nổ hoàn toàn

hệ điều hành.

Nó sử dụng hệ điều hành của bạn.

Hãy để tôi cho bạn một ví dụ, phải không?

Tôi đã có Docker

được cài đặt trên máy của tôi.

Vì thế đừng lo lắng, tôi sẽ làm vậy.

Tôi sẽ hướng dẫn bạn cách thực hiện

để cài đặt Docker và các thứ khác.

Nhưng tôi đã cài đặt Docker rồi.

Hiện tại tôi đang chạy Mac os phải không?

Vậy hãy để tôi mở terminal

và tôi sẽ phóng to lên một chút.

Vậy đây là Mac OS đang chạy.

Vì vậy, chỉ để chứng minh quan điểm của tôi,

Tôi chỉ có thể nói tên của bạn.

Vậy bạn có thể thấy đây là Darwin.

Bây giờ tôi có thể nói Docker chạy

và tôi có thể nói gạch nối nó.

Đừng lo lắng, tôi sẽ kể cho bạn nghe

đây là những gì và tôi có thể

chỉ cần nói Ubuntu và nhập.

Bây giờ những gì bạn sẽ thấy là

một khi tôi cho phép nó, nó

cài đặt Ubuntu này cục bộ.

Bạn có thể thấy nó nói không thể

để tìm hình ảnh Ubuntu.

Vậy là chỉ với 28 MB, Ubuntu đã có mặt ở đây.

Bây giờ chỉ cần xem.

Bạn có thấy cái gốc này không?

Với tỷ lệ một số số

Tôi đang ở trong vùng chứa Docker.

Tôi chỉ có thể nói tôi là ai?

Hoặc tôi có thể nói tên của bạn.

Thấy chưa, bây giờ tôi là Linux, tôi có thể nói

Vậy ra đây không phải là tập tin của tôi.

Ngay khi tôi làm vậy,

đây không phải là tập tin của tôi.

Thiết bị đầu cuối đặc biệt này bây giờ

được kết nối với máy Ubuntu.

Điều đó thật điên rồ làm sao.

Chỉ với 28 MB tôi đã có thể chạy

Ubuntu trên máy Mac OS.

Bạn có thể thấy đây không phải là tập tin của tôi.

Vì vậy tôi chỉ có thể làm một đĩa CD ở nhà.

Tôi chỉ có thể nói ls, tôi có thể CD

vào Ubuntu.

Tôi có thể làm được.

Bạn có thể thấy đây là

một máy Ubuntu.

Để thoát khỏi nó, tôi

chỉ có thể thực hiện Điều khiển D.

Và bây giờ tôi đã trở lại với chiếc MacBook của mình.

Tôi thậm chí có thể nói Docker

chạy tương tác.

Được rồi, đừng lo lắng, chúng ta sẽ thấy

cli và ví dụ tôi có thể nói

Busybox bên phải Busy Box và Enter.

Bây giờ bạn có thể thấy nó sẽ

cài đặt Busy Box cho tôi.

Vì Bus Box chưa được cài đặt.

Vì vậy, nó có Busy Box.

Vì vậy, Busy Box chỉ có một mb.

Và bây giờ tôi đang ở trong Busy Box phải không?

Bạn có thể thấy tôi đang ở trong một chiếc hộp bận rộn.

Vì vậy, tôi chỉ có thể thực hiện một lượt ping như vậy

hoặc một cái gì đó như thế.

Tôi có thể nói ping google.com

vậy đây không phải là máy của tôi.

Tôi đang sử dụng một máy ảo.

Và bây giờ tôi lại có thể đi

vào một thùng chứa Ubuntu.

Hãy xem, tôi đang ở trong Ubuntu.

Vậy chỉ với một cli, với

chỉ một lệnh, tôi đã có thể

để khởi động Ubuntu, tôi đã có thể

để khởi động Busybox.

Tôi thậm chí có thể nói Docker chạy

Alpine tương tác, phải không?

Alpine Linux có thể ở đó.

Vì vậy, Alpine và Enter.

Bây giờ nó sẽ cài đặt Alpine cho tôi.

Vậy chúng ta hãy chờ một lát nhé.

Chuẩn rồi.

Vì vậy, bạn có thể thấy rằng tôi

đang ở trong dãy Alpine phải không?

Vậy đây là những điều khác nhau, khác nhau

Docker container đang chạy.

Vì vậy, Dockers thực sự rất nhẹ.

Vì vậy tôi hy vọng rằng tôi có thể

để giải thích rằng vấn đề gì

Docker đang cố gắng giải quyết.

Nó đang cố gắng giải quyết như thế nào?

Nó tốt hơn ảo hóa như thế nào?

Và tất nhiên nó đi kèm với

nhược điểm riêng của nó, phải không?

Bởi vì nếu bạn là

trên nhân Windows, bạn

không thể chạy hạt nhân Linux.

Linux, thùng chứa.

Nhưng thực ra Windows

có hỗ trợ cho Linux.

Nhưng nếu một.

Một vùng chứa được tạo cho Windows, bạn

không thể chạy nó trên Mac OS hoặc Linux.

Đúng vậy, bởi vì nó sử dụng

hạt nhân của bạn, phải không?

Vì vậy đây là một nhược điểm, nhưng nó

thực ra có thể tránh được vì bạn biết đấy,

về cơ bản tất cả các nhà phát triển đều có thể có

cùng một loại hệ điều hành.

Được rồi, nhưng ít nhất chúng ta

không cài đặt tất cả dev

công cụ, tất cả các phần phụ thuộc của nhà phát triển

và mọi thứ trong đó.

Vì vậy, đó là tất cả cho việc này

video cụ thể.

Trong video tiếp theo tôi sẽ hướng dẫn bạn

thông qua những điều cơ bản về Docker, như

cài đặt Docker như thế nào, làm thế nào

để chạy các lệnh cơ bản của Docker.

Sau đó chúng ta sẽ đi lặn sâu

vào Docker với điều đó.

Hãy kết thúc video.

Hẹn gặp lại các bạn ở video tiếp theo.

Cho đến lúc đó, tạm biệt và chăm sóc nó.