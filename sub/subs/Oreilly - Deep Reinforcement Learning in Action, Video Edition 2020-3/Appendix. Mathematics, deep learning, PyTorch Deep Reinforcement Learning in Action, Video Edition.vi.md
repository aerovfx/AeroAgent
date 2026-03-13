# Phụ lục. Toán học, học sâu, Học tập tăng cường sâu PyTorch trong thực tế, Phiên bản video.vi

---

Phụ lục Toán học Học sâu PyTorch Phụ lục này cung cấp tổng hợp

quan nhanh về học sâu, toán liên quan mà chúng ta sử dụng

trong sách này và cách thực hiện mô hình học sâu trong PyTorch.

Chúng tôi sẽ đề cập đến chủ đề này bằng cách trình bày cách thực hiện hình học

sâu trong PyTorch để phân loại hình ảnh số viết tay từ tập dữ liệu nổi tiếng MNIST.

Thuật toán học sâu còn được gọi là mạng nơ-ron

nhân tạo, là các hàm toán học tương đối đơn giản

và thường yêu cầu hiểu rõ về vectơ và ma trận.

Tuy nhiên, việc đào tạo mạng nơ-ron đòi hỏi

phải hiểu về các cơ sở được phép, cụ thể là chức năng đạo đức.

Do đó, để nắm chắc cơ sở ứng dụng học sâu,

bạn chỉ cần biết cách nhân vectơ và ma trận và lấy

Hàm đạo của các hàm đa biến mà chúng ta sẽ tìm hiểu sau.

Học máy lý thuyết là lĩnh vực nghiên cứu khắc nghiệt về các chất và

hành vi của máy tính toán thuật toán để đưa ra các cách tính toán kỹ thuật tiếp theo và mới.

Học máy lý thuyết bao gồm toán học

học tiến trình cấp cao bao nhiêu

nhiều học toán lớn phân tích

out of the range of this book.

Trong cuốn sách này, chúng tôi chỉ sử dụng toán học phi chính thức để đạt được mục tiêu

mục tiêu thực tế của mình chứ không phải dựa trên cơ sở tính toán học tập cho phép chứng minh quy định nghiêm ngặt.

Đại số tuyến tính A.1 Đại số tuyến tính

là nghiên cứu về phép biến đổi tuyến tính.

Tính toán tuyến biến đổi là biến được phép, ví dụ như một hàm trong tổng số đó

giá trị cho phép biến đổi hai đầu vào riêng biệt, ví dụ như T(a) và T(b), bằng

tổng số đầu vào sau khi cộng lại rồi biến đổi chúng, tức là T(a+b) = T(a+T(b)).

Tính năng tuyến tính biến đổi cũng

có tính chất là T(a)*b = a*T(b).

Tính năng bảo vệ tuyến tính biến đổi được phép và được phép

nhân vì bạn có thể áp dụng các tính năng được phép trước hoặc

sau đó cho phép tính toán biến đổi mà kết quả vẫn như nhau.

Một cách không chính thức để hiển thị các biến được phép

đổi tính năng tuyến tính là chúng không có lợi ích tăng cường.

Ví dụ, hãy sử dụng tính chất biến đổi tuyến tính chính là phép quy đổi tiền khi đầu vào là một tài khoản

dù đó là một nguồn lực khác, nghĩ hạn như vàng, theo công thức T(100 đô la) = 1 lượng vàng.

Đơn giá vàng sẽ không thay đổi

không kể bạn đầu tư bao nhiêu tiền.

Ngược lại, các chuyển đổi không có tính năng tuyến tính có thể mang đến

cho bạn chiết khấu lớn, vì vậy nếu mua 1000 đơn vị vàng trở lại

lên, giá theo mỗi đơn vị sẽ thấp hơn so với mua dưới 1000 đơn vị.

Một cách khác để hiểu các tính năng tuyến chuyển đổi là tạo mối

liên hệ được phép tính, mà chúng ta sẽ xem xét chi tiết hơn sau đây.

Một chức năng hoặc được phép chuyển đổi lấy một số giá trị

đầu vào x và sơ đồ của nó vào một số đầu giá trị y.

Một số đầu ra của công cụ có thể lớn hơn hoặc nhỏ hơn số đầu vào x

hoặc nhìn chung hơn là một vùng lân cận xung quanh số đầu vào x sẽ được

ánh xạ vào một vùng lân cận lớn hơn hoặc nhỏ hơn xung quanh số đầu ra y.

Tại đây, một cận điểm gần

đến tập hợp các điểm x hoặc y tùy chọn gần đây.

Đối với một biến đơn vị như f(x) = 2x +

1, một vùng lân cận thực ra là một khoảng.

Ví dụ, vùng lân cận xung quanh điểm đầu vào x = 2 sẽ là tất cả

các điểm gần 2 tùy ý, có giới hạn như 2.000001 và 1.99999999.

Một cách nghĩ về đạo hàm của một hàm tại một điểm

là tỷ lệ lớn của khoảng đầu ra xung quanh điểm đó

với tốc độ lớn của khoảng đầu vào xung quanh điểm đầu vào.

Các tuyến tính biến đổi được phép sẽ luôn có một hằng số tỷ lệ giữa các khoảng đầu ra và khoảng đầu

to all the point, in while các biến được phép không có tính chất tuyến tính sẽ có tỷ lệ thay đổi.

Các tính năng tuyến biến đổi được phép thường được biểu hiện

dưới các dạng ma trận, là các hình chữ nhật của mạng lưới bao gồm các số.

Ma trận hóa hóa các hệ số cho các

chức năng đa biến tuyến tính, như biểu thức này.

Mặc dù biểu thức này bao gồm cả hai hàm, nhưng đây thực chất là một sơ đồ hàm duy nhất

một điểm hai chiều x,y tới một điểm hai chiều mới x', y', bằng cách sử dụng các số a,b,c,d.

Để tìm x, bạn sử dụng hàm lũy thừa x,

và để tìm y', bạn sử dụng hàm lũy thừa i.

Chúng ta có thể viết biểu tượng

this format under a line.

Xem biểu thức này.

Điều này làm rõ hơn rằng đầu ra là một

vector hai phần tử hoặc vector hai chiều.

Trong bất kỳ trường hợp nào, đều có ích khi nghĩ đến hàm này ở hai phần riêng biệt, bởi vì các

phép tính cho các thành phần x và thành phần y là độc lập.

Mặc dù khái niệm toán học về vector rất chung và hiện vật

tượng, nhưng đối với máy học thì vector chỉ là một mảng một chiều.

Tính toán tuyến tính biến đổi này lấy một vectơ bao gồm hai thành phần, vectơ

có hai thành phần và biến nó thành một vectơ bao gồm hai thành phần khác.

Và để thực hiện điều này, cần có bốn

thành phần dữ liệu đặc biệt, bốn hệ số.

Có sự khác biệt giữa một tuyến tính biến đổi được phép như a, x + b, y và

một số được phép như a, x + b, y + c, điều này sẽ cộng một số không đổi.

Sau khi có các biến đổi

tên được phép biến đổi affine.

Trong thực tế, chúng tôi sử dụng các biến affine được phép trong máy học,

Nhưng trong phần thảo luận này, chúng tôi sẽ chỉ sử dụng tính năng cho phép biến đổi tuyến tính.

Ma trận là một cách thuận lợi

tiện lợi để lưu trữ các số này.

Chúng ta có thể đưa ra

dữ liệu vào ma trận 2x2.

Vui lòng xem biểu thức này.

Hiện tại, tính năng biến đổi tuyến tính được phép biểu diễn hoàn thành bởi ma trận

này, giả sử bạn hiểu cách sử dụng nó, cách sử dụng nó mà chúng tôi sẽ trình bày.

Chúng tôi có thể áp dụng tính năng biến đổi tuyến tính này bằng cách đặt ma trận cạnh nhau với một sự phấn khích,

limit as f(x).

Xem biểu thức này.

Chúng tôi tính toán kết quả của những thay đổi được phép này bằng cách

nhân từng hàng trong f với từng cột – chỉ có một cột tại đây – của x.

Nếu bạn làm điều này, bạn sẽ nhận được kết quả

kết quả tương tự như chức năng định nghĩa rõ ràng ở trên.

Ma trận không cần phải vuông.

Bất kỳ hình dạng nào

chữ cập nhật nào cũng được.

Chúng ta có thể biểu diễn các ma trận dưới dạng đồ họa như

hộp có hai dây nối ra ở mỗi đầu với các số chỉ được gắn nhãn.

Xem hình ảnh này.

Chúng tôi gọi đây là sơ đồ chuỗi.

n đại diện cho chiều của đầu

vào và m là chiều của đầu ra.

Bạn có thể tưởng tượng một sự thay đổi được phép

tuyến tính từ bên trái và một cái mới được tạo ra ở bên phải.

Đối với quá trình học tập sâu mà chúng tôi sử dụng trong cuốn sách này, bạn chỉ cần

hiểu đại số tuyến tính ở mức độ này, tức là các nguyên tắc để nhân các ma trận.

Bất kỳ khoản bổ sung nào được phép sử dụng sẽ được

giới thiệu các chương trình tương ứng.

Cảm ơn bạn.