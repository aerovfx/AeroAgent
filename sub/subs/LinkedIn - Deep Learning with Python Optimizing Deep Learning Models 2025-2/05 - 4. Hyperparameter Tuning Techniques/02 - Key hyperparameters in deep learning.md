# 02 - Các siêu tham số chính trong deep learning

---

- [Người kể chuyện] Trong học sâu,

siêu tham số là các cài đặt bên ngoài xác định

mạng lưới thần kinh được cấu trúc và huấn luyện như thế nào.

Không giống như các tham số được học trong quá trình đào tạo,

siêu tham số được đặt trước khi bắt đầu đào tạo

và có tác động đáng kể đến khả năng của mô hình

để tìm hiểu và khái quát hóa.

Việc lựa chọn đúng loại thông số là rất quan trọng

để đảm bảo đào tạo hiệu quả, hoạt động mạnh mẽ,

và nội bộ hóa tối ưu cho dữ liệu chưa nhìn thấy.

Một trong những loại thông số quan trọng nhất

là tốc độ học tập, điều khiển

mô hình điều chỉnh trọng lượng của nó bao nhiêu

trong mỗi lần lặp lại huấn luyện.

Tốc độ học quá cao có thể khiến mô hình

vượt quá giá trị tối ưu,

dẫn đến việc tập luyện không ổn định,

trong khi tỷ lệ học tập quá thấp,

dẫn đến sự hội tụ chậm

và có thể bẫy mô hình trong một giải pháp tối ưu.

Việc bắt đầu với tốc độ học tập khiêm tốn là điều bình thường,

chẳng hạn như 0,001, đặc biệt khi sử dụng trình tối ưu hóa như Adam.

Giá trị này đóng vai trò là đường cơ sở ổn định

thường hoạt động tốt trên nhiều nhiệm vụ khác nhau.

Từ đó, hãy cân nhắc triển khai công cụ lập lịch tốc độ học tập,

chẳng hạn như phân rã từng bước, ủ cosine hoặc lịch trình khởi động

để điều chỉnh tốc độ học tập một cách linh hoạt

khi quá trình đào tạo của bạn tiến triển.

Những người lập lịch trình này có thể giúp bạn sớm thực hiện các bước lớn hơn,

sau đó tinh chỉnh các bước đó khi bạn tiến gần hơn

tới một giải pháp tối ưu.

Cuối cùng, tiến hành tìm kiếm nhanh chóng,

chẳng hạn như tỷ lệ thử nghiệm trong khoảng từ 0,0001 đến 0,1

có thể giúp xác định điểm phù hợp cho vấn đề cụ thể của bạn.

Một siêu tham số quan trọng khác là kích thước lô,

xác định số lượng mẫu đào tạo được xử lý

trước khi cập nhật các tham số của mô hình.

Kích thước lô nhỏ hơn dẫn đến ước tính ồn ào hơn

của gradient, nhưng có thể giúp mô hình

thoát khỏi cực tiểu cục bộ nông,

và thường dẫn đến sự hội tụ ban đầu nhanh hơn.

Các lô lớn hơn có thể hợp lý hóa việc tính toán,

đặc biệt là trên các GPU hiện đại,

nhưng có thể yêu cầu điều chỉnh cẩn thận tốc độ học tập,

và đôi khi có thể dẫn dắt người mẫu

đến một giải pháp cuối cùng ít lý tưởng hơn.

Điểm khởi đầu tốt là chọn một lô tương đối vừa phải

kích thước từ 32 đến 256,

cân bằng các tài nguyên tính toán có sẵn

với hành vi đào tạo ổn định.

Nếu phần cứng của bạn bị giới hạn về bộ nhớ,

bạn có thể cần phải chọn các lô nhỏ hơn.

Ngược lại, nếu bạn có bộ nhớ GPU dồi dào,

bạn có thể thử lô lớn hơn,

nhưng hãy cân nhắc việc tăng tỷ lệ học lên một chút

để duy trì tốc độ tập luyện tốt.

Như mọi khi, hãy theo dõi hiệu suất và chuẩn bị lặp lại.

Số lượng kỷ nguyên là một siêu tham số khác,

và nó xác định số lần mô hình vượt qua

thông qua toàn bộ tập dữ liệu huấn luyện trong quá trình huấn luyện.

Quá ít kỷ nguyên có thể dẫn đến tình trạng thiếu trang bị,

trong đó mô hình không thể tìm hiểu dữ liệu một cách hiệu quả,

trong khi quá nhiều kỷ nguyên có thể dẫn đến việc trang bị quá mức,

nơi mô hình ghi nhớ dữ liệu huấn luyện

và không thể khái quát hóa được.

Phạm vi bắt đầu thông thường có thể là từ 10 đến 50 kỷ nguyên.

Nhưng điều này phụ thuộc nhiều vào độ phức tạp

của tập dữ liệu và mô hình của bạn.

Để tránh việc đào tạo và trang bị quá mức không cần thiết,

thực hiện dừng sớm

dựa trên sự mất xác thực hoặc độ chính xác của bạn.

Nếu số liệu xác thực ngừng cải thiện,

đó là tín hiệu mạnh mẽ cho thấy bạn nên ngừng tập luyện.

Giám sát chặt chẽ các số liệu xác nhận này,

và dừng lại khi tiến độ bị đình trệ,

có thể tiết kiệm cả thời gian và tài nguyên tính toán.

Siêu tham số cũng chi phối kiến ​​trúc của mô hình.

Các quyết định như số lớp

và số lượng tế bào thần kinh trên mỗi lớp,

đóng một vai trò quan trọng trong việc xác định năng lực của một mô hình

và khả năng nắm bắt các mẫu phức tạp.

Bắt đầu bằng cách bắt đầu đơn giản.

Hãy thử một mô hình nông và xem nó hoạt động như thế nào.

Nếu mô hình không phù hợp,

nghĩa là nó không nắm bắt được sự phức tạp trong dữ liệu của bạn,

tăng dần chiều sâu hoặc chiều rộng

và xem liệu hiệu suất có cải thiện hay không.

Khi thực hiện các nhiệm vụ đã được nghiên cứu kỹ lưỡng,

cân nhắc việc sử dụng các kiến trúc nổi tiếng,

như ResNet để phân loại hình ảnh,

hoặc các biến thể BERT để xử lý ngôn ngữ tự nhiên.

Những mô hình này đã được thử nghiệm rộng rãi

và cung cấp một khuôn khổ khởi đầu đáng tin cậy.

Khi mô hình tăng kích thước,

kết hợp các phương pháp chính quy hóa như bỏ học,

giảm cân hoặc chuẩn hóa theo đợt để duy trì quá trình tập luyện ổn định

và để ngăn ngừa việc trang bị quá mức.

Một trong những phổ biến nhất

và các hình thức chính quy hóa đơn giản là bỏ học.

Tỷ lệ bỏ học xác định một phần tế bào thần kinh

bị rơi hoặc tắt ngẫu nhiên trong quá trình luyện tập.

Điều này ngăn cản mạng phụ thuộc quá nhiều vào

trên bất kỳ nút nào và khuyến khích mạng

để tìm hiểu các mô hình mạnh mẽ, khái quát hơn.

Phạm vi phổ biến cho tỷ lệ bỏ học là từ 0,1 đến 0,5,

tùy thuộc vào loại lớp và độ phức tạp.

Nếu mô hình có vẻ không phù hợp,

việc giảm tỷ lệ bỏ học có thể giúp ích.

Ngược lại, nếu mô hình có vẻ quá phù hợp,

tỷ lệ bỏ học có thể tăng lên.

Lưu ý rằng các lớp khác nhau có thể yêu cầu mức giá khác nhau,

vì vậy đừng ngần ngại thử nghiệm.

Chúng ta cũng có thể đặt các hệ số chính quy

để chuẩn hóa L1 và L2.

Điều quan trọng là bắt đầu với các hệ số nhỏ và điều chỉnh,

dựa trên xu hướng quá vừa hoặc không vừa của người mẫu.

Phương pháp khởi tạo trọng số

cũng là một siêu tham số quan trọng,

vì nó ảnh hưởng đến điểm khởi đầu của quá trình đào tạo

và khả năng hội tụ của mô hình.

Khởi tạo tốt giúp đảm bảo tín hiệu được truyền tốt

và độ dốc đó vẫn ổn định.

Khởi tạo kém có thể dẫn đến biến mất

hoặc độ dốc bùng nổ,

làm cho việc đào tạo trở nên khó khăn hoặc không thể thực hiện được.

Ngoài việc khởi tạo, việc lựa chọn trình tối ưu hóa

là một điểm quyết định quan trọng khác.

Trình tối ưu hóa chỉ ra cách mô hình cập nhật trọng số của nó,

dựa trên độ dốc được tính toán trong quá trình lan truyền ngược.

Xét về các phương pháp hay nhất để khởi tạo trọng số,

nó thường là tốt nhất

để chọn một phương pháp khởi tạo được thiết lập tốt,

như Xavier hoặc He khởi tạo cho mạng sâu,

vì cả hai đều đảm bảo rằng trọng lượng của mô hình

không quá lớn cũng không quá nhỏ.

Đối với trình tối ưu hóa, hãy bắt đầu với tùy chọn thường được đề xuất.

Giảm độ dốc ngẫu nhiên là một trình tối ưu hóa được sử dụng rộng rãi

nổi tiếng vì tính đơn giản và hiệu quả của nó,

đặc biệt là khi kết hợp với động lượng

để tăng tốc độ hội tụ.

Mặt khác, Adam là một người tối ưu hóa thích ứng

điều chỉnh tỷ lệ học tập

cho từng tham số một cách linh hoạt,

làm cho nó trở thành một lựa chọn phổ biến cho hầu hết các nhiệm vụ học sâu

do hiệu suất mạnh mẽ của nó.

Cuối cùng, chỉ tinh chỉnh trình tối ưu hóa khởi tạo trọng số

nếu bạn gặp phải vấn đề hội tụ.

Nếu hiệu suất ổn định,

điều chỉnh tỷ lệ học tập và quy mô lô

thường mang lại những cải tiến đáng kể hơn

hơn các chỉnh sửa tối ưu hóa.

Điều chỉnh siêu tham số là một hành động cân bằng.

Điều quan trọng là luôn bắt đầu với các đường cơ sở hoặc giá trị mặc định đã biết.

Khi đã có một quá trình tập luyện ổn định,

điều chỉnh một siêu tham số tại một thời điểm

và theo dõi các số liệu xác thực.

Bằng cách tinh chỉnh nhiều lần các siêu tham số khác nhau,

cuối cùng bạn sẽ bắt đầu phát triển trực giác

về cách các đòn bẩy khác nhau tương tác với nhau.