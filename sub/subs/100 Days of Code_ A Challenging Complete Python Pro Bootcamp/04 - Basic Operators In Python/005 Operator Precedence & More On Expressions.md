# 005 Độ ưu tiên của toán tử và thông tin khác về biểu thức

---

Xin chào tất cả mọi người.

Chào mừng trở lại.

Chúng ta hãy tiếp tục bài học này với độ ưu tiên của toán tử và tính kết hợp.

Khi các toán tử khác nhau xuất hiện trong cùng một biểu thức.

Áp dụng các quy tắc số học thông thường.

Tất cả các toán tử Python đều có quyền ưu tiên và tính kết hợp.

Ưu tiên nghĩa là gì?

Khi một biểu thức chứa hai loại toán tử khác nhau thì nên áp dụng trước.

Vì vậy, đó không là gì ngoài sự ưu tiên.

Vậy thì tính kết hợp có nghĩa là gì?

Khi một biểu thức chứa hai toán tử có cùng mức độ ưu tiên.

Vì cái gì.

Người vận hành.

Các hoạt động nên được áp dụng đầu tiên.

Ví dụ, trong số học thông thường, phép nhân và phép chia trong Python bằng nhau.

Tổng thống.

Và hoặc được thực hiện trước phép cộng và phép trừ.

Nhưng khi.

Biểu thức bao gồm phép nhân và phép chia.

Chúng sẽ được ưu tiên như nhau và được đánh giá từ trái sang phải.

Ví dụ.

Nếu bạn xem xét biểu thức.

Hai cộng.

Ba nhân bốn.

Được xét xử bởi.

Nhưng phép nhân và phép chia.

Có cùng mức độ ưu tiên khi chúng có cùng mức độ ưu tiên.

Họ được đánh giá từ trái sang phải.

Vì vậy, ba thành bốn sẽ được đánh giá đầu tiên và kết quả sẽ được chia cho hai.

Vậy ba chia bốn chẳng là gì ngoài 12.

12 chia cho hai chẳng là gì ngoài sáu.

Sáu cộng hai chỉ là tám.

Chúng ta hãy xem kết quả.

Vì vậy, chúng tôi có tám mẹo tiếp theo trong biểu thức.

Dấu ngoặc đơn xuất hiện thì dấu ngoặc đơn sẽ được ưu tiên cao nhất so với bất kỳ toán tử nào khác.

Có nghĩa là biểu thức bên trong dấu ngoặc đơn diễn ra trước tiên.

Ví dụ.

Hai cộng ba.

Nhân với bốn.

Vì vậy, ở đây biểu thức trong dấu ngoặc đơn được đánh giá trước tiên, bất kể nó có thể là gì và sau đó là kết quả

sẽ được nhân với bốn.

Hãy để chúng tôi in cái này.

Vậy chúng ta có câu trả lời là 22 cộng ba không bằng năm.

Năm chia bốn chẳng là gì ngoài 20.

Các toán tử nhân như thế nào.

Các toán tử nhân, chia, chia sàn và mô đun có mức độ ưu tiên ngang nhau,

và các toán tử cộng, như phép cộng và phép trừ nhị phân, có độ ưu tiên như nhau với mỗi toán tử

khác.

Các toán tử nhân được ưu tiên hơn các toán tử cộng.

Cuối cùng chúng ta có thể nói rằng giống như trong số học tiêu chuẩn, một lập trình viên Python có thể sử dụng dấu ngoặc đơn để ghi đè

các quy tắc ưu tiên và phép cộng bắt buộc phải được thực hiện trước khi nhân.

Như chúng ta có thể thấy ở đây, nếu chúng ta không sử dụng dấu ngoặc đơn.

Và biểu thức cụ thể này thì phép nhân sẽ được ưu tiên trước, sau đó là phép cộng,

sau đó ba thành bốn sẽ được đánh giá trước, sau đó kết quả sẽ được cộng hai hai.

Nếu chúng ta đánh giá điều này.

Sự biểu lộ.

Chúng tôi nhận được kết quả khác là 14.

Ba ăn bốn chẳng là gì ngoài 12.

12 cộng hai chẳng là gì ngoài 14.

Nếu bạn muốn cộng hai cộng ba, hãy dùng dấu ngoặc đơn rồi nhân với bốn.

Vì vậy, ở đây.

Trong chiếc bàn nhỏ này.

Chúng ta có thể thấy các toán tử trong mỗi hàng.

Có mức độ ưu tiên cao hơn các toán tử bên dưới nó.

Các toán tử trong một hàng có cùng mức độ ưu tiên.

Vì vậy, nhị phân.

lũy thừa.

Và phép cộng và phép trừ có tính kết hợp đúng.

Phép nhân nhị phân Phép chia Phép chia Số nguyên.

Toán tử dấu phẩy động, phép chia và mô đun có tính kết hợp bên trái và phép cộng và trừ nhị phân.

Hoặc cũng có tính kết hợp bên trái, trong khi toán tử gán nhị phân có tính kết hợp bên phải.

Để xem cách hoạt động liên quan.

Hãy xem xét biểu thức to.

Trừ ba.

Trừ bốn.

Ở đây hai toán tử giống nhau.

Vì vậy chúng có quyền ưu tiên bằng nhau nghĩa là trừ và trừ.

Cách biểu thức này được đánh giá thông qua toán tử trừ đầu tiên được áp dụng trước biểu thức thứ hai.

Hoặc toán tử trừ thứ hai được áp dụng trước toán tử thứ nhất.

Vì vậy, phép cộng và phép trừ nhị phân.

Sẽ có mức độ ưu tiên như nhau và chúng được vận hành từ trái sang phải.

Khả năng kết hợp là từ trái nên hai trừ ba sẽ được đánh giá đầu tiên.

Và sau đó bốn sẽ bị trừ khỏi kết quả này.

Vậy hai trừ ba chẳng là gì ngoài trừ một và trừ một.

Trừ bốn không là gì ngoài trừ năm.

Hãy để chúng tôi chạy tế bào này và xem.

Vì vậy, kết quả mong đợi của chúng tôi là âm năm.

Vì vậy việc đánh giá sẽ diễn ra từ trái sang phải.

Chúng ta có thể tránh nhầm lẫn với dấu ngoặc đơn.

Bất cứ khi nào hoặc bất cứ nơi nào có thể.

Vì vậy biểu thức này cũng cho kết quả có cùng giá trị trừ 5.

Nhưng nếu người dùng muốn trừ bốn từ ba.

Sau đó.

Bạn cần phải làm vậy.

Anh ta cần sử dụng dấu ngoặc đơn?

Đối với phép trừ.

Ba trừ bốn.

Bây giờ chúng ta sẽ nhận được câu trả lời khác bởi vì.

Biểu thức trong ngoặc đơn sẽ được đánh giá trước và sau đó kết quả sẽ bị trừ hai.

Vậy ba trừ bốn chẳng là gì ngoài trừ một.

Và trừ của trừ trở thành cộng và hai cộng một trở thành ba.

Hãy để chúng tôi chạy tế bào này.

Một dòng.

Vậy kết quả là cộng ba.

Toán tử một ngôi có độ ưu tiên cao hơn toán tử nhị phân.

Như chúng ta có thể thấy trong bảng, phép cộng và phép trừ một ngôi có độ ưu tiên cao hơn phép cộng nhị phân

và phép trừ.

Và các toán tử đơn nguyên có tính kết hợp đúng.

Điều này có nghĩa là nếu chúng ta quan sát các câu nói như gió.

Trừ ba.

Và cộng thêm vào.

Các toán tử đơn nhất là đúng.

Phương tiện liên kết trong biểu thức này trừ đi ba được đưa ra.

Mức độ ưu tiên cao nhất và chúng được đánh giá từ đó.

Phải.

Đây.

Toán tử một ngôi trừ ba sẽ được xử lý như thế nào.

Điểm trừ của.

Ba.

Vì vậy hãy nhìn vào đây.

Cộng ba này được liên kết với dấu trừ.

Nhưng thực ra cộng ba là giá trị dương, gắn liền với ký hiệu âm.

Có nghĩa là dấu âm đơn nhất.

Do đó nó có tính kết hợp đúng đắn.

Vậy bây giờ cộng hai trừ ba sẽ có kết quả là trừ một.

Nhưng nếu bạn quan sát biểu hiện này.

Điểm trừ.

Ba cộng hai.

Sau đó chúng ta sẽ nhận được.

Hai cộng ba là năm rồi năm sẽ gắn liền với cái.

Đơn nhất.

Dấu âm.

Vậy kết quả là trừ năm.

Loại này.

Sự tiến hóa không gì khác hơn là một sự tiến hóa liên kết.

Vì vậy hãy chắc chắn rằng.

Bất cứ khi nào bạn có nghi ngờ về diễn biến của biểu thức, hãy sử dụng dấu ngoặc đơn.

Để đánh giá theo yêu cầu của bạn.

Vì vậy, nhiều dấu ngoặc đơn bạn sử dụng dễ dàng hơn.

Bạn có thể đánh giá biểu thức theo cách thủ công.

Và chúng tôi có thể giải thích.

Biểu thức toán học được viết bằng mã Python dễ dàng được người khác biết.

Bây giờ chúng ta hãy xem xét bài tập có chuỗi.

Toán tử gán là một loại toán tử khác với toán tử số học.

Các lập trình viên chỉ sử dụng toán tử gán để xây dựng các câu lệnh gán.

Python không cho phép toán tử gán là một phần của biểu thức lớn hơn hoặc một phần của biểu thức khác

tuyên bố.

Như vậy, các khái niệm về quyền ưu tiên và tính kết hợp không được áp dụng trong bối cảnh của nhiệm vụ

nhà điều hành.

Tuy nhiên, Python hỗ trợ một loại toán tử gán đặc biệt gọi là Chuỗi gán.

Ví dụ, ở đây w bằng.

X bằng Y bằng.

G.

Bằng không.

Trong biểu thức này, số không là.

Gán cho biến z, y, x và cuối cùng là W.

Vậy giá trị của biến ngoài cùng bên phải là Z bằng 0.

Sẽ được.

Gán cho các giá trị ở phía bên trái.

Vì vậy Z bằng 0 được coi là một biểu thức.

Hoặc một giá trị sau khi đánh giá.

Và giá trị này được gán cho các biến y, x và W còn lại.

Vì vậy, Z đầu tiên bằng 0 sẽ được đánh giá và kết quả sẽ như vậy.

Giao cho Y.

Sau đó.

Y bằng một giá trị nào đó sẽ được gán cho biến x.

Và X bằng một giá trị nào đó sẽ được gán cho.

Biến W.

Vì vậy, đây được gọi là nhiệm vụ chung.

Nếu bạn in.

W dấu phẩy x, dấu phẩy y, dấu phẩy.

G.

Bạn có thể thấy tất cả các giá trị.

Sáu không.

Loại nhiệm vụ chung này sẽ giúp ích.

Để khởi tạo một số biến thành giá trị ban đầu trong một câu lệnh.

Chúng ta sẽ thấy kiểu gán chuỗi này trong các lần lặp và vòng lặp.

Phương tiện trong báo cáo luồng điều khiển và trong.

Các vòng lặp.

Đối với vòng lặp.

Vòng lặp while.

Vân vân.

Bây giờ chúng ta hãy nói về.

Định dạng các biểu thức.

Định dạng là một kiểu thể hiện biểu thức hoặc phương trình toán học trong Python dưới dạng đại số

hoặc cách con người có thể đọc được.

Ví dụ.

Ba X cộng.

Đến một.

Trừ năm.

Để cho phép biểu thức này trong mã Python.

Chúng ta có thể sử dụng khái niệm đúng theo đại số của toán học.

Vì vậy, chúng ta có thể viết mã này theo nhiều cách khác nhau.

Nhưng chúng tôi sẽ hiển thị.

Điều đúng đắn để làm theo là gì?

Ví dụ: chúng ta có thể sử dụng ba.

Sao X có nghĩa là ba thành x cộng.

Hai thành Y trừ năm.

Vì vậy chúng ta có thể sử dụng định dạng này.

Hãy để chúng tôi sử dụng một định dạng khác như.

Ba.

SpaceX.

SpaceX X.

SpaceX Plus hai.

SpaceX.

Nhân lên trong khi SpaceX trừ SpaceX năm.

Vì vậy hãy nhìn vào đây.

Giữa giá trị và biến.

Ý nghĩa giữa hằng và biến.

Chúng tôi có không gian.

Các toán tử được phân tách bằng dấu cách.

Biểu thức này trông ngắn gọn hơn với con trăn.

Phong cách biểu hiện hơn là phong cách trước đó.

Giả sử nếu chúng ta.

Giảm khoảng trống sau đó.

Biểu hiện này trông như thế này.

Nó trông giống như x cộng hai.

Được nhân với ba.

Và y trừ pi được nhân với x cộng hai.

Nhưng thực tế thì không phải vậy.

Theo nghĩa đó.

Cho dù chúng ta có sử dụng không gian hay không.

Phép nhân sẽ diễn ra đầu tiên.

Nó tìm biến khác để nhân với biến bên trái.

Toán tử nhân này tìm biến bên trái.

Cho dù nó có thể là một biến hoặc biểu thức.

Ví dụ: nếu chúng ta sử dụng dấu ngoặc đơn ở đây.

Sau đó, toán tử nhân này.

Tìm biến hoặc biểu thức bên phải.

Bây giờ ở phía bên phải, phần trên không có gì khác ngoài một biểu thức thay vì chỉ là biến x.

Vì vậy, viết loại biểu thức này.

Không tốt trong Python, vì vậy hãy làm rõ nó bằng khoảng trắng.

Vậy bây giờ.

Chúng ta có thể thấy.

Ba.

Và rồi hai Y trừ năm.

Biểu thức đầu tiên này có vẻ ổn nhưng nó không phải là kiểu định dạng python.

Nó không có trong Python.

Kiểu định dạng biểu thức toán học.

Vì vậy, nếu chúng ta sử dụng loại biểu thức này, Python sẽ dành quyền ưu tiên thực thi các biểu thức

và nó sẽ không thay đổi quyền ưu tiên của toán tử.

Vì vậy, phép nhân sẽ diễn ra trước tiên từ trái sang phải rồi đến phép trừ.

Vì vậy, việc thêm không gian bằng trí thông minh sẽ có ý nghĩa trong toán học hoặc bất kỳ biểu thức mã nào khác.

Lại.

Chúng tôi đang lặp lại một lần nữa.

Khoảng cách không ảnh hưởng đến quyền ưu tiên của toán tử, nhưng định dạng này làm cho việc thêm vào có vẻ như

và phép trừ sẽ diễn ra trước phép nhân.

Về mặt tâm lý, việc thiếu không gian khiến cho dấu cộng và dấu trừ liên kết các toán hạng chặt chẽ hơn

hơn toán tử nhân.

Điều này không đúng.

Vì vậy, tuyên bố này dễ bị người đọc hiểu sai.

Do đó định dạng biểu thức toán học trong này.

Cách là đúng.

Giả định.

Nếu chúng ta muốn.

Thể hiện một cách toán học.

Trong ký hiệu đại số hơn, chúng ta có thể sử dụng dấu ngoặc đơn một cách đúng đắn.

Giống như ba.

Vào x có nghĩa là ba x.

Cộng hai, Y trừ năm.

Vì vậy, điều này trông rất đẹp.

Và nó.

Tuân theo ký hiệu đại số.

Vì vậy, cuối cùng chúng ta có thể gán cái này cho.

Kết quả.

Và điều này trở thành một con trăn có định dạng và phong cách hơn.

Biểu thức toán học trong ký hiệu đại số.

Vì vậy, bất cứ khi nào bạn có biểu thức con rất dài trong phương trình toán học, hãy sử dụng dấu ngoặc đơn để tránh

sự nhầm lẫn.

Và để có được kết quả theo yêu cầu của bạn.

Cảm ơn đã xem bài học này.

Chúng ta hãy gặp nhau trong bài học tiếp theo với các lỗi trong Python.

Tóm lại.

Cho đến lúc đó, hãy tận hưởng việc học.