# 3 - Mã hóa AI Agent.en US đầu tiên của bạn

---

Được rồi, vậy trong này

video cụ thể hãy viết mã

đặc vụ đầu tiên của chúng tôi.

Vì vậy trước tiên hãy thiết lập trực giác

đó là những gì chúng ta sẽ làm

và sau đó chúng ta có thể nhảy vào nó.

Được rồi, ngay bây giờ điều tôi muốn

để xây dựng là điều tôi muốn

để xây dựng một tác nhân thời tiết.

Được rồi thế này là tốt nhất

thứ mà bạn có thể xây dựng

để hiểu các đại lý.

Vì vậy điều tôi muốn làm là

người dùng có thể hỏi điều đó, hãy nói cho tôi biết

thời tiết của hãy nói goa.

Được rồi.

Và rồi bằng cách nào đó LLM của bạn có

để tìm hiểu xem người dùng đang cố gắng làm gì

để hỏi và nó nên

thực hiện lệnh gọi API nội bộ.

Được rồi.

Để dự báo thời tiết API.

Được rồi chúng ta sẽ sử dụng một số open

API thời tiết nguồn và sau đó

LLM phải trả lời.

Vì vậy, đây là điều.

Được rồi tôi sẽ chỉ cho bạn một bước

từng bước một là thế nào

để xây dựng những thứ như thế này.

Bạn sẽ cảm thấy thế nào

những lỗi và mọi thứ?

Được rồi, hãy ở bên tôi nhé

trong video đặc biệt này.

Đây sẽ là điều tốt nhất

video và bạn sẽ nhận được

một ý chính về cách các đại lý làm việc.

Vì vậy, hãy quay lại trình soạn thảo mã của chúng tôi.

Hãy để tôi làm một điều.

Hãy chỉ nói rằng điều này

là tác nhân thời tiết của chúng tôi.

Được rồi, nhân viên thời tiết

và hãy tạo một tệp PY chính.

Được rồi hãy nhanh chóng bắt đầu

bằng cách mã hóa một số điều cơ bản.

Được rồi tôi sẽ làm

từ bạn biết AI mở.

Vì vậy, từ AI mở nhập OpenAI.

Vậy thì thật tuyệt.

Chúng tôi đã nhập AI mở.

Hãy để tôi phóng to một chút cho

bạn để bạn có thể nhìn thấy nó tốt hơn.

Được rồi chúng ta sẽ chỉ nói

khách hàng tương đương với OpenAI và làm ơn

hãy đảm bảo rằng bạn có

các biến môi trường và tất cả các thiết lập.

Được rồi, từ nhập ENV dot

chúa tể tải chấm ENV và chúng ta sẽ đi

để tải tệp ENV chấm ở đây.

Điều đó thật tuyệt.

Hãy tạo một cái chính

hoạt động và đây là những gì chúng ta sẽ làm

việc cần làm là chúng ta sẽ đi

để lấy đầu vào từ người dùng.

Vì thế tôi sẽ chỉ nói

đầu vào bằng không đầu vào.

Tôi sẽ chỉ nói người dùng gạch dưới

truy vấn bằng đầu vào.

Được rồi và tôi sẽ đi

để nói rằng bạn có thể hỏi

một câu hỏi, bất cứ điều gì ở đây.

Được rồi, tốt đẹp.

Sau đó, khi người dùng cung cấp cho tôi thông tin đầu vào

Tôi chỉ có thể nói khách hàng.

Được rồi, đây là AI mở

client.uh hoàn thành.

Được rồi.chat.completions.

tạo và sau đó ở đây chúng tôi

có thể vượt qua mô hình

Vậy hãy cho nó một mô hình

đó là dấu gạch nối GPT 4.

Ồ vậy hãy đi với mô hình 4O

và sau đó chúng tôi sẽ đưa ra

các tin nhắn ngay bây giờ có

không có dấu nhắc hệ thống, không có gì.

Được rồi, đúng vậy, nó chỉ là ngẫu nhiên thôi.

Đó chỉ là một cuộc gọi AI LLM tự trị.

Vì vậy, vai trò là người dùng và sau đó

chúng tôi chỉ có thể cung cấp nội dung

là truy vấn của người dùng.

Đó là tất cả.

Được rồi, bây giờ nội dung cụ thể này là

sẽ cho tôi một số phản hồi.

Được rồi tôi sẽ tạo một biến

phản hồi và cuối cùng chúng ta có thể

chỉ cần lấy, chúng ta chỉ có thể nói in

và hãy có biểu tượng cảm xúc của bot.

Vì vậy tôi chỉ có thể nói rằng bot có

về cơ bản đã trả lời bằng một cái gì đó.

Được rồi tôi sẽ chỉ sử dụng F.

Được rồi và tôi chỉ có thể nói

phản hồi.lựa chọn

tin nhắn Choice@zero.uh.

Nội dung.

Được rồi, về cơ bản đây là nơi tôi đang ở

sẽ nhận được phản hồi trở lại.

Và chúng ta hãy gọi chính

hoạt động ngay tại đây.

Điều đó thật tuyệt.

Vì vậy, hãy xem, lấy đầu vào từ người dùng,

thực hiện cuộc gọi LLM tới GPT.

Được rồi.

Và sau đó bạn có thể chỉ

in phản hồi.

Điều đó thật tuyệt.

Bây giờ hãy để tôi làm một điều.

Tôi chỉ muốn khóa API OpenAI của mình.

Vì vậy, tôi sẽ chỉ sao chép nó từ đây.

Và trong thư mục cụ thể này nữa

Tôi sẽ tạo một môi trường

tập tin và dán này.

Vì vậy, nếu chìa khóa của tôi đang hoạt động, hầu hết

có lẽ chìa khóa của tôi đang hoạt động.

Hãy xem liệu mọi thứ

đang hoạt động tốt.

Được rồi, bạn có thể thấy nó đang hỏi tôi.

Tôi sẽ chỉ hỏi cái gì

thời tiết như ở GOA và nhập

Hãy xem điều gì sẽ xảy ra.

Được rồi, bạn có thể thấy nó đang hoạt động

một số xử lý ngay tại đây.

Và tôi thực sự muốn thể hiện

bạn sẽ nhận được phản hồi trở lại.

Được rồi, được rồi.

Vậy bạn có thể thấy nó

một phản ứng rất lớn.

Vì vậy GOA thường trải nghiệm

khí hậu nhiệt đới gió mùa.

Đây là một ý tưởng chung.

Đây là cái này.

Vì vậy, bạn có thể thấy nó thực sự không phải

có thể cho tôi biết thời tiết hiện tại.

Được rồi, nó không thể cho

cho tôi biết thời tiết hiện tại.

Đó chỉ là thông tin ngẫu nhiên.

Hãy để tôi làm một cái

điều một lần nữa cho bạn.

Nếu tôi chạy lại mã này.

Được rồi.

Nhiệt độ hiện tại là bao nhiêu

bằng độ C ở GOA lúc này?

Được rồi, tôi chỉ hỏi một chút thôi

thông tin thời gian thực ngay bây giờ.

Đi vào.

Hãy xem điều gì sẽ xảy ra.

Được rồi bây giờ nếu chúng ta đợi một lúc,

Tôi xin lỗi nhưng tôi không thể cung cấp

dữ liệu thời gian thực hoặc hiện tại

điều kiện thời tiết để tìm

nhiệt độ hiện tại của goa.

Tôi khuyên bạn nên kiểm tra thời tiết

trang web hoặc ứng dụng để biết thêm

thông tin cập nhật.

Vì vậy, về cơ bản bạn có thể thấy những gì

đã xảy ra là LLM của chúng tôi không thể

để giải quyết truy vấn cụ thể này.

Điều này có ý nghĩa phải không?

Bởi vì LLM hoạt động trước

dữ liệu đào tạo và nó có thể.

Nó không có quyền truy cập vào thực tế

dữ liệu thời gian, dữ liệu trước khi đào tạo.

Không bao giờ có thể có hiện tại

thời tiết ở goa

Đó là vấn đề.

Vì vậy, để có được thời tiết hiện tại, chúng tôi

cần một loại API nào đó, phải không?

Chúng tôi cần một số loại

của lệnh gọi API bên ngoài.

Vì vậy, điều chúng ta có thể làm là chúng ta có thể

sử dụng một số loại lệnh gọi API bên ngoài.

Vì vậy, đây là một

URL, đây là một dịch vụ

cung cấp cho bạn điều đó.

Vì vậy điều tôi có thể làm là

nếu tôi dán nó ở đây.

Được rồi.

Và hãy để tôi loại bỏ tất cả những điều này trở lại

văn bản đã đi kèm

và đối với thành phố, hãy đặt GOA ở đây.

Được rồi.

Vì vậy tôi sẽ chỉ nói GOA và tham gia.

Vậy bạn có thể thấy đây là

về cơ bản nó hoạt động như thế nào.

Vì vậy, bạn có thể thấy chúng tôi đang nhận được

một phản hồi lại.

Vậy điều đó có nghĩa đây là URL

và bạn phải thay thế thành phố.

Vì vậy, hãy để tôi tạo một hàm,

một chức năng nhanh chóng ở đây.

Vì vậy, chắc chắn.

Được rồi, tôi sẽ chỉ nói lấy

nhấn mạnh thời tiết.

Được rồi.

Và bạn phải đưa cho tôi

tên thành phố dưới dạng một chuỗi.

Điều tôi sắp làm là tôi chỉ

sẽ thực hiện cuộc gọi API.

Được rồi.

Vì vậy, hãy nhập các yêu cầu.

Được rồi, nhập yêu cầu.

Được rồi, điều đó thật tuyệt.

Bây giờ tôi chỉ có thể nói này, điều tôi muốn

việc cần làm là tôi sẽ xây dựng

một URL là URL cụ thể này.

Vì vậy, hãy để tôi sao chép nó ở đây.

Đây là URL của tôi.

Vì vậy, bạn có thể thấy URL.

Và sau đó chúng tôi sẽ trao cho thành phố

đặt tên ở đây và chúng ta có thể

thậm chí làm thành phố chấm hai thấp hơn.

Được rồi.

Thành phố chấm thấp hơn nên chỉ

trong trường hợp thấp hơn.

Và sau đó chúng ta chỉ có thể nói

này, phản hồi tương đương với yêu cầu

chấm lấy URL.

Vì vậy, chúng tôi đang thực hiện một yêu cầu nhận

trên URL cụ thể này.

Nếu phản hồi.uhresponse.status

mã thực sự là 200.

Nếu là 200 thì chúng tôi sẽ đi

để nói trả lại một chuỗi nói

thời tiết khô héo ở đâu

thành phố bạn yêu cầu tôi là

bất kể văn bản dấu chấm phản hồi là gì.

Được rồi.

Và nếu có chuyện gì đó xảy ra

sai rồi chúng ta chỉ có thể nói quay lại

có điều gì đó không ổn.

Đó là nó.

Bây giờ đây là một điều rất, rất rất

chức năng đơn giản mà tôi

hiện đã được xây dựng ở đây.

Được rồi.

Để cho bạn thấy điều này hãy để

tôi chỉ cần biết thời tiết thôi.

Được rồi.

Tôi sẽ chỉ nói xin chào in.

Và tôi sẽ gọi get

thời tiết cho hãy nói goa.

Hãy xem điều gì sẽ xảy ra.

Được rồi.

Nếu chúng ta gọi cái này, nếu chúng ta gọi cái này

hoạt động theo cách thủ công và tôi chạy cái này

mã cụ thể để bạn có thể thấy tôi

sẽ lấy thông tin thời tiết ở Goa.

Là mưa loang lổ ở gần điều này.

Chúng ta cũng hãy gọi tới Delhi.

Được rồi, hãy cùng xem hai người nhé

đến ba thành phố nếu nó đang hoạt động.

Tất cả đều tốt.

Vì vậy, Delhi, lưu và chạy.

Được rồi, bạn có thể thấy nó

thực sự đang hoạt động.

Hoàn toàn chính xác.

Được rồi, điều đó thật tuyệt.

Bây giờ chúng ta hãy quay lại vấn đề chính.

Điểm là piyush đó,

mọi thứ đều tốt

Nhưng bây giờ làm sao chúng ta có thể làm được

cuộc gọi LLM này phải không?

Cuộc gọi LLM này bằng cách nào đó đã cho anh ta quyền truy cập

để tự động gọi hàm này.

Đó là những gì chúng tôi muốn làm.

Tôi muốn bằng cách nào đó một cách kỳ diệu cuộc gọi LLM của tôi,

Lệnh gọi API của tôi tới GPT4O bằng cách nào đó có thể

chạy chức năng đặc biệt này.

Có thể được không?

Về mặt kỹ thuật thì có.

Nếu chúng ta quay lại một chút

vào lời nhắc của chúng tôi.

Bạn có nhớ chúng ta đã có

chuỗi suy nghĩ này?

Bạn có nhớ chúng ta đã có

chuỗi suy nghĩ này?

Hãy để tôi sao chép cái này

chuỗi suy nghĩ.

Được rồi, điều tôi sẽ làm là

chúng ta sẽ xây dựng một chuỗi

về suy nghĩ, một lần nữa, được rồi, vì vậy tôi chỉ

sẽ sao chép toàn bộ điều này.

Được rồi?

Và ở đây, hãy để tôi tạo

một Agent.py ở đây.

Được rồi, vậy tôi đi đây

để nói đặc vụ py.

Tôi sẽ dán

mọi thứ vẫn như cũ.

Có thể nói bạn là chuyên gia

AI hỗ trợ giải quyết vấn đề người dùng

truy vấn và mọi thứ đều ở đó.

Được rồi, có một điều tôi sẽ thêm vào

ví dụ cũng là các chức năng

chỉ trong chuỗi suy nghĩ này.

Chúng ta sẽ làm một việc nữa.

Được rồi, đó là nó cũng có thể

là một trong những lời gọi hàm.

Được rồi, nó cũng có thể là một

của cuộc gọi công cụ.

Được rồi, bây giờ chuyện gì xảy ra

là nó có thể được nội dung.

Vì thế tôi sẽ chỉ nói,

chỉ chạy từng bước một.

Trình tự của bước này là bắt đầu.

Được rồi, bạn cũng có thể gọi

một công cụ nếu được yêu cầu từ danh sách

của các công cụ có sẵn.

Được rồi, đây là một điều tôi đang thêm

bây giờ chúng ta hãy cho nó thêm một lần nữa

thứ đó là công cụ có sẵn.

Được rồi, hiện tại có bao nhiêu

công cụ chúng tôi có sẵn?

Vì vậy, các công cụ có sẵn chỉ có một.

Đó là để tôi mang theo

chức năng này ở đây.

Vì vậy tôi sẽ sao chép

chức năng đặc biệt này

chỉ vào tập tin cụ thể này.

Được rồi, vậy là chúng ta đã có sẵn một công cụ.

Ngoài ra, hãy nhập khẩu

yêu cầu ở đây.

Yêu cầu nhập khẩu.

Đó là nhận được thời tiết.

Vì thế tôi chỉ định nói

các công cụ có sẵn.

Được rồi?

Là nhận được thời tiết.

Được rồi.

Và tôi sẽ chỉ nói mất

tên thành phố làm đầu vào,

được rồi, tên Thành phố làm chuỗi đầu vào

và trả lại thời tiết

thông tin về thành phố.

Được rồi?

Vì vậy, việc nắm bắt thời tiết về cơ bản là công cụ

và bạn biết đấy, đây là chữ ký.

Đó là nó.

Bây giờ điều xảy ra là tôi sẽ

cho anh ta thêm một ví dụ nữa.

Vì vậy, đây là ví dụ một.

Vì vậy tôi sẽ chỉ nói ví dụ một.

Hãy để tôi sao chép toàn bộ điều này.

Được rồi.

Và tôi chỉ định nói, này,

có một ví dụ nữa

đó là ví dụ số hai.

Giả sử người dùng hỏi, cái gì

thời tiết ở Delhi thế nào?

Được rồi, giả sử người dùng hỏi,

thời tiết ở Delhi thế nào?

Vậy bây giờ điều chúng ta phải làm là chúng ta có

để viết tất cả những điều này.

Vì vậy, có vẻ như người dùng quan tâm.

Được rồi, đang cập nhật thời tiết

của Delhi ở Ấn Độ.

Được rồi, đây chỉ là một ví dụ.

Sau đó.

Hãy xem liệu chúng ta có cái nào không

công cụ có sẵn công cụ từ danh sách

của các công cụ có sẵn.

Được rồi.

Sau đó, chúng tôi muốn điều đó.

Chào.

Được rồi, về cơ bản có thể nói là tuyệt vời.

Chúng ta có, được rồi, chúng ta có được

nhấn mạnh công cụ thời tiết

có sẵn cho truy vấn này.

Được, điều đó cũng tuyệt vời.

Vì vậy, một lần nữa, đó là một kế hoạch.

Và một lần nữa chúng ta có thể lập kế hoạch đó.

Tôi cần gọi công cụ lấy thời tiết.

Được rồi, hãy tải công cụ thời tiết cho

Delhi làm đầu vào cho thành phố.

Được rồi.

Vì vậy bây giờ khi kế hoạch này được thực hiện,

về cơ bản những gì chúng ta có thể làm là

bước này sẽ là một công cụ.

Được rồi, hãy gọi nó là cuộc gọi công cụ.

Được rồi.

Bởi vì chúng tôi đã cho

nó là một công cụ ngay tại đây.

Vâng, công cụ.

Và điều chúng ta có thể làm là

chúng ta chỉ có thể nói đầu vào.

Được rồi.

Trong trường hợp này, không có nội dung, nó

sẽ là một đầu vào.

Hoặc thậm chí bạn có thể lấy nội dung.

Được rồi, nội dung,

đầu vào sẽ là bao nhiêu hàng ngày?

Đó là nó.

Vì vậy, đó là một cuộc gọi công cụ.

Được rồi.

Và sau đó bạn cũng

cần một điều nữa.

Đó là tên công cụ.

Được rồi.

Dụng cụ.

Hãy coi nó như một công cụ.

Công cụ này có được thời tiết nhấn mạnh.

Vì vậy, bạn muốn LLM của bạn

để đáp ứng với công cụ bước.

Tên công cụ là get

thời tiết và nội dung.

Hoặc chúng ta hãy gọi nó là đầu vào.

Được rồi.

Như Delhi.

Hiểu rồi.

Bây giờ những gì xảy ra sau đó

sắp có một công cụ

một cái gì đó được gọi là quan sát.

Được rồi, tôi chỉ gọi nó là quan sát.

Vì vậy hãy quan sát.

Tôi sẽ chỉ cho bạn công cụ

tên, công cụ nào được gọi và tôi sẽ

chỉ cần cung cấp cho bạn đầu ra.

Vì vậy, giả sử nhiệt độ

của Delhi có mây với

Giả sử là 20 độ C.

Được rồi, sau đó bạn có thể

chỉ cần thực hiện một kế hoạch đó.

Tuyệt vời.

Tôi hiểu rồi, tôi hiểu rồi,

thông tin thời tiết về Delhi.

Được rồi, vậy là mọi việc đã xong.

Rồi cuối cùng chúng ta có thể

chỉ cần làm một đầu ra.

Vì vậy, tất cả những điều này là không cần thiết.

Vì vậy, bạn chỉ có thể xuất ra

thời tiết hiện tại ở Delhi là

20 độ C, có mây vài nơi

bầu trời, một cái gì đó như thế này.

Được rồi, đây là cách chúng ta

về cơ bản đang làm.

Được rồi, bây giờ còn một điều nữa.

Điều chúng ta phải làm là với mỗi,

cuộc gọi công cụ, chờ Observe.

Quan sát.

Bước, là đầu ra

từ công cụ được gọi.

Được rồi?

Vì vậy, về cơ bản đây là của chúng tôi

các bước tổng thể, được chứ?

Vì vậy chúng tôi đã đưa ra hai ví dụ,

điều đó thực sự tuyệt vời

Đây là một ví dụ về một cuộc gọi công cụ.

Vì vậy, định dạng đầu ra, được chứ?

Vì vậy, định dạng đầu ra là

về cơ bản nội dung công cụ.

Sau đó, có một công cụ,

được rồi, đó là một chuỗi.

Hãy gọi nó là một chuỗi.

Và thậm chí có thể có

một đầu vào, cũng là một chuỗi.

Vậy là mọi việc đã xong.

Bây giờ chúng ta hãy làm một việc thôi, được chứ?

Bạn có thể thấy tất cả

mọi thứ đã được thiết lập.

Bạn có thể thấy người dùng có thể hỏi điều gì đó.

Kết quả thô là có.

Kết quả đậu là có.

Bước bắt đầu, kế hoạch bước, bước đầu ra.

Bây giờ có một bước này

mà chúng ta cần thêm vào, được chứ?

Đó là điều chúng ta cần thêm sự hỗ trợ

vì một điều nữa đó là

phân tích, kết quả, dấu chấm, nhận được.

Được rồi?

Và bước đi, nếu bước đi

thực sự là một cuộc gọi công cụ.

Vậy tôi sẽ gọi thôi.

Tôi sẽ chỉ làm công cụ.

Được rồi, nếu đó là một công cụ

gọi, chúng ta cần làm gì đó

thực sự thú vị ở đây.

Vì vậy, trước tiên tôi sẽ in một bản in, được chứ?

Và tôi sẽ chỉ nói, này, để tôi

chỉ cần lấy một biểu tượng cảm xúc của một công cụ.

Vì vậy, hãy sử dụng biểu tượng cảm xúc này.

Và bạn biết đấy, tôi chỉ muốn

để cho bạn thấy điều đó, được rồi, chúng tôi

đang thực hiện cuộc gọi công cụ.

Vì vậy, f.

Được rồi, làm thế nào để nhận được cuộc gọi công cụ.

Nếu bước này là công cụ thì

bạn sẽ có một tài sản

được đặt tên là công cụ.

Được rồi?

Vì thế tôi sẽ chỉ nói, bạn biết đấy,

phân tích, kết quả, dấu chấm, lấy công cụ.

Vì vậy, đây là công cụ được gọi.

Vì vậy, công cụ để gọi, được chứ?

Vậy tôi sẽ chỉ nói là công cụ để gọi, được chứ?

Và rồi tôi cũng muốn viết

đầu vào, như công cụ này hoạt động như thế nào

được gọi với các đầu vào.

Vì vậy, tôi cần lấy đầu vào từ đây.

Vì vậy, công cụ ở đây và đầu vào ở đây.

Vì thế tôi sẽ chỉ nói,

chúng ta hãy sao chép dòng này, được chứ?

Và tôi sẽ chỉ nói đầu vào, đầu vào công cụ.

Vì vậy, tôi sẽ chỉ nói đầu vào công cụ.

Vậy bây giờ điều gì sẽ xảy ra là

chúng tôi chỉ định nói

đây là một công cụ đầu vào.

Bây giờ làm thế nào để thực sự gọi một công cụ là

Nó rất đơn giản.

Tôi sẽ tạo một bản đồ ở đây, được chứ?

Điều đó có sẵn.

Công cụ gạch dưới bằng nhau.

Tôi sẽ chỉ nói, này, tôi có một công cụ

có sẵn đó là getweather.

Đó là điều này.

Thế thôi.

Vì thế chúng tôi sẽ chỉ nói,

chúng ta hãy quay lại.

Vâng, vậy tôi sẽ chỉ nói

những công cụ có sẵn, được chứ?

Tại công cụ này để gọi, được không?

Và sau đó tôi sẽ chỉ nói

với đầu vào cụ thể này,

đây là cách bạn gọi một công cụ.

Và đổi lại bạn

Nhận phản hồi của công cụ.

Bây giờ khi bạn nhận được phản hồi của công cụ,

về cơ bản bạn có thể làm gì, bạn

chỉ cần nói được thôi, tôi sẽ làm.

Bạn nhớ bạn có tin nhắn

lịch sử, vì vậy tôi sẽ chỉ nói

lịch sử tin nhắn, chấm thêm.

Được rồi, vai trò là nhà phát triển

bởi vì đó là việc của nhà phát triển.

Vì thế tôi sẽ chỉ nói nó là

một việc dành cho nhà phát triển và tôi sẽ

chỉ cần đặt một nội dung ở đây.

Được rồi, nội dung.

Được rồi, bây giờ tôi đang nói nội dung gì

sẽ đặt ở đây là,

giả sử dấu chấm JSON, tải.

Được rồi, tải dấu chấm JSON.

Điều này trở lại.

Cái gì, xin lỗi, kết xuất dấu chấm JSON.

Tôi muốn chuyển đổi nó thành chuỗi.

Phải?

Vâng.

Vì vậy, JSON.uh, bỏ đi.

Vì vậy điều tôi sắp làm ở đây là tôi

chỉ định nói này, bước đi.

Được rồi, tôi chỉ định nói bước.

Bước này là quan sát.

Bởi vì về cơ bản quan sát cho biết

bạn biết đấy, đó là một quan sát

của cuộc gọi công cụ.

Tôi chỉ đặt tên nó là quan sát.

Bạn có thể đặt tên cho nó bất cứ điều gì

nếu bạn muốn.

Chúng tôi đã nói rằng nếu đúng như vậy

quan sát, tôi sẽ cung cấp cho bạn công cụ

đó là công cụ thực sự được gọi.

Được rồi, vậy đây là công cụ

được gọi là công cụ để gọi.

Được rồi, chúng ta hãy cung cấp cho nó một đầu vào.

Vậy đầu vào ban đầu là gì?

Vì vậy, đây là đầu vào công cụ.

Điều này sẽ giống như

cái này, không phải sợi dây.

Được rồi.

Và sau đó là điều quan trọng nhất

là đầu ra.

Vì vậy, tôi sẽ chỉ nói đầu ra.

Vậy đầu ra là gì vậy các bác?

Đầu ra về cơ bản là

phản ứng của công cụ.

Bây giờ một khi bạn đã làm điều này

bạn có thể cảm thấy tự do

để bây giờ chạy tiếp tục.

Vì vậy, những gì đã xảy ra là bạn chỉ có thể nói

bạn đã gọi điều đặc biệt này

Chúng ta cũng hãy đưa ra một tuyên bố in

kết quả bạn nhận được là gì?

Được rồi, tôi thực sự muốn

để xem kết quả.

Vì vậy, đây là một phản ứng công cụ.

Vì vậy, đây thực sự là cách bạn

gọi một công cụ bên trong đại lý.

Được rồi, bây giờ hãy xem điều gì sẽ xảy ra.

Được rồi, vậy tôi đi đây

để chạy mã đặc biệt này.

Làm thế nào chúng ta nhận được đầu vào?

Vì vậy, ở đây chúng tôi đang nhận được đầu vào.

Hãy chạy mã cụ thể này.

Vì vậy, bạn có thể thấy nó đang chạy.

Điều đó thật tuyệt.

Hãy để tôi hỏi câu hỏi tương tự

cái gì, chúng ta đã hỏi gì trước đây?

Được rồi, bằng cách nào đó tôi có

đã mất câu hỏi đó.

Thời tiết hiện tại thế nào.

Hãy yêu cầu GOA

và bây giờ chúng ta hãy xem điều gì sẽ xảy ra.

Được rồi, vậy bạn phải

quan sát những gì xảy ra bây giờ Enter.

Hãy xem.

Được rồi, xem dự báo thời tiết đi.

Điều đó thật tuyệt.

Ồ GOA có vẻ như vậy

một địa điểm không xác định.

Được rồi, bạn có thể thấy, xem

chuyện gì xảy ra ở đây

Nhận thời tiết goa.

Thời tiết ở GOA là

vị trí không rõ.

Hãy thử điều này.

Ồ được rồi, có vẻ như có vấn đề

với việc thu thập thời tiết.

Goa, đây là những gì chúng ta có.

Có thể do vị trí

không được công nhận.

Vì vậy, nó thực sự được sử dụng

tọa độ tự động.

Vậy là trời có thời tiết

cho những đầu vào này.

Thời tiết,

trong cái này, cái này, cái này và hay.

Được rồi, tôi hiểu rồi.

Vì vậy, thay vì thành phố, thực ra

nó đã sử dụng tọa độ.

Được rồi, để tôi hỏi nó

một câu hỏi nữa.

Được rồi.

Tôi sẽ chỉ xóa đầu ra.

Hãy chạy nó một lần nữa.

Thời tiết ở Delhi thế nào?

Hoặc bây giờ chúng ta hãy hỏi điều gì khác.

Bangalore.

Thực ra đó là Bengaluru.

Ngay lập tức.

Tôi không chắc liệu nó có hoạt động không.

Nhận thời tiết.

Bangalore, có mây vài nơi.

Tôi đã lấy lại.

Và bạn đã nhận được kết quả như vậy

thời tiết hiện tại của nó

Bangalore thực ra là 23.

Vì vậy bạn có thể thấy chúng tôi

thực sự đã có đầu ra.

Đẹp.

Được rồi, bây giờ chúng ta hãy làm một việc thôi.

Vấn đề là sau mỗi lần

đầu ra, những gì đang xảy ra, nó là như vậy.

Nó đang thoát ra ngoài.

Phải.

Tôi muốn làm cho nó liên tục.

Nhân tiện, thêm một cái nữa

điều tôi muốn cho bạn xem.

Nếu chúng ta chạy cái này cụ thể,

code lại cho em hỏi

đó là một câu hỏi phức tạp

Thời tiết là gì

của Delhi dấu phẩy Bangalore?

Và hãy lấy thêm một thành phố nữa,

có thể bạn biết, Patiala.

Hãy xem điều gì sẽ xảy ra.

Tôi đang hỏi nó ba câu hỏi.

Được rồi.

Nhận thời tiết.

Delhi.

Có Delhi.

Bây giờ nó đang tiến tới Bangalore.

Và bây giờ nó sẽ đến với Patiala.

Được rồi.

Nó sẽ làm lại điều đó cho Patiala.

Vì vậy, thời tiết hiện tại của

Delhi bị bỏ lỡ vào ngày 27.

Ở Bangalore trời có mây một phần.

Và thật không may là tôi không thể

lấy lại cho Patiala.

Không sao đâu.

Đây là cách nó hoạt động.

Bây giờ hãy làm cho nó tốt hơn.

Bởi vì ngay bây giờ chúng ta có thể

chỉ có một đầu vào.

Vậy điều tôi sắp làm là

bên trong thứ này.

Được rồi.

Tôi cũng muốn làm cái này

như một phần của vòng lặp.

Vì vậy, hãy xem những gì chúng ta có thể làm là tôi có thể

thực ra, làm toàn bộ chuyện này

cũng như một phần của vòng lặp while.

Trong khi đúng.

Được rồi.

Trong khi đúng.

Chỉ cần thay đổi điều này.

Được rồi.

Vì vậy, mặc dù đúng.

Lịch sử tin nhắn.

Và sau đó bạn di chuyển đại lý.

Bây giờ hãy xem điều gì sẽ xảy ra.

Được rồi.

Nếu mọi chuyện đều ổn,

Tôi hy vọng tôi đã không làm hỏng bất cứ điều gì.

Thời tiết của Delhi là gì?

Chỉ là một câu hỏi đơn giản.

Thời tiết của Delhi là gì?

Được rồi, cuộc gọi công cụ phải ở đó.

Bạn có thể thấy chúng tôi

thực hiện cuộc gọi công cụ.

Được rồi.

Thời tiết ở Delhi thế nào

và có thể là Hyderabad?

Được rồi, vào đi.

Hãy xem điều gì sẽ xảy ra.

Tôi nên sử dụng.

Được rồi, đó là.

Được rồi.

Vậy là Delhi đã thành công.

Tôi đã nhận được nó cho Hyderabad.

Được rồi.

Và đó là nó.

Để bạn có thể thấy tôi là gì

về cơ bản cố gắng làm là bạn chỉ

tiếp tục đặt câu hỏi.

Nó có quyền truy cập vào thực tế

thông tin thời gian.

Và đây là nơi chúng ta có thể nói rằng chúng ta

đã phát triển đại lý đầu tiên của chúng tôi.

Bạn đã cung cấp một công cụ của bạn

cho đại lý của bạn và đó là

làm việc hoàn toàn tuyệt vời.

Bạn đã có nó ngay bây giờ.

Bây giờ điều bạn phải làm là bạn có

chỉ để viết thêm chức năng

và cung cấp nó như một danh sách có sẵn

công cụ và phần còn lại LLM của bạn sẽ xử lý.

Vậy đây là cách bạn

về cơ bản xây dựng một đại lý.

Vì vậy, bây giờ đại lý thời tiết của bạn có

một tay là tạo API

gọi tới API thời tiết.

Vậy LLM với các công cụ

về cơ bản là đại lý của bạn.

Được rồi, đây là cách bạn

xây dựng đại lý của riêng bạn.