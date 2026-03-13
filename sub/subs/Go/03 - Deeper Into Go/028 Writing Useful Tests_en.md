# 028 Viết bài kiểm tra hữu ích vi

---

Steven: Ở phần cuối

chúng tôi bắt đầu nói về việc thử nghiệm mã của mình.

Chúng tôi đã tạo một tệp mới có tên là deck_test.go,

và bây giờ chúng ta đã sẵn sàng để bắt đầu viết ra

một số mã thực tế kiểm tra nội dung của chúng tôi, phải không?

Bây giờ, đây là phần của mọi khung thử nghiệm đơn lẻ

với mọi ngôn ngữ tôi từng làm việc cùng,

Tôi luôn nhận được câu hỏi tương tự.

Và câu hỏi đó luôn là

"Steven, làm sao chúng ta biết phải kiểm tra cái gì?"

Chà, với Go, điều này thực sự thường kết thúc

một câu hỏi khá đơn giản.

Vì vậy, chúng ta hãy xem một sơ đồ nhanh ở đây.

Vì thế tôi muốn tìm hiểu

làm thế nào chúng ta có thể quyết định nên kiểm tra cái gì?

Trong trường hợp này, hãy nghĩ về hàm newDeck của chúng ta.

Bây giờ hàm newDeck đã có số lượng khá lớn

logic bên trong nó, phải không?

Giống như nếu chúng ta nhìn vào hàm newDeck

bên trong trình soạn thảo mã của chúng tôi,

vì vậy đây là newDeck ngay tại đây, chúng tôi tạo một bộ bài trống,

chúng tôi tập hợp hai loại danh sách bắt đầu này

về những bộ quần áo và giá trị, và sau đó chúng ta có

câu lệnh if lồng nhau này, xin lỗi, câu lệnh if lồng nhau.

Và vì vậy tôi có thể dễ dàng tưởng tượng ra nhiều tình huống

nơi một nhà phát triển khác có thể đến đây

và họ bắt đầu làm rối tung mọi thứ

và bắt đầu phá mã một cách vô tình.

Và vì thế tôi nghĩ hoàn toàn hợp lý khi nói,

"Có lẽ chúng tôi muốn viết một bài kiểm tra về bộ bài mới này."

Nhưng ngay cả khi đó tôi vẫn nhận được câu hỏi,

"Ồ, thực ra chúng ta đang thử nghiệm cái gì vậy?

Giống như cách chúng ta viết bài kiểm tra để đảm bảo

newDeck đó có hoạt động như chúng ta mong đợi không?"

Và câu trả lời của tôi cho bạn,

và câu trả lời cho tất cả các câu hỏi kiểm tra này

đó là việc bạn, với tư cách là nhà phát triển, có quyền nói,

"Tôi thực sự quan tâm đến điều gì với newDeck?"

Bạn thực sự quan tâm đến điều gì?

Vâng, đối với cá nhân tôi,

khi tôi nghĩ về chức năng bộ bài mới

và có lẽ có ba điều tôi thực sự quan tâm

hoặc ba điều đơn giản mà tôi có thể dễ dàng kiểm tra.

Và nếu mỗi tiêu chí nhỏ này đều đúng

khi tôi chạy thử nghiệm, điều đó có thể có nghĩa là

newDeck đó đang hoạt động theo cách tôi mong đợi.

Và đây là ba tiêu chí.

Trước hết, tôi nghĩ nó có ý nghĩa

để nói điều đó sau khi chúng tôi tạo một bộ bài mới

chẳng hạn, chúng ta nên có bốn mục bên trong nó.

Vì vậy, hãy giả sử rằng chúng ta đang tạo một bộ bài có bốn vật phẩm

hoặc bốn chuỗi, bốn thẻ.

Vì thế có lẽ sẽ rất có ý nghĩa khi nói

hãy kiểm tra chiều dài của bộ bài được trả lại

và nó phải giống hệt như bốn lá bài.

Tôi nghĩ đó là một sự kiểm tra hoàn toàn hợp lý, phải không?

Có lẽ một điều khác mà tôi muốn kiểm tra

là đảm bảo rằng lá bài đầu tiên trong bộ bài

bằng với quân át bích, và sau đó có thể là thứ thứ ba

rằng đó là một cuộc kiểm tra thực sự dễ dàng và đơn giản

là để nói rằng tôi muốn chắc chắn

rằng quân bài cuối cùng bằng bốn quân bích.

Và thực sự không có nhiều mánh khóe ở đây

hoặc rất nhiều điều mơ hồ.

Bất cứ khi nào bạn viết bài kiểm tra, chỉ cần nghĩ về,

à, một số khẳng định dễ dàng là gì

hoặc tôi quan tâm đến điều gì

với đoạn mã tôi đang viết?

Bạn có thể viết một số bài kiểm tra xung quanh đó,

và thành thật mà nói, đó là tất cả những gì cần có.

Vậy hãy làm ba bài kiểm tra đó và tìm ra chính xác

cách chúng tôi có thể cấu trúc chúng bên trong tệp thử nghiệm của mình.

Được rồi, đây sẽ là một sơ đồ khó chịu,

nhưng chúng ta sẽ đi từng bước một.

Vì vậy, bất cứ khi nào chúng tôi xác định được một chức năng mà chúng tôi muốn kiểm tra

từ mã thực của chúng ta, chúng ta sẽ tạo một hàm mới

bên trong tệp thử nghiệm của chúng tôi có tên Test

và sau đó là chức năng mà chúng tôi đang thử nghiệm.

Vì vậy trong trường hợp này,

chúng ta sẽ tạo một hàm có tên TestNewDeck.

Và bên trong hàm đó

chúng ta sẽ viết một số mã để thực hiện một số kiểm tra

về một bộ bài mà chúng ta có thể làm.

Vì vậy có lẽ tấm séc đầu tiên chúng ta tập hợp lại

là một số mã để đảm bảo

rằng một bộ bài được tạo ra với một số lượng quân bài nhất định.

Chúng tôi đảm bảo rằng quân bài đầu tiên là quân Át

và rồi lá bài cuối cùng là lá bài giống như bốn câu lạc bộ

hoặc bất cứ điều gì nó thực sự có thể trở thành.

Và cuối cùng khi chúng tôi bắt đầu viết bài kiểm tra

xung quanh các chức năng khác nữa, như nói,

lưu vào tập tin hoặc bộ bài mới từ tập tin,

đó là hai chức năng khác có liên quan rất chặt chẽ với nhau,

chúng ta có thể tạo một hàm khác gọi là

"TestSaveToDeckandNewDeckFromFile",

và nó sẽ có một số mã kiểm tra cả hai chức năng đó

bên trong chức năng đó là tốt.

Đó là cách tiếp cận chung mà chúng ta sẽ thực hiện ở đây.

Ngay cả vào thời điểm này, bạn có thể đang nghĩ,

"Ồ, làm cách nào chúng ta có thể viết mã để đảm bảo

rằng một bộ bài được tạo ra với một số lượng quân bài nhất định?"

Một lần nữa, chúng ta sẽ viết một số điều khá cơ bản

hoặc mã Go đơn giản để đảm bảo trường hợp đó xảy ra.

Vì vậy, để đảm bảo rằng bộ bài được tạo ra

với một số lượng thẻ nhất định,

chỉ cần tưởng tượng quá trình đó trong đầu bạn,

như chúng ta sẽ làm gì?

Chà, có lẽ chúng ta sẽ tạo một bộ bài mới.

Có lẽ sau đó chúng tôi sẽ viết một số câu lệnh if để đảm bảo

rằng bộ bài có đúng số lượng quân bài,

hoặc số lượng thẻ mà chúng ta mong đợi nó có.

Và sau đó nếu không, vậy nếu nó thất bại thì điều này

câu lệnh if ngay tại đây, chúng tôi sẽ thông báo cho bộ xử lý kiểm thử của mình,

đó là điều mà chúng ta sẽ nói đến trong giây lát nữa

chính xác trình xử lý kiểm tra này là gì,

về cơ bản chúng tôi sẽ thông báo cho người chạy thử nghiệm cờ vây của mình

có điều gì đó vừa xảy ra

và đặc biệt là thử nghiệm này đã thất bại.

Vì vậy, hãy thử viết bài kiểm tra này ngay tại đây

và xem nó thực sự trông như thế nào trong thực tế.

Vì vậy, tôi sẽ quay lại tệp deck_test.go của chúng tôi,

và chúng ta sẽ bắt đầu bằng cách viết ra một hàm.

Vì vậy chúng ta sẽ nói func và đặt cho nó một cái tên

của TestNewDeck vì đó là chức năng

rằng chúng tôi đang viết một số bài kiểm tra xung quanh.

Vì vậy chúng ta sẽ nói TesNewDeck như vậy.

Bây giờ hãy lưu ý rằng, không giống như nhiều chức năng khác

mà chúng ta đã ghép lại với nhau, hàm này có chữ T viết hoa

trong từ Kiểm tra ngay tại đây.

Bạn có thể đã nhận thấy khi chúng tôi đặt

cùng với tập tin deck.go của chúng tôi,

rằng tất cả các chức năng chúng tôi kết hợp với nhau

bên trong đây đều là chữ thường.

Và thực sự có một lý do rất chính đáng

rằng chúng tôi đã viết tất cả những chữ này thành chữ thường.

Và chúng tôi đang viết cái này ở đây thành chữ hoa,

và chúng ta sẽ nói về lý do tại sao lại như vậy sau một lát nữa

trong ứng dụng tiếp theo mà chúng tôi làm việc.

Được rồi, chức năng này sẽ chịu trách nhiệm

để thử nghiệm chức năng bộ bài mới.

Bây giờ có một điều thực sự kỳ lạ ở đây,

và điều này sẽ trông hơi kỳ lạ một chút,

chức năng này sẽ được gọi tự động

bởi người chạy thử cờ vây hoặc người chạy thử cờ vây

với một lập luận mà chúng tôi gọi là T

và nó thuộc loại sao, kiểm tra, dấu chấm, chữ T viết hoa như vậy.

Và cái này ở ngay đây, ngôi sao này, thử nghiệm, chữ T viết hoa,

vâng, nó trông khá lạ, tôi đồng ý.

Hãy nhớ rằng trong một cuộc gọi hàm bình thường

điều này sẽ chỉ định loại giá trị

đó đang được chuyển vào hàm.

Vậy chúng ta sẽ nói chuyện một lát sau

về chính xác ý nghĩa của ngôi sao ở đây,

nhưng hiện tại chúng ta sẽ để nó như vậy.

Được rồi, một lần nữa, hãy tập trung vào

những gì chúng tôi đang cố gắng kiểm tra ở đây.

Chúng tôi muốn tạo một bộ bài mới.

Sau đó chúng ta sẽ viết một câu lệnh if để đảm bảo

rằng bộ bài có đủ số lá bài,

và sau đó nếu không, chúng tôi sẽ thông báo cho người xử lý kiểm tra đó

rằng có điều gì đó không ổn.

Vì vậy, chỉ để rõ ràng,

thứ T ở đây là người xử lý thử nghiệm của chúng tôi.

Đó là những gì chúng ta kể điều gì đó,

nếu có vấn đề gì xảy ra với thử nghiệm của chúng tôi,

chúng tôi nói giá trị này ngay tại đây

rằng có điều gì đó không ổn,

và chúng ta sẽ sớm thấy nó trông như thế nào trong thực tế.

Vì vậy chúng ta sẽ làm một bộ bài mới.

Sau đó chúng ta sẽ viết ra một câu lệnh if để đảm bảo

rằng bộ bài có đúng số quân bài.

Vì vậy, chúng ta sẽ nói nếu độ dài của d không bằng,

và sau đó chúng ta cần đảm bảo rằng chúng ta thực sự

lấy số chính xác hoặc độ dài chính xác ngay tại đây.

Vì vậy, nếu chúng ta quay lại tệp deck.go,

hãy nhớ rằng chúng ta có bốn chất và bốn giá trị.

Vì vậy, nếu bạn sử dụng nhiều giá trị hơn tôi đã làm

bạn sẽ có một con số hơi khác một chút.

Nhưng giả sử rằng bạn có bốn chất và bốn giá trị,

điều đó có nghĩa là bạn sẽ có 16 lá bài.

Vì vậy, hãy quay lại phần thử nghiệm của chúng tôi ở đây

chúng tôi sẽ nói rằng chúng tôi mong đợi bộ bài của chúng tôi d

có 16 thẻ bên trong.

Vì vậy, nếu độ dài của d không bằng 16

điều đó có nghĩa là đã xảy ra sự cố

và chúng ta cần thông báo cho người xử lý kiểm tra này ngay tại đây

rằng có điều gì đó không ổn.

Vì vậy, chúng ta sẽ viết ra t.Errorf như vậy,

và chúng ta sẽ chuyển cho nó một chuỗi

mô tả chính xác điều gì vừa xảy ra.

Vì vậy chúng ta sẽ chuyển vào một chuỗi có nội dung:

"Dự kiến chiều dài boong là 20, nhưng đã có"

và sau đó chúng tôi muốn đảm bảo rằng chúng tôi thực sự in ra

chiều dài mà chúng tôi đã nhận được.

Vì vậy, chúng tôi sẽ đóng chuỗi và sau đó làm đối số thứ hai

chúng ta sẽ đi dọc theo chiều dài của bộ bài, hoặc len d.

Xin lỗi, hãy để tôi thu phóng ngay, chúng ta bắt đầu.

Vì vậy bây giờ nếu bộ bài không có 16 lá bài bên trong

chúng tôi sẽ thông báo cho người xử lý kiểm tra

có điều gì đó vừa xảy ra

và chúng tôi sẽ đưa ra thông báo lỗi cho nó,

"Dự kiến thứ này có chiều dài 20,

nhưng thay vào đó chúng tôi lại nhận được blah," bất kể độ dài thực sự là bao nhiêu.

Đó là khá nhiều cho thử nghiệm đầu tiên của chúng tôi.

Hãy lưu tập tin này và sau đó chạy nó để xem điều gì sẽ xảy ra.

Bây giờ ngay khi tôi lưu tệp trong Mã VS,

bạn sẽ nhận thấy rằng chúng tôi nhận được một báo cáo nhập khẩu

để thử nghiệm ngay tại đây.

Một lần nữa, nếu bạn không sử dụng Mã VS,

nếu bạn đang sử dụng một số trình soạn thảo khác,

hãy đảm bảo bạn thêm câu lệnh nhập vào đây.

Vì vậy, bây giờ để chạy thử nghiệm, chúng tôi có thể sử dụng

trình trợ giúp VS Code tích hợp ngay tại đây

và chỉ cần nhấp vào chạy thử.

Ngoài ra, chúng ta có thể quay lại thiết bị đầu cuối của mình

và chạy lệnh go test.

Được rồi, khi tôi làm vậy,

chúng tôi nhận được thông điệp lớn thú vị này nói rằng đã vượt qua.

Có vẻ như tất cả các thử nghiệm của chúng tôi đã được thực hiện thành công.

Bây giờ, chỉ để đảm bảo rằng chúng tôi đã viết bài kiểm tra của mình một cách chính xác,

và nhân tiện, bạn sẽ nhận thấy

một chút nguệch ngoạc màu xanh lá cây ở đây kèm theo lời cảnh báo.

Chúng ta sẽ nói về điều đó chỉ trong hai giây.

Nhưng trước tiên, để đảm bảo rằng chúng ta có

một bài kiểm tra chức năng thực tế ở đây, chúng tôi sẽ thay đổi độ dài

từ 16 đến khoảng gì đó, tôi không biết, 2000

để đảm bảo rằng thử nghiệm của chúng tôi thực sự hoạt động chính xác.

Và bây giờ khi chúng tôi chạy nó, chúng tôi nhận được kết quả này

thông báo lỗi nhỏ hay ho và khó chịu nói rằng,

"Được rồi, chúng tôi đã chạy deck_test, chúng tôi dự kiến chiều dài deck là 20,

nhưng có chuyện gì đó," vậy rõ ràng có điều gì đó không ổn ở đây.

Được rồi, bây giờ hãy giải quyết thông báo lỗi nhỏ này

hoặc cảnh báo nhỏ này ở đây.

Vì vậy bạn sẽ nhận thấy rằng nó nói,

hãy để tôi đóng thanh bên của tôi thật nhanh ở đây

để bạn có thể nhìn thấy toàn bộ dòng.

Thế đấy.

Vì vậy, người báo cáo lỗi nhỏ này ở ngay đây

là những gì chúng ta gọi là một chuỗi được định dạng.

Và do đó, một chuỗi được định dạng có nghĩa là

mà chúng ta có thể chuyển vào một số giá trị bổ sung

và sau đó để chúng được tiêm tự động

vào chuỗi mà chúng tôi cung cấp làm đối số đầu tiên.

Và về cơ bản điều này muốn chúng ta làm là nó nói rằng,

"Này, bạn đang chuyển giá trị tăng thêm này vào đây,

độ dài của d, bạn cần thực sự sử dụng giá trị đó

và đưa nó vào chuỗi ngay tại đây."

Vì vậy, để tiêm nó vào chuỗi

chúng ta sẽ đi đến cuối chuỗi

rồi nói "%v" như vậy.

Vì vậy, điều đó có nghĩa là sử dụng một chuỗi có độ dài dự kiến là 20,

nhưng bị bỏ trống và "%v" ngay tại đây sẽ bị lấy đi

từ bất kỳ giá trị nào chúng ta đã chuyển vào đây.

Vì vậy, hãy chạy lại mã này và bây giờ xem điều gì sẽ xảy ra.

Vì vậy chúng ta sẽ chạy go test.

Và khi chúng ta làm như vậy, chúng ta thấy

"Dự kiến chiều dài boong là 20, nhưng lại có 16."

Và bạn biết tôi vừa nhận ra điều gì không?

Vâng, chúng tôi đã mô tả sai ở đó.

Tôi đặt vào 20, ý tôi là 16, nhưng rõ ràng là nó đang hoạt động

bởi vì chiều dài boong của chúng tôi không phải là 2000.

Và đó là lý do tại sao chúng tôi thấy thông báo lỗi ngay từ đầu.

Vì vậy, chúng tôi sẽ sửa lỗi này trở lại 16.

Vậy là chúng ta có 16, 16, mọi thứ đều ổn.

Hãy chạy thử nghiệm một lần nữa và chúng ta sẽ quay lại đạt kết quả.

Bây giờ một lần nữa, tất nhiên, nếu bạn muốn,

bạn có thể sử dụng các trình trợ giúp tích hợp này với Mã VS

bằng cách nhấp vào nút chạy thử nghiệm.

Và nó sẽ mở ra một bảng điều khiển đầu ra nhỏ ở dưới đây

chỉ chạy một bài kiểm tra cụ thể đó

và sau đó in kết quả ra

và cho bạn biết bài kiểm tra có đạt hay không.

Và nút chạy kiểm tra ngay tại đây là hữu ích nhất

khi bạn đang làm việc trên một dự án

với rất nhiều bài kiểm tra khác nhau bên trong nó.

Vì vậy bạn chỉ cần nói, "Chỉ cần chạy thử nghiệm này,

đừng chạy mọi thứ.

Tôi chỉ muốn biết thử nghiệm đơn lẻ này diễn ra thế nào thôi."

Được rồi, đó là rất nhiều về thử nghiệm. Chúng ta hãy nghỉ ngơi nhanh chóng.

Chúng ta sẽ quay lại ở phần tiếp theo

và chúng ta sẽ viết ra

thêm một vài bài kiểm tra bên trong tập tin này,

vậy tôi sẽ gặp bạn sau một phút nữa.