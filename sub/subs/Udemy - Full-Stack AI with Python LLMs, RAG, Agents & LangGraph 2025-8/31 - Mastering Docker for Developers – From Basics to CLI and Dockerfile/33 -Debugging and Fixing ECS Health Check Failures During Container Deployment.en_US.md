# 33 -Gỡ lỗi và sửa lỗi kiểm tra tình trạng ECS ​​trong quá trình triển khai vùng chứa.en US

---

Vì vậy, các bạn, chào mừng trở lại với một nơi khác

video thú vị trong docker.

Và nếu bạn còn nhớ, cuối cùng

video, chúng tôi đang gặp sự cố

với, kiểm tra sức khỏe của chúng tôi.

Mặc dù chúng tôi đã kiểm tra sức khỏe

ở đó, chúng tôi đã không thể vượt qua nó.

Và vấn đề,

giải pháp rất ngớ ngẩn.

Ý tôi là, làm sao tôi có thể bỏ lỡ điều này?

Vì vậy, không phải lo lắng.

Tôi đây.

Tôi sẽ chỉ cho bạn cách tôi gỡ lỗi

vấn đề đặc biệt này.

tôi.

Và giải pháp đúng đắn là gì?

Vì vậy, hãy chuyển sang tập tin docker.

Vì vậy nếu bạn nhớ những gì

chúng tôi đã cố gắng làm.

Được rồi, để tôi mở

một tấm bảng trắng cho bạn.

Vậy điều chúng tôi đã cố gắng làm

về vấn đề kiểm tra sức khỏe, chúng tôi

đang nói rằng, này, quay đi

lên một shell lệnh, phải không?

Nếu bạn nhớ điều đó

và làm một việc, uốn tóc.

Bây giờ chính xác thì lọn tóc này là gì?

Curl về cơ bản là một công cụ CLI phải không?

Một công cụ CLI để thực hiện lệnh gọi API.

Ví dụ: nếu tôi mở

thiết bị đầu cuối, chỉ một giây.

Thiết bị đầu cuối của tôi ở đâu?

Ừ, nó đây.

Và tôi sẽ nói là hãy uốn tóc ở đây.

Vậy hãy nói là uốn cong.

Và tôi có thể gạch nối F,

đó là thất bại.

Và tôi có thể nói, này, bạn có thể vui lòng không

gọi tới google.com phải không?

Và những gì bạn sẽ nhận thấy

đó là, được rồi, tôi có một.

Tôi nhận được 301, đúng vậy, bởi vì nó

đã được chuyển đến www.google.com

để tôi có thể gọi điện

tới www.google.com và bạn có thể thấy

Tôi đang lấy lại HTML.

Vì vậy, lọn tóc này về cơ bản là một CLI

tiện ích để thực hiện lệnh gọi API.

Vì vậy, quay lại vấn đề của chúng tôi, chúng tôi

họ đang nói, này, để rèn luyện sức khỏe

kiểm tra, thực hiện cuộc gọi tới đâu,

đến máy chủ địa phương, phải không?

Tới một localhost tại port8000.

Đó là nơi ứng dụng của tôi

chạy và để giảm sức khỏe.

Và nếu, nếu yêu cầu cụ thể này

đang thất bại, chỉ cần thực hiện một lối thoát.

Bởi vì lối ra một về cơ bản có nghĩa là

rằng đó không phải là một điều thành công.

Bây giờ lệnh cụ thể này đang diễn ra

để chạy bên trong container.

Nhưng tôi quên làm một điều, đó là

chúng tôi không cài đặt lọn tóc này

tiện ích trong hình ảnh Alpine Docker của chúng tôi.

Nó đang cố nói, được rồi, tôi sẽ

làm một lọn tóc, nhưng lọn tóc này là gì?

Curl này cần được cài đặt

trong một hình ảnh Alpine.

Được rồi, chỉ là một ví dụ thôi,

chỉ là một ví dụ thôi,

chúng ta hãy làm một điều thôi.

Chúng ta hãy lấy cái này, chúng ta hãy

sao chép hình ảnh cơ sở này.

Điều tôi sắp làm là tôi chỉ

sẽ nói docker run, phải không?

Nó gạch nối, gạch nối RM hình ảnh này.

Và hãy thử chạy cái này

lệnh cuộn tròn, được chứ?

Vậy là nó đang diễn ra

để kéo hình ảnh này đầu tiên.

Chúng ta hãy cho phép nó.

Được rồi.

Vì vậy, bạn có thể thấy rằng nó đang cố gắng

để kéo hình ảnh đặc biệt này.

Vậy chúng ta hãy chờ một lát nhé.

Nó rất tiện dụng.

Và đây là lỗi.

Không thể tìm thấy mô-đun cuộn tròn.

Curl chưa được cài đặt.

Đã giải quyết.

Đó là vấn đề.

Vì vậy, những gì tôi đã làm, tôi đã thêm tuyên bố

đó là chạy apk, thêm vào

dấu gạch nối, dấu gạch nối, không có dấu gạch nối.

Dòng đặc biệt này

cài đặt công cụ tiện ích cuộn tròn

trong vùng chứa Docker của chúng tôi.

Hiểu rồi.

Và làm thế nào tôi đến được

đến điểm đặc biệt này?

Làm cách nào tôi có thể thực hiện việc gỡ lỗi này?

Tôi đã thêm phần kiểm tra sức khỏe đó vào đây.

Vì vậy, hãy nói rằng tôi không có cái này.

Tôi sẽ chỉ bình luận về điều này

được một lúc rồi.

Vậy thì sao, điều tôi đã làm, tôi nói, này,

kiểm tra sức khỏe định kỳ

trong 5 giây, thời gian chờ là 5 giây.

Bắt đầu sau 5 giây và thử 3

lần và thực hiện lệnh cuộn tròn

dấu gạch nối f máy chủ cục bộ tại địa điểm đã cho

cổng đang lấy từ đây.

Xin lỗi, lấy từ đây.

Sau đó, làm cho nó như thế này.

Vậy chúng ta hãy thử làm một điều.

Hãy.

Hãy xây dựng hình ảnh này.

Bạn biết đấy, Docker,

xây dựng dấu chấm API nhóm gạch nối bên phải.

Vậy bạn có thể thấy điều đó

lọn tóc không có ở đó.

Tôi đã nhận xét điều này

điều cụ thể và chúng tôi đang cố gắng

để mô phỏng và kiểm tra sức khỏe.

Vì vậy, bạn có thể thấy việc xây dựng đã hoàn tất.

Bây giờ hãy thử chạy hình ảnh đó.

Vì vậy Docker chạy tương tác, loại bỏ

sau đó là API và nhập.

Vì thế nó sẽ cố gắng làm.

Nó sẽ cố gắng kiểm tra sức khỏe.

Làm cách nào tôi có thể xem phiếu kiểm tra sức khỏe đó?

Vì vậy, bạn chỉ có thể mở

bảng điều khiển Docker.

Vì vậy, đi đến bảng điều khiển.

Được rồi, đây là bảng điều khiển của tôi.

Vì vậy, bạn có thể thấy điều đó.

Có, container đang chạy

trong thùng chứa đặc biệt này.

Nếu tôi đi kiểm tra, phải không?

Và bạn có thể thấy nó không lành mạnh.

Bạn có thấy nó không lành mạnh không?

Tại sao nó không lành mạnh?

Bởi vì không tìm thấy cuộn tròn.

Đây là đâu.

Đây là nơi tôi có thể gỡ lỗi.

Ồ, tiện ích cuộn tròn không có ở đó.

Không sao đâu.

Chúng ta hãy thực hiện một điều khiển

C nên nó bị dừng lại.

Hãy quay lại và bây giờ

cài đặt lệnh cuộn tròn.

Bây giờ bạn có thể thấy đường cong

lệnh sẽ được cài đặt.

Vì thế.

Vì vậy tôi phải xây dựng cái này đặc biệt

hình ảnh một lần nữa bởi vì bây giờ

có một đường cong và nếu có

là một sự thay đổi trên lớp này,

tất cả các lớp sẽ được xây dựng lại.

Vì vậy bạn có thể thấy tất cả

các lớp đã được xây dựng lại.

Tốt đấy.

Bây giờ hãy chạy cái này

lệnh cụ thể một lần nữa.

Bây giờ bạn có thể thấy nó đang chạy.

Và nếu tôi đi và nếu tôi đi

vào, kiểm tra.

Vậy bây giờ bạn đang nói rằng nó là như vậy,

nó phải ở trạng thái khỏe mạnh.

Thấy chưa, nó đang khỏe mạnh

trạng thái vì bây giờ nó đã có thể

để có được mã này.

Vì vậy, đây là một vấn đề nhỏ.

Thông thường bất cứ khi nào tôi đang xây dựng

dự án, tôi luôn sao chép một mẫu.

Tôi không viết tập tin docker từ

vết xước và cong luôn ở đó.

Vì vậy đây là một điều

Tôi thực sự đã bỏ lỡ.

Vì vậy, thực sự xin lỗi vì điều đó.

Nhưng thật tốt khi có lỗi

bởi vì bây giờ chúng tôi đã có thể gỡ lỗi

và chúng tôi đã có thể hiểu được

tầm quan trọng của việc này.

Vì vậy bây giờ với điều đó đã được nói,

chúng ta hãy làm một điều thôi.

Hãy thực hiện lại toàn bộ thiết lập.

Được rồi, vậy để tôi mở ECR

tất nhiên là dành cho bạn và trong một tab mới.

Và để tôi mở ECS cho bạn.

Được rồi, vậy chúng ta phải làm gì

đây có phải là hình ảnh của chúng tôi phải không?

Kho riêng, chúng tôi có

hình ảnh này và ở đây bạn có thể

thấy rằng chúng tôi có vài thứ.

Vì vậy điều tôi sẽ làm là tôi sẽ chỉ

sao chép các lệnh đẩy.

Vì vậy, đầu tiên nhập lệnh đăng nhập.

Vậy chúng ta hãy chờ một lát nhé.

Được rồi, hãy để nó đăng nhập.

Vâng, vậy là đăng nhập thành công.

Hãy xây dựng hình ảnh này.

Được rồi.

Được rồi, xong rồi.

Hãy gắn thẻ hình ảnh cụ thể này.

Vì thế tôi chỉ sao chép

dán các lệnh.

Tôi không làm gì cả,

bạn biết đấy, phi thường.

Và chúng ta hãy thực hiện một cú đẩy docker.

Vậy hình ảnh mới là

sắp bị đẩy.

Trong lúc đó chúng ta hãy vào ECS

và đi vào phần định nghĩa nhiệm vụ.

Và bạn đã có, bạn đã

có một nhiệm vụ API.

Chúng ta hãy có một đánh giá về nó.

Cái đó.

Chúng ta có gì?

Vậy là chúng ta có hình ảnh này rồi phải không?

Chúng tôi có.

Ồ, chờ đã, tôi nghĩ là chúng ta

làm nó như là back-end, phải không?

Hình ảnh đó là gì?

Vâng, bạn biết đấy, hãy bắt đầu

tài liệu tham khảo của cái này.

Vì vậy tôi sẽ chỉ sao chép cái này và tôi có

để thực hiện một bản sửa đổi mới từ nó.

Vì vậy, hãy thực hiện một bản sửa đổi mới và bạn

chỉ có thể sử dụng cái này, phải không?

Vì vậy chúng ta sẽ sử dụng

đây là hình ảnh.

Vì vậy, bạn có thể đặt tên cho nó bất cứ điều gì.

Mọi thứ đều tốt.

Mọi thứ đều tốt.

Và một điều nữa, chúng ta hãy có

khám sức khỏe tại chỗ.

Vì vậy, chỉ cần nhấp vào thông tin,

sao chép cụ thể này

lệnh, dán nó vào đây.

Này, trên localhost8000

bởi vì bây giờ chúng ta đã cài đặt xong cuộn tròn,

đưa ra yêu cầu về sức khoẻ

tuyến đường và kiểm tra sức khỏe, phải không?

Vì vậy đây là mệnh lệnh của chúng tôi

mà chúng ta phải sử dụng.

Vậy nó đi đâu rồi?

Vâng, lệnh shell, cuộn tròn,

gạch nối F thực hiện cuộc gọi về điều này

định tuyến hoặc thoát bằng một.

Đẹp.

Bây giờ với điều đó đã được nói,

chúng ta hãy tạo ra nó.

Vậy là việc này đã được thực hiện.

Bây giờ chúng ta hãy đi vào cụm.

Hãy tạo một cụm để tôi có thể

nói này, bạn là nhóm nhà phát triển của tôi.

Về giám sát AWS Fargate và tất cả,

bạn có thể bật nó lên nếu muốn.

Cụm nhà phát triển đã tồn tại.

Được rồi, làm thôi bạn

biết, dàn cụm.

Không sao đâu.

Bạn biết đấy, chúng tôi có một chút

tài nguyên đã được tạo.

Vì vậy, cụm dàn là

đang trong quá trình sáng tạo.

Vâng, điều đó ổn thôi.

Thế là hình ảnh của tôi cũng bị đẩy đi.

Cảm ơn bạn.

Bạn biết đấy, dòng rất nhỏ này

trong khi đó chỉ cần một dòng nhỏ có thể

cụm đang được tạo.

Các bạn sẽ rất tuyệt vời

nếu bạn có thể đánh giá khóa học này.

Ý tôi là tôi thực sự muốn

để có đánh giá chính hãng của bạn.

Vì vậy, bạn có thể nhấp vào nút dấu sao

ở góc trên bên phải

và đưa ra đánh giá chính hãng của bạn.

Nó giúp tôi hoàn thiện bản thân

nếu có điều gì đó

có thể được cải thiện có thể

được bổ sung vào khóa học này.

Thêm vào đó nó cũng sẽ cho phép tương lai

người học có sự lựa chọn tốt hơn

khi mua khóa học này.

Vì vậy, cảm ơn bạn vì điều đó.

Và với điều đó bạn có thể

xem cụm của tôi đã sẵn sàng.

Bây giờ hãy tạo một dịch vụ.

Phải?

Vì vậy, chúng tôi sẽ tạo ra một dịch vụ.

Vậy ở đây, năng lực,

chúng ta phải nói kiểu phóng.

Này, tôi muốn có Fargate và tôi muốn

tạo ra một dịch vụ thuộc nhóm API

nhiệm vụ, Chọn bản sửa đổi mới nhất

và đặt tên nó là API.

Vậy là ổn rồi.

Nhiệm vụ mong muốn sao chép là một

và kết nối mạng.

Mọi thứ đều tốt phải không?

Nó có IP công cộng và những gì

các nhóm bảo mật là gì?

Không sao đâu.

Cân bằng tải.

Đúng.

Tôi cần một bộ cân bằng tải ứng dụng

vì vậy bạn có thể đặt tên này là API LB mới.

Được rồi.

Đây là bộ cân bằng tải của bạn

tên và kiểm tra sức khỏe.

Mọi thứ đều ổn trên cổng 80.

Được rồi.

Trên cổng 80 người nghe của bạn là

sẽ chạy đó là HTTP.

Vì vậy bạn có thể nhìn thấy mọi thứ

là tốt, phải không?

Mọi thứ đều ổn.

Bạn có thể bật tự động

mở rộng quy mô nếu bạn muốn.

Vì thế tôi có thể nói này, tối thiểu,

Tôi muốn cái này tối đa.

Tôi muốn năm container quay lên.

Làm thế nào để quay lên?

Tôi có thể nói, này, nếu CPU

việc sử dụng, nếu việc sử dụng CPU

đạt 70% quay vòng một thùng chứa mới.

Đúng vậy, đó là chính sách của bạn và chỉ

bấm vào nút tạo này.

Vì vậy bây giờ sẽ mất một thời gian

bởi vì nó phải tạo ra trong nội bộ

cân bằng tải, nhóm mục tiêu,

Các vùng chứa, tác vụ docker API.

Vì vậy, về cơ bản nó đang cố gắng tạo ra

rất nhiều thứ chẳng hạn.

Bạn có thể tiếp tục hình thành đám mây,

phải không?

Vì vậy, sự hình thành đám mây, điều này

là nơi nó thúc đẩy.

Bạn có thể thấy đó là sự sáng tạo

đang tiến hành cái gì?

Tất cả các tài nguyên nó đang tạo ra.

Bạn chỉ có thể nhấp vào các tài nguyên.

Vậy là nhóm mục tiêu đã xong.

Đang cân bằng tải.

Nó sẽ thực hiện một nhiệm vụ.

Mọi thứ như bạn biết,

tất cả đều tự động.

Đây là lý do tôi yêu aws.

Mọi chuyện rất rõ ràng, rất

dễ dàng và quá tốt người đàn ông, quá tốt.

Những điều này đã được thử nghiệm trong trận chiến.

Vì vậy, vâng, chúng ta cần phải chờ một thời gian.

Được rồi.

Trong khi đó nó đang tạo ra nguồn lực

và tôi hy vọng rằng mọi thứ

diễn ra hoàn toàn ổn.

Được rồi.

Trong khi đó các bạn có

để làm một việc nữa

Chúng ta phải thiết lập

lên phía trước đám mây là tốt.

Nhưng chúng ta chỉ có thể thiết lập mặt trước đám mây

một khi, bạn biết đấy, tải

bộ cân bằng đang hoạt động.

Cloudfront là gì?

Cloudfront về cơ bản là

một bộ đệm phân tán.

Vì vậy, đây là những gì chúng ta phải làm.

Vậy chúng ta hãy chờ một lát nhé.

Phải?

Vì vậy bạn có thể thấy rằng

dịch vụ đang chạy.

Phải?

Và hãy xem các nhiệm vụ.

Bạn có thể thấy nhiệm vụ

hiện cũng đang chạy.

Ban đầu sẽ mất 30 giây

để thực hiện kiểm tra sức khỏe đầu tiên

bởi vì đó là những gì chúng tôi đã cho đi.

Đó là cái giống như mặc định.

Bây giờ bạn có thể thấy nó đang khỏe mạnh

bởi vì chúng tôi đã cài đặt cuộn tròn.

Vì thế nó khỏe mạnh.

Phải?

Điều đó thực sự tuyệt vời.

Bây giờ hãy thiết lập

lên phía trước đám mây là tốt.

Vì vậy tôi sẽ chỉ làm

một sự phân phối tạo ra.

Bạn phải chọn

cân bằng tải của bạn.

Bạn có thấy điều đó tự động không

cân bằng tải đó đang đến.

Đúng vậy, bạn chỉ cần chọn

trên bộ cân bằng tải này.

Vâng, cân bằng tải, bạn có

chỉ tạo HTTP vì

bộ cân bằng tải đó là

chạy trên giao thức HTTP.

Được rồi.

Sau đó bạn có thể đặt tên cho nó.

Mọi thứ đều ổn.

Mọi thứ đều ổn.

Ở đây bạn chỉ có thể nói, này, viết lại

HTTP thành HTTP và được phép

Bạn có thể thực hiện các phương thức HTTP ở đó

bộ nhớ đệm, điều này rất tuyệt vời.

Mọi thứ đều tốt.

Được rồi.

Và bạn chỉ có thể vô hiệu hóa WAF.

Vì vậy, điều này về cơ bản là dành cho DDoS

tấn công và tất cả những thứ đó.

Nếu bạn muốn kết nối tùy chỉnh của bạn

tên miền bạn có thể làm điều đó từ đây.

Nhưng.

Nhưng vâng, chúng ta sẽ bỏ qua nó

bây giờ và chỉ cần làm

một sự phân phối tạo ra.

Bây giờ đây là gì, cái này sẽ làm được.

Điều này về cơ bản sẽ tạo ra một cái gì đó

được gọi là CDN trên mọi vị trí cạnh.

Điều đó có nghĩa là trên mọi

ở những nơi khác nhau trên thế giới.

Giống như bạn biết đấy, bạn có Mumbai,

bạn có Chandigarh, bạn có Hoa Kỳ,

bạn có Frankfurt, bạn có Châu Âu.

Ở mọi nơi của vị trí đó

về cơ bản sẽ triển khai một cdn.

Và đây là URL cho cdn của chúng tôi.

Và về cơ bản đây là chỉ

cái này đang chỉ tới đâu

nhiệm vụ ECS của bạn.

Điều đó có nghĩa là nó diễn ra như thế nào.

Điểm phía trước đám mây

tới bộ cân bằng tải.

Điểm cân bằng tải

đến dịch vụ đặc biệt này.

Dịch vụ đặc biệt này được tải

cân bằng giữa các thùng chứa.

Được rồi.

Vì vậy bây giờ chúng ta phải chờ một thời gian.

Vì vậy, bạn có thể thấy rằng chúng tôi có

để chờ một lúc.

Bởi vì hiện tại nó

trong quá trình triển khai, nó có

triển khai ở mọi khu vực.

Vậy đó là lý do, bạn biết đấy, nó

hiện đang trong giai đoạn triển khai.

Phải mất một thời gian.

Có thể mất khoảng 15 phút,

20 phút, tùy

về giao thông và tất cả những thứ đó.

Vì vậy, vâng, và một điều nữa

điều mà tôi đã nhận thấy.

Bạn biết đấy, khi bạn có một tuổi già

tài khoản AWS, điều đó có nghĩa là bạn

đã và đang thanh toán hóa đơn của bạn

chính xác, họ quay những thứ này

dịch vụ nhanh hơn cho bạn.

Vì đây là AWS mới

tài khoản và tôi chưa bao giờ thanh toán

hóa đơn cho tài khoản này vì

nó là một cái mới hơn, phải.

Không có hóa đơn nào được tạo

cho tài khoản này.

Mức độ ưu tiên của tài nguyên thấp.

Phải mất thời gian để quay các thùng chứa.

Cần có thời gian để làm mọi việc.

Nhưng một khi tôi bắt đầu sử dụng tài khoản này

hàng ngày, tôi thanh toán hóa đơn,

mức độ ưu tiên tăng lên và những điều này

nguồn lực được tăng cường cho tôi.

Vì vậy, vâng, đây là

những gì tôi đã nhận thấy.

Và tôi đã nhận thấy nó

ở mức độ rất cụ thể.

Giống như, nó xảy ra mọi lúc bởi vì

Tôi đã làm việc với AWS trong

Tôi nghĩ, bốn đến năm năm nay.

Vì vậy, vâng, đây là một cái gì đó

mà tôi thực sự có, bạn biết đấy,

nhận thấy và tôi chắc chắn về.

Vì vậy, vâng, cái này đang chạy.

Được rồi, cái đó.

Điều đó thực sự tuyệt vời.

Điều đó thực sự tuyệt vời.

Và hãy làm mới lại

trên đó và sau đó tôi cũng sẽ cho bạn xem

đó là cách bạn có thể thực hiện cập nhật.

Được rồi.

Cách hoạt động của các bản cập nhật.

Trong khi đó, bạn biết đấy, chúng tôi cần

để chờ cái này triển khai.

Chúng ta hãy làm mới.

Ừ, vẫn không có gì vì

việc thăm dò DNS chưa kết thúc.

Vì vậy tôi sẽ tạm dừng video

ngay bây giờ và tôi sẽ tiếp tục lại nó một lần

việc triển khai đã kết thúc.

Được rồi.

Vì vậy, các bạn, cuối cùng

việc triển khai được thực hiện.

Phải mất khoảng một cõi vĩnh hằng

để triển khai điều này.

Tôi bắt đầu ghi lại khóa học này

trở lại năm 2015 và ngay bây giờ

chúng ta đang hướng tới năm 2025.

Vì vậy, vâng, điều đó xảy ra.

Phải?

Vì vậy, nếu tôi sao chép tên miền cụ thể này

tên và tôi dán nó vào đây,

bạn có thể thấy điều đó, vâng, chúng tôi

thực sự đang đi đến container của chúng tôi.

Phải.

Bạn có thể thấy nó trên HTTP.

Và phần tốt nhất là

rằng nó được lưu trữ.

Nó nằm trên các mạng biên.

Nó có trên cdn.

Bây giờ hãy xem làm thế nào chúng ta có thể

triển khai một số thay đổi.

Giả sử tôi muốn thực hiện một số thay đổi.

Vì vậy điều tôi sẽ làm là tôi sẽ

chỉ cần làm cho nó như V2.

Chính xác.

Tôi sẽ chỉ làm nó thành V2.

Vậy bây giờ bạn phải làm gì

là bạn chỉ cần xây dựng

Hình ảnh của bạn một lần nữa, phải không?

Điều đó là cần thiết.

Xây dựng đã xong.

Điều đó thực sự nhanh chóng.

Sau đó, bạn có thể chỉ cần thực hiện gắn thẻ

và sau đó bạn có thể chỉ cần thực hiện một cú đẩy.

Sau khi đẩy xong, phải,

những gì bạn phải làm là

quay trở lại với các dịch vụ.

Được rồi?

Các dịch vụ đi vào API và bạn có

để nhấp vào dịch vụ cập nhật này

nút và bạn chỉ cần nói,

này, chỉ cần buộc triển khai mới.

Đó là nó.

Và chỉ cần thực hiện một bản cập nhật.

Bây giờ bạn sẽ chú ý điều gì

là nếu tôi quay lại cụm đó,

đúng rồi, và tôi bắt đầu làm nhiệm vụ,

trước hết nó sẽ

quay lên một container mới.

Điều đó có nghĩa là hai container

sẽ chạy.

Được rồi.

Đúng vậy, bây giờ là như vậy

đang tiến triển, tôi nghĩ vậy.

Vâng.

Vì vậy, bạn có thể thấy việc triển khai

của container này đang được tiến hành.

Vì vậy trong một thời gian bạn sẽ

nhìn thấy hai thùng chứa.

Nếu đây là tài khoản cũ hơn,

bạn sẽ thấy nó ngay lập tức.

Nhưng vì đây là tài khoản mới,

nguồn lực bị trì hoãn.

Vì vậy bạn có thể thấy rằng điều này

container đang chạy.

Thùng này đang chạy tốt.

Và một container mới là

đang bị quay cuồng.

Phải?

Container này đã bắt đầu 10

vài phút trước và thùng chứa này

vẫn chưa bắt đầu.

Vậy có một điều rất thú vị

thứ mà tôi muốn cho bạn xem

rằng một khi thùng chứa này được

khỏe mạnh, một khi AWS đã

đã xác nhận rằng, vâng, bạn là

khỏe mạnh, nó sẽ giết chết điều này

thùng chứa tự động.

Đó là vẻ đẹp.

Được rồi?

Vì vậy chúng ta hãy chờ đợi

một lúc và để điều này

container trở nên khỏe mạnh.

Vì vậy bạn có thể thấy điều đó đúng

bây giờ hai container đang chạy

và đó là cân bằng tải

giữa hai thùng chứa.

Được rồi?

Vì vậy nếu tôi tiếp tục làm mới

trong một vài lần.

Được rồi.

Bạn biết đấy, bạn nên xem V2V 1C.

Đó là cách nó đang chuyển đổi.

Tôi chỉ đang làm mới

hết lần này đến lần khác.

Bạn thấy đấy, nó đang tung hứng

giữa hai container đó.

Và bây giờ nếu tôi tiếp tục làm

làm mới và sau 30 giây

sẽ được kiểm tra sức khỏe.

Và tôi chắc chắn rằng thùng chứa này

sẽ vượt qua cuộc kiểm tra sức khỏe.

Phải?

Vì vậy, chúng ta hãy chờ một lát.

Vì vậy hãy để việc kiểm tra sức khỏe làm công việc của nó.

Vâng, bây giờ bạn có thể thấy

thùng chứa khỏe mạnh.

Bây giờ thùng chứa này

sẽ bị giết, được thôi.

Vì thùng mới còn khỏe.

Vậy chúng ta hãy chờ một lát nhé.

Vâng, bây giờ bạn có thể thấy điều đó

container sẽ tự động biến mất.

Và chúng tôi chỉ còn lại một container.

Vì vậy bây giờ chúng ta sẽ luôn nhận được V2.

Được rồi.

Đúng vậy, nó thực sự đã được lưu vào bộ nhớ đệm.

Vì vậy có lẽ nếu bạn chờ đợi

khoảng năm phút nữa thôi bạn

sẽ chỉ nhận được một V2.

Vì vậy, đó là cách lăn

triển khai xảy ra.

Piyush.

Điều gì sẽ xảy ra nếu thùng chứa này

đã không khỏe mạnh?

Nếu container mới mà bạn

quay cuồng không tốt cho sức khỏe,

Vì một số lý do,

container mới sẽ bị giết.

Thùng chứa cũ vẫn sẽ

tiếp tục phục vụ giao thông.

Đó là cách hoạt động của các bản cập nhật luân phiên.

Vì vậy đây là điều tôi muốn

để cho bạn thấy rằng bạn có thể sử dụng như thế nào

các container đang được sản xuất.

Bây giờ làm sao để xóa

lên các nguồn tài nguyên, Rất đơn giản.

Đầu tiên chúng ta hãy làm rõ, đầu tiên bạn có

để vô hiệu hóa đám mây của bạn.

Được rồi.

Và một khi bạn nhấp vào đám mây này

vô hiệu hóa phân phối, nó sẽ

phải mất thêm 10 năm nữa để làm điều đó.

Khi tính năng này bị vô hiệu hóa, bạn

có thể thấy rằng bây giờ nó đang nhận được

được triển khai như một người khuyết tật.

Sau đó bạn có thể đi

phía trước và xóa nó.

Nhưng bạn phải đợi

điều vô hiệu hóa và bạn biết làm thế nào

để dọn sạch tài nguyên, đúng vậy.

Vì vậy, bạn chỉ có thể đi trên các dịch vụ.

Vì vậy trước tiên bạn phải giảm quy mô

dịch vụ đặc biệt này.

Vì vậy tôi sẽ chỉ cập nhật

dịch vụ, giảm quy mô nó

về 0, phải không?

Hạ thấp nó xuống không.

Ngay cả việc mở rộng quy mô tự động,

hạ thấp nó xuống 0 và.

Chỉ cần cập nhật thôi, được chứ.

Vì thế hãy để nó mang lại tất cả

thùng chứa xuống.

Một khi việc đó đã xong, chỉ và duy nhất

thì bạn chỉ cần nói, này,

bạn có thể vui lòng tiếp tục được không

và xóa dịch vụ này cho tôi?

Vì vậy nó sẽ xóa dịch vụ này

vì vậy nó thực sự sẽ xóa sạch tất cả

bộ cân bằng tải, tất cả mọi thứ

những gì nó tạo ra sau khi hoàn thành việc này.

Bây giờ bạn có thể thoải mái, bạn

biết, xóa cụm.

Vì vậy chỉ cần nói xóa, xóa

cụm dàn và xóa.

Vậy là cái này cũng sẽ bị xóa phải không?

Vì vậy, về cơ bản đây là cách

bạn có thể làm điều đó

Vì vậy tôi hy vọng bạn hiểu được một điểm rằng

làm thế nào bạn có thể, bạn biết đấy, sử dụng

kiểm tra sức khỏe này làm thế nào tôi gỡ lỗi nó.

Vì vậy đây là điều tôi muốn cho bạn thấy

rằng lệnh này đã bị thiếu.