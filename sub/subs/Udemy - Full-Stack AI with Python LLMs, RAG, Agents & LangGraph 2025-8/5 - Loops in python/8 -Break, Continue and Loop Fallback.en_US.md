# 8 -Break, Continue và Loop Fallback.en US

---

Được rồi, vậy hãy chuyển sang

có lẽ là video cuối cùng về điều này

phần chúng ta sẽ học

về hai chủ đề quan trọng đó

một cái là bỏ qua, một cái khác là

phá vỡ.

Vì vậy trước hết chúng ta sẽ nghiên cứu

tuyên bố vấn đề và sau đó chúng tôi

sẽ viết mã cho nó.

Và sau đó tôi sẽ cho bạn xem một

về vụ án thú vị

của vòng lặp là tốt.

Nó không phải là một phần của chủ đề

như vậy, nhưng nó đẹp

trường hợp sử dụng thú vị là tốt.

Vì vậy hãy chú ý ở đây nó nói một số

hương vị chai đã hết hàng.

Bạn muốn bỏ qua những điều đó và dừng lại

hoàn toàn nếu ai đó

yêu cầu một hương vị hạn chế.

Vì vậy, nhiệm vụ được bỏ qua nếu hương vị

hết hàng và phá vỡ nếu

hương vị bị ngưng.

Bây giờ chúng ta hãy tiếp tục

và nghiên cứu về chúng.

Trước hết hãy nói rằng

đây là vòng lặp của bạn đang diễn ra.

Vì vậy, đây là vòng lặp của bạn.

Và trong vòng lặp của bạn, bạn liên tục

tiếp tục và cố gắng

để có được các giá trị như thế này.

Đây là cách vòng lặp hoạt động.

Hãy thường xuyên tiếp tục đi sâu vào nó.

Bây giờ điều này bỏ qua và những điều này

có nghĩa là chúng ta hãy nói

bạn sẽ tiếp tục và lặp lại

qua đó có lẽ là năm hoặc sáu

những thời điểm khác nhau như vậy.

Vì vậy chúng ta sẽ thay đổi điều này ở đây

một chút ở đây vậy

rằng nó thực sự có vẻ tốt.

Vậy hãy giả sử đây là năm

những thời điểm khác nhau mà bạn đang lặp lại.

Điều đầu tiên bạn sẽ làm

để nghiên cứu được gọi là tiếp tục.

Đây là một từ khóa bây giờ tiếp tục.

Toàn bộ công việc tiếp tục là

để đảm bảo rằng

bất kể thời gian bạn lặp lại,

Tôi sẽ bỏ qua một trong số chúng.

Vì vậy hãy chỉ nói rằng đây là một trong

họ và có lẽ chúng ta nên

có thêm một cái nữa để làm

chắc chắn rằng chúng tôi đang thực sự đi

thông qua điều này một cách tốt đẹp và chúng tôi

thực sự có thể hiểu được điều này

một phần.

Vì vậy chúng tôi sẽ đưa ra một số

về điều kiện kiểm tra và hãy

chỉ cần nói trong số ba điều này, điều này

là điều kiện phù hợp.

Vì vậy ngay khi chúng tôi viết

tuyên bố tiếp tục, toàn bộ điều này

mọi thứ sẽ biến mất.

Như chúng ta có thể thấy, điều này

sẽ bị xóa.

Vì vậy phần này của vòng lặp

sẽ bị bỏ qua.

Mặt khác, sự nghỉ ngơi

cũng là một từ khóa khác

giống như tiếp tục.

Nhưng vì phần tiếp tục bị hỏng,

hoặc loại cho phép bạn bỏ qua một

của vòng lặp trong khi break cho phép

bạn chỉ cần dừng hoàn toàn vòng lặp

bất cứ nơi nào nó đã gặp phải điều này.

Thực ra nó dễ dàng hơn nhiều

để xem trong phần mã

và nhận ra điều gì đang xảy ra.

Tôi hy vọng bạn có được một số GIST

ít nhất là 20, 30%.

Nhưng nghỉ ngơi bạn sẽ dễ dàng hiểu được

khi chúng ta đi qua cái này.

Vì vậy chúng tôi gọi cái này là

chỉ đơn giản là 07 gạch dưới.

Không phải như vậy, không theo thứ tự.

Py.

Và hãy cứ nói rằng chúng ta có một số

về những mệnh lệnh này trước mặt chúng ta.

Cứ cho là chúng ta gọi chúng là hương vị.

Vậy là có ai đó đang yêu cầu chúng tôi

hương vị của chai, và chúng tôi

sẽ phù hợp với họ theo đúng nghĩa đen.

Đầu tiên là gừng.

Bản thân hương vị thứ hai,

chúng tôi gọi đây là hết hàng.

Hãy đi và nói hết hàng.

Cứ như thế này.

Một cái khác là chanh.

Và cứ như thế này, một điều khác

một cái bị ngưng.

Đã ngừng sản xuất.

Và.

Và hãy nói rằng có

một cái khác là Tulsi.

Đây cũng là một hương vị thú vị.

Vì vậy đây là tất cả những hương vị mà

chúng tôi có và ngay bây giờ chúng tôi muốn

để lặp qua tất cả chúng.

Cách lặp đơn giản như vậy

thông qua đó là.

Hãy gọi cái này là

hương vị ra khỏi hương vị.

Thế đấy.

Vì vậy, hương vị đầu tiên là một biến.

Hương vị thứ hai là một danh sách.

Vì vậy chúng ta cần phải đưa ra một tấm séc.

Kiểm tra luôn xuất hiện

với điều kiện if.

Và vâng, điều này một lần nữa đứng lên.

Vì vậy chúng ta sẽ chỉ nói nếu hương vị

mà chúng tôi có đã ngừng hoạt động,

vì vậy chúng tôi sẽ chỉ khớp nó một cách chính xác.

Trước hết chúng ta sẽ chỉ kiểm tra

vì hết hàng, sau đó chúng tôi sẽ

kiểm tra việc ngừng hoạt động.

Vì vậy nếu hương vị hết hàng,

sau đó chúng ta có thể đơn giản tiếp tục

và bỏ qua vòng lặp cụ thể đó.

Vì vậy tất cả những gì bạn phải làm là

trong trường hợp này, chúng tôi sử dụng

từ khóa tiếp tục.

Vì vậy chúng ta sẽ tiếp tục

và nói tiếp tục.

Bây giờ, đây là một phần nhỏ

sai lầm mà chúng tôi đã làm.

Chúng tôi quên dấu chấm phẩy.

Khoảnh khắc bạn đặt dấu chấm phẩy,

sự tiếp tục đang diễn ra

mang đến cho bạn một vấn đề bởi vì chúng tôi

có vấn đề thụt lề.

Vì vậy hãy chắc chắn rằng bạn đi lên đây

và nhấn vào bốn dấu cách hoặc tab,

bất cứ điều gì bạn muốn ước.

Nghĩa đen trong tệp Python

tự động mã VS sẽ cung cấp

bạn bốn không gian, giống như

cũng được đề cập trong pep.

Bây giờ chúng tôi cũng muốn kiểm tra

cho một điều kiện khác.

Vậy chúng ta có thể lên đây

và kiểm tra một cái khác.

Nếu hương vị bằng.

Hãy tiếp tục và sao chép cái này

rằng chúng tôi không mắc bất kỳ lỗi đánh máy nào.

Và cứ như thế này.

Vì vậy trong trường hợp này, chúng tôi sử dụng

một từ khóa được gọi là break.

Bây giờ, sau đó, chúng ta tiếp tục

và in ấn, bất cứ điều gì

tuyên bố chúng tôi muốn in.

Vì vậy chúng ta sẽ tiếp tục và nói

cái đó, này, tôi, rất muốn in

và sử dụng phương pháp in.

Và chúng ta sẽ chỉ nói điều này

tiếp theo mục Nền tảng.

Bây giờ đây là một điều rất, rất

thú vị, một phần của nó.

Chúng ta có thể tiếp tục và phá vỡ nó

và chúng ta sẽ xem điều gì xảy ra trong chuyện này.

Và chú ý ở đây vết lõm.

Đây là tuyên bố nếu của tôi.

Điều này nằm ngoài câu lệnh if,

nhưng vẫn ở trong vòng lặp.

Và chúng ta có thể có một cái khác như vậy

tuyên bố, nhưng chúng ta thực sự có thể

hãy tiếp tục và di chuyển nó ra bên ngoài

của câu lệnh for là tốt.

Và chúng ta chỉ cần in và xem

chuyện gì xảy ra trong chuyện này.

Vì vậy tôi sẽ tiếp tục và loại bỏ cái này

và tôi sẽ chỉ nói F và chúng ta sẽ chỉ

hãy tiếp tục và nói bên ngoài, vòng lặp.

Vì vậy, điều này chỉ để đảm bảo rằng

bạn hiểu chuyện gì đang xảy ra

và chúng tôi chắc chắn sẽ thêm một chút

thêm một chút nữa là nó diễn ra như thế nào

và cách nó hoạt động và mọi thứ.

Chúng ta hãy tiếp tục và chạy cái này.

Bạn sẽ học được khá nhiều điều,

mặc dù trông có vẻ hơi chút

khó hiểu, nhưng hãy chịu đựng tôi.

Bạn sẽ học được rất nhiều

trong chính video này.

Vậy chúng ta hãy đi thôi

về phía trước và chạy và 07.

Thế đấy.

Chú ý ở đây nó nói

mặt hàng đã ngừng sản xuất được tìm thấy

Sau đó, một lần nữa, mặt hàng đã ngừng sản xuất được tìm thấy.

Và sau đó chúng tôi chỉ đơn giản là

bên ngoài vòng lặp.

Điều này thú vị đó.

Tại sao điều này xảy ra?

Tại sao vậy?

Chúng tôi đã nhận được, cái này là

in hai lần.

Vì vậy, lần đầu tiên nó thực sự lặp lại

xuyên qua, nó tìm thấy gừng và sau đó

nó đã hết hàng.

Vậy là gừng hết hàng rồi, một

đã đi, suốt chặng đường đó.

Chúng tôi không thực hiện bất kỳ việc in ấn nào

của gừng hoặc bất cứ thứ gì, nhưng.

Nhưng như bạn sẽ nhận thấy, đây là

in vào thời điểm gừng.

Sau đó khi chúng ta đơn giản di chuyển ra ngoài

còn hàng, nó chỉ đơn giản nói, này,

Tôi không muốn làm gì cả.

Vì vậy, hết hàng chỉ đơn giản là xuất hiện ở đây.

Và ngay khi nó nhìn thấy sự tiếp tục,

nó không hoạt động ở đó.

Sẽ khá thú vị nếu

chúng tôi tiếp tục và in ra.

Hãy tiếp tục và in

điều này, tuyên bố

bởi vì điều này thật thú vị

Thay vì nói đã ngừng

hết hạn, tìm, tiếp tục và loại bỏ

cái này, thêm cái này và nói

chúng tôi muốn in hương vị.

Chúng ta có thể in hương vị?

Nhiều thứ thú vị hơn.

Được rồi, đi thôi

phía trước và in cái này.

Vì vậy, nó nói lần đầu tiên

món gừng đã được tìm thấy.

Được rồi, không có vấn đề gì cả.

Mặt hàng gừng đã được tìm thấy.

Sau đó nó báo là hết hàng.

Vì vậy ngay khi nó phát hiện ra

trong kho, nó nói tiếp tục.

Điều đó có nghĩa là tôi sẽ không

tiếp tục vòng lặp.

Tôi sẽ bỏ qua ngay từ đây.

Vì vậy, không có gì được in.

Sau đó nó nói chanh.

Vì vậy chanh đã được in ở đây.

Và sau đó, nó đã không

phù hợp với điều kiện này.

Nó không phù hợp với điều kiện này.

Thế là nó được in ra.

Sau đó chúng tôi chỉ đơn giản là tương tác

với sự ngừng hoạt động.

Vì vậy ngay khi bạn tương tác

với sự ngừng hoạt động,

câu lệnh break được nhấn.

Điều đó có nghĩa là toàn bộ vòng lặp là

sẽ không chạy ra ngoài này.

Vì vậy, bạn chỉ có cho đến quả chanh.

Sau đó không có gì in.

Anh chàng này không bao giờ có cơ hội

được in.

Và ngay khi chúng tôi thoát khỏi chuyện này, chúng tôi

cứ tiếp tục và nói rằng, này,

Tôi đang in bên ngoài vòng lặp.

Sự hiểu biết về thụt đầu dòng này

là khá quan trọng và chúng tôi

thực sự, thực sự cần điều đó.

Bây giờ ngoài điều này, bạn có thể có

đã làm điều gì đó như thế này, thế kia

này, trước khi phá vỡ điều này, chúng tôi muốn

để in cái này và rõ ràng là chúng tôi

cần phải làm việc thụt lề.

Thế là chúng ta bắt đầu.

Bây giờ đầu ra sẽ là

khác biệt đáng kể.

Vì vậy nếu tôi tiếp tục và chạy thông báo này

ở đây, Đã tìm thấy mặt hàng bị ngừng sản xuất.

Và chúng tôi chỉ đơn giản nói

bên ngoài vòng lặp.

Bởi vì lần này chúng tôi không

có bất cứ thứ gì để in ra

chỉ trong vòng lặp.

Chúng tôi chỉ đang kiểm tra

cho hai điều kiện.

Cái đầu tiên hết hàng,

cái thứ hai cho việc ngừng sản xuất.

Vì vậy, mục duy nhất được in

bị ngừng sản xuất chỉ vì

sau đó bạn di chuyển vào bên trong vòng lặp này.

Đó là lý do tại sao chúng ta thấy

đã ngừng sản xuất được tìm thấy.

Và sau đó chúng ta chỉ cần có món đồ đó,

bên ngoài điều này được tìm thấy.

Chúng ta có thể làm một điều nữa, một

điều thú vị hơn nữa.

Tôi chỉ có thể tiếp tục và có

một bản sao của cái này

Tôi sẽ in cái này ra và thông báo

đây tôi đang in nó ở bên ngoài.

Vì vậy, đây là khối if.

Đây lại là khối if.

Nhưng đây là một khối vòng lặp.

Lưu ý ở đây nó nằm trong vòng lặp.

Vì vậy khả năng hiểu

chuyện gì đang xảy ra và nó thế nào

thực tế đang xảy ra là rất,

rất thú vị và quan trọng

trong thế giới Python.

Tôi sẽ in thông báo này ở đây.

Gừng, vật phẩm được tìm thấy.

Lemon, mặt hàng được tìm thấy Ngừng sản xuất

Block cũng bị xử tử bên ngoài.

Sau đó không có gì được thực hiện.

Vì vậy, cái này được ra ngoài.

Vì vậy đây là phần quan trọng nhất

mà bạn học và hiểu sâu sắc

về việc tiếp tục nghỉ giải lao và làm thế nào

cấu trúc của vòng lặp hoạt động.

Bây giờ tôi có một ví dụ khác như vậy

và điều đó sẽ rất thú vị.

Tôi nghĩ để giữ nó như là một riêng biệt

video, nhưng tôi sẽ chỉ

giới thiệu bạn trong video này.

Vậy đây là 08 và chúng ta sẽ đi

gọi cái này như cái khác.

Vâng, có một điều như vậy

như được gọi là khác.

Bây giờ hãy nhìn vào điều này rất thú vị

ví dụ mà chúng tôi có.

Vì vậy tôi sẽ tiếp tục

và gọi người này là nhân viên.

Vì vậy chúng tôi có một số nhân viên

thành viên đó là một danh sách.

Bên trong danh sách chúng ta có các bộ dữ liệu.

Trước hết chúng ta có Amit

và chúng tôi cũng lưu trữ tuổi của họ.

Vậy hãy nói là 16.

Và chúng tôi có một nhân viên khác

đó cũng là một Tuple.

Vậy nên tôi sẽ tiếp tục và nói Zara

và nhân viên có lẽ ở độ tuổi 17.

Và sau đó chúng ta có một bộ dữ liệu khác

và hãy nói rằng chúng ta gọi

đây là Raj, tên hư cấu.

Không, không có vấn đề gì ở đó.

Và chúng tôi chỉ đơn giản là đi

về phía trước và làm việc vào ngày 15.

Bây giờ chúng ta có bộ dữ liệu, chúng ta

có tên cũng như tuổi.

Chúng ta có thể lặp qua chúng không?

Chắc chắn rồi.

Chúng ta chỉ có thể tiếp tục và nói

tên tuổi, bởi vì đó là những gì

chúng tôi sắp quay trở lại.

Và chúng ta sẽ chỉ đơn giản nói

điều này trong đội ngũ nhân viên.

Bây giờ tôi không muốn sử dụng nó như thế.

Tôi chỉ muốn in khi

độ tuổi trên 18.

Này Hitesh, bạn đang nói gì vậy?

Không ai trên 18 tuổi.

Đó chính xác là quan điểm của tôi.

Vì thế tôi có thể tiếp tục

và viết nó như thế này.

Nếu tuổi lớn hơn hoặc bằng

đến 18 tuổi thì chỉ còn chúng ta

thực hiện việc tuyển dụng hoặc chúng tôi

in một số tin nhắn.

Trong trường hợp này chúng ta chỉ đơn giản là tiếp tục

và chỉ cần sử dụng bản in giống như

chuỗi này và được định dạng và chúng tôi

sẽ nói tên có đủ điều kiện cho.

Có khả năng quản lý nhân viên.

Quản lý nhân viên hoặc tuyển dụng,

bất cứ điều gì bạn muốn gọi điều này.

Được rồi, bây giờ khi mọi chuyện đã xong

xong, chúng tôi chỉ muốn tiếp tục

và cũng đạt được break.

Bây giờ đây là phần thú vị nhất.

Chúng tôi sẽ tiếp tục và chỉ cần nói khác.

Điều đó thật thú vị.

Có, chỉ ở mức thụt lề

vòng lặp for ở đâu.

Và tôi có thể tiếp tục và in

giá trị như thế này

và có thể có một định dạng

chuỗi theo cách bạn thích.

Không ai đủ điều kiện

để quản lý đồ đạc.

Đây là một trong những điều thú vị nhất

trường hợp và phong cách thú vị

viết mã Python.

Tôi sẽ chạy cái này và chúng ta sẽ gọi

this1as08 và chạy thông báo này tại đây.

Nó nói không ai đủ điều kiện

để quản lý nhân viên.

Nhưng chúng ta hãy tiến về phía trước và đảo ngược

quy tắc chúng tôi đang tìm kiếm

ít hơn tám nên

ít hơn hoặc một lần nữa sử dụng cái này.

Vì vậy tuổi phải nhỏ hơn

hoặc bằng 18.

Vì vậy, tất cả chúng bây giờ là một phần của nó.

Bây giờ đây là phần thú vị.

Những gì sẽ được in?

Đó là nhất

phần thú vị của nó.

Lưu ý ở đây Amit đủ điều kiện, vì vậy

người đầu tiên đủ điều kiện.

Và sau đó chúng tôi

chỉ cần phá vỡ điều này.

Vì vậy chúng tôi không chạy

vòng lặp nữa.

Bất cứ ai là người đầu tiên đến

lên và đáp ứng các tiêu chí,

chúng tôi chỉ đơn giản nói rằng

bạn có đủ điều kiện cho nó

Nhưng hãy chú ý ở đây cái khác

tuyên bố không in.

Và đây là một trong những điều kỳ lạ nhất

hành vi đó ở nơi khác

câu lệnh được sử dụng hoặc có thể

được sử dụng, vết lõm không

trong câu lệnh if.

Đây không phải là một phần của câu lệnh if.

Đây là một phần của câu lệnh For.

Vì vậy đây là một trong những

cách thú vị chỉ chặn khối khác

chạy nếu vòng lặp không bị hỏng.

Sử dụng nó khi bạn đang tìm kiếm

đối với một cái gì đó, nó không được tìm thấy.

Đó là một kiểu hành quyết

của logic dự phòng.

Vì vậy hãy gọi cái này là

một dự phòng ở đây.

Khá thú vị.

Bạn sẽ thấy điều này khá nhiều,

nhưng chỉ trong loạt bài chuyên sâu,

giống như chúng ta đang làm ở đây.

Đó là nó cho video này.

Hy vọng bạn thích cái này.

Đó là một video khá thú vị

hoàn toàn và hy vọng bạn có

đã học được điều đó và chỉ thế thôi

về các vòng lặp trong Python.

Đó là nó cho video này.

Và chúng ta hãy bắt kịp phần tiếp theo.