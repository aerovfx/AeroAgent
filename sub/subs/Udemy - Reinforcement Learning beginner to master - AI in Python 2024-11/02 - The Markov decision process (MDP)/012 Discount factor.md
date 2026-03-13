# Hệ Số Chiết Khấu

## Nội dung

### 00:00:00 - 00:00:04
Trong video này, chúng ta sẽ học hệ số chiết khấu là gì và nó được sử dụng để làm gì.

### 00:00:06 - 00:00:07
Hãy xem nhiệm vụ điều khiển này.

### 00:00:08 - 00:00:15
Nó là một mê cung 5x5 trong đó tác tử (hình tròn đỏ) phải tìm lối ra, là hình vuông màu xanh lá

### 00:00:15 - 00:00:17
Ở góc dưới bên phải.

### 00:00:19 - 00:00:27
Sau khi thực hiện mỗi hành động, nó sẽ nhận được phần thưởng bằng 0 ngoại trừ khi nó đến lối ra, khi

### 00:00:27 - 00:00:30
Nó sẽ nhận được phần thưởng dương là +1.

### 00:00:31 - 00:00:34
Con đường ngắn nhất là con đường bạn thấy trên màn hình.

### 00:00:37 - 00:00:42
Nếu theo con đường đó, tác tử sẽ đạt được mục tiêu trong 10 bước và nó sẽ nhận được lợi nhuận

### 00:00:42 - 00:00:44
Là +1.

### 00:00:45 - 00:00:52
Tuy nhiên, nếu tác tử lang thang trong phần này của mê cung và sau đó quay lại con đường đúng

### 00:00:52 - 00:00:58
Cho đến khi nó đạt được mục tiêu, nó cũng sẽ nhận được lợi nhuận là +1.

### 00:00:59 - 00:01:06
Trong trường hợp đầu tiên, nó đã giải quyết nhiệm vụ một cách hiệu quả và trong trường hợp thứ hai, chậm hơn nhiều. Cách chúng ta

### 01:06:00 - 00:01:14
Đã thiết kế các phần thưởng, tác tử không có động lực để tìm lối ra nhanh nhất có thể, mặc dù

### 01:14:00 - 00:01:16
Rõ ràng đó là những gì chúng ta muốn nó đạt được.

### 01:18:00 - 00:01:26
Để làm điều đó, chúng ta phải sửa đổi theo cách nào đó lợi nhuận theo cách thưởng cho các hành vi hiệu quả nhất.

### 01:27:00 - 00:01:32
Và chúng ta có thể làm điều đó bằng cách nhân các phần thưởng tương lai với một hệ số chiết khấu.

### 01:32:00 - 00:01:39
Khi chúng ta tính lợi nhuận. Ở đây bạn thấy lợi nhuận tại thời điểm không.

### 01:40:00 - 00:01:46
Đó là tổng các phần thưởng từ khi nhiệm vụ bắt đầu cho đến khi nó kết thúc.

### 01:47:00 - 00:01:55
Và khi tính lợi nhuận này, chúng ta nhân mỗi phần thưởng tương lai với gamma lũy thừa của thời điểm

### 01:55:00 - 00:01:59
Khi phần thưởng đó được nhận trừ đi một.

### 02:01:00 - 00:02:09
Gamma là một giá trị giữa không và một, vì vậy bằng cách nhân, nó làm giảm các giá trị của phần thưởng

### 02:09:00 - 00:02:10
Nhận được trong tương lai.

### 02:12:00 - 00:02:16
Số mũ càng cao, giá trị của phần thưởng càng giảm.

### 02:18:00 - 00:02:21
Bằng cách đó, phần thưởng đầu tiên có giá trị đầy đủ của nó.

### 02:22:00 - 00:02:30
Phần thưởng tiếp theo được chiết khấu bởi gamma, phần thưởng tiếp theo được chiết khấu hai lần bởi gamma và cứ tiếp tục như vậy

### 02:30:00 - 00:02:32
Cho đến khi kết thúc đợt.

### 02:36:00 - 00:02:40
Chúng ta càng mất nhiều thời gian để đạt được một phần thưởng cụ thể.

### 02:42:00 - 00:02:50
Chúng ta càng giảm giá trị của nó khi tính lợi nhuận, bằng cách đó, tác tử có động lực để

### 02:50:00 - 00:02:51
Nhận chúng càng sớm越好.

### 02:53:00 - 00:03:01
Bây giờ, hãy xem điều gì xảy ra khi chúng ta cho các giá trị cực đoan cho hệ số chiết khấu, nếu gamma = 0,

### 03:01:00 - 00:03:06
Tất cả các phần thưởng tương lai ngoại trừ phần thưởng đầu tiên sẽ bằng 0.

### 03:08:00 - 00:03:13
Do đó, tác tử có động lực thực hiện các hành động mang lại cho nó phần thưởng tức thì.

### 03:14:00 - 00:03:22
Tức là, nó sẽ đưa ra quyết định hoàn toàn thiên vị mà không tính đến hậu quả tương lai

### 03:22:00 - 00:03:23
Của các hành động của nó.

### 03:26:00 - 00:03:33
Ngược lại, nếu gamma bằng một, chúng ta sẽ cung cấp cho tác tử nhiều kiên nhẫn hơn để xây dựng chiến lược dài hạn của nó.

### 03:33:00 - 00:03:34
Chiến lược.

### 03:35:00 - 00:03:42
Trong thực tế, các giá trị trung gian thường được sử dụng. Trong nhiều nhiệm vụ, giá trị mặc định là 0,99

### 03:42:00 - 00:03:47
Được sử dụng vì nó tạo ra động lực để nhận các phần thưởng càng sớm越好.

### 03:48:00 - 00:03:52
Nhưng nó cũng cho phép tác tử duy trì tầm nhìn dài hạn.

### 03:54:00 - 00:04:01
Tóm lại, gamma đo mức độ xa vào tương lai mà tác tử có thể nhìn khi lập kế hoạch các hành động của nó.

### 04:02:00 - 00:04:09
Và bây giờ với động lực mà chúng ta đã kết hợp vào định nghĩa của lợi nhuận, chúng ta có thể thay đổi

### 04:09:00 - 00:04:10
Mục tiêu của nhiệm vụ điều khiển.

### 04:11:00 - 00:04:16
Chúng ta muốn tối đa hóa tổng phần thưởng chiết khấu dài hạn.
