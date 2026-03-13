# 02 suy luận nhân quả

---

Trong bài học này, bạn sẽ

tìm hiểu về những gì đã biết

như vấn đề cơ bản

của suy luận nhân quả.

Bạn cũng sẽ học cách bạn

có thể sử dụng máy học

kỹ thuật để được

có thể xác định cái nào

rất có thể bệnh nhân

để được hưởng lợi từ việc điều trị.

Để quyết định có nên cho hay không

một phương pháp điều trị cho một bệnh nhân,

một bác sĩ sẽ muốn biết điều gì

tác dụng của một điều trị

trên một bệnh nhân sẽ được.

Nếu việc điều trị là

có khả năng giảm

nguy cơ bất lợi

kết quả giống như một cơn đau tim,

thì chúng tôi sẽ muốn

đưa ra cách điều trị.

Nếu việc điều trị có thể

để không ảnh hưởng, hoặc tệ hơn,

làm hại bệnh nhân thì chúng ta

sẽ không muốn

đưa ra cách điều trị.

Một tập hợp tiềm năng có thể

kết quả cho một bệnh nhân

sẽ là như vậy với

cách điều trị họ sẽ không

bị đau tim,

trong khi không có

họ sẽ điều trị.

Trong trường hợp này

kết quả của bệnh nhân với

điều trị là đau tim,

trong khi bệnh nhân

kết quả mà không có

cách điều trị là họ

không bị đau tim,

chúng ta có thể nói rằng tác dụng của

việc điều trị mang lại lợi ích

cho bệnh nhân này.

Nhưng việc điều trị có thể không

mang lại lợi ích cho mọi người,

một số bệnh nhân có thể có tiềm năng

kết quả sao cho họ

bị đau tim

bất kể liệu

họ được điều trị.

Một số bệnh nhân có thể không có

một cơn đau tim bất kể

liệu họ có được điều trị hay không.

Trong cả hai trường hợp đó,

chúng ta sẽ nói rằng việc điều trị

không có tác dụng gì với bệnh nhân.

Cuối cùng, bệnh nhân có thể có

một cơn đau tim với

điều trị và không phải không có,

trong trường hợp đó việc điều trị

đã làm hại bệnh nhân.

Chúng ta có thể đại diện cho những điều này

bốn khả năng cho

kết quả tiềm năng của bệnh nhân

sử dụng Neyman-Rubin

mô hình nhân quả.

Đối với mỗi bệnh nhân tôi,

chúng tôi đại diện cho họ

kết quả khi được đưa ra

xử lý với Y_i là 1,

đó là 0 khi

kết quả bất lợi của

lợi ích không xảy ra,

khi cơn đau tim

không xảy ra,

trong khi nó là 1 khi nó xảy ra.

Tương tự, Y_i của 0

đại diện cho kết quả của bệnh nhân

khi họ không

được điều trị.

Tính năng quan tâm chính của chúng tôi

là cấp độ đơn vị

tác dụng điều trị,

đó là sự khác biệt giữa

những kết quả tiềm năng.

Ở đây, -1 tượng trưng cho lợi ích,

0 đại diện cho không có hiệu lực,

và 1 đại diện cho tích cực.

Bạn có thể xác nhận rằng những

âm 0 và một tương ứng

đến sự khác biệt giữa

cột đầu tiên và

cột thứ hai.

Vì vậy nếu chúng ta biết

kết quả tiềm năng

cho nhiều bệnh nhân trong một tập dữ liệu,

chúng ta có thể tính toán

nghĩa cho mỗi cột.

Vì vậy, hãy lấy cột đầu tiên,

chúng tôi có năm bệnh nhân,

và nếu chúng ta lấy mức trung bình ở đây,

chúng ta có 2 trên 5,

đó là 4 trên 10, hay 0,40.

0,4 hoặc 40 phần trăm đại diện

tỷ lệ bệnh nhân ở đây

người trải nghiệm một kết quả.

Tương tự, ở cột thứ hai,

chúng ta có thể tính trung bình ở đây,

và chúng ta nhận được 3 trên 5, hay 0,6.

0,6 hoặc 60 phần trăm là

sẽ đại diện

tỷ lệ bệnh nhân ở

cánh tay điều khiển ai

trải nghiệm một sự kiện.

Cuối cùng, chúng ta có thể lấy

mức trung bình trong

cột thứ ba ở đây.

Vậy chúng ta cộng những thứ này lại,

chúng ta nhận được âm 1 trên 5,

hoặc âm 2 trên

10 hoặc âm 0,2.

Âm 0,2 là

giảm trung bình

gặp nguy hiểm khi điều trị.

Vậy tại sao điều này lại hữu ích?

Lý do điều này hữu ích là

bởi vì giá trị thứ ba của chúng tôi trên

đây là cái được gọi là

hiệu quả điều trị trung bình.

Về mặt hình thức, trung bình

tác dụng điều trị là

kỳ vọng về sự khác biệt

trong các kết quả tiềm năng,

và sự mong đợi có thể được đưa ra

bằng cách lấy trung bình

của cột này,

con số ở đây là bao nhiêu,

âm 0,2, và đây là

kỳ vọng của Y_1 trừ

kỳ vọng của Y_0.

Chúng ta có thể nhận được kỳ vọng của Y_1

bằng cách nhìn vào mức trung bình

của cột này ở đây,

đó là 0,4, và

sự mong đợi của

Y_0 bằng cách lấy trung bình của

cột này là 0,6.

Chúng ta có thể

xác nhận rằng âm 0,2.

là âm 0,4 trừ 0,6.