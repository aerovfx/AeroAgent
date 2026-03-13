# 15 -Xây dựng hình ảnh Docker nhiều giai đoạn được tối ưu hóa để sử dụng trong sản xuất.en US

---

Được rồi, cụ thể là thế này

video, hãy hiểu nó là gì

xây dựng Docker nhiều giai đoạn.

Đây là một trong số ít khái niệm

điều đó rất quan trọng

trong việc tối ưu hóa tệp Docker của bạn.

Và nhiều nhà phát triển ngoài kia

không sử dụng tính năng này

đó là xây dựng nhiều giai đoạn.

Vì vậy hãy đi sâu vào

video và hiểu những gì

là xây dựng nhiều giai đoạn.

Được rồi, hãy tưởng tượng.

Vâng, vậy hãy tưởng tượng, Hãy tưởng tượng rằng bạn

có rất nhiều mã nguồn phải không?

Bạn có rất nhiều mã nguồn.

Vì vậy, hãy nói rằng mã này là

viết bằng C, giả sử, được chứ?

Và cái này có rất nhiều mã, rất nhiều

của các tập tin mã, rất nhiều C

các tập tin và rất nhiều thứ.

Nếu bạn được bảo rằng bạn có

để Dockerize thứ này,

bạn sẽ làm gì

Trước hết, tính đến thời điểm hiện tại,

kiến thức mà chúng ta có, chúng ta

đầu tiên sẽ sao chép cái này

tập tin vào hình ảnh của chúng tôi, phải không?

Toàn bộ, cái.

Tất cả.

Giả sử có 30 tập tin.

Có 30 tập tin.

Chúng tôi sẽ sao chép tất cả 30

tập tin mã nguồn vào hình ảnh của chúng tôi.

Được rồi?

Sau đó chúng ta sẽ làm gì,

chúng ta sẽ làm,

một cái gì đó được gọi là xây dựng, phải không?

Chúng tôi sẽ xây dựng.

Xây dựng về cơ bản có nghĩa là, bạn biết đấy,

gcc, biên dịch nội dung, xây dựng hoặc bạn

có thể nói biên dịch, và sau đó là

được biên dịch, chúng ta có thể, chúng ta có thể viết một

cmd, một lệnh đó là, đó là

những gì chúng ta có thể nói, như dấu chấm, dấu gạch chéo,

dấu chấm, dấu gạch chéo, cái gì, cái gì cũng được

xuất ra tập tin nhị phân, thật tuyệt vời,

điều đó thật tuyệt vời.

Bạn đã làm một công việc tốt.

Bạn lấy toàn bộ mã nguồn

tập tin, đặt nó vào hình ảnh,

xây dựng nó và đặt lệnh

chấm, gạch bỏ một dấu chấm.

Nó sẽ chạy.

Vấn đề là tại sao khi bạn

có bản dựng đó, bạn có thực sự không

cần tất cả 30 tập tin đó?

Hay thậm chí bạn có cần C đó không?

cài vào máy à?

Hãy hiểu điều này.

Hãy để tôi cho bạn một ví dụ thực tế

ở đây.

Tôi có một ứng dụng

được viết bằng TypeScript.

Vì vậy, bạn có thể thấy rằng đây là

một ứng dụng TypeScript.

Bạn có tệp TypeScript

chạy, a, server.

Bạn có thể thấy điều đó.

Và bạn có một ứng dụng

là một máy chủ tốc hành.

Vì vậy, về cơ bản đây là

một máy chủ TypeScript.

Bây giờ luồng diễn ra như thế nào trong TypeScript

bạn có TypeScript không.

Bạn phải cài đặt

TypeScript trên máy của bạn.

Sau đó, điều bạn phải làm là bạn có

để xây dựng toàn bộ ứng dụng này.

Làm thế nào để xây dựng?

Tôi chỉ có thể làm npm, chạy, xây dựng.

Bây giờ trong quá trình xây dựng, tôi cần

TypeScript, xem này, tôi cần TypeScript.

Tôi cần các loại cho nút, tôi

cần các loại cho Express.

Sau khi xây dựng xong, bạn có thể thấy

rằng sau khi quá trình xây dựng hoàn tất, những

ba điều không còn cần thiết nữa.

Tôi không cần TypeScript

để được cài đặt.

Tôi không cần những thứ này

ở mức giá mà tôi không cần.

Tôi chỉ cần thư mục dist này

và tôi chỉ có thể nói npm bắt đầu,

điều này sẽ nói là nút dist

chỉ số và nó, nó

hoàn toàn chạy được phải không?

Vậy điều đó có nghĩa là chỉ dành cho việc xây dựng

mã này, tôi cần TypeScript,

nhưng tôi không cần TypeScript

cho mục đích sử dụng sản xuất thực tế.

Hãy thử tạo

một tập tin docker cho việc này.

Được rồi?

Sau đó chúng ta sẽ tối ưu hóa nó.

Vì vậy, tập tin docker.

Vì vậy tôi có thể nói từ.

Được rồi.

Và tôi có thể sử dụng nút,

bạn biết đấy, 20 điểm.

Hãy sao chép nó.

Bạn biết đấy, nó luôn luôn

tốt để sao chép nó.

Vậy hub.docker.com

và tôi có thể tìm kiếm node.

Vậy hãy để tôi tìm kiếm

cho nút vì tôi cần

để cài đặt nút js phải không?

Vậy node, chúng ta hãy đi vào node js

và ở đây chúng ta có thể

sử dụng phiên bản Alpine này.

Vì vậy hãy sử dụng khoảng 20 điểm

một cái gì đó nếu bạn có thể nhìn thấy.

Vậy 20 điểm, 17 có thể dùng được.

Vì vậy, tôi sẽ chỉ sao chép cái này.

Được rồi, đây chính là thứ tôi muốn sử dụng.

Ôi sao chép nhiều quá.

Vâng, vì vậy tôi muốn sử dụng

đây làm hình ảnh cơ sở.

Vậy thì chúng ta sẽ làm gì

để làm, chúng ta sẽ sao chép.

Ồ, hãy thiết lập công việc

thư mục đầu tiên.

Vì vậy thư mục công việc có thể là

chém, ứng dụng chém nhà.

Được rồi.

Sau đó tôi có thể sao chép và tôi muốn

sao chép gói *.JSON sang gói2.

Và tôi cũng muốn sao chép

cấu hình TS này.

Vậy T S, config vì nếu không có cái này

ở đó, tôi không thể xây dựng dự án.

Vì vậy, tsconfig JSON cũng có thể

được sao chép vào tsconfig JSON.

Được rồi.

Cuối cùng điều tôi có thể làm là lúc này

vào một thời điểm cụ thể, tôi có thể

hãy chạy cài đặt npm, nó sẽ

cài đặt TypeScript, tất cả

đánh máy, nó sẽ cài đặt tất cả

gói, tất cả các yêu cầu

gói.

Thế thì điều gì tôi có thể làm, tôi có thể

chỉ cần sao chép thư mục dist.

Bạn hiểu điều này chứ?

Tôi có thể.

Thực ra tôi không muốn

để sao chép thư mục này.

Xem nào, hãy sao chép mã nguồn.

Vì vậy, tôi chỉ có thể sao chép nguồn này.

Hãy, hãy loại bỏ điều này.

Vì vậy, đây là mã nguồn.

Thế nên tôi chỉ có thể nói, này,

sao chép nguồn mọi thứ

vào thư mục nguồn.

Vậy về cơ bản những gì bạn đang làm,

lấy thư mục nguồn và sao chép

vào thư mục nguồn.

Mát mẻ.

Sau đó, bạn có thể chạy NPM

cài đặt bản dựng chạy NPM.

Sau đó bạn phải xây dựng

dự án này phải không?

Vì vậy nếu bạn thấy điều đó một cách hiệu quả

bạn phải xây dựng dự án này.

Bây giờ xây dựng dự án này sẽ con.

Sẽ tạo một dist

thư mục tự động.

Chính xác.

Chúng ta sẽ tạo một thư mục đĩa.

Bây giờ bạn chỉ có thể nói lệnh

nút hoặc bạn chỉ có thể nói NPM Start.

Vậy một cách hiệu quả những gì chúng ta có

xong, đây là tệp Docker.

Có thể có một số lỗi.

Chúng ta có thể thấy điều đó.

Vì thế chúng ta đang nói, này,

bộ thư mục làm việc.

Sao chép các gói và sao chép TS

config, cài đặt NPM, đang diễn ra

để cài đặt rất nhiều thứ.

Sau đó sao chép thư mục nguồn,

mã nguồn, sau đó xây dựng nó.

Nó sẽ tạo ra một dist

thư mục và sau đó bắt đầu.

Bởi vì NPM Start về cơ bản

bắt đầu từ thư mục dist.

Hãy thử xem.

Vì vậy Docker xây dựng dấu gạch nối T.

Tôi sẽ gọi nó là ứng dụng TS,

Ứng dụng TypeScript và dấu chấm.

Được xây dựng.

Tôi không biết tại sao tôi lại nói là được xây dựng.

Nó nên được xây dựng.

Được rồi, lỗi của tôi.

Đó là một lỗi đánh máy.

Vì vậy, chỉ cần gọi nó là xây dựng.

Vì vậy chúng ta hãy chờ đợi

việc xây dựng sẽ xảy ra.

Phải?

Vậy là NPM chạy, xây dựng và hoàn thành.

Đẹp.

Bây giờ hãy để tôi chạy cái này

ứng dụng dành cho các bạn.

Được rồi, tôi sẽ đi vào thư mục gốc của mình.

Vì vậy Docker chạy tương tác

ở chế độ tách rời.

Chúng ta đừng đặt nó bằng dấu gạch nối tách rời.

Vốn P, P.

Hoặc thậm chí tôi có thể nói, này,

bản đồ 8000 đến 8000.

Và tôi có thể nói ts ứng dụng.

Vì vậy, bây giờ bạn có thể thấy cổng HTTP

đang chạy trên cổng 8000.

Và để xác minh tôi chỉ có thể

truy cập localhost 8000.

Xin chào từ TypeScript

máy chủ đang đến.

Tuyệt vời.

Bây giờ hãy chịu đựng với tôi.

Đây là vùng chứa, ứng dụng TS.

Đi vào thùng chứa này,

đi vào các tập tin.

Và thư mục là gì

mà chúng tôi đã gắn kết?

Chém về nhà.

Ứng dụng chém.

Chém về nhà.

Không phải ở đây, không phải ở đây.

Chém.

Nhà ở đâu?

Vâng, chém ứng dụng chém nhà.

Bạn có thấy nguồn đó không

mã cũng có ở đó à?

Bạn có thể thấy điều đó không?

Tôi có thể nhìn thấy đầy đủ

mã nguồn ở đây.

Vì vậy, mã nguồn cũng có ở đó.

Và dist cũng ở đó.

Bây giờ các bạn, hãy nói với tôi một điều.

Tôi có thực sự cần mã nguồn này không?

Tôi có thực sự cần mã nguồn không?

Một khi việc xây dựng đã được thực hiện?

Khi bạn đã xây dựng xong mã,

sự cần thiết của mã nguồn là gì?

Nó chỉ gây ô nhiễm.

Nó chỉ là tăng kích thước thôi.

Bởi vì hãy tưởng tượng nếu bạn đang ở trong một thực tế

thế giới, nguồn này có thể có dung lượng một gb.

Đó là một dự án rất lớn.

Dự án rất, rất, rất lớn.

Và rất nhiều sự phụ thuộc.

Có rất nhiều gói ở đó.

Điều đó chỉ được yêu cầu

trong môi trường phát triển

khi bạn đang xây dựng nó.

Nhưng một khi nó đã được xây dựng, tại sao tôi lại không thể

chỉ cần sử dụng thiết bị nhẹ này,

bạn biết đấy, đây chỉ là bản biên soạn

tập tin và tạo một docker từ nó.

Nhưng tại thời điểm đặc biệt này,

bạn có thể đang nghĩ,

piyush, điều chúng ta có thể làm là

tại sao chúng ta sao chép mọi thứ?

Bạn có thể thắc mắc, piyush, tại sao

bạn không xây dựng mã cụ thể này sao

trên máy của bạn sau khi hoàn tất?

nhu cầu là gì

sao chép mọi thứ này?

Chỉ cần sao chép đĩa bây giờ.

Chỉ cần sao chép đĩa,

đó là sự thật, tôi có thể làm được điều này.

Nhưng vấn đề là hai vấn đề.

Thứ nhất, tôi vẫn còn bản đánh máy

và mọi thứ khác được cài đặt

trong máy Docker này.

6.

Thứ hai, vì dự án này

được xây dựng trên Mac OS, bởi vì

dự án này được xây dựng trên Mac OS,

có nhiều khả năng là nó có thể

không hoạt động trong Linux hoặc Windows.

Vì vậy điều quan trọng là chúng ta xây dựng

mã đặc biệt này chỉ ở đây

bởi vì nếu bạn đến từ Rust

nền, bạn biết đấy, trên

bạn xây dựng nền tảng nào

mã, nó tương thích với

đó.

Vì vậy đó là một yêu cầu

chúng ta phải xây dựng dự án này

chỉ trong hình ảnh Docker này.

Chúng tôi chỉ phải xây dựng cái này ở Alpine.

Vì vậy, những gì bạn có thể làm, bạn có thể

sử dụng các bản dựng nhiều giai đoạn ở đây.

Được rồi, làm thế nào?

Vì vậy chúng ta sẽ tạo

một hình ảnh cơ sở cho nó.

Tôi chỉ đang loại bỏ mọi thứ,

bạn biết đấy, hãy làm một điều.

Chúng ta hãy gọi nó là

chấm tập tin cũ, được chứ?

Và tôi sẽ tạo thêm một tệp Docker nữa.

Vì vậy đây chính là tài liệu tham khảo dành cho bạn.

Vì vậy trước hết hãy lấy một căn cứ

hình ảnh và hãy gọi nó như một cái gì đó

làm cơ sở như người xây dựng.

Vì vậy, bạn có thể đặt tên nó là bất cứ điều gì.

Tôi muốn gọi nó là cơ sở.

Bạn có thể nói người xây dựng, bạn có thể nói,

bạn biết đấy, abc, bạn

có thể gọi nó là bất cứ điều gì.

Vì vậy tôi sẽ chỉ nói rằng

đây là người xây dựng của tôi

Ồ, xin lỗi.

Tôi sẽ chỉ gọi nó như vậy.

Đây là hình ảnh cơ sở của tôi.

Bây giờ hãy xem tôi có thể làm gì.

Hãy tạo ra một sân khấu.

Giai đoạn này là duy nhất và duy nhất

chịu trách nhiệm xây dựng các công cụ.

Vì vậy, tôi sẽ nói từ cơ sở là người xây dựng.

Bây giờ hãy xem bạn đang làm gì?

Bạn đang tạo ra một sân khấu,

được rồi, bạn đang tạo ra một sân khấu.

Vì vậy, hãy để tôi chỉ bình luận.

Giai đoạn một.

Được rồi, vậy căn cứ này là gì

cơ sở đang đề cập đến ở đây?

Về cơ bản điều này có nghĩa là lấy cái này,

nó giống như một biến mà nút 20

và gọi nó là người xây dựng ở đây.

Những gì tôi định làm, tôi chỉ

muốn làm công việc xây dựng,

chỉ là phần xây dựng.

Vậy làm thế nào để xây dựng.

Vậy điều đó có nghĩa là xây dựng cái gì?

Chúng ta muốn những thứ gì?

Phải?

Vì vậy, nếu tôi vào Docker, tệp cũ.

Vì vậy hãy thiết lập thư mục làm việc

để gạch chéo ứng dụng.

Hãy nói xây dựng.

Bất cứ điều gì có thể ở đó.

Và chúng ta cần gì?

Chúng ta cần sao chép gói JSON.

Được rồi.

Chúng ta cần sao chép TS

cấu hình thì ổn.

Và chúng ta cần cài đặt NPM.

Được rồi, điều đó thật tuyệt.

Và chúng ta cần thực hiện việc sao chép

của nguồn và nguồn

và chúng ta cần thực hiện xây dựng chạy NPM.

Tôi có thể nói rằng đây chỉ là

giai đoạn xây dựng?

Được rồi, tuyệt.

Bây giờ công cụ xây dựng đặc biệt này

sân khấu có rất nhiều thứ.

Nó có toàn bộ mã nguồn, nó có

TypeScript được cài đặt vì chúng tôi

đang đề cập đến TypeScript ở đây.

Bạn biết đấy, nó đã được cài đặt nút,

nó đã được cài đặt nhanh,

điều đó thực sự không cần thiết,

nhưng nó là bắt buộc

khi chúng tôi đang xây dựng tòa nhà,

mọi thứ khi chúng tôi đang xây dựng.

Bây giờ hãy tạo giai đoạn hai.

Được rồi.

Băm giai đoạn hai.

Về cơ bản điều này đang diễn ra

là giai đoạn cuối cùng của tôi.

Được rồi, giai đoạn hai.

Về cơ bản nó là loại người chạy.

Nó được biết đến như một Á hậu.

Vì vậy, những gì chúng tôi sẽ nói, chúng tôi

sẽ nói, này, từ

cơ sở, hình ảnh cơ sở của tôi là gì?

Đây là hình ảnh cơ sở của tôi.

Phần này là Á hậu.

Bây giờ các bạn phải làm gì đây

sân khấu, điều tôi sẽ làm là hãy chuẩn bị

thư mục làm việc đầu tiên.

Thư mục làm việc có thể là/home/app.

Bây giờ điều tôi sẽ làm là

nếu bạn nghĩ, tôi có thể nói

ở giai đoạn số một,

ở giai đoạn một có thư mục dist.

Tôi có thể sao chép nó được không

thư mục kiểm tra từ đây?

Tôi có thể sao chép thư mục kiểm tra đó không?

Được rồi, vậy bạn chỉ cần nói sao chép.

Được rồi.

Dấu gạch nối, dấu gạch nối từ.

Này, đi vào giai đoạn xây dựng.

Thấy chưa, tôi lấy tên này từ đây.

Đi vào giai đoạn xây dựng.

Bạn muốn sao chép cái gì?

Tôi muốn sao chép.

Bạn muốn sao chép cái gì?

Vì vậy, trong trình xây dựng, hãy đi vào dấu gạch chéo

thư mục chính, vào nhà

thư mục, gạch chéo, đi vào bản dựng

thư mục và gạch chéo sao chép disp

thư mục vào thư mục đĩa của tôi.

Ồ.

Những gì bạn đang làm là bạn

không sao chép từ của bạn

mã nguồn, bạn đang sao chép nó

từ giai đoạn xây dựng.

Cũng.

Chúng ta hãy sao chép

các tệp JSON của gói.

Hãy sao chép các tệp JSON của gói.

Xong.

Tôi không muốn cấu hình TS ở đây.

Tôi không muốn sao chép cấu hình TS.

Tôi sẽ không sao chép mã nguồn.

Bây giờ điều tôi có thể làm là một khi điều này được thực hiện

xong, tôi sẽ chỉ cài đặt NPM

nhưng với một lá cờ bị bỏ qua dev.

Điều này về cơ bản có nghĩa là

chỉ và chỉ cài đặt express.

Tôi muốn bỏ qua sự phụ thuộc của nhà phát triển.

Tôi không muốn cài đặt TypeScript.

Tôi không muốn cài đặt cái này.

Tôi không muốn cài đặt cái này.

tôi.

Tôi chỉ muốn cài đặt cái này

chỉ và duy nhất điều này.

Mát mẻ.

Mới cài cái này

và cuối cùng tôi có thể làm

một lệnh đó là NPM Start.

Ồ.

Vì vậy, những gì bạn đã làm là

giai đoạn đặc biệt này sẽ chỉ

xây dựng mã của bạn và sau đó bạn

chỉ cần sao chép những thứ cần thiết này

từ bản dựng và chạy nó.

Vậy hãy để tôi chỉ cho bạn một điều.

Trước hết, các bạn, hãy để tôi

dọn dẹp mọi thứ cho anh, được chứ?

Hãy để tôi xóa tất cả

các thùng chứa cho bạn.

Hãy để tôi xóa tất cả các hình ảnh cho bạn

để dễ hình dung hơn.

Vì vậy, trước tiên hãy xây dựng tập tin cũ này.

Bạn biết đấy, tập tin cũ này.

Vì vậy tôi sẽ chỉ nói docker,

xây dựng ứng dụng TS gạch nối cũ.

Hãy gọi nó là dấu gạch nối cũ f

bởi vì theo mặc định nó cố gắng

để đọc tập tin docker.

Vì vậy, tôi muốn cung cấp docker theo cách thủ công

dấu chấm ngữ cảnh tập tin cũ để bạn có thể

nói dấu gạch nối f nếu bạn muốn

chỉ định đường dẫn tập tin của riêng bạn.

Được rồi, vào đi.

Vì vậy, hãy để nó xây dựng.

Hãy để nó xây dựng.

Vì vậy tôi sẽ chỉ cho nó một thời gian.

Vì vậy hiện tại chúng tôi đang

xây dựng cái cũ.

Vì vậy, bạn có thể thấy rằng đây là

cái cũ hơn, đó là

có kích thước 163 MB.

Bây giờ hãy xây dựng cái mới hơn.

Vì vậy, docker build dấu gạch nối t ts node.

Thế thôi.

Và không cần thiết

làm dấu gạch nối f vì docker

tập tin theo mặc định có màu đỏ.

Được rồi, vậy chúng ta hãy đợi một lát.

Tập tin docker của tôi ở đâu?

Vâng, đây là tập tin docker của tôi.

Vì vậy, bạn có thể thấy nó được xây dựng.

Được rồi, vậy là có nhiều giai đoạn.

Có nhiều giai đoạn.

Và bạn có thể thấy rằng ở đó không

là một sự khác biệt kích thước?

Có một sự khác biệt về kích thước.

Bây giờ tôi sẽ cho bạn thấy điều gì

thực sự đã xảy ra.

Được rồi, để tôi chạy nút TS này.

Đó là cái mới hơn.

Vì vậy, docker chạy, không làm hỏng

Docker chạy gạch nối nó.

Bạn có thể cung cấp bản đồ cổng.

Tôi thực sự không quan tâm đến nó.

Tôi TS ứng dụng.

Vậy bây giờ.

Xin lỗi, xin lỗi, xin lỗi.

Nút TS.

Được rồi, T.

Chỉ một giây thôi.

Nút TS.

Mát mẻ.

Nó đang chạy.

Nó hoàn toàn chạy ổn.

Tới đây, vào tập tin,

vào nhà, vào ứng dụng.

Bạn có thể thấy điều đó ở đó không

không có mã nguồn?

Và có

hoàn toàn không có mã nguồn.

Và trong các mô-đun nút, bạn

sẽ chỉ có, bạn biết đấy, bày tỏ

ứng dụng, không có gì khác.

Không phải bản đánh máy hoặc không có gì.

Vì vậy, bạn có thể thấy bạn có thứ này.

Bạn có thứ này.

Bạn có các mô-đun nút,

bạn có các gói.

Có một bài kiểm tra.

Không có mã nguồn.

Và bài kiểm tra đặc biệt này thực ra là,

bạn gọi là gì, nén?

Được rồi?

Vì vậy, bạn có thể sử dụng

việc xây dựng nhiều giai đoạn này.

Vì vậy, trong các bản dựng nhiều giai đoạn, làm thế nào nó

xảy ra là Docker xây dựng cái đầu tiên

giai đoạn, giai đoạn xây dựng này, nó là

tòa nhà, tòa nhà, tòa nhà.

Một khi nó được xây dựng xong, được chứ?

Sau đó, nó sẽ bắt đầu cả hai.

Một khi nó bắt đầu, nó sẽ

chỉ cần sao chép các tập tin cần thiết

và Xóa giai đoạn đầu tiên,

sao chép các tập tin cần thiết.

Nó biết rằng, được thôi, bạn là vậy

chỉ quan tâm đến việc sao chép

dist và quan tâm đến việc sao chép

gói JSON, phần còn lại.

Tất cả mọi thứ sẽ bị xóa.

Cho dù bạn có hàng trăm

và hàng ngàn thứ được cài đặt

ở đây mọi thứ đều bị xóa.

Bạn chỉ còn lại

với hai điều này.

Vì vậy, về cơ bản đây là Docker của bạn.

Tôi sẽ cho bạn một điều thực tế hơn

ví dụ về cách bạn có thể sử dụng cái này

xây dựng nhiều giai đoạn trong trường hợp

Rust, anh có thể làm gì thì được, vậy nếu

bạn đang ở trong đó, nếu bạn là Rust

nhà phát triển, bạn có thể làm gì, bạn

có thể có một sân khấu, được thôi, ở đâu bạn

có thể cài đầy đủ Rust trong này

giai đoạn này, giống như cài đặt Rust đầy đủ

ngôn ngữ lập trình ở đây, sao chép

toàn bộ mã nguồn.

Được rồi, đây giống như giai đoạn một.

Sao chép mã nguồn, mã nguồn.

Sau đó xây dựng mã nguồn này.

Xây dựng mã nguồn.

Đây là giai đoạn một của bạn.

Giả sử giai đoạn này rất nặng nề.

Đây là một gb bởi vì bạn

đã cài đầy đủ Rust, đầy đủ

mã nguồn và mọi thứ.

Sau khi xây dựng, tôi có thể nói điều đó không?

Rust sẽ chỉ cho bạn một cái

tập tin thực thi nhị phân.

Tệp thực thi nhị phân.

Tạo thêm một giai đoạn nữa.

Không cài đặt Rust ở đây.

Đừng cài đặt.

Không cần thiết.

Chỉ cần sao chép tệp thực thi nhị phân này

đây và thực hiện nó.

Chỉ cần bắt đầu nhị phân này, thế là xong.

Và chỉ cần chia sẻ điều này

với thế giới.

Bây giờ hãy xem vùng chứa Docker của bạn,

hình ảnh Docker của bạn làm được

không có mã nguồn.

Điểm cộng an toàn, rất nhẹ.

Nó thậm chí còn không có Rust

môi trường vì đó là

chỉ được yêu cầu khi chúng tôi đang mã hóa

chỉ dành cho tòa nhà.

Chúng tôi đã cài đặt Rust, chúng tôi

đã sao chép và chúng tôi đã xây dựng nó.

Sau khi nó được xây dựng, chúng tôi

không cần Rust nữa.

Vì vậy, trong điều đặc biệt này mà bạn

đang xuất bản ra thế giới bởi vì

giai đoạn cuối cùng được coi là.

Là, là một trong những được xem xét.

Được rồi, hãy nhớ điều này,

dù cuối cùng là gì

giai đoạn, đó là những gì nó đang diễn ra

để chia sẻ với mọi người.

Vì vậy ở giai đoạn cuối cùng bạn chỉ cần

có một tập tin thực thi

và bạn chỉ mới bắt đầu nó.

Rất nhẹ.

Đây là bản dựng nhiều giai đoạn,

nên bạn thậm chí có thể tìm kiếm nó,

xây dựng Docker nhiều giai đoạn để bạn

có thể đọc về nó rằng nó là

về cơ bản để tối ưu hóa Docker

các tập tin trong khi vẫn dễ dàng

đọc và duy trì.

Được rồi, vậy bạn có thể sử dụng

xây dựng nhiều giai đoạn.

Đúng vậy, họ đang có

một ví dụ về cờ vây, vì vậy bạn có thể

xem họ đang làm gì đầu tiên.

Ở giai đoạn đầu tiên họ đang sử dụng

golang, đúng như hình ảnh cơ sở.

Họ thực sự cần Go đầy đủ,

thiết lập môi trường.

Vậy là Go đã được cài đặt,

cái đó rất nặng.

Vậy là bạn đã có nguồn

thư mục làm việc.

Họ đang sao chép một số thứ.

Họ đang làm điều này.

Họ đang xây dựng nó

một khi nó được xây dựng ở đó.

Được rồi, vậy họ đặt tên nó là gì?

Vì vậy, về cơ bản đây là giai đoạn 0.

Sau đó lại từ đầu,

theo nghĩa đen là không có hệ điều hành.

Họ đang ở một giai đoạn khác

sao chép từ số không.

Chỉ cần sao chép tệp thực thi, Thấy không?

Chỉ cần sao chép tệp thực thi

đây và chạy nó.

Ở giai đoạn cuối cùng này có

hoàn toàn không cài đặt Golang.

Rất nhẹ.

Không có mã nguồn, không có gì cả.

Chỉ là tệp thực thi nhị phân.

Vì vậy, điều này được gọi là nhiều giai đoạn.

Docker xây dựng.