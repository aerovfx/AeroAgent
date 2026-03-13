# 02 xác nhận-thông tin khách hàng

---

Vì vậy, bây giờ bước tiếp theo chúng ta sẽ làm là xác thực toàn bộ trang.

Bây giờ tại sao phải xác nhận nó?

Ví dụ: bây giờ, giả sử nếu đây là dữ liệu của bạn thì tôi đang thực thi mã này và tôi

thay vì Tracy thì mình chỉ viết Tracy123 thì có đúng tên không?

Không.

Vì vậy, có lẽ mọi người có thể sử dụng tên hoặc bất kỳ thứ gì khác.

Vì vậy, chúng ta cần xác thực nó để nó chỉ chấp nhận lượng dữ liệu cụ thể đó

với chúng tôi.

Vì vậy, để xác thực chúng, được rồi, điều chúng ta sẽ làm ở đây là, điều đầu tiên

bước.

Chúng tôi đã lấy tên khách hàng, phải không?

Vì vậy, sau khi lấy tên của khách hàng, chúng ta sẽ sử dụng biểu thức chính quy trong

để phù hợp với điều này.

Vì vậy, để thêm biểu thức chính quy vào mã, chúng ta phải nhập re.

Đây là viết tắt của biểu thức thông thường.

Bây giờ điều bạn cần làm là, nếu lại, đó là biểu thức chính quy khớp dấu chấm, vì vậy chúng tôi đang sử dụng

hàm khớp trong đó chúng ta phải lấy tham số kiểu chuỗi.

Vì vậy, điều chúng ta sắp làm ở đây là, chúng ta sẽ lấy một tham số, giả sử tôi đang nói

rằng tôi cần các tên từ dấu gạch ngang z đến dấu gạch ngang z, đó là chữ A viết hoa đến chữ a nhỏ, nghĩa là trong

cái này và đô la.

Vì vậy, đây là mẫu nhập tên của tôi và mẫu này sẽ được áp dụng cho tên khách hàng.

Vì vậy, nếu mẫu cụ thể này phù hợp với tiêu chí, chẳng hạn, tôi sẽ nói rằng nếu

tên khách hàng của tôi trùng khớp, sau đó chỉ chấp nhận số liên lạc, loại căn hộ và số tiền,

nếu không thì không chấp nhận dữ liệu này.

Vì vậy, chúng ta chỉ cần chuyển bước này lên trước một bước, được rồi, tiến lên một tab.

Vì vậy, bây giờ giả sử, nếu điều này không phù hợp với tiêu chí thì điều gì sẽ xảy ra?

Vì vậy, giả sử nếu chúng tôi lấy tên là Tracy123 thì nó sẽ không hỏi tôi bất kỳ dữ liệu nào khác,

phải không?

Nó có hỏi dữ liệu nào khác không?

Không, vì họ nói Tracy123 không phải số chính xác.

Vì vậy, những gì chúng ta có thể làm là sau đó, chúng ta có thể đặt một điều kiện khác.

Vì vậy, như thế này, nếu ở đây, nó kết thúc ở đây, vì vậy chúng ta chỉ cần đề cập đến else print

vui lòng nhập tên hợp lệ.

Bây giờ nếu tôi thực thi đoạn mã này, được rồi, xin lỗi, chúng ta sẽ có một Elif ở đây, phải không?

Vì vậy, cái này sẽ đến đây và cái này sẽ tiến một bước vào bên trong.

Bây giờ nếu tôi thực thi đoạn mã này và tôi nói, giả sử Tracy123, nó sẽ báo lỗi cho tôi

nhập tên hợp lệ và tiếp tục bước phía trước, phải không?

Vì vậy, đây là cách đầu tiên, đó là nhập xác thực chính xác cho tên khách hàng.

Lấy tên khách hàng đó xong chúng ta mới lấy số liên lạc phải không?

Vì vậy, giả sử nếu dữ liệu cụ thể này hoạt động thành công, bạn có thể cân nhắc rằng

nếu dữ liệu của tôi được nhập thành công thì nó sẽ yêu cầu số liên lạc.

Vì vậy, bây giờ bước tiếp theo những gì chúng ta cần làm là xác thực số liên lạc của mình.

Vì vậy, chúng tôi sẽ nói với số liên lạc là if re.match, re.match và chúng tôi sẽ làm gì

để khớp là, chúng ta sẽ nói rằng chữ số đầu tiên phải là 7, 8 hoặc 9, chữ số đầu tiên

phải là 7, 8 hoặc 9 và gạch chéo d cho một chữ số và sau đó chúng ta cần số có 9 chữ số.

Vì vậy, đây là những gì xác nhận trên số liên lạc.

Vì vậy, nếu việc xác thực này thành công thì hãy chấp nhận loại căn hộ, số lượng và tất cả những thứ khác

chi tiết.

Nếu nó không chấp nhận dữ liệu đó thì được, điều đó có nghĩa là nếu số liên lạc không có 10 chữ số

hoặc bất kỳ thứ gì khác, sau đó bạn có thể đặt một cái khác, cái đó ở đằng này, nếu không thì in, nhập

Số liên lạc 10 chữ số.

Vì vậy, giả sử nếu bây giờ tôi thực thi mã này và nói 1, tên là Tracy và có thể nếu tôi

lấy số liên lạc 1, 2, 3, 3 chữ số, nó bảo tôi nhập số liên lạc gồm 10 chữ số thích hợp,

phải không?

Vì vậy, điều đó có nghĩa là việc xác thực cụ thể này cũng đang hoạt động thành công.

Hoặc nếu tôi thử lại như Tracy và tôi lấy đúng 10 chữ số thì nó sẽ yêu cầu căn hộ

loại.

Vì vậy, điều đó có nghĩa là việc xác thực cụ thể này cũng đang hoạt động.

Vì vậy, bằng cách sử dụng biểu thức chính quy, tôi có thể nhập rất nhiều xác thực cho nó.

Được rồi.

Vì vậy, tôi vừa xác nhận ngay bây giờ, tên khách hàng và số liên lạc.

Được rồi.

Vì vậy, việc xác thực tiếp theo mà chúng tôi sẽ thực hiện là dành cho loại phẳng.

Được rồi.

Bây giờ, để xác thực loại phẳng của bạn, điều chúng ta sẽ làm ở đây là, bây giờ

vấn đề là bất cứ khi nào chúng ta sử dụng một biểu thức chính quy, nó chỉ thu được một kiểu chuỗi

của dữ liệu.

Nó sẽ không cho phép bạn lấy bất kỳ định dạng dữ liệu số nguyên nào.

Ví dụ: nếu tôi đang sử dụng loại phẳng này và tôi đang thử lại loại đó sau khi lấy

loại phẳng, nếu khớp lại và đối với loại phẳng, điều tôi muốn là, chúng chỉ có loại phẳng từ

1 đến 4 BHK phải không?

Vì vậy, tôi sẽ chỉ lấy lượng dữ liệu đó.

Vì vậy, tôi đang nói ở đây rằng sẽ có từ 1 đến 4 số.

Được rồi.

Vì vậy, từ 1 đến 4 và áp dụng trên loại phẳng.

Vì vậy, nếu điều này khớp thành công, thì bạn đi lấy số tiền và phần còn lại là dữ liệu.

Và nếu không, thì loại in phẳng khác phải nằm trong khoảng từ 1 đến 4.

Được rồi.

Bây giờ hãy chạy mã này.

Vì vậy, giả sử nếu tôi nhập 1 Tracy và tôi lấy loại phẳng là 5.

Bây giờ hãy xem, ở đây, chúng ta gặp lỗi adi.match thuộc loại phẳng, trả về mẫu biên dịch flag.match

chuỗi.

Vì vậy, ở đây, chúng ta cần một loại dữ liệu phải là chuỗi chứ không phải là số nguyên.

Được rồi.

Nó chỉ nên là chuỗi, không phải bất kỳ số nguyên nào.

Vì vậy, tôi phải loại bỏ số nguyên này khỏi đây.

Bây giờ, nếu tôi xóa số nguyên này khỏi đây và giả sử nếu tôi thực thi mã, Tracy

và tôi lấy loại phẳng là 5, hiện tại nó đang hoạt động thành công.

Nhưng có một vấn đề nảy sinh đối với chúng tôi.

Giả sử nếu tôi nhập dữ liệu từ 1 đến 4 thì đó là 2BHK, được rồi, chúng ta vẫn nhận được

điều tương tự đó là nhập kiểu phẳng từ 1 đến 4, phải không?

Vì vậy, giả sử chúng ta có mẫu từ 1 đến 4, được rồi, chúng ta có thêm một dấu gạch ngang ở đây.

Bây giờ, hãy dừng và chạy lại và tôi sẽ nhập Tracy và tôi cho kiểu phẳng là 2.

Bây giờ tôi đã nhận được số tiền rồi phải không?

Vấn đề là khi tôi chấp nhận số tiền, bây giờ nó báo cho bạn biết số tiền môi giới là

không được xác định.

Nhưng số tiền môi giới đang được xác định ngay tại đây.

Vậy thì tại sao nó lại báo lỗi rằng số tiền môi giới không được xác định?

Vì mỗi lần mình lấy kiểu phẳng thì lúc đó mình lấy kiểu số nguyên phải không?

Nhưng do nếu tôi phải áp dụng xác thực cho nó, tôi cần rằng giá trị này không phải là số nguyên

bây giờ.

Vì vậy, nó ở định dạng chuỗi.

Vì vậy, điều tôi sắp làm ở đây là tôi sẽ đưa dạng dữ liệu này thành một kiểu chuỗi

của dữ liệu.

Bây giờ, tôi sẽ lấy loại dữ liệu này làm loại dữ liệu chuỗi.

Và bây giờ nếu tôi chạy mã này, giả sử tôi sẽ thêm toàn bộ chi tiết chính xác, giống như

Tracy số 9876543210, loại phẳng là 2 và.

Bây giờ, bạn có thể thấy chi tiết khách hàng đã được thêm thành công và tất cả các chi tiết mà chúng tôi

đã viết thư cho Tracy, số liên lạc, loại căn hộ đã hiển thị thành công với chúng ta phải không?

Vì vậy, điều đó có nghĩa là tất cả quá trình xác thực này hiện đang hoạt động thành công.

Đó là xác thực tên khách hàng mà chúng tôi đã sử dụng A gạch ngang Z và A gạch ngang Z, có nghĩa là

chỉ cho phép bảng chữ cái.

Đối với số liên lạc, chúng tôi đã nói rằng số bắt đầu phải nằm trong khoảng từ 7, 8 hoặc 9 và còn lại

là số có 9 chữ số

Vậy 9 và 1 có 10 chữ số

Loại phẳng chúng ta muốn lấy nằm trong khoảng từ 1 đến 4, nếu lớn hơn 1 đến 4 thì không thể

chấp nhận.

Bây giờ, vì số tiền được ghi vào float, nên nếu có cách nào chúng ta cố gắng nhập bất kỳ cách nào khác

loại dữ liệu thay vì float, nó sẽ báo lỗi cho tôi, phải không?

Và sau đó dựa trên số tiền này sẽ lấy loại căn hộ và đưa ra số tiền môi giới

và thêm chi tiết này vào danh sách khách hàng, được chứ?

Vì vậy, đây là một ví dụ về cách viết biểu thức chính quy và xác thực dữ liệu của chúng tôi bằng Python

kịch bản.