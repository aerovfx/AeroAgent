# 02 - Bộ điều hợp LoRA

---

- [Người hướng dẫn] Cùng khám phá bộ điều hợp LoRa,

một tập hợp con mạnh mẽ của việc tinh chỉnh tham số hiệu quả,

hoặc PEFT, nơi chúng ta sẽ bắt đầu

với cái nhìn tổng quan cấp cao bằng cách sử dụng phép tương tự nấu ăn của chúng tôi,

và sau đó chúng ta sẽ lặn sâu hơn

và đi sâu hơn vào các chi tiết kỹ thuật.

Hãy tưởng tượng bạn là một đầu bếp với một công thức nấu ăn tuyệt vời.

Bạn muốn nâng tầm món ăn của mình

mà không cần đại tu toàn bộ quá trình nấu ăn.

Bạn mang theo một dụng cụ chuyên dụng như máy bào siêu nhỏ để bào vỏ.

Công cụ này tạo ra tác động lớn với nỗ lực tối thiểu.

Trong thế giới học máy,

Bộ điều hợp LoRa đóng vai trò tương tự.

Chúng mang lại sự cải thiện đáng kể

mà không sửa đổi toàn bộ mô hình.

LoRa là viết tắt của Thích ứng cấp thấp.

Những bộ chuyển đổi này được thiết kế

để tinh chỉnh các mô hình được đào tạo trước một cách hiệu quả

bằng cách tập trung vào một tập hợp nhỏ các tham số.

Chúng đặc biệt hiệu quả khi bạn cần

để điều chỉnh mô hình cho phù hợp với nhiệm vụ mới

với dữ liệu hạn chế.

Trong trường hợp này, hãy giả sử

rằng chúng ta có ba nhiệm vụ khác nhau.

Thay vì có ba bản

của mẫu 13,5 gigabyte,

có thể tinh chỉnh hoặc chuyển giao đã học,

chúng ta sẽ thấy một chiến lược tốt hơn.

Về mặt kỹ thuật, bộ điều hợp LoRa là ma trận

được chèn vào các lớp của mạng lưới thần kinh.

Thay vì cập nhật toàn bộ ma trận trọng số,

khổng lồ,

trong quá trình đào tạo, LoRa chỉ cập nhật thứ hạng thấp nhỏ hơn này,

do đó tên, ma trận.

Cách tiếp cận này làm giảm đáng kể số lượng tham số

điều đó cần được đào tạo.

Hãy đi sâu hơn một chút.

Trong một lớp mạng nơ-ron điển hình, các trọng số được biểu diễn

bằng một ma trận lớn.

Trong quá trình tinh chỉnh, ma trận này được điều chỉnh

để cải thiện hiệu suất của mô hình.

Tuy nhiên, quá trình này có thể tốn kém về mặt tính toán

và cần rất nhiều dữ liệu.

Giả sử trong ví dụ của chúng ta về LoRa,

n đó có nghĩa là kích thước của ma trận là 512,

đó là khá bảo thủ.

Và hãy giả sử trường hợp cực đoan

rằng chúng ta sẽ lấy r,

điều đó có nghĩa là thứ hạng của bộ điều hợp LoRa là một.

Điều đó có nghĩa là nếu chúng ta lấy số lượng tham số

mà chúng ta cần tinh chỉnh trong LoRa,

sẽ chỉ có 500 lần một lần,

à, độ chính xác của dấu phẩy động 32, nhân hai,

đó là 32.000 tham số

thay vì tham số bình phương 512,

tức là hơn 2 triệu.

Đây là thông số cần điều chỉnh ít hơn gần 20 lần.

Vì vậy, bạn có thể thấy rằng nó có tác dụng rất lớn.

Trong LoRa, như chúng tôi đã nói, hai ma trận A và B này,

được sử dụng sao cho chúng ta có thể phân tách ma trận W

vào ma trận nhân của A và B,

Một mẫu từ phân phối chuẩn.

Và bằng cách này thì mẹo là

rằng chúng ta có thể thay đổi những trọng lượng nhỏ đó

và tạo ra một sự thay đổi to lớn, rất lớn.

Nếu điều này rất, rất kỹ thuật, đừng lo lắng về nó,

bởi vì bạn không thực sự cần phải biết toán học

đằng sau LoRa để hiểu chính xác cách triển khai nó.

Được rồi, đừng lo lắng.

Như chúng tôi đã nói, điều quan trọng nhất cần ghi nhớ là

bây giờ trọng lượng mới mà chúng ta đang sử dụng

để thực hiện đào tạo của chúng tôi sẽ là

một số trọng lượng được đào tạo trước đông lạnh, W,

cộng với phép nhân ma trận của A và B,

cái nào nhỏ hơn nhiều, được chứ?

Một lần nữa, đừng lo lắng về toán học

nếu bạn không quen thuộc với đại số tuyến tính.

Chỉ cần lấy khái niệm quan trọng.

Ta có hai ma trận A và B.

Chúng sẽ nhỏ.

Số lượng tham số cần điều chỉnh sẽ ít hơn rất nhiều,

và chúng ta sẽ có cùng mức độ hiệu quả.

Phương pháp này không chỉ hiệu quả về mặt tính toán,

nhưng cũng đòi hỏi ít dữ liệu hơn.

Vì A và B là ma trận cấp thấp nên

số lượng tham số cần cập nhật giảm đáng kể,

làm cho quá trình đào tạo nhanh hơn

và ít tốn tài nguyên hơn.

Điều này đặc biệt quan trọng trong trường hợp của bạn

nếu bạn không có quyền truy cập vào GPU A100 hoặc L4.

Hãy nghĩ về nó giống như sử dụng một bộ

dụng cụ chuyên dụng trong nấu ăn.

Mỗi công cụ tạo ra một phần nhỏ

nhưng cải thiện đáng kể

vào món ăn mà không thay đổi công thức cốt lõi.

Tương tự, bộ điều hợp LoRa thực hiện các điều chỉnh chính xác

vào mô hình, nâng cao hiệu suất của nó

không được đào tạo lại đầy đủ.

Nếu mức độ này

chi tiết có vẻ hơi quá toán học hoặc sâu sắc,

điều đó hoàn toàn ổn.

Nếu tôi muốn bạn để lại một tin nhắn,

đó là bộ điều hợp LoRa cung cấp một cách hiệu quả cao

để tinh chỉnh các mô hình,

đặc biệt là khi dữ liệu khan hiếm

và nguồn lực tính toán còn hạn chế.

Tóm lại, bộ điều hợp LoRa là một tập hợp con của PEFT

sử dụng ma trận cấp thấp để tinh chỉnh mô hình một cách hiệu quả.

Bằng cách chỉ cập nhật một số lượng nhỏ các tham số,

họ cung cấp những cải tiến hiệu suất đáng kể

với chi phí tính toán tối thiểu.

Điều này làm cho chúng trở thành một công cụ vô giá

để điều chỉnh các mô hình được đào tạo trước cho các nhiệm vụ mới.