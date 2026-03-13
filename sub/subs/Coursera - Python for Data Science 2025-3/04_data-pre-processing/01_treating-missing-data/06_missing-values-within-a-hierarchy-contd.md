# 06 giá trị thiếu trong một hệ thống phân cấp tiếp theo

---

Chào mừng trở lại.

Chúng ta sẽ tiếp tục nơi chúng ta đã rời đi

tắt ở video trước.

Bây giờ chúng ta hãy làm nhanh việc khác

kiểm tra các giá trị còn thiếu.

Bây giờ chúng ta thấy rằng có 128

các hàng có giá trị bị thiếu.

Đây là số hàng đó, được chứ?

Chúng tôi vừa in chúng ra đây để hiển thị

bạn rằng nếu bạn có khả năng làm điều đó,

bạn có thể đi và kiểm tra điều này bằng tay.

Ở đây không khả thi lắm, nhưng

nó có thể hoạt động trong một số trường hợp nhỏ hơn, được chứ?

Và chỉ để nhắc nhở bản thân,

dữ liệu bị thiếu bây giờ trông như thế này.

Được rồi, chúng tôi chưa thực sự

đã thay đổi bất cứ điều gì ở đây.

Chúng tôi chưa thay thế bất kỳ giá trị còn thiếu nào,

chúng tôi chỉ giải quyết được sự mơ hồ

vấn đề với chất lỏng, được chứ?

Bây giờ chúng ta hãy làm việc ở cột ngành nhé?

Và đây là logic, hãy làm theo

cẩn thận vì chúng tôi sẽ sử dụng chính xác

cùng một logic và

cho các cột còn lại.

Chúng tôi tạo ra một danh sách các lĩnh vực khác nhau.

Trong trường hợp của chúng tôi, có ba.

Sau đó chúng ta sẽ tạo một từ điển cho

từng lĩnh vực và

tất cả các danh mục đi kèm

thuộc lĩnh vực đó, được chứ?

Tên ngành sẽ là khóa và danh sách

của các danh mục sẽ là giá trị, được chứ?

Cặp giá trị chính, đó là một từ điển.

Chúng ta sẽ tạo từ điển đó.

Sau đó chúng ta sẽ viết một hàm

ánh xạ khu vực này sang danh mục khác.

Chúng tôi sẽ tìm thấy một hàng nếu thiếu khu vực,

chúng tôi sẽ kiểm tra những gì

thể loại nằm trong đó,

hàng đó thuộc loại nào, được chứ?

Và sau đó tra cứu nó trong từ điển này,

được không?

Nếu đây là thể loại,

lĩnh vực này nên là gì, được chứ?

Từ điển này sẽ phục vụ như

một loại tra cứu hoặc một tài liệu tham khảo cho

chúng tôi và chúng tôi sẽ thay thế nó bằng

lĩnh vực cụ thể đó.

Và chúng ta sẽ gọi chức năng này là chúng ta

sẽ viết bằng phương pháp áp dụng, được chứ?

Vì vậy, chúng ta hãy làm điều này từng bước một.

Đầu tiên, tạo một danh sách các lĩnh vực,

khá đơn giản, được chứ?

Một cách để làm điều đó, có những cách khác.

Những gì tôi đã làm là tôi đã lấy cái này và

Tôi đã tính giá trị.

Cũng như để thuận tiện, bất cứ nơi nào

nó in ra danh sách các giá trị duy nhất,

Tôi đã lấy chỉ số đếm giá trị.

Remember, when you do value counts,

bạn nhận được chỉ mục này.

Đây là chỉ số,

đây là những giá trị, được chứ?

Bạn nhận được chỉ mục và

Tôi biến chỉ mục đó thành một danh sách.

Tôi cũng thiết lập một từ điển trống

được gọi là từ điển danh mục ngành.

Bây giờ hãy điền vào từ điển đó.

Vì vậy đây là những gì chúng ta sẽ làm.

Chúng tôi sẽ lấy từng cái

giá trị trong danh sách ngành,

tra cứu tương ứng

hãy tra từ điển vào, được chứ?

Và bất cứ nơi nào khu vực đều bình đẳng

với giá trị cụ thể đó,

chúng tôi sẽ lấy

danh mục tương ứng, được chứ?

Vì vậy những gì chúng tôi làm chỉ là

thủ thuật chúng tôi đã làm ở đây,

giá trị thực sự được tính

không có ý nghĩa gì cả

Một số cách để lấy chỉ mục,

được rồi, thuộc thể loại.

Danh sách tất cả các mục duy nhất trong danh mục,

số lượng giá trị sẽ hoàn thành công việc.

Một số phương pháp khác cũng vậy, nhưng

đây là một cách để làm điều đó

Vì vậy tôi đang đếm giá trị,

Tôi không quan tâm đến số lượng giá trị.

Điều tôi quan tâm là

chỉ số của kết quả đó.

Tôi sẽ lấy chỉ mục đó,

biến nó thành một danh sách.

Và danh sách đó sẽ là giá trị

tương ứng với khóa,

lĩnh vực đó là gì được không?

Hãy để tôi in ra danh sách ngành,

được không?

In, viết hoa, được chứ?

Đây là tất cả các lĩnh vực khác nhau.

Vì thế tôi sẽ đi và nhìn lên,

trong từ điển tôi sắp tạo

một mục dành cho việc chăm sóc vải quan trọng.

Và đối với chiếc chìa khóa đó,

Tôi sẽ chọn mọi hạng mục ở đâu

lĩnh vực là chăm sóc vải, được chứ?

Đó thực chất là những gì chúng tôi đang làm ở đây.

Và đây chính là điều đặc biệt

từ điển trông như thế nào, được chứ?

Giá trị khóa, giá trị khóa, giá trị khóa.

Key là tên ngành, value là danh sách

của các danh mục thuộc lĩnh vực đó.

Bây giờ hãy xác định hàm

chúng ta đã nói chuyện, được chứ?

Vì vậy điều chúng tôi làm là, chúng tôi muốn chọn

lĩnh vực chính xác dựa trên giá trị

của danh mục khi thiếu ngành, được chứ?

Vì vậy tôi sẽ gọi đây là một lĩnh vực

category map, this is essentially a map.

Tôi đang tìm kiếm một lĩnh vực

dựa trên một thể loại.

Những gì chúng ta làm là,

nếu khu vực này trống, được không?

Tôi sẽ đi từng hàng một.

So I define a function

có đầu vào là một hàng, cho

hàng cụ thể đó nếu

khu vực cột trống.

Nếu PD là NA thì được chứ?

Nếu PD là NA sẽ trả về giá trị đúng hoặc sai.

Vậy điều gì ở dưới nếu sẽ xảy ra,

nếu điều này trả về một sự thật.

Vì vậy, nếu khu vực này trống,

nếu không phải PD là loại NA,

nếu danh mục không rỗng, được không?

Nếu chúng ta biết danh mục,

thì điều chúng ta có thể làm là trong từ điển này,

được không?

Nếu danh mục có trong từ điển,

chúng ta trả về giá trị cụ thể đó, được chứ?

Đây là điều chúng ta đang làm ở đây, được chứ?

Và nếu điều này là sai,

nếu cái này không bị thiếu, nếu nó có sẵn,

chúng tôi không làm gì cả

Chúng tôi chỉ trả về giá trị hiện có.

Vì vậy, đây là những gì chúng tôi đang làm ở đây.

Hãy để tôi chạy cái này, cho bạn một phút để

hãy để điều này thấm vào vì đây chính xác là

chúng ta sẽ làm gì

các tính năng còn lại, được chứ?

Khi chúng ta đã viết xong hàm này,

hãy áp dụng nó vào khung dữ liệu và

kiểm tra các giá trị còn thiếu.

Chúng tôi đã sắp xếp khu vực ngoại trừ

ba, được chứ?

Trước đây chúng tôi có 50 giá trị bị thiếu,

chúng ta đã giải quyết được 47 vấn đề rồi, được chứ?

Tại sao vậy?

bởi vì trong những trường hợp này,

danh mục cũng bị thiếu.

Vậy cách tiếp cận của chúng tôi không hiệu quả,

chúng ta sẽ nói đến điều đó sau.