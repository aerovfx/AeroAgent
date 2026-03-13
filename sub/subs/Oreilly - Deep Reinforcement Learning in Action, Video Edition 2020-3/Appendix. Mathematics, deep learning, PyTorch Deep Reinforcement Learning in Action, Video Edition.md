# Phụ lục. Toán học, học sâu, Học tập tăng cường sâu PyTorch trong thực tế, Phiên bản video

---

Phụ lục Toán học Deep Learning PyTorch

Phụ lục này cung cấp bản đánh giá nhanh về deep learning, toán học liên quan mà chúng tôi sử dụng

trong cuốn sách này và cách triển khai các mô hình deep learning trong PyTorch.

Chúng tôi sẽ đề cập đến các chủ đề này bằng cách trình bày cách triển khai mô hình học sâu trong

PyTorch để phân loại hình ảnh của các chữ số viết tay từ bộ dữ liệu MNIST nổi tiếng.

Các thuật toán học sâu, còn được gọi là mạng lưới thần kinh nhân tạo, tương đối

các hàm toán học đơn giản và chủ yếu chỉ yêu cầu hiểu biết về vectơ và

ma trận.

Tuy nhiên, việc đào tạo một mạng lưới thần kinh đòi hỏi sự hiểu biết cơ bản về tính toán,

cụ thể là đạo hàm.

Do đó, các nguyên tắc cơ bản của học sâu ứng dụng chỉ cần biết cách nhân

vectơ và ma trận và lấy đạo hàm của các hàm nhiều biến mà chúng ta sẽ xem xét

sau này.

Học máy lý thuyết đề cập đến lĩnh vực nghiên cứu nghiêm ngặt các đặc tính

và hành vi của các thuật toán học máy và mang lại những cách tiếp cận và thuật toán mới.

Học máy lý thuyết liên quan đến toán học nâng cao ở cấp độ sau đại học bao gồm nhiều lĩnh vực

nhiều ngành toán học nằm ngoài phạm vi của cuốn sách này.

Trong cuốn sách này, chúng tôi chỉ sử dụng toán học không chính quy để đạt được các mục tiêu thực tế chứ không phải

toán học dựa trên bằng chứng chặt chẽ.

A.1 Đại số tuyến tính

Đại số tuyến tính là nghiên cứu về các phép biến đổi tuyến tính.

Phép biến đổi tuyến tính là một phép biến đổi, ví dụ, một hàm, trong đó tổng

của phép biến đổi hai đầu vào riêng biệt, chẳng hạn như T(a) và T(b), giống như tính tổng

hai đầu vào và biến đổi chúng cùng nhau, nghĩa là T(a+b) = T(a+T(b)).

Một phép biến đổi tuyến tính cũng có tính chất là T(a)*b = a*T(b).

Các phép biến đổi tuyến tính được cho là bảo toàn các phép tính cộng và nhân

vì bạn có thể áp dụng các thao tác này trước hoặc sau phép biến đổi tuyến tính

và kết quả là như nhau.

Một cách không chính thức để nghĩ về điều này là các phép biến đổi tuyến tính không có tính kinh tế

về quy mô.

Ví dụ, hãy nghĩ về một phép biến đổi tuyến tính như việc chuyển đổi tiền làm đầu vào thành một số

nguồn tài nguyên khác, như vàng, sao cho T(100$) = 1 đơn vị vàng.

Đơn giá của vàng sẽ không đổi, bất kể bạn bỏ vào bao nhiêu tiền.

Ngược lại, các phép biến đổi phi tuyến có thể mang lại cho bạn mức giảm giá lớn, do đó nếu bạn mua

1000 đơn vị vàng trở lên, giá mỗi đơn vị sẽ thấp hơn so với khi bạn mua

dưới 1000 đơn vị

Một cách khác để nghĩ về các phép biến đổi tuyến tính là tạo mối liên hệ với phép tính,

chúng tôi sẽ xem xét chi tiết hơn trong thời gian ngắn.

Một hàm hoặc phép biến đổi nhận một số giá trị đầu vào, x và ánh xạ nó tới một giá trị đầu ra nào đó,

y.

Một đầu ra y cụ thể có thể có giá trị lớn hơn hoặc nhỏ hơn đầu vào x hoặc tổng quát hơn,

vùng lân cận xung quanh đầu vào x sẽ được ánh xạ tới vùng lân cận lớn hơn hoặc nhỏ hơn xung quanh

đầu ra y.

Ở đây, vùng lân cận đề cập đến tập hợp các điểm gần x hoặc y tùy ý.

Đối với một hàm biến duy nhất như f(x) = 2x + 1, một vùng lân cận thực sự là một khoảng.

Ví dụ: vùng lân cận xung quanh điểm đầu vào x = 2 sẽ là tất cả các điểm tùy ý

gần bằng 2, chẳng hạn như 2,000001 và 1,99999999.

Một cách để nghĩ về đạo hàm của hàm số tại một điểm là tỉ số giữa kích thước của

khoảng đầu ra xung quanh điểm đó với kích thước của khoảng đầu vào xung quanh đầu vào

điểm.

Các phép biến đổi tuyến tính sẽ luôn có một số tỷ lệ đầu ra và đầu vào không đổi

cho tất cả các điểm, trong khi các phép biến đổi phi tuyến sẽ có tỷ lệ khác nhau.

Các phép biến đổi tuyến tính thường được biểu diễn dưới dạng ma trận, là các lưới hình chữ nhật có

những con số.

Ma trận mã hóa các hệ số cho các hàm tuyến tính nhiều biến, chẳng hạn như

Biểu hiện này.

Mặc dù đây có vẻ là hai hàm, nhưng đây thực sự là một hàm duy nhất ánh xạ một không gian hai chiều.

điểm, x,y, tới một điểm hai chiều mới, x', y', sử dụng các hệ số a,b,c,d.

Để tìm x, bạn sử dụng f lũy thừa của hàm x và để tìm y', bạn sử dụng f để

sức mạnh của chức năng tôi.

Chúng ta có thể viết điều này thành một dòng duy nhất.

Xem biểu hiện này.

Điều này làm rõ hơn rằng đầu ra là một vectơ hai bộ hoặc hai chiều.

Trong mọi trường hợp, sẽ hữu ích nếu chia chức năng này thành hai phần riêng biệt, vì

tính toán cho các thành phần x và y là độc lập.

Trong khi khái niệm toán học của vectơ rất tổng quát và trừu tượng, đối với máy

học một vectơ chỉ là một mảng số một chiều.

Phép biến đổi tuyến tính này lấy một vectơ hai, một vectơ có hai phần tử và biến nó thành

hai vectơ khác.

Và để làm được điều này cần có bốn phần dữ liệu riêng biệt, bốn hệ số.

Có sự khác biệt giữa một phép biến đổi tuyến tính như a, x + b, y và một số thứ như a, x

+ b, y + c, cộng một hằng số.

Cái sau được gọi là phép biến đổi affine.

Trong thực tế, chúng tôi sử dụng các phép biến đổi affine trong học máy, nhưng trong cuộc thảo luận này

chúng ta sẽ chỉ sử dụng các phép biến đổi tuyến tính.

Ma trận là một cách thuận tiện để lưu trữ các hệ số này.

Chúng ta có thể gói dữ liệu thành ma trận 2x2.

Xem biểu hiện này.

Phép biến đổi tuyến tính hiện được biểu diễn hoàn toàn bằng ma trận này, giả sử bạn hiểu

cách sử dụng nó mà chúng tôi sẽ đề cập đến.

Chúng ta có thể áp dụng phép biến đổi tuyến tính này bằng cách đặt ma trận cạnh một vectơ, với

ví dụ, f(x).

Xem biểu hiện này.

Chúng tôi tính toán kết quả của phép biến đổi này bằng cách nhân mỗi hàng trong f với mỗi cột

– chỉ có một ở đây – của x.

Nếu bạn làm điều này, bạn sẽ nhận được kết quả tương tự như định nghĩa hàm rõ ràng ở trên.

Ma trận không cần phải vuông.

Chúng có thể là bất kỳ hình chữ nhật nào.

Chúng ta có thể biểu diễn ma trận bằng đồ họa dưới dạng các hộp có hai chuỗi ở mỗi đầu với

các chỉ số được dán nhãn.

Xem hình này.

Chúng tôi gọi đây là sơ đồ chuỗi.

n đại diện cho thứ nguyên của vectơ đầu vào và m là thứ nguyên

của vectơ đầu ra.

Bạn có thể tưởng tượng một vectơ chảy vào phép biến đổi tuyến tính từ bên trái và một

vectơ mới được tạo ra ở phía bên phải.

Đối với phương pháp học sâu thực tế mà chúng tôi sử dụng trong cuốn sách này, bạn chỉ cần hiểu điều này

nhiều đại số tuyến tính, tức là nguyên lý nhân vectơ với ma trận.

Bất kỳ phép toán bổ sung nào sẽ được giới thiệu trong các chương tương ứng.

Cảm ơn.