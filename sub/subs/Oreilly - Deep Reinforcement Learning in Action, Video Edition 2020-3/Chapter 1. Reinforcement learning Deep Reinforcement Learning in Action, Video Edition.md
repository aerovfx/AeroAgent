# Chương 1. Học tăng cường Học tăng cường sâu trong thực tế, Phiên bản video

---

1.2 Học tăng cường Điều quan trọng là phải phân biệt giữa các vấn đề

và giải pháp của chúng, hay nói cách khác là giữa nhiệm vụ chúng ta muốn giải quyết và các thuật toán

chúng tôi thiết kế để giải quyết chúng. Các thuật toán học sâu có thể được áp dụng cho nhiều loại vấn đề và nhiệm vụ.

Nhiệm vụ phân loại và dự đoán hình ảnh là những ứng dụng phổ biến của học sâu vì

xử lý hình ảnh tự động trước khi học sâu rất hạn chế do độ phức tạp của hình ảnh.

Nhưng có nhiều loại nhiệm vụ khác mà chúng ta có thể muốn tự động hóa, chẳng hạn như lái xe ô tô hoặc

cân bằng danh mục đầu tư cổ phiếu và các tài sản khác. Lái xe ô tô bao gồm một số lượng hình ảnh

nhưng quan trọng hơn, thuật toán cần học cách hành động chứ không chỉ đơn thuần là phân loại

hoặc dự đoán. Những loại vấn đề này, trong đó các quyết định phải được đưa ra hoặc một số hành vi phải được thực hiện.

được ban hành, được gọi chung là nhiệm vụ kiểm soát. Học tăng cường là một phương pháp chung

khuôn khổ để biểu diễn và giải quyết các nhiệm vụ điều khiển. Nhưng trong khuôn khổ này, chúng ta được tự do

để chọn thuật toán nào chúng ta muốn áp dụng cho một tác vụ điều khiển cụ thể (Hình 1.4).

Thuật toán học sâu là một lựa chọn tự nhiên vì chúng có thể xử lý dữ liệu phức tạp một cách hiệu quả,

và đây là lý do tại sao chúng ta sẽ tập trung vào học tăng cường sâu. Nhưng phần lớn những gì bạn sẽ học được trong cuốn sách này

cuốn sách là khung củng cố chung cho các nhiệm vụ điều khiển (xem Hình 1.5).

Sau đó, chúng ta sẽ xem cách bạn có thể thiết kế một mô hình học sâu phù hợp với

khuôn khổ và giải quyết một nhiệm vụ. Điều này có nghĩa là bạn sẽ học được nhiều điều về học tăng cường,

và bạn có thể sẽ học được một số điều về học sâu mà bạn chưa biết.

Hình 1.4. Ngược lại với bộ phân loại hình ảnh, thuật toán học tăng cường một cách linh hoạt

tương tác với dữ liệu. Nó liên tục tiêu thụ dữ liệu và quyết định những hành động cần thực hiện,

hành động sẽ thay đổi dữ liệu tiếp theo được trình bày cho nó. Một màn hình trò chơi điện tử có thể

dữ liệu đầu vào cho thuật toán RL, sau đó thuật toán này sẽ quyết định hành động nào sẽ thực hiện bằng bộ điều khiển trò chơi,

và điều này khiến trò chơi phải cập nhật (ví dụ: người chơi di chuyển hoặc bắn vũ khí).

Hình 1.5. Học sâu là một lĩnh vực con của học máy.

Các thuật toán học sâu có thể được sử dụng để hỗ trợ các phương pháp RL nhằm giải quyết các nhiệm vụ điều khiển.

Thêm một sự phức tạp nữa khi chuyển từ xử lý hình ảnh sang miền nhiệm vụ kiểm soát

là yếu tố bổ sung của thời gian. Với xử lý hình ảnh, chúng ta thường đào tạo một deep learning

thuật toán trên một tập dữ liệu hình ảnh cố định. Sau một thời gian đào tạo đầy đủ,

chúng tôi thường nhận được một thuật toán hiệu suất cao mà chúng tôi có thể triển khai cho một số hình ảnh mới, chưa được nhìn thấy.

Chúng ta có thể coi tập dữ liệu như một "không gian" dữ liệu, trong đó các hình ảnh tương tự ở gần nhau hơn trong

không gian trừu tượng và hình ảnh riêng biệt cách xa nhau hơn (Hình 1.6).

Hình 1.6. Mô tả đồ họa này của các từ trong không gian 2D hiển thị mỗi từ dưới dạng một điểm màu.

Những từ giống nhau thì tập hợp lại với nhau, còn những từ khác nhau thì cách xa nhau hơn. Dữ liệu tồn tại một cách tự nhiên

trong một loại không gian nào đó có dữ liệu tương tự sống gần nhau hơn. Các nhãn A, B,

C và D chỉ ra các cụm từ cụ thể có chung một số ngữ nghĩa.

Trong các nhiệm vụ kiểm soát, chúng ta cũng có một không gian dữ liệu để xử lý. Nhưng mỗi phần dữ liệu cũng

có một chiều thời gian. Dữ liệu tồn tại cả về thời gian và không gian. Điều này có nghĩa là thuật toán

quyết định tại một thời điểm bị ảnh hưởng bởi những gì đã xảy ra ở thời điểm trước đó. Đây không phải là

trường hợp phân loại hình ảnh thông thường và các vấn đề tương tự. Thời gian làm cho nhiệm vụ đào tạo trở nên năng động.

Tập dữ liệu mà thuật toán đang huấn luyện không nhất thiết phải cố định,

nhưng thay đổi dựa trên các quyết định mà thuật toán đưa ra.

Các tác vụ giống như phân loại hình ảnh thông thường thuộc danh mục học có giám sát,

bởi vì thuật toán được đào tạo về cách phân loại hình ảnh chính xác bằng cách đưa ra câu trả lời đúng.

Đầu tiên, thuật toán thực hiện các dự đoán ngẫu nhiên và được sửa chữa lặp đi lặp lại cho đến khi học được

các đặc điểm trong ảnh tương ứng với nhãn thích hợp. Điều này đòi hỏi chúng ta phải

biết câu trả lời đúng là gì, điều này có thể phức tạp. Nếu bạn muốn đào tạo một deep learning

thuật toán để phân loại chính xác hình ảnh của nhiều loài thực vật khác nhau, bạn sẽ phải tỉ mỉ

thu được hàng nghìn hình ảnh như vậy và liên kết thủ công các nhãn lớp với mỗi hình ảnh và

chuẩn bị dữ liệu ở định dạng mà thuật toán học máy có thể hoạt động, nói chung

một số loại ma trận. Ngược lại, ở RL, chúng tôi không biết chính xác điều đúng đắn cần làm là gì.

mỗi bước. Chúng ta chỉ cần biết mục tiêu cuối cùng là gì và những điều cần tránh làm. bạn làm thế nào

dạy chó một trò lừa? Bạn phải cho nó những món ngon. Tương tự như tên cho thấy, chúng tôi đào tạo

một thuật toán RL bằng cách khuyến khích nó hoàn thành một số mục tiêu cấp cao và có thể không khuyến khích

nó làm những điều chúng ta không muốn nó làm. Trong trường hợp xe tự lái, cấp độ cao

mục tiêu có thể là "đến điểm B từ điểm xuất phát A mà không bị va chạm". Nếu nó hoàn thành nhiệm vụ,

chúng tôi khen thưởng nó, và nếu nó gặp sự cố, chúng tôi sẽ phạt nó. Chúng tôi sẽ thực hiện tất cả việc này trong một trình mô phỏng thay vì

trên đường thật, vì vậy chúng tôi có thể để nó liên tục thử và thất bại trong nhiệm vụ cho đến khi nó

học và được khen thưởng. Mẹo. Trong ngôn ngữ tự nhiên, phần thưởng luôn mang ý nghĩa tích cực,

trong khi trong thuật ngữ học tăng cường, đó là một đại lượng bằng số cần được tối ưu hóa.

Vì vậy, phần thưởng có thể tích cực hoặc tiêu cực. Khi nó dương, nó ánh xạ tới điều kiện tự nhiên

cách sử dụng ngôn ngữ của thuật ngữ, nhưng khi nó là giá trị âm, nó sẽ ánh xạ tới ngôn ngữ tự nhiên

từ “hình phạt”. Thuật toán có một mục tiêu duy nhất là tối đa hóa phần thưởng của nó và theo thứ tự

để làm được điều này, nó phải học thêm những kỹ năng cơ bản để đạt được mục tiêu chính. Chúng tôi cũng có thể cung cấp

phần thưởng tiêu cực khi thuật toán chọn làm những việc chúng ta không thích và vì nó đang cố gắng

tối đa hóa phần thưởng của mình, nó sẽ học cách tránh những hành động dẫn đến phần thưởng tiêu cực. Đây là

tại sao nó được gọi là học tăng cường. Chúng ta củng cố tích cực hoặc tiêu cực một số

hành vi sử dụng tín hiệu khen thưởng (xem Hình 1.7). Điều này khá giống với cách học của động vật. Họ

học cách làm những điều khiến họ cảm thấy dễ chịu hoặc hài lòng và tránh những điều gây đau đớn.

Hình 1.7. Trong khung RL, một số loại thuật toán học sẽ quyết định hành động nào cần thực hiện

cho một nhiệm vụ điều khiển (ví dụ: lái robot hút bụi) và hành động đó dẫn đến kết quả tích cực hoặc

phần thưởng tiêu cực, sẽ củng cố tích cực hoặc tiêu cực hành động đó và do đó

huấn luyện thuật toán học tập.