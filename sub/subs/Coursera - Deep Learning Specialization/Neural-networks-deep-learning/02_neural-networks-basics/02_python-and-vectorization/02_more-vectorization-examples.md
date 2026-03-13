# 02 ví dụ khác về vector hóa

---

Trong video trước bạn đã thấy một vài

ví dụ về cách vector hóa,

bằng cách sử dụng các hàm dựng sẵn và

bằng cách tránh rõ ràng cho

vòng lặp, cho phép bạn tăng tốc

tăng mã của bạn một cách đáng kể.

Hãy xem xét thêm một vài ví dụ.

Nguyên tắc cần nhớ là khi

bạn đang lập trình mạng lưới thần kinh của mình, hoặc

khi bạn đang lập trình chỉ là một phép hồi quy,

bất cứ khi nào có thể tránh

vòng lặp for rõ ràng.

Và không phải lúc nào cũng có thể không bao giờ

sử dụng vòng lặp for, nhưng khi bạn có thể

sử dụng chức năng tích hợp hoặc tìm một số

cách khác để tính toán bất cứ điều gì bạn cần,

bạn sẽ thường đi nhanh hơn nếu

bạn có một vòng lặp for rõ ràng.

Hãy xem một ví dụ khác.

Nếu bạn muốn tính toán một vectơ

u là tích của ma trận A,

và một vectơ v khác,

sau đó định nghĩa của ma trận của chúng tôi

nhân lên thì Ui của bạn là

bằng tổng trên j,, Aij, Vj.

Đó là cách bạn xác định Ui.

Và thế là

việc thực hiện không vector hóa này

sẽ là đặt u bằng NP.zeros,

nó sẽ là n x 1.

Đối với tôi, v.v.

Đối với j, v.v..

Và sau đó u[i] cộng bằng

a[i][j] lần v[j].

Bây giờ đây là hai vòng lặp for,

lặp qua cả i và j.

Vì vậy, đó là phiên bản không được vector hóa,

việc thực hiện vector hóa

nghĩa là u bằng np chấm (A,v).

Và việc thực hiện ở bên phải,

phiên bản vector hóa,

bây giờ loại bỏ hai vòng lặp for khác nhau,

và nó sẽ nhanh hơn nhiều.

Chúng ta hãy đi qua một ví dụ nữa.

Giả sử bạn đã có một vectơ,

v, trong ký ức và em

muốn áp dụng phép toán hàm mũ

trên mọi phần tử của vectơ này v.

Vì vậy bạn có thể đặt u bằng vectơ,

đó là e đến v1,

e đến v2, v.v.,

xuống e tới vn.

Vậy đây sẽ là

một triển khai không được vector hóa,

đó là lúc đầu bạn khởi tạo

u theo vectơ số không.

Và sau đó bạn có một vòng lặp for

tính toán từng phần tử một.

Nhưng hóa ra Python và NumPy

có nhiều chức năng tích hợp cho phép

bạn có thể tính toán các vectơ này chỉ bằng

một cuộc gọi đến một chức năng duy nhất.

Vậy tôi sẽ làm gì để

thực hiện điều này là nhập khẩu

numpy như np, và sau đó bạn

chỉ cần gọi u = np.exp(v).

Và vì vậy, hãy lưu ý rằng, trong khi trước đó

bạn đã có vòng lặp for rõ ràng đó,

chỉ với một dòng mã ở đây, chỉ cần v

là vectơ đầu vào u là vectơ đầu ra,

bạn đã thoát khỏi sự rõ ràng

vòng lặp for và việc triển khai trên

bên phải sẽ nhanh hơn nhiều

cái cần một vòng lặp for rõ ràng.

Trên thực tế, thư viện NumPy có rất nhiều

của các hàm giá trị vectơ.

Vậy np.log(v) sẽ tính

nhật ký theo yếu tố,

np.abs tính giá trị tuyệt đối,

np.maximum tính toán

mức tối đa theo phần tử

để tận dụng tối đa mọi thứ

phần tử của v bằng 0.

v**2 chỉ lấy yếu tố khôn ngoan

bình phương mỗi phần tử của v.

Một trên v lấy nghịch đảo theo phần tử,

và vân vân.

Vì vậy, bất cứ khi nào bạn muốn viết

hãy thử vòng lặp for và xem liệu có

một cách để gọi hàm tích hợp NumPy

để làm điều đó mà không cần vòng lặp for đó.

Vì vậy, chúng ta hãy học hỏi tất cả những điều này và

áp dụng nó vào hồi quy logistic của chúng tôi

thực hiện giảm độ dốc,

và xem liệu ít nhất chúng ta có thể thoát khỏi

của một trong hai vòng lặp for mà chúng tôi có.

Vì vậy đây là mã của chúng tôi cho

tính toán các dẫn xuất cho logistic

hồi quy và chúng tôi có hai vòng lặp for.

Một là cái này ở trên này, và

cái thứ hai là cái này.

Vì vậy, trong ví dụ của chúng ta, chúng ta có nx bằng 2, nhưng

nếu bạn có nhiều tính năng hơn

chỉ cần 2 tính năng thì bạn sẽ

cần có vòng lặp for trên dw1,

dw2, dw3, v.v.

Vì vậy, nó như thể thực sự có

a 4j bằng 1, 2 và x.

dWj được cập nhật.

Vì vậy chúng tôi muốn loại bỏ

vòng lặp for thứ hai này.

Đó là những gì chúng ta sẽ làm trên slide này.

Vì vậy, cách chúng ta sẽ làm như vậy

đó là thay vì rõ ràng

khởi tạo dw1, dw2, v.v. thành số không,

chúng ta sẽ loại bỏ điều này và

thay vào đó hãy biến dw thành một vectơ.

Vì vậy, chúng ta sẽ đặt dw bằng np.zeros,

và

hãy biến cái này thành nx x 1,

vectơ chiều.

Sau đó, ở đây, thay vì cái này cho

lặp qua các thành phần riêng lẻ,

chúng ta sẽ chỉ sử dụng cái này

hoạt động giá trị vector,

dw cộng bằng xi nhân dz(i).

Và cuối cùng, thay vì thế này,

chúng ta sẽ chỉ có dw chia bằng m.

Vì vậy bây giờ chúng ta đã chấm dứt việc có hai

vòng lặp for thành chỉ một vòng lặp for.

Chúng tôi vẫn có vòng lặp for này

qua các ví dụ đào tạo cá nhân.

Vì vậy tôi hy vọng video này mang lại cho bạn

một cảm giác vector hóa.

Và bằng cách loại bỏ một vòng lặp for

mã của bạn sẽ chạy nhanh hơn.

Nhưng hóa ra chúng ta còn có thể làm tốt hơn nữa.

Vì vậy, video tiếp theo sẽ nói về cách

để vector hóa sự xâm lược hậu cần thậm chí

hơn nữa.

Và bạn thấy một kết quả khá đáng ngạc nhiên,

mà không cần sử dụng bất kỳ vòng lặp for nào,

không cần vòng lặp for

qua các ví dụ đào tạo,

bạn có thể viết mã để xử lý

toàn bộ tập huấn luyện.

Vì vậy, khá nhiều tất cả cùng một lúc.

Vì vậy, hãy xem điều đó trong video tiếp theo.