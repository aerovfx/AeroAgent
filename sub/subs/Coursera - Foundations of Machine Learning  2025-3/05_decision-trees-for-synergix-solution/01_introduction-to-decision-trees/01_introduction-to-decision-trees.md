# 01 cây giới thiệu cây quyết định

---

Xin chào các bạn học viên,

chào mừng bạn đến với mô-đun tiếp theo của khóa học của chúng tôi.

Trong mô-đun này, chúng ta sẽ khám phá phần tiếp theo

thuật toán học máy phổ biến,

cây quyết định.

Cây quyết định là một trụ cột

thuật toán trong học máy,

không chỉ vì cấu trúc đơn giản của nó,

nhưng bởi vì nó phục vụ như

một mô hình nền tảng cho hầu hết

mô hình học máy tiên tiến.

Trong khi các mô hình tuyến tính mà chúng tôi

đã học ở module trước

giúp chúng tôi hiểu biết

mối quan hệ tuyến tính,

cây quyết định tốt hơn

tìm các mẫu phi tuyến tính.

Vì vậy chúng ta hãy bắt đầu với sự hiểu biết

cây quyết định là gì

>> Diễn giả 2: Cây quyết định là

một thuật toán học máy cơ bản.

Về cốt lõi, nó là một sơ đồ như

cấu trúc hỗ trợ việc ra quyết định.

Nó phá vỡ một quyết định phức tạp

thành một chuỗi các quyết định đơn giản hơn,

cái có thể được hình dung

như những cành cây.

Cây quyết định trông giống như

một cây đảo ngược theo cách tương tự

một cái cây bắt đầu từ rễ của nó và

cành hướng về phía lá của nó.

Cây quyết định bắt đầu bằng gốc

nút và mở rộng các nhánh của nó cho đến khi

nó đạt đến điểm cuối của nó,

được gọi là các nút lá.

Bây giờ chúng ta hãy xem xét kỹ hơn

một cây quyết định để đạt được một cái nhìn toàn diện

hiểu biết về sự đa dạng của nó

các thành phần thiết yếu.

Nút gốc tương tự

tới gốc cây.

Giống như rễ cây tạo nên nền tảng

và điểm bắt đầu của cây,

nút gốc đóng vai trò là

cơ sở của cây quyết định.

Nó đại diện cho quyết định ban đầu hoặc

điểm bắt đầu của cây và

đại diện cho toàn bộ tập dữ liệu.

Các nút gốc tiếp tục được chia thành hai hoặc

nhiều nút phụ hơn,

phân tách dữ liệu trong quá trình này.

Lưu ý rằng số lượng nút phụ được tạo

trong một sự phân chia phụ thuộc vào loại

cây quyết định

Loại cây quyết định mà chúng tôi

đang sử dụng chỉ tạo hai nút phụ

trong mỗi lần chia.

Việc phân chia cây quyết định cũng tương tự

đến sự lan rộng của cành cây.

Đó là quá trình chia một nút thành

hai nút phụ dựa trên một tính năng nhất định,

đó là một bước quan trọng trong

việc xây dựng cây quyết định.

Mục đích chính của việc chia tách là

tạo ra một tập dữ liệu đồng nhất hơn,

một tập dữ liệu hoàn toàn đồng nhất là một tập dữ liệu

tập hợp có các mẫu chỉ từ một lớp.

Các nút nhánh, còn được gọi là

các nút nội bộ hoặc các nút quyết định,

là các nút trung gian

trong cây quyết định.

Giống như nút gốc, dữ liệu được tách ra từ

một nút nhánh dựa trên một điều kiện trên

một tính năng cụ thể hoặc một thuộc tính.

Dựa trên kết quả của bài kiểm tra này,

cây có thể mở rộng hơn nữa đến cây khác

các nhánh hoặc nút cuối cùng,

đó là nút lá.

Như chiếc lá đánh dấu sự kết thúc của một cái cây,

nút lá hoặc

các nút đầu cuối đánh dấu các điểm cuối

của một cây quyết định.

Họ đại diện cho sự chia rẽ cuối cùng

của tập dữ liệu dựa vào đó

những quyết định sẽ được đưa ra

trên các tập dữ liệu chưa được nhìn thấy.

Các nút lá có thể có hai loại

nút thuần túy và nút không tinh khiết.

Các nút thuần túy là các nút trong đó tất cả

các mẫu dữ liệu chỉ thuộc về một lớp,

có nghĩa là nút là

hoàn toàn đồng nhất.

Các nút không tinh khiết là những nút ở đó

dữ liệu có các mẫu thuộc về

nhiều lớp,

có nghĩa là nút không đồng nhất.

Một phần phụ của toàn bộ quyết định

cây được gọi là một nhánh hoặc

một cây con, như chúng ta có thể thấy trong hình,

nó là kết quả từ

sự phân chia cây chính.

Cũng giống như điều quan trọng là phải cắt tỉa

sự phát triển quá mức hoặc không mong muốn của cây,

theo cùng một cách, nó rất quan trọng

để loại bỏ các nhánh nhất định hoặc

các cây con của cây quyết định.

Quá trình này được gọi là cắt tỉa,

nó giúp ngăn ngừa

những lo ngại như trang bị quá mức.

Tôi hy vọng bây giờ bạn đã có kiến thức cơ bản

hiểu biết về cây quyết định.

Cây quyết định ban đầu được xây dựng

để giải quyết vấn đề phân loại.

Vì vậy trong loạt video tiếp theo chúng ta sẽ

hiểu cây quyết định tốt hơn bằng cách lặn

vào công việc thực tế của việc xây dựng một

cây quyết định phân loại từ đầu.