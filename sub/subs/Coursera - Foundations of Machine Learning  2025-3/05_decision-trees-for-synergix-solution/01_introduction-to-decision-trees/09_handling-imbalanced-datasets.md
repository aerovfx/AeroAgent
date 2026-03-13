# 09 bộ dữ liệu xử lý mất cân bằng

---

Các bạn trong video này hãy cùng đi sâu tìm hiểu nhé

thế giới phức tạp của các tập dữ liệu mất cân bằng.

Trong khi làm như vậy, chúng ta cũng sẽ khám phá

những thách thức họ đặt ra và

khám phá hiệu quả

chiến lược để giải quyết chúng.

Những chiến lược này giúp đảm bảo rằng

mô hình học máy của bạn hoạt động ở mức

tốt nhất của họ.

Vì vậy, hãy bắt đầu.

Hãy bắt đầu bằng sự hiểu biết

mất cân bằng giai cấp là gì

Như chúng ta đã thấy trước đó trong khóa học,

tập dữ liệu tổng hợp

dung dịch bị mất cân bằng.

Như chúng ta có thể quan sát từ cốt truyện,

nhãn một, đó là doanh thu cao,

hiện diện thường xuyên hơn so với

gắn nhãn số 0, tức là doanh số bán hàng thấp.

Cho đến nay trong khóa học,

chúng tôi đã giải quyết vấn đề này bằng cách sử dụng f một

làm thước đo đánh giá trong video này.

Hãy cùng tìm hiểu một số cách khác

để xử lý sự mất cân bằng lớp học này.

Đây là sử dụng đánh giá thích hợp

các số liệu như điểm số, độ chính xác và

thu hồi, phù hợp hơn cho

tập dữ liệu không cân bằng.

Thực hiện phân chia theo tầng và

sử dụng trọng số lớp siêu tham số.

Việc phân chia theo tầng là một yếu tố quan trọng

kỹ thuật phân vùng dữ liệu và

nó được thiết kế để duy trì một đẳng cấp bình đẳng

phân bổ giữa đào tạo và

bộ dữ liệu thử nghiệm.

Ví dụ: trong tập dữ liệu của chúng tôi, doanh số thấp

đại diện cho x phần trăm của dữ liệu,

trong khi doanh thu cao chiếm

y phần trăm còn lại.

Sự phân chia ngẫu nhiên có thể vô tình làm gián đoạn

số dư này trong phần thi thử tàu,

phân bổ số lượng mẫu thậm chí còn ít hơn

của tầng lớp thiểu số đối với đoàn tàu.

Sự phân chia theo tầng đảm bảo

rằng cả việc đào tạo và

bộ thử nghiệm phản ánh chặt chẽ

phân phối ban đầu,

bảo toàn tỷ số x và y ở mức thấp

doanh số bán hàng cao ở cả hai bộ.

Một phương pháp phổ biến khác được sử dụng để giải quyết vấn đề này

Mất cân bằng lớp trong mô hình học máy

là trọng lượng lớp.

Các mô hình cụ thể như cây quyết định và

hồi quy logistic đến

với siêu tham số này.

Trong kỹ thuật này, chúng tôi chỉ định khác nhau

cân nặng cho mỗi lớp trong thời gian

giai đoạn đào tạo sao cho

sự đóng góp của mỗi lớp là cân bằng.

Trọng số được gán cho mỗi lớp là

thường tỷ lệ nghịch với

tần số trong tập dữ liệu.

Có hai cách để

đặt siêu tham số này.

Kỹ thuật phổ biến là thiết lập lớp

siêu tham số trọng lượng để cân bằng.

Một cách khác có thể là định nghĩa

một từ điển trong đó các phím đại diện

nhãn lớp và

các giá trị đại diện cho trọng số.

Những trọng lượng này có thể được điều chỉnh

dựa trên các yêu cầu.

Bây giờ bạn đã quen thuộc với

các kỹ thuật xử lý sự mất cân bằng dữ liệu,

hãy cùng tìm hiểu về cách cân bằng dữ liệu.

Nhưng tại sao chúng ta thực sự cần

để cân bằng tập dữ liệu?

Có một câu trích dẫn của Jana Kingsford rằng

nói rằng sự cân bằng không phải là thứ bạn tìm thấy,

đó là thứ mà bạn tạo ra.

Điều này cũng đúng với dữ liệu.

Trong cuộc sống thực, chúng ta thường phải

làm việc với các tập dữ liệu không cân bằng.

Hầu hết các thuật toán học máy đều giả định

dữ liệu được phân bố đồng đều, do đó

thuật toán sẽ thiên vị hơn

hướng tới việc dự đoán tầng lớp đa số,

trong trường hợp của chúng tôi, doanh thu cao.

Cân bằng tập dữ liệu bằng cách có gần như

tỷ lệ bằng nhau của lớp 0 và

lớp một giải quyết vấn đề này, vì nó

giúp ngăn chặn mô hình trở thành

thiên về giai cấp đa số.

Khi tập dữ liệu của chúng tôi được cân bằng,

độ chính xác cũng có thể được sử dụng như

một số liệu để đánh giá các mô hình của chúng tôi.

Bây giờ bạn đã quen với các thủ thuật

về việc xử lý tình trạng mất cân bằng dữ liệu, hãy cùng tìm hiểu

thành hai phương pháp chính để cân bằng

tập dữ liệu, lấy mẫu dưới và lấy mẫu quá mức.

Chúng ta hãy tìm hiểu chúng từng cái một.

Đầu tiên, hãy nói về việc lấy mẫu dưới.

Mục đích của việc lấy mẫu dưới là

nhằm giảm bớt tầng lớp đa số.

Nó được thực hiện bằng cách loại bỏ một số

quan sát của lớp đa số.

Tuy nhiên, trong thực tế, việc lấy mẫu dưới

kỹ thuật không được ưa thích vì có

là một cơ hội để mất

thông tin có giá trị.

Điều này cũng dẫn đến sự thiên vị,

vì chúng tôi đang xóa dữ liệu để thực hiện

tỉ lệ của hai lớp bằng nhau.

Một cách lấy mẫu chung

kỹ thuật lấy mẫu ngẫu nhiên.

Trong kỹ thuật này, các trường hợp từ

lớp đa số được loại bỏ ngẫu nhiên cho đến khi

đạt được sự cân bằng mong muốn.

Kỹ thuật này đơn giản và

dễ thực hiện,

nhưng nó dẫn đến mất thông tin.

Ngoài việc lấy mẫu ngẫu nhiên,

một số mẫu dưới phổ biến khác

kỹ thuật là Tomek Links,

thuật toán suýt trượt, v.v.

Tiếp theo, hãy nói về việc lấy mẫu quá mức.

Như bạn có thể đã đoán được,

lấy mẫu quá mức chỉ đơn giản là

ngược lại với lấy mẫu dưới.

Trong kỹ thuật này, các mẫu của

tầng lớp thiểu số ngày càng tăng lên

rằng những quan sát của cả đa số và

các giai cấp thiểu số trở nên bình đẳng.

Không giống như lấy mẫu dưới mức, lấy mẫu quá mức

không liên quan đến việc xóa dữ liệu, vì vậy

không có nguy cơ mất mát

thông tin quan trọng.

Tuy nhiên, một nhược điểm của việc lấy mẫu quá mức

là nó có thể dẫn đến việc trang bị quá mức

do sự trùng lặp của

thông tin giống nhau.

Có hai cách chính để thực hiện

lấy mẫu quá mức ngẫu nhiên và

NHẸ.

Trước tiên hãy nói về

lấy mẫu ngẫu nhiên.

Như tên cho thấy, lấy mẫu quá mức ngẫu nhiên

trường hợp sao chép ngẫu nhiên

từ tầng lớp thiểu số cho đến

đạt được sự cân bằng mong muốn.

Mặc dù kỹ thuật này

rất dễ thực hiện,

nó làm tăng kích thước của tập huấn luyện,

có thể tốn kém về mặt tính toán.

Để giảm bớt mối lo ngại về việc trang bị quá mức

do sự lặp lại của các mẫu ngẫu nhiên

lấy mẫu quá mức, một cách tiếp cận khác,

NHỎ, được sử dụng.

Hãy xem những gì nó cung cấp.

SMote là viết tắt của

Kỹ thuật lấy mẫu thiểu số tổng hợp.

SMOTE dựa trên KNN

thuật toán theo mặc định.

Nó tạo ra các mẫu tổng hợp cho

giai cấp thiểu số bằng cách tạo ra mới

những trường hợp tương tự như những trường hợp hiện có.

Hãy hiểu làm thế nào

SMOTE hoạt động bằng đồ họa.

Để tạo mẫu mới

thuộc tầng lớp thiểu số,

một mẫu được rút ngẫu nhiên

từ tầng lớp thiểu số.

Đối với mẫu đã chọn,

k hàng xóm gần nhất của nó được tìm thấy.

Theo mặc định, k là năm,

nhưng điều này có thể được điều chỉnh.

Tiếp theo, trong số năm người hàng xóm,

một người hàng xóm được chọn ngẫu nhiên và

sau đó một điểm ngẫu nhiên được tạo ra trong

không gian vectơ giữa hai điểm này.

Các bước này được lặp lại cho đến khi đạt yêu cầu

số lượng mẫu thu được

Mặc dù SMote là

một kỹ thuật phổ biến để

xử lý tập dữ liệu mất cân bằng trong máy

học thì nó có những hạn chế nhất định.

Vì kỹ thuật này tạo ra

tổng hợp mẫu ngẫu nhiên,

chất lượng hoặc sự liên quan của tổng hợp

mẫu được tạo ra không được xem xét.

Các mẫu tổng hợp có thể không phải lúc nào cũng

thể hiện chính xác nội dung cơ bản

sự phân bố của tầng lớp thiểu số.

Ngoài ra, do thuật toán này

dựa trên KNN,

trong nhiều nhược điểm của KNN

cũng được phản ánh bởi kỹ thuật này.

Vậy đó là tất cả về sự khác nhau

cách cân bằng dữ liệu.

Trong video tiếp theo,

chúng tôi sẽ thực hiện tất cả các kỹ thuật này một

bằng một để cân bằng tập dữ liệu Synergx.

Sau đó chúng ta sẽ huấn luyện mô hình

với những bộ dữ liệu mới này và

đoán hiệu suất của họ.