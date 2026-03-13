# Chương 1. Lập trình động so với Học tập tăng cường sâu Monte Carlo trong thực tế, Phiên bản video

---

1.3 Lập trình động so với Monte Carlo. Bây giờ bạn biết rằng bạn có thể huấn luyện một thuật toán để

hoàn thành một số nhiệm vụ cấp cao bằng cách giao cho việc hoàn thành nhiệm vụ một phần thưởng cao,

nghĩa là củng cố tích cực và củng cố tiêu cực những điều chúng ta không muốn nó làm.

Hãy làm cho điều này trở nên cụ thể. Giả sử mục tiêu cấp cao là huấn luyện robot hút bụi di chuyển từ

một phòng trong một ngôi nhà đến bến tàu của nó, đó là nhà bếp. Nó có bốn hành động – đi

sang trái, rẽ phải, tiến lên và lùi lại. Tại mỗi thời điểm, robot cần

quyết định thực hiện hành động nào trong số bốn hành động này. Nếu nó đến bến tàu, nó sẽ nhận được phần thưởng là

cộng thêm 100 và nếu nó chạm vào bất cứ thứ gì trên đường đi, nó sẽ nhận được phần thưởng âm là âm 10.

Giả sử robot có bản đồ 3D hoàn chỉnh của ngôi nhà và có vị trí chính xác

của dock, nhưng nó vẫn không biết chính xác chuỗi hành động nguyên thủy nào cần thực hiện

để đến bến tàu. Một cách tiếp cận để giải quyết vấn đề này được gọi là lập trình động (DP), đầu tiên

được phát biểu bởi Richard Bellman vào năm 1957. Lập trình động tốt hơn có thể được gọi là phân rã mục tiêu,

vì nó giải quyết các vấn đề cấp cao phức tạp bằng cách phân tách chúng thành các phần nhỏ hơn và nhỏ hơn

các bài toán con cho đến khi gặp một bài toán con đơn giản có thể giải được mà không cần thêm thông tin.

Thay vì robot cố gắng nghĩ ra một chuỗi dài các hành động nguyên thủy

sẽ đưa nó đến bến tàu, trước tiên nó có thể chia vấn đề thành "ở trong phòng này"

so với "ra khỏi phòng này". Vì nó có bản đồ hoàn chỉnh của ngôi nhà nên nó biết nó cần

để ra khỏi phòng, vì bến tàu ở trong bếp. Thế mà nó vẫn chưa biết chuyện gì

chuỗi hành động sẽ cho phép nó thoát khỏi phòng, do đó nó sẽ giải quyết vấn đề sâu hơn

để "di chuyển về phía cửa" hoặc "di chuyển ra khỏi cửa". Vì cánh cửa gần hơn

tới bến tàu và có đường dẫn từ cửa tới bến tàu, robot biết nó cần

để di chuyển về phía cửa. Nhưng một lần nữa nó không biết chuỗi hành động nguyên thủy nào sẽ

đưa nó về phía cửa. Cuối cùng, nó cần quyết định xem có nên di chuyển sang trái, phải, tiến lên,

hoặc ngược lại. Nó có thể thấy cánh cửa ở phía trước nên nó tiến về phía trước. Nó giữ cái này

xử lý cho đến khi nó ra khỏi phòng, khi đó nó phải thực hiện thêm một số phân tách mục tiêu cho đến khi

nó đến bến tàu. Đây là bản chất của lập trình động.

Đó là một cách tiếp cận chung để giải quyết một số loại vấn đề có thể được chia nhỏ

thành các bài toán con và các bài toán con, và nó có ứng dụng trên nhiều lĩnh vực, bao gồm

tin sinh học, kinh tế và khoa học máy tính. Để áp dụng quy hoạch động Bellman,

chúng ta phải có khả năng chia vấn đề của mình thành các bài toán con mà chúng ta biết cách giải quyết. Nhưng

ngay cả giả định tưởng chừng như vô hại này cũng khó thành hiện thực trong thế giới thực. Làm thế nào

bạn có phá vỡ mục tiêu cấp cao cho một chiếc xe tự lái là "đi đến điểm B từ điểm A mà không

đâm" vào các bài toán con nhỏ không va chạm? Liệu một đứa trẻ có thể học đi bằng cách giải quyết lần đầu tiên

vấn đề đi bộ dễ dàng hơn? Trong RL, nơi chúng ta thường gặp những tình huống phức tạp có thể bao gồm

yếu tố ngẫu nhiên nào đó, chúng ta không thể áp dụng quy hoạch động chính xác như Bellman đã trình bày

nó ra ngoài. Trên thực tế, DP có thể được coi là một thái cực của quá trình giải quyết vấn đề liên tục.

kỹ thuật, trong đó đầu kia sẽ là thử và sai ngẫu nhiên.

Một cách khác để xem quá trình học tập liên tục này là trong một số tình huống, chúng ta có tối đa

kiến thức về môi trường, còn ở những nơi khác chúng ta có kiến thức tối thiểu về môi trường,

và chúng ta cần sử dụng các chiến lược khác nhau trong từng trường hợp. Nếu bạn cần sử dụng phòng tắm

trong chính ngôi nhà của mình, bạn biết chính xác, à, ít nhất là trong vô thức, trình tự cơ bắp nào

các chuyển động sẽ đưa bạn vào phòng tắm từ bất kỳ vị trí bắt đầu nào, tức là lập trình động.

Điều này là do bạn biết rất rõ ngôi nhà của mình. Bạn có một mô hình ít nhiều hoàn hảo

về ngôi nhà của bạn trong tâm trí bạn. Nếu bạn dự một bữa tiệc tại một ngôi nhà mà bạn chưa từng đến

trước đây, bạn có thể phải nhìn xung quanh cho đến khi tìm được phòng tắm cho riêng mình, tức là,

thử và sai, bởi vì bạn không có mô hình tốt về ngôi nhà của người đó.

Chiến lược thử và sai thường thuộc về phương pháp Monte Carlo.

Phương pháp Monte Carlo về cơ bản là lấy mẫu ngẫu nhiên từ môi trường. Trong nhiều thế giới thực

vấn đề, chúng ta có ít nhất một số kiến thức về cách thức hoạt động của môi trường, vì vậy cuối cùng chúng ta

sử dụng một chiến lược hỗn hợp bao gồm một số thử nghiệm và sai sót và một số mức độ khai thác

những gì chúng ta đã biết về môi trường để giải quyết trực tiếp các mục tiêu phụ dễ dàng.

Một ví dụ ngớ ngẩn về chiến lược hỗn hợp là nếu bạn bị bịt mắt, đặt vào một tình huống không xác định.

vị trí trong nhà của bạn và được yêu cầu tìm phòng tắm bằng cách ném sỏi và lắng nghe

vì tiếng ồn. Bạn có thể bắt đầu bằng cách phân tách mục tiêu cấp cao "tìm phòng tắm"

thành mục tiêu phụ dễ tiếp cận hơn "tìm hiểu xem bạn hiện đang ở phòng nào". Để giải quyết

mục tiêu phụ này, bạn có thể ném một vài viên sỏi theo các hướng ngẫu nhiên và đánh giá kích thước của

phòng, có thể cung cấp cho bạn đủ thông tin để suy ra bạn đang ở phòng nào, chẳng hạn như phòng ngủ.

Sau đó, bạn cần chuyển sang mục tiêu phụ khác, điều hướng đến cánh cửa để bạn có thể vào

hành lang. Sau đó bạn lại bắt đầu ném sỏi, nhưng vì bạn nhớ được kết quả

trong lần ném sỏi ngẫu nhiên cuối cùng của bạn, bạn có thể nhắm mục tiêu ném của mình đến những khu vực ít chắc chắn hơn.

Lặp lại quá trình này, cuối cùng bạn có thể tìm thấy phòng tắm của mình. Trong trường hợp này, bạn sẽ

đang áp dụng cả phân rã mục tiêu của quy hoạch động và lấy mẫu ngẫu nhiên

của phương pháp Monte Carlo.