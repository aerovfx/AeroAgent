# 09 mạng giảm dần độ dốc cho mạng nơ-ron

---

Được rồi. Tôi nghĩ đây sẽ là một video thú vị.

Trong video này, bạn sẽ thấy cách triển khai

giảm độ dốc cho mạng lưới thần kinh của bạn

với một lớp ẩn.

Trong video này, tôi sẽ chỉ cung cấp cho bạn

các phương trình bạn cần

thực hiện để có được sự lan truyền ngược

hoặc để việc giảm độ dốc hoạt động,

và trong video sau video này,

Tôi sẽ cung cấp thêm một số trực giác về lý do tại sao

những phương trình cụ thể này là

phương trình chính xác,

là các phương trình đúng để tính toán

độ dốc bạn cần cho mạng lưới thần kinh của mình.

Vì vậy, mạng lưới thần kinh của bạn,

hiện tại chỉ có một lớp ẩn,

sẽ có tham số W1,

B1, W2 và B2.

Vì vậy, như một lời nhắc nhở,

nếu bạn có tính năng nhập liệu NX hoặc N0,

và N1 đơn vị ẩn,

và đơn vị đầu ra N2 trong các ví dụ của chúng tôi.

Cho đến nay tôi chỉ có N2 bằng một,

thì ma trận W1 sẽ là N1 x N0.

B1 sẽ là vectơ chiều N1,

vì vậy chúng ta có thể viết nó là N1

bằng ma trận một chiều,

thực sự là một vector cột.

Kích thước của W2 sẽ là N2 x N1,

và kích thước của B2 sẽ là N2 một.

Đúng, cho đến nay chúng ta chỉ

đã thấy các ví dụ trong đó N2 bằng một,

nơi bạn chỉ có một đơn vị ẩn duy nhất.

Vì vậy, bạn cũng có một hàm chi phí

cho một mạng lưới thần kinh.

Hiện tại, tôi chỉ giả sử

rằng bạn đang thực hiện phân loại nhị phân.

Vì vậy, trong trường hợp đó,

chi phí của các thông số của bạn như

sau đây sẽ là một

trên M của giá trị trung bình của hàm mất mát đó.

Vì vậy, L ở đây là sự mất mát khi bạn

mạng lưới thần kinh dự đoán mũ Y, phải không.

Đây thực sự là A2 khi

nhãn gradient bằng Y.

Nếu bạn đang thực hiện phân loại nhị phân,

hàm mất có thể chính xác là gì

bạn sử dụng cho hồi quy logistic trước đó.

Vì vậy, để huấn luyện các tham số của thuật toán,

bạn cần thực hiện giảm độ dốc.

Khi huấn luyện mạng nơron,

điều quan trọng là phải khởi tạo các tham số

ngẫu nhiên thay vì tất cả các số không.

Sau này chúng ta sẽ biết tại sao lại như vậy,

nhưng sau khi khởi tạo tham số

đến điều gì đó,

mỗi vòng lặp hoặc độ dốc giảm dần

với những dự đoán được tính toán.

Vì vậy, về cơ bản bạn tính Y mũ I,

vì I bằng một đến M, chẳng hạn.

Sau đó, bạn cần tính đạo hàm.

Vì vậy, bạn cần tính DW1,

và đó là đạo hàm của hàm chi phí

đối với tham số W1,

bạn có thể tính toán một biến khác,

tôi sẽ gọi DB1 nhé,

đó là đạo hàm hay độ dốc

của hàm chi phí của bạn với

liên quan đến biến B1, v.v.

Tương tự cho các thông số khác W2 và B2.

Cuối cùng là bản cập nhật giảm độ dốc

sẽ cập nhật W1 thành W1 trừ Alpha.

Tốc độ học nhân với D, W1.

B1 được cập nhật thành B1 trừ đi tốc độ học tập,

lần DB1 và tương tự cho W2 và B2.

Đôi khi, tôi sử dụng dấu hai chấm bằng

và đôi khi bằng,

vì một trong hai ký hiệu đều hoạt động tốt.

Vì vậy, đây sẽ là một lần lặp lại

độ dốc giảm dần,

và sau đó bạn lặp lại điều này một số

lần cho đến khi các thông số của bạn

trông như thể họ đang hội tụ.

Vì vậy, trong các video trước,

chúng tôi đã nói về cách

tính toán dự đoán,

cách tính toán kết quả đầu ra,

và chúng tôi đã thấy cách thực hiện điều đó trong

một cách vector hóa là tốt.

Vì vậy, điều quan trọng là phải biết cách tính toán

các số hạng đạo hàm riêng này,

DW1, DB1 cũng như

dẫn xuất DW2 và DB2.

Vì vậy, điều tôi muốn làm chỉ là đưa cho bạn

các phương trình bạn cần để

tính toán các đạo hàm này.

Tôi sẽ chuyển sang video tiếp theo

là một video tùy chọn, để đi

hiểu rõ hơn về Jeff về cách chúng tôi

đã nghĩ ra những công thức đó.

Vì vậy, hãy để tôi tóm tắt lại

các phương trình cho sự lan truyền.

Vì vậy, bạn có Z1 bằng W1X cộng B1,

và sau đó A1 bằng hàm kích hoạt

trong lớp đó phần tử được áp dụng khôn ngoan như Z1,

và sau đó Z2 bằng W2,

A1 cộng V2, và cuối cùng,

giống như tất cả được vector hóa trên tập huấn luyện của bạn, phải không?

A2 bằng G2 của Z2.

Một lần nữa, bây giờ, nếu chúng ta cho rằng chúng ta

thực hiện phân loại nhị phân,

thì chức năng kích hoạt này thực sự

phải là hàm sigmoid,

tương tự chỉ dành cho phần cuối đó.

Vì vậy, đó là sự lan truyền về phía trước hoặc bên trái để

phù hợp để tính toán cho mạng lưới thần kinh của bạn.

Tiếp theo, hãy tính đạo hàm.

Vì vậy, đây là bước lan truyền ngược.

Sau đó tôi tính DZ2 bằng A2

trừ đi độ dốc của Y,

và chỉ như một lời nhắc nhở,

tất cả điều này được vector hóa qua các ví dụ.

Vì vậy, ma trận Y là ma trận này bằng

Ma trận M liệt kê tất cả M của bạn

ví dụ xếp chồng lên nhau theo chiều ngang.

Thì ra DW2 bằng cái này,

và thực tế, ba phương trình đầu tiên này là

rất giống với việc giảm độ dốc

cho hồi quy logistic.

X bằng một,

dấu phẩy, giữ dims bằng true.

Chỉ cần một chi tiết nhỏ np.sum này là

lệnh NumPy của Python để tính tổng

trên một chiều của ma trận.

Trong trường hợp này, tính tổng theo chiều ngang,

và những gì Keepdims làm là,

nó ngăn Python khỏi

xuất ra một trong những điều buồn cười

xếp hạng một mảng, phải không?

Kích thước ở đâu là dấu phẩy N của bạn.

Vì vậy, bằng việc có keepdims bằng true,

điều này đảm bảo rằng đầu ra Python cho

DB một vectơ có N nhân một.

Trên thực tế, về mặt kỹ thuật thì tôi đoán là N2 một.

Trong trường hợp này, nó chỉ là từng số một,

nên có lẽ điều đó không quan trọng.

Nhưng sau này, chúng ta sẽ thấy khi nào nó thực sự quan trọng.

Vì vậy, cho đến nay những gì chúng tôi đã làm là rất

tương tự như hồi quy logistic.

Nhưng bây giờ khi bạn tiếp tục

lan truyền ngược,

bạn sẽ tính toán điều này,

DZ2 nhân G1 số nguyên tố của Z1.

Vì vậy, số nguyên tố G1 này là

đạo hàm của việc liệu đó có phải là sự kích hoạt hay không

chức năng bạn sử dụng cho lớp ẩn,

và đối với lớp đầu ra,

Tôi cho rằng bạn đang làm nhị phân

phân loại bằng hàm sigmoid.

Thế là đã nướng xong rồi

vào công thức đó cho DZ2,

và thời đại của anh ấy là sản phẩm có yếu tố khôn ngoan.

Vì vậy, đây sẽ là N1

bằng ma trận M, và cái này ở đây,

thứ phái sinh theo nguyên tố này là

cũng sẽ là ma trận N1 nhân N,

và vì vậy lần này có một yếu tố khôn ngoan

tích của hai ma trận.

Cuối cùng, DW1 bằng với điều đó,

và DB1 bằng cái này,

và trục p.sum DZ1

bằng một, keepdims bằng true.

Vì vậy, trong khi trước đây các Keepdims

có thể ít quan trọng hơn nếu N2 bằng một.

Kết quả chỉ là từng cái một

thứ, chỉ là một con số thực.

Ở đây, DB1 sẽ là N1 theo một vectơ,

và vì vậy bạn muốn Python, bạn muốn Np.sons.

Tôi sẽ đặt thứ gì đó có kích thước này

hơn một mảng xếp hạng buồn cười

về kích thước đó có thể kết thúc

làm rối tung một số tính toán dữ liệu của bạn.

Cách khác là không

phải giữ nguyên các thông số

nhưng để định hình lại một cách rõ ràng

đầu ra của NP.sum vào chiều này,

mà bạn muốn DB có.

Vì vậy, đó là sự lan truyền về phía trước

trong tôi đoán có bốn phương trình,

và lan truyền ngược trong tôi đoán có sáu phương trình.

Tôi biết tôi vừa viết ra những phương trình này,

nhưng trong video tùy chọn tiếp theo,

chúng ta hãy xem qua một số trực giác về cách

sáu phương trình cho mặt sau

thuật toán lan truyền đã được bắt nguồn.

Xin vui lòng xem nó hay không.

Nhưng dù sao đi nữa, nếu bạn

thực hiện các thuật toán này,

bạn sẽ có cách thực hiện chính xác

của chỗ dựa phía trước và chỗ dựa phía sau.

Bạn sẽ có thể tính toán đạo hàm

bạn cần để áp dụng phương pháp giảm độ dốc,

để tìm hiểu các thông số của mạng lưới thần kinh của bạn.

Có thể thực hiện thuật toán này và

làm cho nó hoạt động mà không cần sâu sắc

hiểu phép tính.

Rất nhiều thành công sâu sắc

người học tập làm như vậy.

Nhưng, nếu bạn muốn,

bạn cũng có thể xem video tiếp theo,

chỉ để có thêm một chút trực giác về

đạo hàm của các phương trình này là gì.