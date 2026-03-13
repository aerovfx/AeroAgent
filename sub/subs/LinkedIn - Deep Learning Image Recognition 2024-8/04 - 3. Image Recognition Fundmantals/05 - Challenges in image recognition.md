# 05 - Những thách thức trong nhận dạng hình ảnh

---

- Không phải mọi hình ảnh đều ở tình trạng hoàn hảo

Thật không may, để chúng tôi xử lý,

trong các dự án học sâu.

Vì vậy có một số thách thức trong việc nhận dạng hình ảnh

mà chúng ta có thể cần phải giải quyết trong cuộc sống thực.

Vậy đây là những gì?

Chà, chúng ta sẽ xử lý các điều kiện ánh sáng khác nhau,

chúng ta có thể đang giải quyết vấn đề tắc nghẽn,

chúng ta có thể đang giải quyết những biến đổi về quy mô,

chúng ta có thể đang giải quyết sự mất cân bằng giai cấp,

hoặc chúng ta có thể đang giải quyết vấn đề tương tự giữa các lớp.

Vậy còn điều kiện ánh sáng thì sao?

Vâng, điều kiện ánh sáng khác nhau

có thể ảnh hưởng đến hiệu suất nhận dạng hình ảnh.

Vì vậy chúng tôi mô phỏng các điều kiện ánh sáng khác nhau

bằng cách điều chỉnh độ sáng và độ tương phản.

Điều này giúp người mẫu học cách nhận biết đối tượng

trong các tình huống ánh sáng khác nhau.

Ví dụ: chúng tôi tạo hình ảnh

với độ sáng tăng và giảm

và hình dung chúng để hiểu tác động.

Tiếp theo là xử lý tắc nghẽn.

Vâng, tắc nghẽn là gì?

Vâng, chúng xảy ra khi một phần của một vật thể

được che đậy hoặc ẩn giấu,

khiến việc nhận dạng trở nên khó khăn hơn.

Một số kỹ thuật mà chúng ta có thể áp dụng là gì?

Vâng, mô phỏng sự tắc nghẽn

bằng cách thêm một hình chữ nhật màu đen vào hình ảnh

hoặc các hình dạng khác để che các phần của hình ảnh.

Điều này giúp người mẫu học cách nhận biết đối tượng

khi chúng bị tắc một phần.

Ví dụ: chúng tôi tạo một hình ảnh có phần tắc

và hình dung nó để xem mô hình xử lý nó như thế nào.

Tiếp theo, là các biến thể quy mô.

Các đối tượng có thể xuất hiện ở các tỷ lệ khác nhau trong ảnh,

ảnh hưởng đến việc nhận dạng.

Kỹ thuật để giải quyết vấn đề này là gì?

Vâng, chúng tôi hiển thị ví dụ về hình ảnh ở các tỷ lệ khác nhau

bằng cách thay đổi kích thước chúng.

Điều này giúp người mẫu học cách nhận biết đối tượng

bất kể kích thước của chúng trong hình ảnh.

Ví dụ: chúng tôi tạo hình ảnh được phóng to và thu nhỏ

và hình dung chúng để hiểu tác động

của các biến thể quy mô.

Làm thế nào để đối phó với sự mất cân bằng giai cấp?

Mặc dù một số lớp có thể có nhiều mẫu hơn những lớp khác,

ví dụ, chúng ta có thể có nhiều mèo hơn chó,

we might have more airplanes than horses, et cetera.

Điều này dẫn đến các mô hình sai lệch.

Vâng, chúng ta phải làm gì với nó?

Chúng tôi hình dung sự phân bố lớp

và sử dụng các kỹ thuật như tăng cường dữ liệu

hoặc lấy mẫu lại để cân bằng các lớp.

Ví dụ: chúng tôi vẽ biểu đồ phân phối

của mỗi lớp trong tập dữ liệu

để xác định bất kỳ sự mất cân bằng nào và thảo luận về các giải pháp khả thi.

Làm thế nào về sự tương đồng giữa các lớp?

Vâng, các lớp tương tự có thể bị nhầm lẫn bởi mô hình.

Những hình ảnh giống nhau, như thể cả hai đều là động vật,

chó và mèo có thể bị nhầm lẫn với nhau

bởi vì máy bay rõ ràng khác nhiều so với một con chó.

Nếu so sánh sự giống nhau

giữa con mèo và con chó chẳng hạn.

Vâng, kỹ thuật là gì?

Chúng tôi minh họa cách các lớp tương tự

có thể bị nhầm lẫn bởi mô hình

và đưa ra ví dụ về các lớp này.

Ví dụ: chúng tôi hiển thị hình ảnh của các lớp tương tự,

chẳng hạn như mèo và chó,

để làm nổi bật việc mô hình có thể khiến họ bối rối như thế nào

và thảo luận các cách để cải thiện sự khác biệt.

Vâng, trong phiên này,

chúng tôi đã thảo luận về những thách thức khác nhau trong việc nhận dạng hình ảnh,

và chúng ta sẽ tiếp tục và chứng minh

những kỹ thuật này trong mã Python

về cách chúng ta có thể xử lý chúng một cách hiệu quả.

Vâng, những thách thức này bao gồm

xử lý các điều kiện ánh sáng khác nhau,

xử lý tắc nghẽn, quản lý các biến thể quy mô,

và giải quyết sự mất cân bằng giai cấp,

và hiểu sự tương đồng giữa các lớp.

Bằng cách giải quyết những thách thức này,

chúng ta có thể xây dựng mạnh mẽ hơn

và hệ thống nhận dạng hình ảnh chính xác.

Bây giờ, hãy tiếp tục và áp dụng chúng vào mã.

Bây giờ, như mọi khi,

chúng ta đi đến tệp 03_05_begin.python

và nhìn vào khung mã.

Vì vậy, chúng tôi thực sự sẽ tập trung

về những thách thức trong việc nhận dạng hình ảnh trong mã của chúng tôi.

Chúng ta sẽ giải quyết các điều kiện ánh sáng khác nhau,

xử lý tắc nghẽn, biến thể quy mô.

Chúng ta sẽ giải quyết vấn đề mất cân bằng giai cấp

và sự tương đồng giữa các lớp.

Vậy chúng ta hãy đi thôi.

Hãy minh họa những điểm này.

Đầu tiên, hãy bắt đầu với việc nhập thư viện,

GPU bị vô hiệu hóa, tải tập dữ liệu, chuẩn hóa tập dữ liệu,

chuyển đổi nhãn lớp thành các vectơ được mã hóa một lần.

Xác định thư mục đầu ra,

xác định thư mục cốt truyện,

tạo ra mô hình.

Sau đó, biên dịch mô hình, huấn luyện mô hình,

đánh giá mô hình như chúng tôi đã làm trước đây.

Vì vậy, đây chỉ là sự chuyển giao các số liệu gây nhầm lẫn

và mã báo cáo phân loại từ phiên trước của chúng tôi.

Tiếp theo là cốt lõi của cuộc thảo luận về thách thức này.

Vì vậy, chúng ta sẽ bắt đầu với việc giải quyết

với các điều kiện ánh sáng khác nhau trước tiên.

Vì vậy, chúng ta hãy tiếp tục

và xác định một hàm để xử lý

điều kiện ánh sáng khác nhau.

Đây là thử thách số một của chúng tôi.

Chúng ta hãy tiếp tục và đánh số đó

thế là chúng ta có một bản đồ để tham khảo lại.

Bây giờ chúng ta bắt đầu với chức năng này

và chúng tôi bắt đầu cung cấp thông tin đầu vào.

Đầu vào sẽ là hình ảnh

và sau đó chúng ta sẽ có alpha=1.0

và sau đó beta=0,0,

đóng dấu ngoặc đơn rồi tiếp tục thêm nó vào.

Vì vậy đây là cả hai giá trị dòng chảy

và chúng ta cũng có thể

tiến về phía trước và quay trở lại

np, là thư viện NumPy của chúng tôi, .clip

hình ảnh nhân alpha

+ beta, 0, 1.

Và sau đó chúng ta sẽ tiếp tục và tạo ra hình ảnh tươi sáng

và hình ảnh tối,

thì chúng ta sẽ tiếp tục và lưu những thứ này,

và sau đó chúng ta sẽ có thể

để xem chúng sau đó trong thư mục đã lưu.

Hoàn hảo.

Vì vậy, tiếp theo chúng ta sẽ bắt đầu xử lý các tắc nghẽn.

Vì vậy chúng ta có rất nhiều thứ cần phải giải quyết,

đó là lý do tại sao chúng tôi đang sử dụng một số thư viện tích hợp

để làm cho nó nhanh hơn một chút.

Vì vậy chúng ta sẽ tiếp tục và xử lý những điều này

bằng cách tạo hàm add_occlusion,

và sau đó chúng ta sẽ nói hình ảnh,

x, y, chiều rộng và chiều cao.

Và đây là hình ảnh bị che khuất.

Nó sẽ là một image.copy,

vì vậy chúng ta sẽ tiếp tục và sao chép hình ảnh.

Và sau đó chúng ta sẽ có một điểm tắc trong hình ảnh này,

đó là occluded_image.

Sau đó chúng ta sẽ tiếp tục và chèn tắc đó

đến x và sau đó là x+width,

đó là một trong những đầu vào.

Hãy tiếp tục và đảm bảo chúng ta viết đúng chính tả

và sau đó là y:+chiều cao.

Sau đó tiếp theo chúng ta tiếp tục và hoàn thành việc đó

và sau đó = 0.

Sau đó, những gì chúng tôi làm là trả về occluded_image.

Vì vậy, đây thực sự là thêm một lớp che khuất vào hình ảnh của chúng ta.

Tiếp theo, chúng ta sẽ tiếp tục và áp dụng điều này

cũng như lưu cái này vào thư mục của chúng tôi

để chúng ta có thể tiếp tục và xem nó đã làm gì,

nó đã thêm vào tắc gì.

Tiếp theo là ví dụ về tỷ lệ,

vì vậy chúng ta hãy tiếp tục và chuyển sang phần thứ ba.

Một lần nữa, chúng ta sẽ tạo một hàm khác cho việc này,

sẽ được thay đổi kích thước,

rescale_image.

Vì vậy, hình ảnh, tỷ lệ.

Và rồi nó sẽ quay trở lại,

hãy đảm bảo rằng vết lõm là chính xác,

và sau đó chúng ta sẽ nói TensorFlow.image.resize,

đó là một chức năng thực sự thuận tiện trong trường hợp này.

Và sau đó chúng ta sẽ tiếp tục

và hoàn thành chức năng thay đổi kích thước ở đây.

Hãy tiếp tục và sửa nó.

Sau đó chúng ta sẽ đi tiếp

và tạo ra những hình ảnh thu nhỏ từ điều này,

và sau đó chúng ta sẽ cứu họ

vào sc_variations.png.

Vì vậy, tiếp theo chúng ta sẽ giải quyết vấn đề mất cân bằng giữa các lớp.

Vì vậy chúng tôi sẽ chỉ ra các kỹ thuật phân phối lớp

để giải quyết vấn đề này.

Vì vậy, hãy tiếp tục và bắt đầu xác định điều đó.

Sẽ là 4 đối phó với sự mất cân bằng trong lớp.

Hãy tiếp tục và xem sự cân bằng

trong dữ liệu hiện tại của chúng tôi.

Vì vậy chúng ta sẽ tiếp tục và lưu nó vào phần phân phối của lớp.

Vì vậy, nó sẽ có y-train NumPy.sum,

nó sẽ tạo ra một biểu đồ thanh

hiển thị phân phối lớp hiện có mà chúng tôi có.

Sau đó chúng ta cũng sẽ giải quyết vấn đề mất cân bằng giai cấp,

bao gồm cả việc sửa chúng

như lấy mẫu quá mức hoặc lấy mẫu dưới mức, v.v.

Tiếp theo, chúng ta thực sự sẽ có sự tương đồng giữa các lớp.

Vì vậy, đây lại là việc chúng ta tạo một hàm mới,

sẽ là display_similar_images.

Nó sẽ lấy hình ảnh, nhãn, class_1 và class_2,

và nó sẽ xem những hình ảnh nào giống nhau.

Ví dụ, trong trường hợp này chúng ta sẽ

nhìn vào hình ảnh mèo và chó giống nhau.

Rồi cuối cùng, chúng ta sẽ tiếp tục

và giới thiệu hình ảnh chó và mèo

trong thư mục đầu ra.

Tuyệt vời.

Vì vậy nếu bạn làm theo,

hãy tiếp tục và chạy nó.

Tôi biết đây là một đoạn mã Python khá dài,

vì vậy bạn cũng có thể chọn đi

đến mã python 03_05_end

và chỉ cần tiếp tục và chạy nó,

và sau đó bạn sẽ thấy nó sẽ tạo ra tất cả các kết quả đầu ra này

cho chúng tôi sau khi chạy một số kỷ nguyên.

Và sau đó chúng ta sẽ có thể tiếp tục

và hình dung tất cả những kỹ thuật này

mà chúng ta đã từng giải quyết các thử thách,

và sau đó chúng ta sẽ có thể thấy sự khác biệt

dựa trên những gì nó đã làm.

Vì vậy sau vài phút,

chúng ta có thể thấy tệp 03_05_end.python đã chạy xong.

Như chúng ta thấy rằng các ô của chúng ta đã được lưu vào vị trí

mà chúng ta đã xác định,

ở ngay đây,

và chúng được cấu hình gọn gàng khi bắt đầu

với 03_05_lighting_conditions.

Vì vậy, đây là, ví dụ,

cách chúng ta xử lý các điều kiện ánh sáng.

Vì vậy, chúng tôi làm cho hình ảnh nhẹ hơn một chút,

tối hơn một chút để cung cấp sự đa dạng

để mô hình của chúng tôi huấn luyện tốt hơn

với các điều kiện ánh sáng khác nhau.

Đây là một ví dụ về một hình ảnh bị che khuất.

Bạn thấy rằng chúng tôi thực sự đã tạo ra một hình tam giác

chặn một phần hình ảnh

để chúng tôi cải thiện sự đa dạng

của những hình ảnh chúng tôi cung cấp cho tập dữ liệu

để người mẫu biết phải làm gì

khi nó nhìn thấy một hình ảnh bị che khuất.

Đây là ví dụ về hình ảnh được thu nhỏ ở bên trái

và hình ảnh được phóng to ở bên phải,

và bạn có thể thấy sự khác biệt của độ phân giải.

Một lần nữa, điều này giúp mô hình thấy được các kích cỡ khác nhau,

hình ảnh thu nhỏ khác nhau

và các hình ảnh thu nhỏ khác nhau

nhằm nâng cao tính đa dạng của mô hình

để nó hoạt động tốt hơn với các bộ dữ liệu khác nhau.

Đây là điểm tương đồng giữa hình ảnh mèo và chó.

Nó thực sự nhận thấy rằng một số lớp học,

như chúng ta đã nói,

giống nhau hơn các lớp khác,

và ở đây chúng tôi đang giới thiệu điều đó

mèo và chó khá giống nhau.

Điều đó tóm tắt các kỹ thuật của chúng tôi

về cách chúng ta giải quyết những thách thức chung

mà chúng ta phải đối mặt với việc học sâu

và một số giải pháp mà chúng tôi có thể thực hiện.