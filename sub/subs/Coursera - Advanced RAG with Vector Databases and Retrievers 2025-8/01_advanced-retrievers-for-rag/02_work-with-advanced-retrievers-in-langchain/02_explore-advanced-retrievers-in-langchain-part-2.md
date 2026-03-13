# 02 khám phá-nâng cao-retrievers-in-langchain-part-2

---

Chào mừng bạn đến khám phá

chó tha mồi tiên tiến

trong LangChain, Phần 2.

Sau khi xem video này,

bạn sẽ có thể mô tả

các loại khác nhau của

Chó tha mồi LangChain,

cụ thể là đa truy vấn

người săn mồi,

trình truy xuất tự truy vấn,

và cha mẹ

người truy xuất tài liệu.

Bạn cũng sẽ có thể xác định

sự khác biệt giữa

những chú chó tha mồi này.

Một chú chó săn LangChain

là một giao diện

trả lại tài liệu dựa trên

trên một truy vấn không có cấu trúc.

Loại chó tha mồi đơn giản nhất,

cửa hàng vector

chó săn dựa trên,

lấy tài liệu

từ cơ sở dữ liệu vectơ.

Trình truy xuất nhiều truy vấn là

tương tự như vectơ

chó săn dựa trên,

ngoại trừ việc nó sử dụng LLM

để tạo ra sự khác biệt

các phiên bản của truy vấn,

tạo ra một tập hợp phong phú hơn

của các tài liệu được truy xuất.

Điều này được thực hiện để vượt qua

kết quả có thể khác nhau

điều đó có thể là kết quả của sự tinh tế

thay đổi trong từ ngữ truy vấn,

hoặc nếu phần nhúng không

nắm bắt ngữ nghĩa

của dữ liệu tốt.

Trong ví dụ cụ thể này,

một phiên bản Watson XLLM có

được tạo ra để sử dụng

Mixtral tám của

mô hình nền tảng bảy B

để tạo ra sự khác biệt

các phiên bản truy vấn

Trình truy xuất nhiều truy vấn

bản thân đối tượng là sau đó

được tạo bằng cách sử dụng

lớp truy xuất nhiều truy vấn

từ phương pháp LLM.

Phương pháp này ngoại trừ một

tham số truy xuất,

đó là vectơ

chó săn dựa

được sử dụng để lấy

kết quả cho mỗi truy vấn.

Trong ví dụ cụ thể này,

tìm kiếm tương tự đơn giản

chó săn đang được sử dụng.

Tuy nhiên, những chú chó tha mồi khác

có thể được sử dụng ở đây,

chẳng hạn như chó săn MMR.

Ngoài ra, nhiều truy vấn

lớp chó tha mồi từ

phương pháp LLM chấp nhận

một tham số LLM,

LLM ở đâu

được sử dụng để tạo ra

phiên bản thay thế của

truy vấn được chuyển vào.

Đối với mỗi truy vấn, nhiều truy vấn

chó săn lấy một bộ

của các tài liệu liên quan

và có được sự độc đáo

liên kết trên tất cả các truy vấn

để có được một bộ lớn hơn

các tài liệu liên quan tiềm năng.

Bây giờ, giả sử rằng thay vì

tài liệu đó

chỉ chứa văn bản,

bạn cũng có siêu dữ liệu

về những tài liệu này.

Nói cách khác, giả sử

tài liệu của bạn trông giống như

những cái được trình bày trong mã này.

Ở đây bạn thấy các tài liệu

chứa văn bản mô tả phim,

cũng như một số siêu dữ liệu

liên quan đến những bộ phim đó,

chẳng hạn như năm mà

bộ phim đã được phát hành,

đạo diễn của bộ phim,

và xếp hạng IMDB của phim.

Không ai trong số những người tha mồi

bạn đã nhìn

cho đến nay có khả năng

truy cập siêu dữ liệu này vì

chỉ có tài liệu

văn bản được xem xét.

Đây là nơi tự truy vấn

chó tha mồi bước vào.

Tự truy vấn

chó tha mồi chuyển đổi

truy vấn thành hai thành phần,

một chuỗi để nhìn

lên về mặt ngữ nghĩa,

và bộ lọc siêu dữ liệu

để đi cùng với nó.

Hãy thiết lập

trình truy xuất tự truy vấn.

Ô đầu tiên chuyển đổi

những tài liệu bạn vừa

cưa vào một cửa hàng vector

từ đó bạn có thể

lấy tài liệu.

Ô thứ hai mô tả

các trường siêu dữ liệu cho

các tài liệu trong

cửa hàng vector.

Chẳng hạn, năm

thuộc tính được mô tả là

một số nguyên chỉ ra

năm mà

bộ phim đã được phát hành.

Trường siêu dữ liệu này

mô tả giúp LLM

tạo ra ý nghĩa

bộ lọc siêu dữ liệu

để lựa chọn các tài liệu liên quan.

Cho một cửa hàng vector và

mô tả siêu dữ liệu,

như được mô tả ở đây,

bạn có thể lấy tài liệu

dựa vào văn bản và

siêu dữ liệu bằng cách sử dụng

lớp truy xuất tự truy vấn

từ phương pháp LLM.

Phương pháp này chấp nhận một

LLM, cơ sở dữ liệu vectơ,

mô tả tài liệu và

trường siêu dữ liệu

mô tả dưới dạng thuộc tính.

Truy xuất tài liệu

sử dụng truy vấn,

Tôi muốn xem một bộ phim

được đánh giá cao hơn 8,5,

trở lại đóng phim thành công

với xếp hạng lớn hơn 8,5.

Khi chia tài liệu

để truy xuất,

thường xuyên có

những yêu cầu mâu thuẫn nhau.

Một mặt, bạn có thể

muốn có tài liệu nhỏ

để phần nhúng của họ có thể

phản ánh chính xác

ý nghĩa của chúng.

Mặt khác, bạn muốn

tài liệu đủ dài để

bối cảnh của mỗi

đoạn được giữ lại.

Đây là nơi cha mẹ

người truy xuất tài liệu đi vào.

Trong quá trình truy xuất,

trình truy xuất tài liệu gốc

đầu tiên lấy

khối nhỏ hơn,

tra cứu ID cha mẹ của họ,

và trả về các tài liệu lớn hơn

trong đó các khối nhỏ sinh sống.

Hãy thiết lập cha mẹ

người truy xuất tài liệu.

Trình truy xuất tài liệu gốc

có hai bộ chia văn bản,

một bộ chia cha mẹ chia tách

văn bản thành lớn

các khối cần được lấy ra,

và một bộ chia con

chia tách tài liệu

thành từng phần nhỏ để tạo ra

nhúng có ý nghĩa.

Bạn cũng cần một cửa hàng vector cho

các phần nhúng và một cửa hàng

cho các tài liệu gốc.

Cuối cùng, bạn cần tạo

đối tượng truy xuất cha mẹ

và thêm tài liệu vào đó

bằng cách sử dụng phương pháp thêm tài liệu.

Trình truy xuất tài liệu gốc

có thể được gọi bằng cách sử dụng

cú pháp thống nhất tương tự như

tất cả những điều trước đây

nhìn thấy chó tha mồi.

Lưu ý rằng đối với

truy vấn chính sách hút thuốc,

tài liệu gốc

chó tha mồi lấy

khối lớn được tạo ra

bởi bộ chia cha mẹ,

không phải những khối được tạo ra

bởi bộ chia con.

Ở đây, đoạn được lấy

là chính sách hút thuốc,

chính xác truy vấn là gì

đã yêu cầu. Hãy tóm tắt lại.

Trong video này, bạn đã học được

rằng nhiều truy vấn

chó tha mồi sử dụng LLM

để tạo ra sự khác biệt

các phiên bản của truy vấn,

tạo ra một tập hợp phong phú hơn

của các tài liệu được truy xuất.

Trình truy xuất tự truy vấn

chuyển đổi truy vấn

thành hai thành phần,

một chuỗi để nhìn

lên về mặt ngữ nghĩa,

và bộ lọc siêu dữ liệu

để đi cùng nó.

Cuối cùng bạn đã học được rằng

trình truy xuất tài liệu gốc

có hai bộ chia văn bản,

một bộ chia cha mẹ chia tách

văn bản thành lớn

các khối cần được lấy ra,

và một bộ chia con

chia tách tài liệu

thành từng phần nhỏ để tạo ra

nhúng có ý nghĩa.