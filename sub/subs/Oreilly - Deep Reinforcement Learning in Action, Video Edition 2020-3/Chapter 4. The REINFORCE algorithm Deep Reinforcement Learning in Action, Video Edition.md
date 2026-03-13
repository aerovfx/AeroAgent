# Chương 4. Thuật toán REINFORCE Học tăng cường sâu trong thực tế, Phiên bản video đã dịch

---

Phần 4.4, thuật toán tăng cường.

Bây giờ bạn phải tạo một môi trường tập thể dục AI mở và hy vọng đã phát triển được

trực quan về thuật toán gradient chính sách, hãy cùng đi sâu vào việc triển khai hoạt động.

Thảo luận của chúng tôi về độ dốc chính sách trong phần trước tập trung vào một thuật toán cụ thể

đã tồn tại hàng thập kỷ, giống như hầu hết các phương pháp học sâu và học tăng cường,

gọi là tăng cường.

Có, nó luôn được viết hoa đầy đủ.

Chúng ta sẽ củng cố những gì chúng ta đã thảo luận trước đó, chính thức hóa nó và sau đó biến nó thành một

vào mã Python.

Hãy triển khai thuật toán tăng cường cho ví dụ thăm dò giỏ hàng.

Phần 4.4.1, tạo mạng lưới chính sách.

Chúng tôi sẽ xây dựng và khởi tạo một mạng lưới thần kinh hoạt động như một mạng chính sách.

Mạng chính sách sẽ chấp nhận các vectơ trạng thái làm đầu vào và nó sẽ tạo ra một, rời rạc,

phân phối xác suất cho các hành động có thể xảy ra.

Bạn có thể coi tác nhân như một lớp bao bọc mỏng xung quanh mạng chính sách lấy mẫu từ

phân bố xác suất để thực hiện một hành động.

Hãy nhớ rằng, tác nhân trong học tăng cường là bất kỳ hàm hoặc thuật toán nào cần

trạng thái và trả về một hành động cụ thể sẽ được thực thi trong môi trường.

Hãy thể hiện điều này bằng mã.

Liệt kê 4.4, thiết lập mạng chính sách.

Tất cả những điều đó có vẻ khá quen thuộc với bạn vào thời điểm này.

Mô hình chỉ có hai lớp, chức năng kích hoạt rò rỉ tia-loo cho lớp đầu tiên và

chức năng softmax cho lớp cuối cùng.

Chúng tôi chọn Leaky-ray-loo vì nó hoạt động tốt hơn về mặt thực nghiệm.

Bạn đã thấy hàm softmax ở chương 2.

Nó chỉ lấy một dãy số và xếp chúng vào phạm vi từ 0 đến 1 và đảm bảo

tất cả chúng đều có tổng bằng 1, về cơ bản tạo ra sự phân bố xác suất rời rạc từ bất kỳ danh sách nào

của những con số không phải là xác suất để bắt đầu.

Ví dụ hàm softmax áp dụng cho mảng trừ 1, 2, 3 cho kết quả là mảng

0,0132, 0,2654, 0,7214.

Không có gì đáng ngạc nhiên, hàm softmax sẽ biến những số lớn hơn thành xác suất lớn hơn.

Mục 4.4.2, yêu cầu tác nhân tương tác với môi trường.

Tác nhân sử dụng trạng thái và thực hiện một hành động, a, theo xác suất.

Cụ thể hơn, trạng thái là đầu vào của mạng chính sách, sau đó tạo ra

phân phối xác suất theo các hành động, xác suất của sự kiện theta nhất định và

s t cho các thông số hiện tại của nó trong trạng thái.

Lưu ý, chữ hoa a đề cập đến tập hợp tất cả các hành động có thể xảy ra đối với trạng thái, trong khi

chữ thường a thường đề cập đến một hành động cụ thể.

Mạng chính sách có thể trả về một phân bố xác suất rời rạc dưới dạng

vectơ, chẳng hạn như 0,25, 0,75, cho hai hành động có thể xảy ra của chúng ta trong cuộc thăm dò giỏ hàng.

Điều này có nghĩa là mạng chính sách dự đoán rằng hành động 0 là tốt nhất với xác suất 25% và

hành động 1 là tốt nhất với xác suất hoặc độ tin cậy 75%.

Chúng tôi gọi mảng này là PRED.

Sử dụng 4.5, sử dụng mạng chính sách để lấy mẫu một hành động.

Môi trường phản ứng lại hành động bằng cách tạo ra trạng thái mới, s2 và phần thưởng, r2.

Chúng tôi lưu trữ chúng thành hai mảng, mảng trạng thái và mảng hành động khi chúng tôi cần

để cập nhật mô hình của chúng tôi sau khi tập phim kết thúc.

Sau đó, chúng tôi cắm trạng thái mới vào mô hình của mình, nhận trạng thái và phần thưởng mới, lưu trữ những trạng thái đó và

lặp lại cho đến khi tập phim kết thúc.

Cuộc thăm dò kết thúc và trò chơi kết thúc.

Mục 4.4.3, huấn luyện mô hình.

Chúng tôi đào tạo mạng chính sách bằng cách cập nhật các tham số để giảm thiểu mục tiêu, đó là

là sự mất mát, chức năng.

Điều này bao gồm ba bước.

1.

Tính xác suất của hành động thực sự được thực hiện ở mỗi bước thời gian.

2.

Nhân xác suất với lợi nhuận chiết khấu, tổng phần thưởng.

3.

Sử dụng lợi nhuận có trọng số theo xác suất này để truyền ngược và giảm thiểu tổn thất.

Chúng ta sẽ lần lượt xem xét những điều này.

Tính xác suất của hành động.

Tính xác suất của hành động được thực hiện là đủ dễ dàng.

Chúng ta có thể sử dụng các chuyển đổi lượt được lưu trữ để tính toán lại phân bố xác suất bằng cách sử dụng

mạng lưới chính sách

Tại thời điểm này, chúng tôi chỉ trích xuất xác suất dự đoán cho hành động thực tế

đã lấy.

Chúng ta sẽ biểu thị đại lượng này là xác suất xảy ra sự kiện tại theta và st đã cho. Đây là một

giá trị xác suất duy nhất như 0,75.

Cụ thể hơn, giả sử trạng thái hiện tại là s5, trạng thái ở bước 5.

Chúng tôi nhập dữ liệu đó vào mạng chính sách và nó trả về phân bố xác suất của

hành động cho trạng thái s5 là 0,25 cho hành động đầu tiên và 0,75 cho hành động thứ hai.

Chúng tôi lấy mẫu từ phân phối này và thực hiện hành động bằng 1, phần tử thứ hai trong hành động

mảng và sau đó cuộc thăm dò kết thúc và tập phim đã kết thúc.

Tổng thời lượng của tập phim là t bằng 5.

Đối với mỗi hành động theo xác suất của sự kiện, một điểm nhất định và chúng tôi đã lưu trữ thông tin cụ thể

xác suất của các hành động đã thực sự được thực hiện, xác suất của biến số đã cho

các điều kiện st dưới tham số theta trong một mảng có thể trông giống như 0,5, 0,30,

0,25, 0,5, 0,75.

Chúng tôi chỉ cần nhân những xác suất này với phần thưởng chiết khấu được giải thích trong phần tiếp theo.

phần.

Lấy tổng, nhân với âm 1 và gọi đó là tổng thiệt hại của chúng ta trong tập này.

Giống như thế giới lưới, trong cuộc thăm dò giỏ hàng, hành động cuối cùng là hành động thua tập.

Chúng tôi giảm giá nó nhiều nhất vì chúng tôi muốn trừng phạt nước đi tồi tệ nhất.

Trong thế giới lưới, chúng tôi sẽ làm ngược lại và giảm bớt hành động đầu tiên trong tập phim nhiều nhất.

vì nó sẽ ít chịu trách nhiệm nhất cho việc thắng hay thua.

Việc giảm thiểu hàm mục tiêu này sẽ có xu hướng làm tăng các xác suất đó.

Xác suất của biến a với điều kiện st theo tham số theta chờ

bằng những phần thưởng được giảm giá.

Vì vậy, mỗi tập phim chúng ta đều có xu hướng tăng xác suất của biến a cho trước

điều kiện st theo tham số theta.

Nhưng đối với một tập phim đặc biệt dài, nếu chúng ta chơi trò chơi tốt và đạt được kết quả lớn

của tập trở lại, chúng ta sẽ tăng xác suất của biến a với điều kiện st dưới

tham số theta ở mức độ lớn hơn.

Do đó, trung bình qua nhiều tập, chúng tôi sẽ củng cố những hành động tốt và

những hành động xấu sẽ bị bỏ lại phía sau.

Vì các xác suất phải có tổng bằng 1, nếu chúng ta tăng xác suất của một hành động tốt thì điều đó sẽ

tự động đánh cắp khối lượng xác suất từ những hành động khác được cho là kém tốt hơn.

Nếu không có tính chất phân phối lại của xác suất, sơ đồ này sẽ không hoạt động, tức là mọi thứ đều không thể thực hiện được.

tốt và xấu đều có xu hướng tăng lên.

Tính toán phần thưởng trong tương lai.

Ta nhân xác suất của biến cố a, t với các tham số theta và các điều kiện

tính bằng tổng phần thưởng, hay còn gọi là tiền lãi.

Chúng tôi đã nhận được sau trạng thái này.

Như đã đề cập trước đó trong phần này, chúng ta có thể nhận được tổng số phần thưởng chỉ bằng cách cộng các phần thưởng,

bằng với số bước thời gian mà tập đó kéo dài trong cuộc thăm dò giỏ hàng.

Và tạo một mảng trả về bắt đầu bằng thời lượng tập và giảm dần 1 cho đến khi

1.

Nếu tập kéo dài 5 bước thời gian thì mảng trả về sẽ là 5, 4, 3, 2, 1.

Điều này có ý nghĩa vì hành động đầu tiên của chúng ta sẽ được khen thưởng nhiều nhất vì đó là hành động đầu tiên.

ít chịu trách nhiệm nhất về việc cuộc thăm dò rơi xuống và mất tập phim.

Ngược lại, hành động ngay trước khi cuộc thăm dò thất bại là hành động tồi tệ nhất và lẽ ra nó phải có

phần thưởng nhỏ nhất.

Nhưng đây là một sự suy giảm tuyến tính.

Chúng tôi muốn giảm giá phần thưởng theo cấp số nhân.

Để tính toán phần thưởng được chiết khấu, chúng tôi tạo một mảng gamma t bằng cách lấy tham số gamma của mình,

chẳng hạn, có thể được đặt thành 0,99 và lũy thừa nó theo khoảng cách từ

kết thúc tập phim.

Ví dụ: chúng ta bắt đầu với gamma gạch dưới t bằng 0,99, 0,99, 0,99, 0,99, 0,99, sau đó tạo

một mảng số mũ khác.

Giá trị này bằng 1, 2, 3, 4, 5 và tính lũy thừa của dấu gạch dưới gamma t được nâng lên số mũ

x bằng thư viện torch, thư viện này sẽ cho chúng ta 1.00.9, 9, 0.98, 0.97, 0.96.

Hàm mất mát.

Bây giờ chúng ta đã chiết khấu lợi nhuận, chúng ta có thể sử dụng chúng để tính hàm mất mát để huấn luyện

mạng lưới chính sách

Như chúng ta đã thảo luận trước đây, chúng ta biến hàm mất mát của mình thành xác suất log âm của

hành động được đưa ra ở trạng thái, được tính theo phần thưởng.

Trong PyTorch, giá trị này được định nghĩa là âm một lần tổng của tích phần tử

của R và logarit tự nhiên của Preds.

Chúng tôi tính toán tổn thất bằng dữ liệu đã thu thập cho tập và chạy trình tối ưu hóa ngọn đuốc

để giảm thiểu tổn thất.

Hãy chạy qua một số mã thực tế.

Bắt đầu từ phiên bản 4.6, tính toán phần thưởng chiết khấu.

Ở đây chúng tôi xác định một hàm đặc biệt để tính toán phần thưởng chiết khấu cho một loạt phần thưởng

nó sẽ trông giống như 50, 49, 48, 47.

Nếu tập phim kéo dài 50 bước thời gian thì về cơ bản, tập phim sẽ biến chuỗi phần thưởng tuyến tính này thành

một chuỗi phần thưởng giảm dần theo cấp số nhân.

Ví dụ: 50.000, 48.510, 47.0448, 45.6441.

Và sau đó nó chia cho giá trị lớn nhất để giới hạn các giá trị trong khoảng 0, 1.

Lý do của bước chuẩn hóa này là để nâng cao hiệu quả học tập và tính ổn định

vì nó giữ giá trị trả về trong cùng một phạm vi cho dù lợi nhuận thô lớn đến đâu

là.

Nếu lợi nhuận thô là 50 khi bắt đầu đào tạo nhưng sau đó đạt 200 vào cuối

trong quá trình đào tạo, độ dốc sẽ thay đổi gần như theo cấp độ lớn, điều này cản trở

sự ổn định.

Nó vẫn sẽ hoạt động mà không cần chuẩn hóa, nhưng không đáng tin cậy bằng.

Tuyên truyền ngược.

Bây giờ chúng ta có tất cả các biến trong hàm mục tiêu, chúng ta có thể tính tổn thất

và lan truyền ngược để điều chỉnh các tham số.

Danh sách sau đây hiển thị hàm mất mát, đây chỉ là bản dịch Python của

toán học mà chúng tôi đã mô tả trước đó.

Liệt kê 4.7, xác định hàm mất mát.

Phần 4.4.4, vòng đào tạo đầy đủ.

Khởi tạo, thu thập kinh nghiệm, tính toán tổn thất từ những kinh nghiệm đó, truyền ngược,

và lặp lại.

Danh sách sau đây xác định vòng đào tạo đầy đủ của đại lý tăng cường của chúng tôi.

Liệt kê 4.8, vòng huấn luyện củng cố.

Chúng tôi bắt đầu một tập, sử dụng mạng chính sách để thực hiện hành động và ghi lại các trạng thái và

hành động chúng ta quan sát.

Sau đó, khi thoát ra khỏi một tập, chúng tôi phải tính toán lại xác suất dự đoán

để sử dụng trong hàm mất mát của chúng tôi.

Sau khi chúng tôi ghi lại tất cả các chuyển tiếp trong mỗi tập dưới dạng danh sách các bộ dữ liệu, khi chúng tôi kết thúc

của tập phim, chúng ta có thể tách từng thành phần của từng chuyển tiếp, trạng thái, hành động và

phần thưởng, thành các tensor riêng biệt để huấn luyện trên một loạt dữ liệu tại một thời điểm.

Nếu bạn chạy mã này, bạn sẽ có thể vẽ biểu đồ thời lượng của tập theo tập

và hy vọng bạn sẽ thấy xu hướng tăng lên rõ rệt như trong hình 4.10.

Hình 4.10.

Sau khi đào tạo mạng chính sách tới 500 kỷ nguyên, chúng ta có được một biểu đồ minh họa tác nhân

thực sự là học cách chơi trò thăm dò giỏ hàng.

Lưu ý rằng đây là biểu đồ trung bình động có cửa sổ là 50 để làm phẳng biểu đồ.

Người đại diện học cách chơi trò thăm dò giỏ hàng.

Điều thú vị ở ví dụ này là nó có thể huấn luyện trong vòng chưa đầy một phút

trên máy tính xách tay của bạn chỉ với CPU.

Trạng thái thăm dò giỏ hàng chỉ là một vectơ bốn chiều và mạng lưới chính sách của chúng tôi chỉ có hai

các lớp nhỏ nên việc huấn luyện sẽ nhanh hơn nhiều so với DQN mà chúng tôi đã tạo để chơi GridWorld.

Tài liệu của Open AI nói rằng trò chơi được coi là đã giải quyết nếu tác nhân có thể chơi

một tập phim vượt quá 200 bước thời gian.

Mặc dù cốt truyện có vẻ như kết thúc vào khoảng 190, đó là vì nó là một câu chuyện cảm động.

cốt truyện trung bình.

Có nhiều tập đạt 200 nhưng có vài tập ngẫu nhiên bị lỗi sớm

tiếp tục, làm giảm mức trung bình xuống một chút.

Ngoài ra, chúng tôi đã giới hạn thời lượng tập ở mức 200.

Vì vậy, nếu bạn tăng giới hạn, nó sẽ có thể chơi lâu hơn nữa.

Mục 4.4.5 Chương Kết luận

Củng cố là một cách hiệu quả và rất đơn giản để đào tạo một chức năng chính sách, nhưng nó

một chút quá đơn giản.

Đối với cuộc thăm dò giỏ hàng, nó hoạt động rất tốt vì không gian trạng thái rất nhỏ và chỉ có

hai hành động.

Nếu chúng ta đang xử lý một môi trường có nhiều hành động khả thi hơn, hãy củng cố tất cả

trong mỗi tập và hy vọng rằng ở mức độ trung bình, nó sẽ chỉ củng cố những điều tốt đẹp

hành động ngày càng trở nên kém tin cậy hơn.

Trong hai chương tiếp theo, chúng ta sẽ khám phá những cách đào tạo nhân viên phức tạp hơn.