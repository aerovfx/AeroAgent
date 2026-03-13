# 04 giá trị shapley-cho-tất-cả-bệnh-nhân

---

Chúng ta có thể tính các giá trị Shapley

cho tất cả bệnh nhân trong một tập dữ liệu.

Bằng cách sử dụng sơ đồ tóm tắt,

chúng ta có thể hình dung

sự phân phối của

những giá trị Shapley này cho

từng tính năng.

Vì vậy, đối với bệnh nhân đầu tiên,

hãy gọi họ là Bệnh nhân K,

chúng ta có thể vẽ biểu đồ của bệnh nhân

Giá trị Shapley theo tuổi.

Vậy chúng ta có 0,11,

có thể xuất hiện quanh đây và

chúng ta có thể vẽ sơ đồ của họ

Giá trị Shapley của sBP,

điều này sẽ đến

đến 0,12 và dBP,

đó là tại cùng một điểm

Chúng ta có thể làm như vậy cho

mỗi bệnh nhân như vậy ở

tập dữ liệu này để có được

sự phân bố của Shapley

giá trị cho mọi bệnh nhân.

Ở đây chúng ta có thể thấy điều đó

đặc điểm tuổi tác có

dương lớn và

giá trị tầm quan trọng tiêu cực

cho nhiều bệnh nhân

trong tập dữ liệu này.

Một thách thức ở đây là

mà chúng ta không thể nói

liệu chúng ta có

giá trị Shapley cao

cho những bệnh nhân này

bởi vì họ rất

già hoặc bởi vì họ rất

còn non hoặc hỗn hợp cả hai.

Để giải quyết điều này, chúng ta có thể

tô màu các điểm trong

cốt truyện tóm tắt dựa trên

về giá trị đặc tính.

Màu đỏ ở đây là giá trị tính năng cao,

điều đó có nghĩa là khi một

điểm có màu đỏ cho tuổi,

điều này có nghĩa là bệnh nhân đã già.

Tương tự, điểm màu xanh là

khi giá trị tính năng thấp.

Về tuổi tác, điều này có nghĩa là

một bệnh nhân còn trẻ.

Vì vậy, bài học rút ra ở đây,

hãy nói về tuổi tác là như vậy

tuổi tác là quan trọng và

góp phần làm tăng nguy cơ

khi bệnh nhân đã già.

Tuổi tác cũng quan trọng

như một tính năng và

góp phần giảm rủi ro

khi bệnh nhân còn trẻ.

Chúng ta có thể sử dụng biểu đồ tóm tắt thanh

để có được tổng thể

tầm quan trọng của một tính năng.

Chúng tôi tính toán tổng thể

tầm quan trọng bằng cách lấy

giá trị tuyệt đối của

các giá trị Shapley cho

tất cả bệnh nhân và sau đó dùng

trung bình của những

Giá trị Shapley

cho từng tính năng.

Vì vậy, theo cách đó chúng ta có được mức trung bình

về giá trị tuyệt đối của

các giá trị Shapley

và có thể nói

tuổi đó là nhiều nhất

tính năng quan trọng tổng thể,

do đó cho phép chúng tôi đi từ

các giá trị Shapley riêng lẻ để

tầm quan trọng toàn cầu

trong một dân số.

Chúng tôi đã thấy rằng phương pháp này

đòi hỏi chúng ta phải xây dựng

một số mô hình có

trong các tập con khác nhau

của các tính năng.

Có những phần mở rộng mới hơn và

việc thực hiện

Các giá trị Shapley như SHAP,

không cần đào tạo lại

của những mô hình này và có thể

thực hiện các phép tính này

các giá trị Shapley một cách hiệu quả.