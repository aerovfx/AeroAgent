# 06 siêu tham số của cây quyết định

---

Trong video cuối cùng,

chúng tôi đã xây dựng mô hình cây quyết định

sử dụng bộ dữ liệu của giải pháp synergyx.

Một trong những điều rút ra rõ ràng từ video

là mô hình của chúng tôi đã được trang bị quá mức.

Trong video này chúng ta sẽ tìm hiểu về nhiều loại

siêu tham số được sử dụng để cải thiện

Hiệu suất của mô hình cây quyết định

>> Người nói 2: Để tôi nhanh lên

nhắc nhở bạn về mét.

Siêu tham số là một tham số có

giá trị được đặt trước khi học máy

quá trình bắt đầu.

Các siêu tham số này

được cố tình thiết lập để tinh chỉnh và

điều chỉnh hành vi của mô hình.

Hãy cùng khám phá các siêu tham số chính

của cây quyết định và

hiểu chúng biểu thị điều gì.

Siêu tham số quan trọng đầu tiên là tiêu chí.

Tiêu chí trong cây quyết định đề cập đến

phương pháp được sử dụng để phân chia dữ liệu tại mỗi nút.

Như đã thảo luận trước đó, hai

các phương pháp thường được sử dụng là thần đèn,

tạp chất và entropy.

Ngoài hai cách tiếp cận này,

mất logarit là một cách tiếp cận khác

được sử dụng cho các vấn đề phân loại.

Tham số bộ chia xác định

chiến lược được sử dụng để chọn sự phân chia tại

mỗi nút.

Có hai lựa chọn ở đây tốt nhất và

ngẫu nhiên.

Thông số tốt nhất là

chiến lược mặc định.

Nó tìm kiếm

sự phân chia tốt nhất bằng cách đánh giá

một số lượng lớn các phân chia có thể.

Cách tiếp cận này có thể

tính toán đắt tiền.

Trong chiến lược ngẫu nhiên, một

tập hợp con các tính năng được chọn và

sự phân chia tốt nhất được tìm thấy từ

tập hợp con các tính năng này.

Chiến lược này có thể tăng tốc độ đào tạo, nhưng

cũng có thể dẫn đến cây dưới mức tối ưu.

Nếu bạn nhớ lại, trong khi xây dựng mô hình,

chúng tôi đã sử dụng một cách cụ thể

siêu tham số được gọi là trạng thái ngẫu nhiên.

Cây quyết định của chúng tôi có rất nhiều

tính ngẫu nhiên được xây dựng bên trong mô hình và

siêu tham số này giúp trong

kiểm soát tính ngẫu nhiên này.

Tuy nhiên, điều quan trọng cần lưu ý là

nó không loại bỏ tính ngẫu nhiên.

Ngoài các siêu tham số này,

chúng tôi có nhiều siêu tham số khác

giúp ích trong việc Cắt tỉa cây quyết định.

Cắt tỉa, như đã thảo luận trước đó,

là quá trình chọn lọc

loại bỏ các cành khỏi cây.

Quá trình này rất quan trọng vì nó giúp

trong việc giải quyết vấn đề trang bị quá mức.

Hãy hiểu làm thế nào chúng ta biết điều đó

cây quyết định được phép phát triển cho đến khi

đạt đến các nút lá hoàn toàn thuần khiết.

Vì thế, đôi khi chiếc lá cuối cùng

các nút còn lại với một phần rất nhỏ

số lượng mẫu dựa vào đó

lớp dự đoán được xác định.

Ví dụ, chúng ta hãy xem

tại cây quyết định ngẫu nhiên này.

Bạn có thể nhìn thấy những tờ giấy bạc này không?

Chúng chỉ chứa một mẫu

loại có doanh thu thấp và loại có doanh thu cao.

Chỉ dựa trên một mẫu này,

chúng tôi đã xác định lớp dự đoán

lần lượt là doanh thu thấp và doanh thu cao.

Điều này cũng làm cho mô hình

cụ thể cho dữ liệu huấn luyện.

Những mô hình như vậy thường không thực hiện được trên

dữ liệu thử nghiệm, dẫn đến tình trạng quá khớp.

Bằng cách cắt tỉa, chúng ta có thể kiểm soát cách

cây sẽ ngắn đi nhiều.

Cây thấp hơn là cơ hội

của việc trang bị quá mức,

mặc dù nếu chúng ta tỉa cây hoàn toàn,

mô hình có thể dễ bị thiếu trang bị.

Vì vậy chúng ta phải tìm ra mức độ phù hợp

cắt tỉa cho từng vấn đề học máy.

Chúng ta hãy xem xét các siêu tham số

giúp ích trong việc cắt tỉa cây quyết định.

Trước khi hiểu độ sâu tối đa.

Chúng ta phải hiểu cái gì là

độ sâu của cây quyết định

Độ sâu của cây quyết định, còn được gọi là

như chiều cao của nó, đề cập đến số lượng

của các cấp độ hoặc các lớp trong cây từ

nút gốc đến các nút lá.

Mỗi quyết định hoặc

một sự phân chia tương ứng với một độ sâu.

Nút gốc ở độ sâu 0.

Các nút nhánh của nó ở độ sâu 1.

Do đó, các nút nhánh của chúng

đang ở độ sâu 2, v.v.

Giới hạn độ sâu tối đa của siêu tham số

độ sâu tối đa của cây quyết định.

Nó kiểm soát bao nhiêu cấp độ

quyết định hoặc phân chia cây có thể có.

Ví dụ: nếu chúng ta giữ độ sâu tối đa

là một, cây quyết định mẫu sẽ

trông giống như thế này như bạn có thể thấy,

cây bây giờ chỉ có một độ sâu,

và do đó các nút lá

có số lượng mẫu nhiều hơn

Một siêu tham số cắt tỉa khác

là min_ sample_split.

Đúng như tên gọi,

nó đặt số lượng tối thiểu

các mẫu cần thiết để phân chia một nút.

Nếu một nút có ít mẫu hơn thế này

giá trị cụ thể, nó sẽ không được chia thêm.

Ví dụ,

nếu chúng ta chọn mức phân chia mẫu Min là 12,

cây của chúng ta sẽ trông giống như thế này.

Chú ý nó khác biệt như thế nào

từ cây ban đầu.

Các nút được đánh dấu không bị phân chia

hơn nữa bởi vì họ có ít hơn

12 mẫu.

Sử dụng siêu tham số min_samples_leaf

đảm bảo rằng mỗi nút lá

có số lượng tối thiểu là

mẫu trong cây.

Nó có thể hữu ích để đảm bảo rằng

dự đoán xác suất không được thực hiện dựa trên

trên một cỡ mẫu rất nhỏ.

Bây giờ hãy xem cái cây trông như thế nào

giống như nếu chúng tôi chỉ định các mẫu tối thiểu

như bốn.

Như bạn thấy, cái cây đã được cắt tỉa

theo cách mà mỗi nút lá có bốn hoặc

nhiều mẫu hơn.

>> Diễn giả 2: Với những điều này,

chúng tôi đã đề cập đến các siêu tham số chính

used in decision tree models.

Hãy thoải mái khám phá tài liệu

để tìm hiểu thêm về họ.

Để đạt được hiệu suất mô hình tối ưu,

chúng ta nên lựa chọn cẩn thận

các siêu tham số tùy thuộc vào

những vấn đề cụ thể

mà mô hình đang phải đối mặt.

Ở video tiếp theo mình sẽ cố gắng cải thiện

hiệu suất của mô hình cây quyết định của chúng tôi

bằng cách thực hiện điều chỉnh siêu tham số.