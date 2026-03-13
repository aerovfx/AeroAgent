# 04 vectorizing-hậu cần-hồi quy-gradient-đầu ra

---

Trong video trước,

bạn đã thấy cách sử dụng vector hóa để tính toán các dự đoán của họ.

Chữ a thường dành cho toàn bộ tập huấn luyện cùng một lúc.

Trong video này, bạn sẽ thấy cách sử dụng vector hóa để

thực hiện tính toán gradient cho tất cả các mẫu huấn luyện M.

Một lần nữa, tất cả các loại cùng một lúc.

Và ở cuối video này,

chúng tôi sẽ kết hợp tất cả lại với nhau và chỉ ra cách bạn có thể rút ra

thực hiện hồi quy logistic rất hiệu quả.

Vì vậy, bạn có thể nhớ rằng để tính toán độ dốc,

điều chúng tôi đã làm là tính toán dz1 cho ví dụ đầu tiên,

có thể là a1 trừ y1 và sau đó dz2 bằng

a2 trừ y2, v.v.

Và cứ thế cho tất cả các ví dụ huấn luyện M.

Vì vậy, điều chúng ta sắp làm là xác định một biến mới,

dZ sẽ là dz1, dz2, dzm.

Một lần nữa, tất cả các biến z chữ D viết thường được xếp chồng lên nhau theo chiều ngang.

Vì vậy, đây sẽ là ma trận 1 x m hoặc cách khác là vectơ hàng m chiều.

Bây giờ hãy nhớ lại điều đó từ slide trước,

chúng ta đã tìm ra cách tính chữ A viết hoa như thế này: a1 đến

am và chúng tôi đã xác định chữ Y viết hoa là y1 đến ym.

Ngoài ra bạn biết đấy, xếp chồng lên nhau theo chiều ngang.

Vì vậy, dựa trên những định nghĩa này,

có lẽ bạn có thể tự mình thấy rằng dz có thể được tính là

chỉ A trừ Y vì nó sẽ bằng a1 - y1.

Vì vậy, phần tử đầu tiên, a2 - y2,

vì vậy trong phần tử thứ hai, v.v.

Và, phần tử đầu tiên a1 - y1 này chính xác là định nghĩa của dz1.

Phần tử thứ hai chính xác là định nghĩa của dz2, v.v.

Vì vậy, chỉ với một dòng mã,

bạn có thể tính toán tất cả những điều này cùng một lúc.

Bây giờ, trong lần triển khai trước,

chúng tôi đã loại bỏ một vòng lặp for rồi nhưng chúng tôi vẫn còn

ví dụ huấn luyện vòng lặp for thứ hai này.

Vì vậy, chúng ta khởi tạo dw bằng 0 thành một vectơ số 0.

Nhưng sau đó chúng ta vẫn phải lặp lại hơn 20 ví dụ mà chúng ta có

dw cộng bằng x1 nhân dz1,

đối với ví dụ huấn luyện đầu tiên dw cộng bằng x2 dz2, v.v.

Vậy chúng ta thực hiện M lần rồi dw chia bằng cho M và tương tự cho B, phải không?

db được khởi tạo là 0 và db cộng bằng dz1.

db cộng bằng dz2 bạn biết đấy

dz(m) và db chia bằng M. Vì vậy, đó là những gì chúng ta đã có trong lần triển khai trước.

Chúng tôi đã loại bỏ một vòng lặp for.

Vì vậy, ít nhất bây giờ dw là một vectơ và chúng tôi đã cập nhật riêng dw1,

dw2 và vân vân.

Vì vậy, chúng tôi đã loại bỏ điều đó rồi nhưng chúng tôi vẫn

có vòng lặp for trên M ví dụ trong tập huấn luyện.

Vì vậy, hãy thực hiện các thao tác này và vector hóa chúng.

Đây là những gì chúng ta có thể làm, vì

việc triển khai db được vector hóa, về cơ bản những gì nó đang làm là tổng hợp,

tất cả các dz này rồi chia cho m. Vì vậy,

db về cơ bản là một trên m,

tổng từ I bằng một đến m của dzi và

tất cả các dz đều nằm trong vectơ hàng đó và trong Python,

những gì bạn làm là thực hiện, bạn biết đấy,

1 trên một m nhân np.

tổng của dz.

Vì vậy, bạn chỉ cần lấy biến này và gọi np.

sum trên đó và điều đó sẽ cung cấp cho bạn db.

Thế còn dw thì sao? Tôi sẽ chỉ viết

ra các phương trình chính xác ai có thể xác minh là điều đúng đắn để làm.

DW hóa ra là một trên M,

nhân ma trận X nhân dz chuyển vị.

Và, hãy xem tại sao lại như vậy.

Cái này bằng một trên m thì ma trận X,

x1 đến xm xếp thành cột như thế và dz

chuyển vị sẽ từ dz1 xuống dz(m) như vậy.

Và vì vậy, nếu bạn tìm ra ma trận này nhân với vectơ này sẽ bằng bao nhiêu,

hóa ra là một trên m nhân x1

dz1 cộng... cộng xm dzm.

Và vì vậy, đây là một vectơ n/1 và đây là những gì bạn thực sự có được,

với dw vì dw đã dùng những thứ này, bạn biết đấy,

xi dzi và cộng chúng lại và đó chính xác là những gì

phép nhân vectơ ma trận này đang được thực hiện và lặp lại,

với một dòng mã bạn có thể tính dw.

Vì vậy, việc thực hiện vector hóa các phép tính đạo hàm chỉ là thế này,

bạn sử dụng dòng này để triển khai db và sử dụng

dòng này để triển khai dw và lưu ý rằng không có vòng lặp for trên tập huấn luyện,

bây giờ bạn có thể tính toán các cập nhật bạn muốn cho các thông số của mình.

Vì vậy, bây giờ, hãy tập hợp tất cả lại để tìm ra cách bạn thực sự triển khai hồi quy logistic.

Vì vậy, đây là bản gốc của chúng tôi,

thực hiện không vector hóa rất kém hiệu quả.

Vì vậy, điều đầu tiên chúng ta làm trong video trước là loại bỏ tập này, phải không?

Vì vậy, thay vì lặp qua dw1,

dw2, v.v.,

chúng ta đã thay thế giá trị này bằng giá trị vectơ dw là dw+= xi,

bây giờ là vectơ nhân dz(i).

Nhưng bây giờ, chúng ta sẽ thấy rằng chúng ta cũng có thể loại bỏ không

chỉ là một vòng lặp for bên dưới nhưng cũng loại bỏ vòng lặp for này.

Vì vậy, đây là cách bạn làm điều đó.

Vì vậy, bằng cách sử dụng những gì chúng ta có từ các slide trước,

bạn sẽ nói, chữ Z viết hoa,

Z bằng w hoán vị X + B và mã bạn viết hoa Z bằng np.

w hoán vị X + B và sau đó a bằng sigmoid của chữ Z viết hoa.

Vì vậy, bây giờ bạn đã tính toán tất cả những điều này và tất cả những điều này cho tất cả các giá trị của I.

Tiếp theo trên slide trước,

chúng tôi đã nói bạn sẽ tính dz bằng A - Y.

Vì vậy, bây giờ bạn đã tính toán tất cả những điều này cho tất cả các giá trị của i.

Khi đó, cuối cùng dw bằng 1/m x

dz chuyển vị và db bằng 1/m bạn biết đấy, np.

tổng dz.

Như vậy, bạn vừa thực hiện xong việc truyền tiến và truyền ngược,

thực sự tính toán các dự đoán và tính toán các đạo hàm trên

tất cả các ví dụ huấn luyện M mà không sử dụng vòng lặp for.

Và do đó, bản cập nhật giảm độ dốc sẽ là bạn biết đấy W

được cập nhật khi w trừ đi số lần tốc độ học tập

dw vừa được tính toán ở trên và B được cập nhật dưới dạng B trừ đi tốc độ học nhân với db.

Đôi khi việc đặt dấu hai chấm vào đó để biểu thị đó là một bài tập,

nhưng tôi đoán là tôi chưa hoàn toàn nhất quán với ký hiệu đó.

Nhưng với điều này, bạn vừa thực hiện

một lần lặp lại độ dốc giảm dần cho hồi quy logistic.

Bây giờ, tôi biết tôi đã nói rằng chúng ta nên loại bỏ

vòng lặp for rõ ràng bất cứ khi nào bạn có thể nhưng nếu bạn muốn

thực hiện nhiều lần lặp như

giảm dần độ dốc thì bạn vẫn cần một vòng lặp for theo số lần lặp.

Vì vậy, nếu bạn muốn có hàng nghìn lần lặp lại độ dốc giảm dần,

bạn có thể vẫn cần một vòng lặp for qua số lần lặp.

Có một vòng lặp for ngoài cùng như thế thì tôi

đừng nghĩ có cách nào để loại bỏ vòng lặp for đó.

Nhưng tôi nghĩ thật tuyệt vời khi bạn có thể thực hiện

ít nhất một lần lặp lại quá trình giảm độ dốc mà không cần sử dụng vòng lặp for.

Vậy là xong, bây giờ bạn đã có một vector hóa cao và

thực hiện hiệu quả cao việc giảm độ dốc cho hồi quy logistic.

Chỉ còn một chi tiết nữa mà tôi muốn nói đến trong video tiếp theo,

trong phần mô tả của chúng tôi ở đây, tôi đã ám chỉ ngắn gọn đến kỹ thuật này được gọi là phát sóng.

Phát sóng hóa ra là một kỹ thuật mà Python và

numpy cho phép bạn sử dụng để làm cho một số phần nhất định trong mã của bạn hiệu quả hơn nhiều.

Vì vậy, chúng ta hãy xem thêm một số chi tiết về phát sóng trong video tiếp theo.