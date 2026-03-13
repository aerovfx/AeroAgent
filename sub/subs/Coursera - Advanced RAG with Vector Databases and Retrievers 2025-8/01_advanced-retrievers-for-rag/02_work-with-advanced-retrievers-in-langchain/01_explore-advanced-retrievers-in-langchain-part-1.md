# 01 khám phá-nâng cao-retrievers-in-langchain-part-1

---

[ÂM NHẠC]

Chào mừng bạn đến với Khám phá Advanced Retrievers

trong LangChain, phần một. Sau

xem video này, bạn sẽ có thể

giải thích công cụ truy xuất LangChain là gì.

Bạn cũng sẽ có thể mô tả

công cụ truy tìm dựa trên cửa hàng vector và

giải thích cách nó hoạt động.

Hãy bắt đầu bằng sự hiểu biết

công cụ truy tìm LangChain là gì.

Công cụ truy xuất LangChain là một giao diện

trả về tài liệu dựa trên

một truy vấn không có cấu trúc.

Nó tổng quát hơn một cửa hàng vector.

Nó không nhất thiết phải lưu trữ tài liệu

vì mục đích của nó là lấy chúng hoặc

khối của họ.

Một công cụ truy tìm LangChain chấp nhận

một truy vấn chuỗi làm đầu vào và

trả về một danh sách các tài liệu hoặc

khối làm đầu ra.

Mặc dù quá trình

lấy dữ liệu nghe có vẻ đơn giản,

nó có thể phức tạp một cách tinh tế với

một số triển khai có thể.

Hãy cùng tìm hiểu thêm về cách đơn giản nhất

loại chó săn vector

công cụ truy xuất dựa trên cửa hàng để truy xuất

tài liệu từ cơ sở dữ liệu vector.

Hãy nhớ lại rằng cơ sở dữ liệu vector này là

được đưa vào tồn tại bằng cách tải nguồn

tài liệu, chia chúng thành nhiều phần,

và nhúng chúng.

Các phích cắm tha mồi dựa trên cửa hàng vector

vào kho vector hiện có này.

Nó chấp nhận một truy vấn và

truy xuất dữ liệu giống nhau nhất,

trong trường hợp này là những phần giống nhau nhất.

Công cụ truy tìm dựa trên cửa hàng vector

hoạt động bằng cách nhúng truy vấn và

sau đó so sánh nó với nhúng

các khối bằng cách sử dụng tìm kiếm tương tự hoặc

mức độ liên quan cận biên tối đa, còn được gọi là

MMR, để lấy các đoạn có liên quan nhất.

Công cụ truy xuất dựa trên cửa hàng vector là

đơn giản dễ hiểu vì nó truy vấn

một cửa hàng vector hiện có và

không yêu cầu LLM để

lấy ra những đoạn giống nhau nhất.

Ngoài việc sử dụng điểm tương đồng,

bạn có thể sử dụng biên tối đa

truy xuất liên quan hoặc MMR.

MMR trong cửa hàng vector là một kỹ thuật

được sử dụng để cân bằng giữa mức độ liên quan và

sự đa dạng của kết quả truy xuất.

Nó chọn các tài liệu có cả hai

rất phù hợp với truy vấn và

tối thiểu giống với

tài liệu đã chọn trước đó.

Cách tiếp cận này giúp

tránh sự dư thừa và

đảm bảo phạm vi bao phủ toàn diện hơn

các khía cạnh khác nhau của truy vấn.

Trong ví dụ cụ thể này,

kết quả chính sách email truy vấn

trong ba tài liệu được lấy ra.

Hãy tóm tắt lại.

Trong video này, bạn đã biết rằng Lanchain

Retriever là một giao diện trả về

tài liệu dựa trên một truy vấn phi cấu trúc.

Nó có một số loại.

Công cụ truy xuất dựa trên cửa hàng vector là một

loại như vậy lấy tài liệu từ

cơ sở dữ liệu vectơ.

Nó có thể được tạo trực tiếp từ vector

lưu trữ đối tượng bằng phương thức truy xuất bằng cách

sử dụng tìm kiếm tương tự hoặc MMR.

Tìm kiếm tương tự là khi

người truy tìm chấp nhận một truy vấn và

truy xuất dữ liệu giống nhau nhất.

MMR là một kỹ thuật được sử dụng để

cân bằng giữa sự liên quan và

sự đa dạng của kết quả truy xuất.