# 05 từ khóa-tìm kiếm-bm25

---

Mặc dù TF-IDF vẫn là một thuật toán tìm kiếm từ khóa cổ điển,

thuật toán được sử dụng trong hầu hết các công cụ truy tìm được gọi là Best Matching 25,

hay đơn giản hơn là BM25. Nó được gọi như vậy vì nó là biến thể thứ 25 trong chuỗi tính điểm

chức năng do người tạo ra nó đề xuất. Nó thực hiện một số cải tiến trên TF-IDF,

vì vậy hãy khám phá cách chúng hoạt động. Đây là công thức cho BM25.

Nó thực sự hoạt động rất giống với TF-IDF với một số bổ sung quan trọng mà bạn sẽ thấy ngay sau đây.

Công thức này tạo ra điểm phù hợp cho một từ khóa cho một tài liệu cụ thể.

Tổng hợp những điểm số này trên tất cả các từ khóa sẽ tạo ra tổng số điểm phù hợp cho một từ khóa

tài liệu, sau đó có thể được sử dụng để xếp hạng. Bây giờ chúng ta hãy xem BM25 cải thiện như thế nào trên TF-IDS.

Đầu tiên, các tài liệu có kết quả trả về giảm dần khi chúng bao gồm nhiều trường hợp từ khóa hơn.

Ý tưởng ở đây là một tài liệu bao gồm từ khóa pizza 20 lần không thực sự là hai lần

có liên quan như một cái bao gồm pizza 10 lần. Hành vi giảm giá các trường hợp bổ sung này

của một từ khóa được gọi là bão hòa tần số thuật ngữ. Thứ hai, các tài liệu dài hơn vẫn còn

bị phạt như ở TF-IDF, nhưng ở BM25 những hình phạt này cũng giảm dần. Trong khi

phạt các tài liệu dài là quan trọng, TF-IDF có thể làm điều đó một cách quá quyết liệt theo cách quá đáng.

giảm giá tài liệu dài hơn. BM25 áp dụng mức phạt bổ sung giảm dần làm văn bản

phát triển chiều dài. Kết quả là các tài liệu dài vẫn đạt điểm cao miễn là chúng có độ dài khá

tần suất cao của các từ khóa. Quá trình điều chỉnh điểm này dựa trên độ dài tài liệu

được gọi là chuẩn hóa độ dài tài liệu. BM25 cũng khác với TF-IDF ở chỗ nó bao gồm hai

siêu tham số có thể điều chỉnh được. Những điều này cho phép bạn kiểm soát mức độ bão hòa tần số thuật ngữ

và chuẩn hóa độ dài tài liệu, hay nói cách khác là tốc độ tài liệu ngừng được khen thưởng

đối với các từ khóa lặp lại và bị phạt nếu tăng độ dài. Trong một công cụ truy xuất sản xuất, bạn sẽ điều chỉnh

các siêu tham số này để đạt được hệ thống tính điểm tổng thể phù hợp nhất với dữ liệu

trong cơ sở kiến thức của bạn. Trong công cụ truy xuất sản phẩm, thuật toán tìm kiếm từ khóa tiêu chuẩn là BM25.

Nó có xu hướng hoạt động tốt hơn đáng kể so với TF-IDF trong việc tìm kiếm các tài liệu liên quan,

gần tương đương về nguồn lực tính toán mà nó yêu cầu,

và khả năng điều chỉnh các siêu tham số của nó cho phù hợp với tập dữ liệu của bạn khiến nó trở nên linh hoạt hơn nhiều. Hãy

xem xét ngắn gọn tìm kiếm từ khóa và nói về cách sử dụng điểm mạnh của từ khóa bên trong một điển hình

đường ống thu hồi. Ý tưởng cốt lõi của tìm kiếm từ khóa là bạn khớp tài liệu với lời nhắc

dựa trên tần suất các từ khóa từ lời nhắc xuất hiện trong mỗi tài liệu. Là một phần của quá trình này,

cả lời nhắc và tài liệu đều được chuyển đổi thành các vectơ thưa thớt để đếm tần suất mỗi từ

trong từ vựng của hệ thống xuất hiện trong đoạn văn bản đó. TF-IDF hay BM25 chỉ khác nhau thôi

các phương pháp xử lý các vectơ thưa thớt này để cho điểm và xếp hạng tài liệu. Những cái này

các phương pháp cũng tính đến các yếu tố quan trọng như độ hiếm của từ khóa, tần suất một tài liệu

chứa một từ khóa và độ dài tài liệu. BM25 là thuật toán tìm kiếm từ khóa được sử dụng phổ biến nhất

đã vượt qua thử thách của thời gian trong nhiều thập kỷ kể từ khi được phát minh. Nó đạt được sự cân bằng tốt

giữa độ phức tạp và hiệu suất trong các ứng dụng trong thế giới thực. Sức mạnh chính của từ khóa

tìm kiếm là sự đơn giản của nó. Đó là một cách tiếp cận tương đối đơn giản và có tác dụng tốt trong

luyện tập, thường có khả năng tự thực hiện khá tốt và thường xuyên tạo ra một môi trường cạnh tranh

tiêu chuẩn mà các kỹ thuật tiên tiến hơn có thể khó vượt qua. Nó cũng đảm bảo rằng

tài liệu được truy xuất sẽ chứa các từ khóa từ lời nhắc của người dùng. Đặc biệt trong những tình huống khi

bạn mong muốn người dùng sử dụng thuật ngữ kỹ thuật hoặc tên sản phẩm chính xác, loại từ khóa chính xác này

phù hợp là đặc biệt quan trọng. Bất chấp tất cả những điểm mạnh của nó, tìm kiếm từ khóa vẫn có những điểm yếu.

Cuối cùng, nó phụ thuộc vào truy vấn chứa các từ khóa khớp chính xác với các từ trong

tài liệu. Nếu người dùng gửi lời nhắc có ý nghĩa tương tự với tài liệu nhưng không phải

bao gồm các từ phù hợp, tìm kiếm từ khóa sẽ không thể tìm thấy kết quả phù hợp. Vì vậy chúng ta hãy nhìn vào

tìm kiếm ngữ nghĩa và cách nó giải quyết vấn đề này.