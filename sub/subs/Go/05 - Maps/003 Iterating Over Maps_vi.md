# 003 Lặp lại bản đồ vi

---

Bây giờ chúng tôi đã có cơ hội chơi với các bản đồ một chút, tôi muốn tìm ra

cách họ có thể lấy một bản đồ và lặp lại trên tất cả các cặp giá trị quan trọng bên trong nó.

Vì vậy, trước tiên hãy bắt đầu bằng cách thực hiện một chút dọn dẹp mã hóa.

Tôi sẽ đưa ra hai cách khai báo bản đồ ban đầu ngay tại đây.

Chúng tôi sẽ loại bỏ chúng.

Và sau đó tôi sẽ bỏ ghi chú tất cả các mã mà chúng tôi đã đặt trước đó để khai báo bản

this color color.

Và tôi sẽ bổ sung thêm một đôi giá trị quan trọng nữa chỉ để làm cho mọi thứ trở về nên thú vị một chút.

Chúng tôi sẽ nói màu trắng là F, F, F, F, F và sau đó chúng tôi sẽ xóa nơi chúng tôi đã thêm cặp giá trị bổ sung khóa bổ sung này

và sau đó xóa nó.

To to ở đây.

Vì vậy, điều tôi muốn làm ngay bây giờ, tôi muốn tạo một hàm mới chấp nhận một bản đồ, lặp lại trên

bản đồ và in ra mọi cặp giá trị khóa bên trong nó.

Và vì vậy, điều này sẽ cho họ một cảm giác khác tốt hơn không chỉ về cách

loop qua tập hợp các cặp giá trị chính nhưng chúng ta biết cách chuyển một bản đồ sang một hàm khác.

Vì vậy, chúng tôi sẽ xem trước một chút về mã hóa để bắt đầu và sau đó chúng tôi sẽ quay lại trình soạn thảo

soạn thảo mã của chúng tôi và thực hiện phát triển khai thực tế.

Vì vậy, đây mơ hồ là bây giờ nó sẽ nhìn như thế nào khi chúng ta xem mã này ngay

tại đây, tôi muốn nhấn mạnh rằng mọi thứ mà chúng ta sẽ thấy ngay tại đây sẽ rất giống với mã mà

chúng tôi đã tìm thấy xung quanh các lát và lặp lại các lát đó.

Vì vậy, chúng tôi sẽ khai báo một hàm được gọi là bản đồ trong đó và sau đó chúng tôi sẽ thêm một đối số vào đó.

Chúng ta sẽ nói rằng đối số sẽ được đặt tên là C, hãy nhớ rằng, hãy lưu ý đến chủ đề sử dụng các

tên biến rất ngắn ở đây.

Và sau đó, chúng tôi sẽ chú thích loại bản đồ hoặc loại đối số đó.

Và vì vậy, chúng tôi sẽ vượt qua bản đồ màu sắc đó.

Vì vậy, đây là loại bản đồ với các khóa của chuỗi loại và các giá trị của chuỗi loại.

Sau đó, với các chức năng của bản đồ này, chúng tôi sẽ đặt mã hóa để thực hiện lặp lại trên bản đồ chính.

Và vì vậy đây là phần có thể nhìn rất giống với cú pháp lặp lại cắt lát mà chúng ta đã thấy

bây giờ đã một vài lần rồi.

Vì vậy, chúng tôi sẽ đặt từ khóa và sau đó chúng tôi sẽ đặt hai biến ngay tại đây để nhận từng khóa

và giá trị qua mỗi bước của vòng lặp.

Bây giờ tôi đang sử dụng các tên ở đây, hãy xem màu sắc và hex của chúng tôi.

Những điều này thực sự có thể được coi là chìa khóa và giá trị.

Giống như vậy, vì vậy thực sự quan trọng trong giá trị.

Tôi chỉ sử dụng một mô tả tên nhỏ ở đây của mã màu và hex mã hóa, sau đó chúng tôi sử dụng lại từ khóa phạm vi

đó để biết rằng chúng tôi đang cố gắng lặp lại trên bản đồ.

Vì vậy, bên trong phần thân thực thi của vòng lặp, sau đó chúng ta có thể đặt một số mã sẽ được thực thi

cho mọi cặp khóa giá trị khác nhau.

Vì vậy, hiện tại chúng tôi đã có bản xem trước nhỏ này, hãy cùng nhau chỉnh sửa trình chỉnh sửa mã của chúng tôi và tập hợp nó lại với nhau.

Vì vậy, bên dưới các chức năng chính của chúng tôi, chúng tôi sẽ tạo ra một chức năng mới được gọi là bản đồ như vậy.

Chúng tôi sẽ bắt đầu bằng cách bổ sung một số đối số duy nhất mà chúng tôi mong đợi điều này sẽ được yêu cầu.

Vì vậy, bất cứ điều gì được phép toán mà nó được gọi, chúng ta sẽ gọi nó là C viết tắt của màu sắc trong trường hợp này.

Và sau đó chúng tôi sẽ bổ sung vào các loại mà chúng tôi mong đợi trên bản đồ này.

Vì vậy, tôi mong đợi nó là một bản đồ với các loại khóa, chuỗi và các giá trị của chuỗi loại.

Sau đó, bên trong hàm, chúng ta sẽ thiết lập vòng lặp cho chúng ta để lặp lại trên bản đồ này.

Vì vậy, chúng tôi sẽ nói cho mỗi mã màu và mã hex đến từ vi phạm bản đồ.

C Run this code.

Bây giờ hãy nhớ rằng khi chúng ta gán các biến này hoặc tạo và gán các biến này là màu và

hex ngay tại đây, chúng tôi đang khai báo, khởi tạo và phân bổ giá trị cho chúng trong một bước.

Và vì vậy, chúng tôi chắc chắn rằng chúng tôi sử dụng cú pháp dấu chấm bằng.

Sau đó, bên trong chúng tôi sẽ thêm một chút mã hóa để ra từng màu và mã hex bên trong bản đồ.

Vì vậy, giả sử định dạng, dòng trong, mã hóa hex cho màu đã chọn.

Và vì vậy màu sắc ở đây là chìa khóa của chúng ta và sau đó chúng ta sẽ đặt xuống giá trị sẽ là hex.

Ví dụ như vậy.

Vì vậy, điều đó trông khá tốt.

Bây giờ chúng ta hãy quay trở lại các chức năng chính của chúng ta và chắc chắn rằng chúng ta gọi là bản đồ.

Vì vậy, tôi sẽ thay thế dòng lệnh hiện có ở đây bằng bản đồ trong và chúng tôi sẽ chuyển vào bản

đồ họa của chúng tôi, hãy xem như vậy.

Được chứ.

Tôi sẽ lưu tệp.

Có vẻ như tôi đang gặp lỗi đánh máy ở đây.

Tôi đã không đặt dấu comma sau giá trị cuối cùng của khóa giá trị này.

Vì vậy, cấu trúc rất giống nhau.

Hãy nhớ rằng chúng ta phải đặt dấu comma sau mỗi thuộc tính mà chúng ta thêm vào đây.

Vì vậy, tôi sẽ bổ sung thêm bình comma vào, tôi sẽ lưu trữ tệp và mọi thứ khác ổn định.

Bây giờ chúng ta sẽ quay trở lại thiết bị cuối cùng của mình, chúng ta sẽ chạy chương trình của mình và sau đó chúng ta sẽ tìm thấy một câu

các dòng lệnh khác nhau cho mọi cặp giá trị chính trong bản đồ.

Vì vậy, điều này trông khá tốt.

Bây giờ, như tôi đã nói lúc trước, tại thời điểm này, có thể bạn đang ngồi đó và suy nghĩ, Stephen, điều

cái này khác với cấu trúc như thế nào?

Tôi sẽ sử dụng cấu trúc so với bản đồ ở đâu?

Thôi, nghỉ ngơi nhanh đi.

Chúng tôi sẽ quay lại phần tiếp theo và sau đó chúng tôi sẽ chỉ tóm tắt nhanh về bản đồ và

nói về lý do tại sao chúng ta có thể sử dụng cấu trúc thay vì bản đồ hoặc quay ngược lại.

Vì vậy, hãy nhanh chóng nghỉ ngơi và chúng tôi sẽ trả lời câu hỏi đó chỉ sau một phút.