# 4 -Về việc tạo văn bản từ các mô hình được huấn luyện trước

---

Bạn đã biết cách mã hóa văn bản và tạo văn bản từ một mô hình bằng cách sử dụng trình tạo

phương pháp.

Tuy nhiên, những mẫu máy bạn có thể tải xuống từ Ôm Mặt có một số cài đặt cụ thể

và các thông số, đồng thời có thể đưa ra các thông báo cảnh báo đối với một số đầu vào nhất định hoặc thiếu đầu vào.

Và video này là một bản demo mã ngắn mà tôi sẽ chỉ dành vài phút để khám phá

các tham số của tokenizer và các mô hình được đào tạo trước.

Hãy nhớ rằng cú pháp chính xác

để tương tác với các mô hình khác nhau giữa các mô hình khác nhau,

các mã thông báo khác nhau, các tổ chức khác nhau, v.v.

Vì vậy, hãy nhớ rằng các quy ước đặt tên chính xác

có thể khác nhau, chẳng hạn như GPT và BERT.

Vì vậy trong video này, tôi sẽ tập trung vào GPT-2.

Có một mã thông báo đặc biệt gọi là mã thông báo pad,

được sử dụng khi bạn có các chuỗi trong một đợt

có độ dài khác nhau.

Ví dụ, hãy tưởng tượng rằng bạn có một câu

trong số 10 thẻ, và sau đó là câu tiếp theo

trong lô có 15 mã thông báo.

Bây giờ, các lô được tổ chức dưới dạng tensor,

hoặc ma trận trong trường hợp này, và vì vậy mỗi hàng

cần phải có cùng số phần tử trong đó.

Và vì vậy bạn sẽ đệm các chuỗi ngắn hơn

để đạt đến độ dài của chuỗi dài nhất.

Hiện tại, mã thông báo GPT-2 không có

một bộ mã thông báo đệm mặc định.

Và thành thật mà nói, tôi không biết tại sao lại như vậy,

nhưng nó không phải là vấn đề lớn.

Đây chỉ là một dòng mã để đặt mã thông báo đệm,

đó là những gì bạn sẽ thấy ở đây.

Thông thường, mã thông báo đệm được đặt thành EOS,

viết tắt của sự kết thúc của chuỗi.

Thường được dùng để kết thúc một đoạn văn bản

giống như phần cuối của một trang Wikipedia.

Khi mô hình được huấn luyện trên EOS,

nó sẽ biết rằng mã thông báo này tương ứng với việc dừng lại.

Vì vậy, mô hình nhìn thấy mã thông báo EOS

và nó sẽ ngừng tạo mã thông báo mới sau đó.

Sau đó tôi sẽ chỉ cho bạn cách token hóa một loạt nhiều câu có độ dài khác nhau.

Bạn có thể thấy rằng đầu ra của tokenizer giờ đây không còn chỉ là danh sách các số nguyên nữa,

nhưng thay vào đó là một cuốn từ điển có nhiều khóa.

Tôi sẽ thảo luận vấn đề này chi tiết hơn khi chuyển sang viết mã, nhưng tôi nghĩ khi bạn nhìn

ở mặt nạ chú ý ở đây, bạn đã có thể đoán được

rằng điều này sẽ tương ứng với các mã thông báo hợp lệ

mà người mẫu cần chú ý đến.

Sau đó tôi sẽ chỉ cho bạn cách tham số hóa đầy đủ một cuộc gọi

đến lớp .generate.

Bây giờ tôi đã thảo luận về một số lựa chọn này

trong một số video trước đây nên điều này sẽ hơi ngắn một chút

lời nhắc nhở và một số thông tin mới.

Hãy nhớ rằng không phải lúc nào bạn cũng cần nhập

tất cả các thông số này.

Tôi chỉ hiển thị chúng ở đây để bạn hiểu

về những lựa chọn là gì.

Và ở cuối phần demo mã,

Tôi cũng sẽ chỉ cho bạn một cú pháp rất đơn giản mà bạn có thể sử dụng,

đôi khi tạo ra cảnh báo,

nhưng hầu hết thời gian bạn không cần phải lo lắng về chúng.

Được rồi, hãy chuyển sang Python.

Vì thế ở đây chúng ta chỉ cần Torch,

chúng ta cần thư viện Transformers từ Ôm mặt,

và từ đó chúng ta sẽ nhận được tokenizer

và mô hình được đào tạo trước cho GPT-2.

Và đó là những gì tôi đang nhập ở đây hoặc đang nhập ở đây.

Được rồi, vậy bạn có thể xem ở đây

Tôi đang in tokenizer.padToken

và cả tokenizer.eos.

Một lần nữa, đây là phần cuối của chuỗi.

Và như tôi đã đề cập, việc đặt padToken là điều bình thường

là mã thông báo kết thúc chuỗi.

Bây giờ, điều này đôi khi có thể gây ra một số vấn đề trong quá trình đào tạo

bởi vì bất cứ khi nào mô hình nhìn thấy token EOS

thường được liên kết với phần cuối của văn bản,

phần cuối của một trang web, phần cuối của một email,

phần cuối của một tài liệu.

Vì vậy, khi bạn sử dụng mã thông báo EOS làm mã thông báo đệm,

có một chút nguy cơ gây nhầm lẫn cho mô hình

một chút để nghĩ rằng có nhiều đầu

của chuỗi văn bản.

Bây giờ để đào tạo, điều này thường không phải là vấn đề

bởi vì khi bạn đang đào tạo trước một người mẫu

và khi bạn tinh chỉnh một mô hình,

bạn thường sử dụng những văn bản rất dài

được nối hoặc cắt bớt

thành các chuỗi nhỏ hơn có độ dài bằng nhau.

Vì vậy, trong quá trình đào tạo, nó thực sự không phải là vấn đề lớn.

Và sau đó trong quá trình đánh giá,

nói chung là ổn vì những token đệm này

đi vào cuối.

Vì vậy, về cơ bản mô hình sẽ chỉ xem

nhiều mã thông báo EOS,

nhưng điều đó cũng không thực sự quan trọng lắm

vì chiếc mặt nạ chú ý

mà tôi sẽ giải thích trong giây lát.

Được rồi, vậy chúng ta hãy xem cái này.

Vì vậy chúng ta có thể thấy dòng mã này

là trạng thái mà mã thông báo pad được đặt thành không.

Và ở đây bạn có thể thấy token EOS ở cuối văn bản

hoặc kết thúc chuỗi.

Được rồi, và sau đó, chúng ta xác định mã thông báo pad ở đây.

Tôi đang định nghĩa lại nó là, thay vì không có,

nó sẽ là phần cuối của mã thông báo văn bản.

Điều đó ổn thôi.

Có những lúc khác bạn có thể muốn đặt điều này

là một khoảng trắng hoặc có thể là một tab,

nhưng việc đặt mã thông báo pad này khá phổ biến

trở thành mã thông báo EOS.

Được rồi, bây giờ chúng ta có một tình huống thú vị

nơi tôi muốn mã hóa hoặc mã hóa ba câu lệnh này,

ba chuỗi văn bản này,

chúng có số lượng ký tự khác nhau,

số lượng từ khác nhau,

điều đó không có nghĩa tầm thường

rằng chúng sẽ có số lượng token khác nhau,

nhưng có thể chắc chắn rằng ba câu này

sẽ tương ứng với ba độ dài khác nhau của mã thông báo.

Vì vậy, chúng ta có thể viết phần đệm bằng true,

Và hãy chú ý xem điều đó mang lại cho chúng ta điều gì ở đầu ra.

Đây là chuỗi mã thông báo cho câu đầu tiên.

Và bạn có thể thấy đây là những token

tương ứng với văn bản.

Và ở đây chúng ta có các thẻ đệm ở đây.

Và câu thứ ba cũng tương tự,

có hai mã thông báo pad ở đây.

Và cái ở giữa, đó là cái dài nhất,

đó là mỗi gia đình bất hạnh đều bất hạnh theo cách riêng của mình.

và nó không có phần đệm, không có thẻ đệm,

vì đó là thời gian dài nhất

Vì vậy, về cơ bản, tokenizer đã xem qua

ba tuyên bố này, ba trình tự này,

nhận ra rằng đây là cái dài nhất,

và sau đó đệm hai cái còn lại

sao cho chúng đều có cùng độ dài.

Được rồi, đó là ID đầu vào chính,

vì vậy hãy nhập ID mã thông báo.

Và có một trong số đó cho mỗi yếu tố

trong danh sách này ở đây.

Được rồi, sau đó chúng ta có thứ khác ở đây

được gọi là mặt nạ chú ý.

Và khi bạn nhìn vào những con số này,

Tôi nghĩ điều đó khá rõ ràng đây là gì.

Đây là mã dành cho tất cả các mã thông báo hợp lệ

thực sự phù hợp với văn bản.

Và đó là số 0 cho các mã thông báo không xuất hiện

trong văn bản nhưng chỉ được điền vào một số giá trị mặc định.

Được rồi, bên trong là những mẫu mặt ôm

được lập trình để tránh xử lý các mã thông báo này tại đây

có mặt nạ chú ý bằng 0.

Được rồi, vậy bây giờ tôi sẽ làm gì

về cơ bản chỉ là in ra tất cả thông tin này

theo cách dễ nhìn hơn một chút.

Thế nên gia đình hạnh phúc nào cũng giống nhau

và nó có những mã thông báo và mặt nạ chú ý này.

Mỗi gia đình không hạnh phúc đều bất hạnh theo cách riêng của mình.

Và tại sao con gà lại băng qua đường?

Tôi không biết ba câu này được kết nối với nhau như thế nào.

Trên thực tế, hai cái này là.

Và nếu bạn không biết điều này,

đó là phần mở đầu nổi tiếng của một cuốn sách nổi tiếng.

Và tôi sẽ để bạn tự tìm hiểu xem đó là gì.

Được rồi, bây giờ những gì tôi sắp cho bạn xem

đang tạo ra một số văn bản.

Vì vậy ở phần trước,

chúng tôi chỉ đang tạo ra loại văn bản một cách nhanh chóng,

không phải là siêu lừa đảo cẩn thận về nó.

Và về cơ bản chúng tôi chỉ đang làm điều gì đó như thế này.

Chúng tôi vừa nói model.generate

và sau đó là token, về cơ bản là tất cả.

Phương pháp tạo này trong các mô hình khuôn mặt ôm

có rất nhiều lựa chọn bổ sung.

Vì vậy, chúng tôi có ID đầu vào,

đó là cách chúng tôi đã sử dụng nó cho đến nay.

Chú ý mặt nạ, bây giờ dòng này bạn không nhất thiết phải cần

trừ khi bạn có nhiều đầu vào

với độ dài chuỗi khác nhau.

Vì vậy, chỉ đôi khi bạn cần phải lo lắng về điều này.

Bạn có thể chỉ định rõ ràng mã thông báo đệm,

chiều dài tối đa.

Bây giờ, đây là độ dài tối đa của đầu ra,

trong đó bao gồm đầu vào.

Và cũng nên nhớ rằng tham số này ở đây, độ dài tối đa,

không có nghĩa là đầu ra nhất thiết phải chính xác

dài 66 token.

Mô hình có thể dừng sớm hơn nếu đã quyết định

rằng nó đã hoàn thành suy nghĩ của mình,

và nó tự tạo ra mã thông báo kết thúc chuỗi.

Vì vậy, đây là độ dài tối đa có thể.

Điều đó không có nghĩa là chuỗi đầu ra sẽ dài như vậy.

Vâng, và sau đó chúng tôi chỉ muốn quay lại một chuỗi.

Làm mẫu này bạn đã thấy trước đây.

Điều này sẽ kích hoạt mô hình để chọn theo xác suất

không chỉ là mã thông báo lớn nhất hoặc mã thông báo

với logit cao nhất,

nhưng có lẽ nằm trong số đó.

Ở đây chúng ta có trường hợp trên cùng,

vì vậy chúng tôi sẽ chỉ chọn trong số 50 nhật ký hàng đầu.

Và đây là đỉnh P,

chúng tôi sẽ chỉ chọn trong số bộ sưu tập

số mã thông báo cùng nhau mang lại xác suất 95%.

Như tôi đã đề cập trong các slide,

bạn không nhất thiết phải bao gồm

tất cả những đầu vào này.

Mình ít dùng 2 cái này.

Tôi chỉ đưa chúng vào đây để bạn có ý tưởng

về một số tùy chọn này là gì.

Được rồi, bạn vẫn sẽ nhận được một số thông báo cảnh báo khác.

Điều đó khá phổ biến với phương thức generate,

nhưng đừng lo lắng về điều đó.

Được rồi, vậy ở đây chúng ta có được tất cả các chuỗi được tạo ra.

Bạn có thể thấy rằng chúng tôi vẫn nhận được khá nhiều

của các mã thông báo đệm.

Và điều này về cơ bản có nghĩa là mô hình

đã ngừng tạo văn bản vào thời điểm này.

Vì vậy người mẫu nói, được rồi, tôi đã tạo đủ văn bản ở đây

và không có gì khác sẽ cực kỳ thú vị.

Được rồi, bây giờ bạn đã biết phương pháp này rồi,

tokenizer.decode, nó hoạt động khi bạn có

một danh sách các token.

Nếu bạn có nhiều danh sách và thực tế chúng ta có thể xem xét

kích thước của cái này.

Vì vậy, đầu ra, đầu ra.shape,

bạn có thể thấy nó là 3 x 66.

Vậy ba tương ứng với ba dãy

mà chúng tôi đã nhập và 66 tương ứng

đến độ dài tối đa mà tôi đã chỉ định ở đây.

Được rồi, khi bạn gặp tình huống như thế này,

thì bạn có thể sử dụng giải mã hàng loạt vì đây là hàng loạt.

Tôi đang chọn bỏ qua các token đặc biệt

chỉ để về cơ bản chúng ta chỉ có được văn bản bình thường.

Điều này phù hợp với những tình huống như thế này,

nơi bạn có một loạt mã thông báo kết thúc chuỗi.

Được rồi, tôi đang in ra những gì chúng ta sẽ nhận được.

Một lần nữa, đây là văn bản mà tôi đã nhập.

Mọi gia đình hạnh phúc đều giống nhau.

Và sau đó, đây là những gì GPT đã tạo ra.

Ông nói, khi đứa trẻ lớn lên cũng vậy,

nếu điều này xảy ra, nó sẽ hủy diệt tất cả chúng ta.

Điều đó rất tối.

Bây giờ, đây không phải là 66 token.

Đây là ít hơn 66 mã thông báo.

Tất cả các mã thông báo sau mã thông báo này đều ở cuối chuỗi.

Điều đó tương ứng với tất cả 5.256 mã thông báo giá trị ở đây.

Được rồi, và sau đó, tôi sẽ cho bạn đọc những thứ này.

Tôi thấy nó buồn cười.

Như tôi đã đề cập trước đó, tôi thực sự thích kết quả đầu ra của GPT-2 hơn so với sản phẩm thương mại hiện đại.

có sẵn CHAT GPT.

CHAT GPT hữu ích hơn, nhiều thông tin hơn, nhưng tôi nghĩ GPT-2 mới là thứ kích thích tư duy nhất

đầu ra của mô hình.

Được rồi, như tôi đã đề cập, nếu tất cả những gì bạn muốn làm là tạo ra một số kết quả đầu ra thì bạn thực sự không

quan tâm quá nhiều đến việc kiểm soát tối đa bản chất của đầu ra, thì đây là

tuyệt vời.

Bạn chỉ cần nhập danh sách mã thông báo và bạn sẽ nhận được một loạt kết quả đầu ra.

Bạn sẽ nhận được thông báo cảnh báo giống như thế này.

Bạn không cần phải lo lắng về họ.

Đây là những cảnh báo.

Đây không phải là lỗi và chúng hoàn toàn ổn.

Tôi hy vọng bạn thấy bản demo đó hữu ích.

Tôi chỉ muốn nhắc lại điều tôi đã nói ở đầu bài giảng này, đó là

là cú pháp chính xác và tên biến khác nhau giữa các mô hình khác nhau.

Vì vậy, hãy cố gắng đừng ghi nhớ một chút mã mà thay vào đó hãy làm quen với việc khám phá các đầu vào

vào các mã thông báo và lệnh gọi tạo mô hình này.