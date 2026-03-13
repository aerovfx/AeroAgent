# 03 - Cắt chuyển màu

---

- [Người hướng dẫn] Cắt chuyển màu là

một kỹ thuật được sử dụng trong học sâu

để ngăn chặn độ dốc của mô hình

trở nên quá lớn trong quá trình đào tạo.

Hiện tượng này được gọi là độ dốc bùng nổ

xảy ra khi độ dốc của hàm mất mát

các tham số của mô hình tương ứng

phát triển quá lớn trong quá trình nhân giống ngược,

điều này có thể làm mất ổn định việc đào tạo gây ra các vấn đề về số lượng

và ngăn chặn mô hình khỏi

hội tụ về một giải pháp tối ưu.

Cắt bớt gradient giải quyết vấn đề này bằng cách đặt một giới hạn

hoặc giới hạn mức độ chuyển màu có thể lớn đến mức nào.

Có hai cách tiếp cận chính để cắt gradient,

cắt theo giá trị và cắt theo định mức.

Khi cắt theo giá trị, mỗi gradient riêng lẻ

được cắt bớt để nó không vượt quá

một giá trị tối thiểu hoặc giá trị tối đa cụ thể.

Chúng ta hãy xem qua một ví dụ đơn giản về cách thức hoạt động của nó.

Giả sử chúng ta có một vectơ gradient G

với giá trị hai, âm sáu,

tám, âm ba và năm

với ngưỡng gradient C được đặt thành bốn.

Điều này có nghĩa là giá trị lớn hơn tối thiểu được phép là

bốn âm và bốn tối đa.

Đối với mỗi gradient GI trong G, nếu giá trị

lớn hơn 4, nó sẽ bị cắt thành 4,

và nếu giá trị nhỏ hơn âm 4,

nó sẽ bị cắt xuống còn âm 4.

Do đó, với ngưỡng là bốn.

Cắt vectơ gradient theo giá trị

dẫn đến vectơ có giá trị hai, âm bốn,

bốn, âm ba và bốn.

Ngoài ra, thay vì cắt bớt các gradient riêng lẻ,

cắt theo định mức hạn chế kích thước tổng thể

hoặc chuẩn của vectơ gradient tới ngưỡng cực đại C.

Nếu tổng định mức vượt quá C, tất cả các gradient trong vectơ

được thu nhỏ lại theo tỷ lệ, do đó chuẩn bằng C.

Định mức L hai của vectơ gradient G được tính toán

như được hiển thị ở đây, trong đó GI đại diện cho mỗi

của các gradient cuối cùng trong vectơ.

Nếu L hai chuẩn của vectơ gradient

vượt quá ngưỡng tối đa C,

sau đó vectơ được chia tỷ lệ bởi

một yếu tố được tính toán như được hiển thị ở đây.

Chúng ta hãy xem qua một ví dụ đơn giản về cách thức hoạt động của nó.

Giả sử chúng ta có một vectơ gradient G với các giá trị

hai, âm sáu, tám, âm ba và năm

với ngưỡng gradient C được đặt thành sáu.

Chuẩn L hai của vectơ gradient

sẽ là khoảng 11 giờ 75.

Vì 11,75 lớn hơn ngưỡng 6 này,

vectơ cần phải được thay đổi kích thước.

Với giá trị ngưỡng sáu và L hai chỉ tiêu là 11,75,

hệ số tỷ lệ sẽ xấp xỉ là 0,51.

Mỗi gradient trong vectơ là

nhân với hệ số tỷ lệ,

dẫn đến vectơ có giá trị

1,02, âm 3,06, 4,08,

âm 1,53 và 2,55.

Ở mức cao hơn, bạn chọn cắt theo giá trị,

nếu bạn cần một cách tiếp cận đơn giản để hạn chế độ dốc

và không muốn tính toán các chỉ tiêu

hoặc khi bạn cần giới hạn độ lớn

của các thành phần gradient riêng lẻ

để tránh cập nhật mạnh mẽ các thông số cụ thể.

Mặt khác, việc cắt bớt theo định mức sẽ phù hợp hơn

cho những tình huống quan trọng

để duy trì hướng tương đối của vectơ gradient

trong khi kiểm soát độ lớn tổng thể của nó,

đảm bảo cập nhật nhất quán trên tất cả các thông số.

Tóm lại, sự lựa chọn giữa việc cắt theo giá trị

và cắt theo định mức phụ thuộc vào đặc điểm cụ thể

mô hình của bạn, thiết lập đào tạo,

và loại bất ổn mà bạn đang gặp phải.

Cắt gradient mang lại một số lợi ích

điều đó làm cho nó trở thành một công cụ có giá trị trong học sâu.

Một trong những ưu điểm chính của nó là

rằng nó ổn định quá trình đào tạo

bằng cách giới hạn kích thước của độ dốc,

nó ngăn chặn việc cập nhật thất thường các tham số mô hình

dẫn đến sự hội tụ mượt mà hơn.

Sự ổn định này đặc biệt có lợi

cho mạng sâu và mạng thần kinh tái phát

nơi độ dốc bùng nổ phổ biến hơn

do chuỗi lan truyền ngược dài

qua nhiều lớp hoặc dấu thời gian.

Việc cắt chuyển màu cũng đi kèm với một số hạn chế nhất định.

Mặc dù nó giải quyết hiệu quả độ dốc bùng nổ,

nó không giải quyết được nguyên nhân cơ bản của vấn đề

chẳng hạn như khởi tạo trọng lượng kém

hoặc một kiến trúc mô hình không phù hợp.

Điều này có nghĩa là việc cắt gradient

có thể hoạt động như một giải pháp băng bó,

che giấu các vấn đề sâu sắc hơn trong quá trình thiết lập đào tạo.

Ngoài ra, hiệu quả của nó phụ thuộc vào việc lựa chọn

ngưỡng cắt thích hợp,

điều này không phải lúc nào cũng đơn giản,

và thường đòi hỏi phải thử nghiệm cẩn thận để tối ưu hóa.