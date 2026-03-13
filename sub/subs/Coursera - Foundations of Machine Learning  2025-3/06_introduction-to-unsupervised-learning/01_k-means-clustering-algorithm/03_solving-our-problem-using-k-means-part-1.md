# 03 giải-vấn-đề-bằng-k-nghĩa-phần-1

---

Tôi chắc chắn rằng bạn rất hào hứng khi xây dựng

máy không được giám sát đầu tiên của bạn

mô hình học tập sử dụng

thuật toán K-means.

Hãy nhanh chóng nhớ lại một báo cáo vấn đề

trước khi chúng ta bắt đầu quá trình

xây dựng mô hình.

Synergix Solutions đã phát hiện ra rằng

chiến lược tiếp thị của nó dựa trên

các phân khúc hiện có

không hiệu quả lắm.

Họ muốn dùng thử gói thời đại mới

chiến lược tiếp thị trực tuyến sẽ

yêu cầu họ nhóm các sản phẩm tương tự

với nhau không phân biệt phân khúc.

Để thực hiện phân cụm bằng K-mean

bạn sẽ làm theo các bước sau.

Đầu tiên, chúng tôi sẽ tải tập dữ liệu,

sau đó chúng tôi sẽ thực hiện lựa chọn tính năng và

xử lý trước dữ liệu.

Sau đó,

chúng tôi sẽ áp dụng phân cụm K-mean và

tìm giá trị tối ưu của K, và

sau đó đánh giá và giải thích các cụm.

Vì vậy, hãy bắt đầu bằng cách nhập

các thư viện đầu tiên.

Thay đổi thư mục làm việc thành

nơi chúng tôi đã lưu trữ tập dữ liệu.

Bây giờ, bước đầu tiên là

để đọc tập dữ liệu.

Chúng tôi đã cung cấp bộ dữ liệu

trong phần tài nguyên bên dưới.

Đây là tập dữ liệu chúng tôi sẽ

sử dụng xuyên suốt mô-đun này,

vì vậy hãy đảm bảo bạn tải xuống trước khi chúng ta bắt đầu.

Giống như chúng tôi đã làm trước đó, chúng tôi sẽ

bắt đầu với một tập dữ liệu đã được xử lý một phần,

tương tự như những gì chúng tôi đã sử dụng

trong các mô-đun trước đó.

Vì vậy, hãy nhanh chóng đọc dữ liệu.

Hãy nhìn vào cái đầu tiên

năm hàng dữ liệu.

Bây giờ chúng ta đã có ý tưởng về dữ liệu của mình,

hãy chuyển sang bước tiếp theo,

tức là tiền xử lý và

lựa chọn tính năng.

Đây là bước rất quan trọng để

báo cáo vấn đề khi chúng tôi phải xử lý

dữ liệu và tìm các tính năng để thực hiện

dữ liệu phù hợp cho vấn đề của chúng tôi.

Chúng tôi muốn tìm sản phẩm hoặc

SK_ ID tương tự nhau.

Hãy sắp xếp dữ liệu của chúng tôi theo SKU_ID và

ngày để hiểu dữ liệu tốt hơn.

Như bạn có thể thấy từ dữ liệu được sắp xếp,

mỗi hàng dữ liệu đại diện

sự kết hợp của tuần và SKU_ID.

Nếu chúng tôi muốn tìm SKU_ID tương tự,

chúng ta nên tổng hợp tất cả các giá trị để

mà mỗi hàng đại diện

thông tin về SKU_ID duy nhất.

Ngoài ra, như bạn đã

biết về học máy,

nếu chúng ta cung cấp dữ liệu chất lượng kém vào mô hình của mình,

chúng ta chắc chắn sẽ nhận được kết quả tồi tệ.

Điều này có nghĩa là,

nếu bạn cung cấp cho nó dữ liệu không liên quan,

thì đầu ra cũng sẽ không liên quan.

Mục tiêu của chúng tôi là tạo ra một thời đại mới

chiến lược tiếp thị trực tuyến trọn gói dành cho

những sản phẩm tương tự nhau.

Khi chúng tôi nói những sản phẩm tương tự,

có một số yếu tố nhất định

ngay lập tức hiện lên trong tâm trí chúng ta phải không?

Giống như quy mô sử dụng sản phẩm, trường hợp

sản phẩm, thông tin liên quan đến bán hàng,

xếp hạng và đánh giá, v.v.

nhiều yếu tố linh tinh khác.

Hãy cùng xác minh chéo những tính năng nào trong số này

có sẵn bằng cách đi qua danh sách

các tính năng và lựa chọn các tính năng có liên quan

các tính năng để xây dựng mô hình của chúng tôi.

Có vẻ như tập dữ liệu bán xử lý của chúng tôi có

không có thông tin liên quan đến kích thước của

sản phẩm.

Mặc dù đây có thể là thông tin có liên quan,

nó không cần thiết trong thế giới thực

kịch bản để có tất cả các dữ liệu có ích.

Hãy chuyển sang yếu tố tiếp theo.

Tiếp đến là trường hợp sử dụng của sản phẩm.

Từ tập dữ liệu của chúng tôi, chúng tôi có một phân khúc

cột có ba loại,

chăm sóc tóc, chăm sóc da và trang điểm,

mà mỗi sản phẩm thuộc về.

Nhưng nếu bạn nhớ lại,

một trong những điểm rút ra lớn từ chúng tôi

tuyên bố vấn đề là hiện tại

Chiến lược tiếp thị dựa trên

các phân khúc có sẵn không hiệu quả.

Và những chiến lược mới cần thiết

được kết hợp cho

các sản phẩm không phân biệt

các phân khúc của họ.

Như vậy, do phân khúc

sự kém hiệu quả và

cũng nên nhớ rằng bao gồm cả điều này

tính năng phân khúc trong các tính năng đã chọn của chúng tôi

có thể khiến mô hình của chúng tôi bị sai lệch

hướng tới những phân khúc có sẵn này,

chúng ta đừng thêm tính năng này vào

trong khi chúng tôi xây dựng mô hình của mình.

Tiếp theo chúng ta hãy tìm

các thông tin liên quan đến bán hàng.

Không còn nghi ngờ gì nữa, điều quan trọng là phải

hiểu sản phẩm nào đã mang lại

doanh thu cao nhất và trong số đó

các sản phẩm đã không hoạt động tốt.

Hãy cùng xem danh sách của chúng tôi

cột có thông tin như vậy.

Thật tuyệt vời, chúng tôi có các cột

như Đơn giá, Doanh thu,

Đơn vị đã bán, cung cấp tất cả

thông tin chúng tôi yêu cầu, phải không?

Nhưng câu hỏi là,

chúng ta có cần cả ba thứ đó không?

Ờ, không hẳn,

bởi vì bằng cách chia tổng doanh thu cho

một sản phẩm theo đơn giá của nó,

chúng ta có thể có được các đơn vị được bán.

Vì vậy, cột đơn vị bán không thực sự

mang lại bất kỳ giá trị gia tăng nào với nó

đưa vào quá trình xây dựng mô hình của chúng tôi.

Như đã thảo luận,

chúng ta sẽ cần tổng hợp các giá trị cho

các tính năng được lựa chọn của chúng tôi vì vậy

rằng mỗi hàng có một SKU_ID duy nhất.

Đối với cột Doanh thu, lưu ý rằng

chúng ta sẽ chọn phần tóm tắt

giá trị vì doanh thu có xu hướng tăng thêm

tăng lên trong nhiều tuần trong tập dữ liệu của chúng tôi.

Mặt khác, trong trường hợp đơn giá,

chúng tôi sẽ chỉ chọn mục nhập dữ liệu cuối cùng,

vì những giá trị này không cộng lại hoặc

thay đổi qua các tuần.

Hãy thêm các cột này

vào các tính năng đã chọn của chúng tôi.

Hãy chuyển sang yếu tố tiếp theo,

đó là đánh giá và xếp hạng.

Chúng tôi có đánh giá khá chi tiết cho

mỗi sản phẩm,

xếp hạng từ một đến năm sao.

Nhưng đợi một chút, những xếp hạng này

có thể được coi là tích lũy

xếp hạng cho đến một ngày nhất định,

khi mọi người thực sự đánh giá một sản phẩm.

Vì vậy, chúng ta có thể đánh giá dựa trên

mục nhập ngày cuối cùng từ tập dữ liệu của chúng tôi.

Bây giờ chúng ta hãy xem các tính năng khác

từ tập dữ liệu của chúng tôi sẽ

có liên quan đến việc xây dựng mô hình của chúng tôi.

Vì vậy chúng tôi có một cột như vậy

như Số lượng tiêu đề, Số lượng hình ảnh,

Số lượng đạn và độ dài mô tả.

Tiêu đề thường là phần đầu tiên của

thông tin mà người mua tiềm năng đọc được.

Độ dài tiêu đề tối ưu đảm bảo

sản phẩm được mô tả

hiệu quả mà không cần

choáng ngợp người đọc.

Tương tự, việc kết hợp những thứ khác

các tính năng, chẳng hạn như số lượng hình ảnh,

số lượng dấu đầu dòng và độ dài mô tả

khi xem xét tiếp thị trực tuyến

Chiến lược đóng gói sản phẩm có thể

nâng cao sự hiểu biết của khách hàng và

nhận thức về ưu đãi đi kèm.

Những giá trị này cũng không thay đổi theo thời gian.

Vì vậy, khi lựa chọn những đặc điểm này,

giống như chúng ta đã làm trước đó,

chúng tôi sẽ chỉ chọn cái cuối cùng

mục nhập ngày tháng từ tập dữ liệu.

Vì vậy, hãy thêm phần này vào cột chúng ta sẽ có

lựa chọn cho một quá trình xây dựng khuôn.

Tập dữ liệu của chúng tôi có một vài

cột thú vị hơn,

chẳng hạn như Xếp hạng tìm kiếm không phải trả tiền và

Lưu lượng truy cập trang.

Thứ hạng tìm kiếm không phải trả tiền đề cập đến việc không trả tiền

kết quả tìm kiếm được tạo ra

bởi công cụ tìm kiếm.

Các tính năng tương tự khác liên quan đến

hoạt động trực tuyến là những cú nhấp chuột trực tuyến,

chi phí trực tuyến, số lần hiển thị trực tuyến và

lưu lượng truy cập trang.

Lưu lượng truy cập trang có thể là một dấu hiệu

rằng nội dung hoặc

sản phẩm trên trang đó

đang gây được tiếng vang với người dùng.

Vì vậy, chúng tôi chỉ có thể chọn lưu lượng truy cập trang

thay vì bốn tính năng khác nhau,

sẽ phục vụ mục đích của chúng tôi.

Vậy chúng ta hãy tiếp tục và

thêm lưu lượng truy cập trang vào các tính năng đã chọn của chúng tôi.

Khi chúng tôi chọn các tính năng,

bước tiếp theo là tạo

một tập dữ liệu tổng hợp sử dụng

những tính năng này như đã thảo luận.

Ở đây,

chúng tôi đã chọn các tính năng có liên quan và

sau đó nhóm chúng theo SKU_ID trong

để loại bỏ các bản sao.

Vì vậy, bây giờ chúng tôi có một hàng cho mỗi SKU_ID

với tất cả các tính năng được lựa chọn.

Chúng tôi đã đặt tên cho dữ liệu này

frame dưới dạng Dữ liệu được chọn.

Hãy xem tập dữ liệu tổng hợp.

Lựa chọn tính năng đăng bài,

dữ liệu khung dữ liệu của chúng tôi đã chọn,

có 239 hàng và 13 cột trong đó.

Hãy nhanh chóng kiểm tra xem có

các giá trị bị thiếu trong tập dữ liệu của chúng tôi trước khi chúng tôi

áp dụng phân cụm K-mean cho nó.

Vì vậy, không có bất kỳ giá trị nào bị thiếu trong

tập dữ liệu, nhưng bạn có nhận thấy điều gì không?

Các giá trị trong tập dữ liệu không

chính xác trong cùng một phạm vi.

Mặc dù cột doanh thu tính bằng triệu,

kết quả tìm kiếm không phải trả tiền lên tới hàng trăm.

Như chúng ta đã thảo luận, K-mean hoạt động

dựa trên tiêu chí khoảng cách.

Vì vậy chúng tôi khuyên bạn nên mở rộng quy mô

tập dữ liệu trước khi áp dụng K-mean

ma trận khoảng cách có thể

được tính toán chính xác.

Vì vậy, chúng ta hãy tiếp tục và

chia tỷ lệ dữ liệu của chúng tôi bằng cách sử dụng bộ chia tỷ lệ tiêu chuẩn.

Hãy nhìn vào dữ liệu bây giờ.

Bây giờ phạm vi của tất cả các số của chúng tôi

các cột có tỷ lệ tương tự.

Chúng tôi đã hoàn thành thành công tất cả

quá trình tiền xử lý cần thiết trên tập dữ liệu của chúng tôi.

Hãy ghi nhớ, xử lý và

lựa chọn tính năng là một trong những điều quan trọng nhất

các giai đoạn quan trọng trong máy của bạn

quá trình xây dựng mô hình học tập.

Điều này quyết định chất lượng của bạn

dự đoán dựa trên lựa chọn

tính năng.

Trong video tiếp theo,

chúng tôi sẽ tiếp tục làm theo các bước của

xây dựng mô hình bằng thuật toán K-mean.

Hẹn gặp bạn ở đó.