# Chương 10. Học tập tăng cường sâu Double Q-learning trong thực tế, Phiên bản video được dịch

---

Phần 10.5, Q-learning kép.

Bây giờ chúng ta hãy bắt đầu đào tạo nó.

Bởi vì môi trường thế giới dạng lưới này có ít phần thưởng nên chúng ta cần thực hiện quá trình đào tạo của mình

suôn sẻ nhất có thể, đặc biệt là khi chúng tôi không sử dụng phương pháp học tập dựa trên sự tò mò.

Hãy nhớ lại Chương 3 khi chúng tôi giới thiệu Q-learning và mạng mục tiêu để ổn định

đào tạo?

Nếu không, ý tưởng là trong Q-learning thông thường, chúng ta tính toán giá trị Q mục tiêu bằng phương trình này.

Xem biểu hiện này.

Vấn đề ở đây là mỗi lần chúng ta cập nhật DQN theo phương trình này,

để các dự đoán của nó tiến gần đến mục tiêu này hơn, Q của ST cộng 1 sẽ thay đổi, nghĩa là

lần tới khi chúng ta cập nhật chức năng Q, mục tiêu Q-mới sẽ khác

ngay cả đối với cùng một trạng thái.

Đây là vấn đề vì khi chúng tôi huấn luyện DQN, các dự đoán của nó đang đuổi theo một mục tiêu đang di chuyển,

dẫn đến việc tập luyện rất không ổn định và hiệu suất kém.

Để ổn định quá trình huấn luyện, chúng tôi tạo một hàm Q trùng lặp được gọi là hàm đích.

chúng ta có thể biểu thị Q nguyên tố và chúng ta sử dụng giá trị Q nguyên tố của ST cộng 1 để thế vào phương trình

và cập nhật chức năng Q chính.

Xem biểu hiện này.

Chúng tôi chỉ huấn luyện và do đó truyền ngược lại vào hàm Q chính.

Nhưng chúng ta sao chép các tham số từ hàm Q chính sang hàm Q đích, Q prime,

cứ 100 hoặc một số số sử thi tùy ý khác.

Điều này giúp ổn định đáng kể quá trình luyện tập vì chức năng Q chính không còn theo đuổi liên tục nữa.

mục tiêu di động nhưng là mục tiêu tương đối cố định.

Nhưng đó không phải là tất cả những điều sai với phương trình cập nhật đơn giản đó vì nó liên quan đến

hàm tối đa.

Nghĩa là, chúng tôi chọn giá trị Q dự đoán tối đa cho trạng thái tiếp theo.

Nó khiến nhân viên của chúng tôi đánh giá quá cao giá trị Q cho các hành động, điều này có thể ảnh hưởng đặc biệt đến việc đào tạo

từ rất sớm.

Nếu DQN thực hiện hành động 1 và học giá trị Q cao sai cho hành động 1, điều đó có nghĩa là hành động

1 sẽ được chọn thường xuyên hơn trong các sử thi tiếp theo, hơn nữa khiến nó được đánh giá quá cao,

điều này một lần nữa dẫn đến việc tập luyện không ổn định và hiệu suất kém.

Để giảm thiểu vấn đề này và có được ước tính chính xác hơn cho giá trị Q, chúng tôi sẽ triển khai

học Q kép, giải quyết vấn đề bằng cách tách ước tính giá trị hành động khỏi

lựa chọn hành động, như bạn sẽ thấy.

Mạng Q sâu gấp đôi, DQN, bao gồm một sửa đổi đơn giản đối với việc học Q thông thường với mục tiêu

mạng.

Như thường lệ, chúng tôi sử dụng mạng Q chính để chọn các hành động bằng chính sách tham lam của Epsilon.

Nhưng khi đến lúc tính Q mới, trước tiên chúng ta sẽ tìm arg max của Q, giá trị chính

mạng Q.

Giả sử arg max, dấu ngoặc mở Q của ST cộng với 1 dấu ngoặc đơn đóng bằng 2.

Vì vậy, hành động 2 được liên kết với giá trị hành động cao nhất ở trạng thái tiếp theo, dựa trên giá trị chính

hàm Q.

Sau đó, chúng tôi sử dụng điều này để lập chỉ mục vào mạng mục tiêu Q prime, để nhận được giá trị hành động, chúng tôi sẽ

sử dụng trong phương trình cập nhật.

Xem biểu hiện này.

Chúng tôi vẫn đang sử dụng giá trị Q từ mạng mục tiêu Q prime, nhưng chúng tôi không chọn giá trị

giá trị Q cao nhất từ Q nguyên tố.

Chúng tôi chọn giá trị Q trong Q prime, dựa trên hành động liên quan đến Q cao nhất

giá trị trong hàm Q chính, trong mã.

Xem mã này.

Hàm DQN lấy dấu gạch dưới mục tiêu Q chỉ tính Q mới bằng RT cộng

gamma nhân x dấu hai chấm.

Xem mã này.

Chúng tôi cung cấp xong, đây là một Boolean, bởi vì nếu một tập của trò chơi được hoàn thành, thì sẽ có

không có trạng thái tiếp theo để tính Q của ST cộng 1.

Vì vậy, chúng tôi chỉ huấn luyện trên RT và đặt phần còn lại của phương trình về 0.

Đó là tất cả những gì cần làm để tăng gấp đôi việc học Q, chỉ là một cách đơn giản khác để cải thiện việc đào tạo

sự ổn định và hiệu suất.