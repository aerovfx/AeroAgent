# 06 - Thử thách demo trong LoRA

---

- [Người hướng dẫn] Trong bản demo này,

chúng ta sẽ làm một số thử nghiệm

để xác minh cách thực hiện điều chỉnh tham số

về kích thước cấp bậc và kích thước lô

khi huấn luyện LoRA trên mô hình T5.

Sự khởi đầu của cuốn sổ này cũng giống như trước đây.

Vì vậy, chúng tôi kết nối với GPU, chúng tôi thực hiện cài đặt PIP tương tự.

Chúng ta cần tải xuống tập dữ liệu.

Nó sẽ là cùng một tập dữ liệu.

Và chúng ta sẽ thực hiện quá trình xử lý trước dữ liệu tương tự.

Tuy nhiên, vì kích thước lô sẽ thay đổi,

điều đó có nghĩa là việc tạo ra tập dữ liệu tensorflow

cần phải được thực hiện ở mỗi phần của vòng lặp đầy đủ.

Hãy để tôi chỉ cho bạn những gì tôi muốn nói.

Ở đây chúng tôi có cách triển khai LoRA tương tự.

Vì vậy, điều chúng ta sắp làm là, ở đây tôi đã triển khai

một phương pháp nhỏ để đếm các tham số,

có thể đào tạo được và không thể đào tạo được,

để bạn có thể thấy những gì chúng tôi đang làm.

Và sau đó chúng ta sẽ thử xếp hạng 1, 4 và 16,

và đối với kích cỡ lô, 8, 64 và 128, được chứ?

Và với mỗi sự kết hợp của cả hai, điều chúng ta sẽ làm

là chúng ta sẽ chỉ áp dụng LoRA trên lớp cuối cùng.

Vì vậy, chúng tôi sẽ không áp dụng LoRA trên bộ giải mã,

ngay trên lớp cuối cùng, bởi vì bây giờ bạn đã biết

cách thực hiện trên bộ giải mã hoặc bộ mã hóa.

Vì vậy, chúng tôi sẽ chỉ ra một điểm ở đây.

Chúng ta sẽ đếm các tham số.

Và sau đó chúng ta cần thực hiện tính thực tế của tập dữ liệu.

Vì kích thước bản vá này, như bạn có thể thấy, nó có thể thay đổi,

sau đó chúng ta cần thực hiện quá trình tiền xử lý

và tạo tập dữ liệu cho từng điểm của vòng lặp đầy đủ.

Sau đó, chúng tôi biên dịch, huấn luyện và lưu nó.

Vì vậy, việc này sẽ mất thời gian vì nó liên quan đến,

ba lần ba, chín bài tập, được chứ?

Vì vậy, việc này có thể dễ dàng mất khoảng một giờ,

nhưng hãy tin tôi, nó đáng giá.

Trong trường hợp này, đối với bản demo này,

nếu bạn chỉ muốn xem kết quả

và muốn tin tưởng chúng tôi, điều đó không sao cả,

bởi vì, theo một nghĩa nào đó, về cơ bản đó là những gì chúng tôi đã làm,

và tôi chỉ muốn cho bạn thấy sự khác biệt,

điều gì xảy ra khi chúng tôi thay đổi kích thước lô

và điều gì sẽ xảy ra khi chúng ta thay đổi thứ hạng.

Một điểm nhỏ tôi muốn nhấn mạnh

đó là sự thay đổi về cấp bậc và quy mô lô

hiển thị nhiều hơn khi số lượng kỷ nguyên là số lượng thực,

như 20 hoặc 30 và khi chúng tôi sử dụng toàn bộ tập dữ liệu.

Điều đó có nghĩa là, trong trường hợp của chúng tôi, sự khác biệt

có lẽ sẽ là vài giây và nó có thể không được cảm nhận rõ ràng.

Nhưng nếu chúng ta sử dụng toàn bộ tập dữ liệu, một lượng kỷ nguyên thực sự,

để đào tạo thực tế, cho các mô hình sản xuất thực tế,

đó là lúc bạn sẽ thấy sự khác biệt thực sự, được chứ?

Vì vậy, xu hướng sẽ tiếp tục.

Nó sẽ chỉ nhấn mạnh sự khác biệt.

Như đã nói, hãy chạy mô hình này,

và hãy đợi cho đến khi nó kết thúc.

Như tôi đã nói, nếu bạn tham gia việc này cùng tôi,

hãy nhớ rằng, việc này có thể mất một chút thời gian.

Được rồi, hoàn hảo!

Như bạn đã thấy, trong GPU của tôi,

phải mất 52 phút để chạy những thí nghiệm này.

Đó là lý do tôi đã nói với bạn, nếu bạn chỉ muốn xem kết quả,

điều đó còn hơn cả ổn,

bởi vì điều này đòi hỏi phải đào tạo rất nhiều.

Bây giờ, chúng ta sẽ thấy gì?

Những điều quan trọng.

Những điều quan trọng khi chúng ta đang giao dịch

với thứ hạng và kích cỡ lô

Mất bao lâu và tác động lên trí nhớ, được chứ?

Vì vậy, nếu chúng ta tiếp tục rèn luyện sự ổn định,

vì vậy, ví dụ: nếu chúng ta thấy khóa đào tạo đầu tiên,

chỉ để cho bạn một ví dụ,

nhận thấy rằng với quy mô lô thấp và thứ hạng thấp,

chúng ta có thể thấy rằng phải mất rất nhiều bước: 2.500.

Quá nhiều và mất gần 325 giây.

Một lần nữa, một thời gian rất dài vì kích thước lô thấp.

Chúng ta vẫn có thể thấy rằng khóa đào tạo đã thành công,

nhưng bạn có thể thấy ở chỗ mất xác thực,

bước nhảy không quá cao.

Nguyên nhân là do thứ hạng thấp.

Nếu chúng ta đi sang một thái cực khác, chỉ để cho bạn thấy,

bởi vì ở giữa bạn sẽ thấy tất cả sự tiến triển.

Khi chúng tôi huấn luyện với hạng 16 và lô 128,

chúng ta có thể thấy rằng chúng ta đã giảm các bước xuống chỉ còn 157.

Bạn có thể thấy thời gian khởi động chỉ là 200 giây,

không phải 325, và kỷ nguyên thứ hai là 111,

và bạn có thể thấy rằng bước nhảy vọt trong việc mất xác thực

lớn hơn nhiều và cũng bị lỗ.

Điều này là do, với thứ hạng cao hơn và quy mô lô cao hơn,

chúng tôi có một đào tạo ổn định hơn.

Nhưng hãy nhớ, sử dụng nhiều GPU và RAM hơn, được chứ?

Vì vậy, chúng tôi muốn xem tất cả những điều này chỉ trong một lệnh nhỏ.

Ở đây chúng tôi đang in tất cả lịch sử,

và bạn có thể xác minh ở một nơi duy nhất

tất cả những gì tôi đã nói với bạn.

Nếu tôi muốn bạn rút ra một điều gì đó từ bản demo này,

đó là điều sau đây

Cấp bậc cao hơn bao gồm việc đào tạo ổn định hơn,

cũng có thêm một chút thông số để huấn luyện,

và chúng ta sẽ thấy tổn thất giảm trên mỗi kỷ nguyên tốt hơn.

Mặt khác, kích thước lô cao hơn

sẽ đòi hỏi nhiều trí nhớ hơn nhưng thời gian luyện tập ngắn hơn.

Vì vậy thông thường bạn sẽ muốn thử nghiệm một chút

và chơi xung quanh, dựa trên cấu hình của bạn,

cơ sở hạ tầng của bạn,

và hãy thành thật mà nói, dữ liệu của bạn ngẫu nhiên đến mức nào,

bởi vì nếu bạn có nhiều nhiễu trong dữ liệu văn bản của mình,

thì thứ hạng cao hơn sẽ tốt hơn.