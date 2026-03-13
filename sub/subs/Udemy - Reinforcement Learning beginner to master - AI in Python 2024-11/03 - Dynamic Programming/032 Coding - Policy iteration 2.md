# Lập Trình - Lặp Chính Sách 2

## Nội dung

### 00:00:00 - 00:00:06
Trong video này, chúng ta sẽ triển khai phần đầu tiên của thuật toán lặp chính sách. Phần đầu tiên

### 00:00:06 - 00:00:10
Là nơi chúng ta đánh giá chính sách mà chúng ta có tại thời điểm hiện tại.

### 00:00:13 - 00:00:22
Tức là, nó lấy một bảng giá trị và làm cho các mục của bảng đó phản ánh các giá trị của các trạng thái theo

### 00:00:22 - 00:00:25
Chính sách đó, chính sách mà chúng ta có ngay bây giờ.

### 00:00:26 - 00:00:34
Như bạn có thể thấy, phần này của thuật toán bao gồm một vòng lặp sẽ thực hiện miễn là Delta

### 00:00:34 - 00:00:36
Lớn hơn giá trị của Theta.

### 00:00:38 - 00:00:44
Khi Delta, đo lường thay đổi cao nhất được thực hiện đối với giá trị của một trạng thái trong lần lặp này

### 00:00:44 - 00:00:53
Của vòng lặp nhỏ hơn Theta, chúng ta sẽ dừng phần này của thuật toán và chúng ta sẽ trả về bảng giá trị

### 00:00:53 - 00:00:59
Vì chúng ta sẽ coi rằng các giá trị trong bảng đó phản ánh chính xác các giá trị theo chính sách hiện tại

### 00:00:59 - 00:00:59
Chính sách.

### 01:02:00 - 00:01:05
Điều đầu tiên chúng ta sẽ làm là tạo hàm đánh giá chính sách.

### 01:11:00 - 00:01:17
Hàm này đại diện cho phần đầu tiên của thuật toán, và nó sẽ lấy bốn đầu vào:

### 01:19:00 - 00:01:25
