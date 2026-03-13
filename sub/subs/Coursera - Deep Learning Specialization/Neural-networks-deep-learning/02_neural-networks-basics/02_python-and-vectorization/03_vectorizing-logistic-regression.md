# 03 vectorizing-hậu cần-hồi quy

---

Chúng ta đã nói về cách vector hóa cho phép bạn tăng tốc mã của mình một cách đáng kể.

Trong video này, chúng ta sẽ nói về cách bạn có thể vector hóa

việc thực hiện hồi quy logistic,

để họ có thể xử lý toàn bộ tập huấn luyện,

đó là thực hiện một độ cao duy nhất của việc giảm điểm đối với

toàn bộ tập huấn luyện mà không sử dụng dù chỉ một vòng lặp for rõ ràng.

Tôi cực kỳ hào hứng với kỹ thuật này,

và sau này khi chúng ta nói về mạng lưới thần kinh mà không

sử dụng ngay cả một vòng lặp for rõ ràng.

Hãy bắt đầu. Trước tiên chúng ta hãy xem xét bốn bước lan truyền của hồi quy logistic.

Vì vậy, nếu bạn có M ví dụ huấn luyện,

sau đó để đưa ra dự đoán ở ví dụ đầu tiên,

bạn cần phải tính toán điều đó,

tính Z. Tôi đang sử dụng công thức quen thuộc này,

sau đó tính toán kích hoạt,

bạn tính y hat trong ví dụ đầu tiên.

Sau đó, để đưa ra dự đoán về ví dụ huấn luyện thứ hai,

bạn cần phải tính toán điều đó.

Sau đó, để đưa ra dự đoán ở ví dụ thứ ba,

bạn cần phải tính toán điều đó, v.v.

Và bạn có thể cần phải làm điều này M lần,

nếu bạn có ví dụ đào tạo M.

Vì vậy, hóa ra là để thực hiện bốn bước nhân giống,

đó là tính toán những dự đoán này trên các ví dụ huấn luyện M của chúng tôi,

có một cách để làm điều đó,

mà không cần vòng lặp for rõ ràng.

Hãy xem bạn có thể làm được điều đó như thế nào.

Trước tiên, hãy nhớ rằng chúng tôi đã xác định chữ hoa ma trận X làm đầu vào đào tạo của bạn,

xếp chồng lên nhau thành các cột khác nhau như thế này.

Vì vậy, đây là một ma trận,

đó là ma trận NX by M.

Vì vậy, tôi đang viết cái này dưới dạng một hình khối Python,

điều này chỉ có nghĩa là X là ma trận NX theo M chiều.

Bây giờ, điều đầu tiên tôi muốn làm là chỉ ra cách bạn có thể tính Z1, Z2,

Z3 và vân vân,

tất cả chỉ trong một bước,

thực tế là chỉ với một dòng mã.

Vì vậy, tôi sẽ xây dựng 1

bởi ma trận M thực sự là một vectơ hàng trong khi tôi tính Z1,

Z2, v.v.,

xuống ZM, tất cả cùng một lúc.

Nó chỉ ra rằng điều này có thể được thể hiện như

W chuyển sang ma trận vốn X plus và sau đó là vectơ B này,

B và vân vân.

B, thứ này ở đâu,

cái này B, B, B, B,

Thứ B là vectơ 1xM hoặc

Ma trận 1xM hoặc đó là vectơ hàng M chiều.

Vì vậy, hy vọng bạn làm được với phép nhân ma trận.

Bạn có thể thấy rằng W hoán vị X1,

X2, v.v. cho đến XM,

chuyển vị W đó có thể là một vectơ hàng.

Vì vậy, chuyển vị W này sẽ là một vectơ hàng như thế.

Và do đó số hạng đầu tiên này sẽ có giá trị là W hoán vị X1,

W chuyển vị X2, v.v., chấm, chấm, chấm,

W hoán vị XM, và sau đó chúng ta thêm số hạng thứ hai B này,

B, B, v.v.,

cuối cùng bạn thêm B vào mỗi phần tử.

Vì vậy, bạn kết thúc với một vectơ 1xM khác.

Vâng, đó là yếu tố đầu tiên,

đó là yếu tố thứ hai, v.v.,

và đó là phần tử thứ n.

Và nếu bạn tham khảo các định nghĩa ở trên,

phần tử đầu tiên này chính xác là định nghĩa của Z1.

Phần tử thứ hai chính xác là định nghĩa của Z2, v.v.

Vì vậy, giống như X đã từng có được,

khi bạn lấy các ví dụ đào tạo của mình và

xếp chúng cạnh nhau, xếp chúng theo chiều ngang.

Tôi sẽ xác định chữ Z viết hoa ở đây

bạn lấy chữ Z viết thường và xếp chúng theo chiều ngang.

Vì vậy, khi bạn xếp các chữ X viết thường tương ứng với các ví dụ huấn luyện khác,

theo chiều ngang bạn nhận được biến vốn X này và

theo cách tương tự khi bạn lấy các biến Z chữ thường này,

và xếp chúng theo chiều ngang,

bạn nhận được chữ Z vốn biến đổi này.

Và hóa ra, để thực hiện điều này,

lệnh không phải là hình tròn là Z viết hoa bằng NP dot W dot T,

đó là W hoán vị X rồi cộng B.

Bây giờ có một sự tinh tế trong Python,

ở đây B là số thực hoặc nếu bạn muốn nói rằng bạn biết ma trận 1x1,

chỉ là một số thực bình thường.

Tuy nhiên, khi bạn thêm vectơ này vào số thực này,

Python tự động lấy số thực B này và mở rộng nó ra vectơ hàng 1XM này.

Vì vậy, trong trường hợp hoạt động này có vẻ hơi bí ẩn,

cái này được gọi là phát sóng trong Python,

và hiện tại bạn không phải lo lắng về điều đó,

chúng ta sẽ nói về nó nhiều hơn trong video tiếp theo.

Nhưng điều đáng chú ý là chỉ với một dòng mã, với dòng mã này,

bạn có thể tính chữ Z viết hoa và chữ Z viết hoa là

sẽ là ma trận 1XM chứa tất cả các chữ Z viết thường.

Chữ thường Z1 đến chữ thường ZM.

Vậy đó là Z, còn những giá trị A này thì sao.

Điều chúng tôi muốn làm tiếp theo,

là tìm cách tính A1,

A2 và cứ thế đến AM,

tất cả cùng một lúc,

và giống như việc xếp chồng chữ X thường dẫn đến

chữ X viết hoa và xếp các chữ Z thường theo chiều ngang sẽ tạo thành chữ Z viết hoa,

xếp chồng chữ thường A,

sẽ dẫn đến một biến mới,

mà chúng ta sẽ định nghĩa là chữ A viết hoa.

Và trong phần phân công chương trình,

bạn thấy cách triển khai hàm sigmoid có giá trị vectơ,

sao cho hàm sigmoid,

đầu vào vốn Z này như một biến số và đầu ra vốn A một cách rất hiệu quả.

Vì vậy, bạn có thể xem chi tiết về điều đó trong bài tập lập trình.

Vì vậy, chỉ để tóm tắt lại,

những gì chúng ta đã thấy trên slide này là thay vì cần phải lặp lại

Ví dụ đào tạo M để tính chữ Z thường và chữ A thường,

đôi khi, bạn có thể triển khai một dòng mã này,

để tính toán tất cả các Z này cùng một lúc.

Và sau đó, một dòng mã này,

với việc triển khai phù hợp

Sigma chữ thường để tính toán tất cả các chữ A viết thường cùng một lúc.

Vì vậy, đây là cách bạn thực hiện

triển khai vector hóa

bốn lần lan truyền cho tất cả các mẫu huấn luyện M cùng một lúc.

Tóm lại, bạn vừa thấy cách bạn có thể sử dụng

vector hóa để tính toán rất hiệu quả tất cả các kích hoạt,

tất cả các chữ A thường cùng một lúc.

Tiếp theo, hóa ra bạn cũng có thể sử dụng vector hóa rất

hiệu quả để tính toán sự lan truyền ngược,

để tính toán độ dốc.

Hãy xem bạn có thể làm điều đó như thế nào trong video tiếp theo.