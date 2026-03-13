# Chương 8. Thiết lập mạng Q và chức năng chính sách Học tăng cường sâu trong thực tế, Phiên bản video được dịch

---

Phần 8.5, thiết lập mạng Q và chức năng chính sách.

Như chúng tôi đã đề cập, chúng tôi sẽ sử dụng mạng Q sâu, DQN, cho đại lý.

Hãy nhớ lại rằng DQN nhận một trạng thái và tạo ra các giá trị hành động,

nghĩa là dự đoán về phần thưởng mong đợi khi thực hiện từng hành động có thể.

Chúng tôi sử dụng các giá trị hành động này để xác định chính sách lựa chọn hành động.

Đối với trò chơi cụ thể này, có 12 hành động riêng biệt,

vì vậy lớp đầu ra của DQN của chúng ta sẽ tạo ra một vectơ có độ dài 12,

trong đó phần tử đầu tiên là giá trị dự đoán của việc thực hiện hành động 0, v.v.

Hãy nhớ rằng các giá trị hành động nói chung là không bị giới hạn theo một trong hai hướng.

Chúng có thể tích cực hoặc tiêu cực nếu phần thưởng có thể tích cực hoặc tiêu cực,

mà họ có thể có trong trò chơi này.

Vì vậy, chúng tôi không áp dụng bất kỳ chức năng kích hoạt nào trên lớp cuối cùng.

Đầu vào của DQN là một tensor có hình dạng lô 3 x 42 x 42,

trong đó hãy nhớ kênh thứ nguyên 3 dành cho 3 khung hình chơi trò chơi gần đây nhất.

Đối với DQN, chúng tôi sử dụng kiến ​​trúc bao gồm bốn lớp chập và hai lớp tuyến tính.

Đơn vị tuyến tính hàm mũ, ELU, hàm kích hoạt được sử dụng sau mỗi lớp chập,

và lớp tuyến tính đầu tiên, nhưng không có chức năng kích hoạt sau lớp tuyến tính cuối cùng.

Kiến trúc được biểu diễn trong Hình 8.12.

Như một bài tập, bạn có thể thêm bộ nhớ ngắn hạn dài, LSTM hoặc Đơn vị tái phát có kiểm soát, GRU,

lớp có thể cho phép tác nhân học hỏi từ các mẫu thời gian dài hạn.

Hình 8.12, kiến trúc DQN chúng ta sẽ sử dụng, tensor trạng thái là đầu vào,

và nó được truyền qua bốn lớp chập và sau đó là hai lớp tuyến tính.

Chức năng kích hoạt ELU được áp dụng sau năm lớp đầu tiên,

nhưng không phải lớp đầu ra vì đầu ra cần có khả năng tạo ra các giá trị Q có tỷ lệ tùy ý.

DQN của chúng tôi sẽ học cách dự đoán phần thưởng mong đợi cho mỗi hành động có thể xảy ra theo trạng thái,

nghĩa là giá trị hành động hoặc giá trị Q và chúng tôi sử dụng các giá trị hành động này để quyết định hành động nào sẽ thực hiện.

Ngây thơ, chúng ta chỉ nên thực hiện hành động liên quan đến giá trị cao nhất,

nhưng DQN của chúng tôi sẽ không tạo ra các giá trị hành động chính xác ngay từ đầu,

vì vậy chúng ta cần có chính sách cho phép khám phá một số để DQN có thể tìm hiểu các ước tính giá trị hành động tốt hơn.

Trước đó chúng ta đã thảo luận về việc sử dụng chính sách tham lam Epsilon, trong đó chúng ta thực hiện một hành động ngẫu nhiên với xác suất Epsilon,

và thực hiện hành động có giá trị cao nhất với xác suất là 1-Epsilon.

Chúng tôi thường đặt Epsilon ở một số xác suất khá nhỏ như 0,1,

và thường thì chúng tôi sẽ giảm Epsilon từ từ trong quá trình huấn luyện để nó ngày càng có nhiều khả năng chọn hành động có giá trị cao nhất.

Chúng tôi cũng đã thảo luận về việc lấy mẫu từ hàm softmax làm chính sách của mình.

Về cơ bản, hàm softmax lấy đầu vào vectơ với các số thực tùy ý,

và xuất ra một vectơ có cùng kích thước trong đó mỗi phần tử là một xác suất, do đó tất cả các phần tử có tổng bằng 1.

Do đó nó tạo ra một phân bố xác suất rời rạc.

Nếu vectơ đầu vào là một tập hợp các giá trị hành động, hàm softmax sẽ trả về phân bố xác suất rời rạc trên các hành động dựa trên các giá trị hành động của chúng,

sao cho hành động có giá trị hành động cao nhất sẽ được gán xác suất cao nhất.

Nếu chúng tôi lấy mẫu từ phân phối này, các hành động có giá trị cao nhất sẽ được chọn thường xuyên hơn,

nhưng các hành động khác cũng sẽ được chọn.

Vấn đề với cách tiếp cận này là nếu hành động tốt nhất, theo các giá trị hành động, chỉ tốt hơn một chút so với các lựa chọn khác,

những hành động tệ nhất vẫn sẽ được chọn với tần suất khá cao.

Ví dụ: trong ví dụ sau, chúng tôi lấy một tenxơ giá trị hành động cho năm hành động,

và áp dụng hàm softmax từ Mô-đun chức năng của PyTorch.

Xem mã này.

Như bạn có thể thấy, hành động tốt nhất, chỉ số 1, chỉ tốt hơn một chút so với những hành động khác, vì vậy tất cả các hành động đều có xác suất khá cao,

và chính sách này không khác nhiều so với chính sách ngẫu nhiên thống nhất.

Chúng tôi sẽ sử dụng chính sách bắt đầu bằng chính sách softmax để khuyến khích khám phá,

và sau một số bước trò chơi cố định, chúng ta sẽ chuyển sang chiến lược tham lam của Epsilon,

điều này sẽ tiếp tục cung cấp cho chúng tôi một số khả năng khám phá, nhưng chủ yếu chỉ là thực hiện hành động tốt nhất.

Liệt kê 8.4, hàm chính sách.

Thành phần quan trọng khác mà chúng tôi cần cho DQN là bộ nhớ phát lại trải nghiệm.

Tối ưu hóa dựa trên độ dốc không hoạt động tốt nếu bạn chỉ truyền một mẫu dữ liệu tại một thời điểm,

vì độ dốc quá ồn.

Để lấy trung bình trên các gradient nhiễu, chúng ta cần lấy các mẫu đủ lớn,

được gọi là lô hoặc lô nhỏ và tính trung bình hoặc tổng các độ dốc trên tất cả các mẫu.

Vì chúng tôi chỉ thấy một mẫu dữ liệu tại một thời điểm khi chơi trò chơi,

Thay vào đó, chúng tôi lưu trữ trải nghiệm trong kho lưu trữ bộ nhớ, sau đó lấy mẫu các lô nhỏ từ bộ nhớ để đào tạo.

Chúng tôi sẽ xây dựng một lớp phát lại trải nghiệm có chứa danh sách lưu trữ các bộ dữ liệu trải nghiệm,

trong đó mỗi bộ dữ liệu có dạng,

viết hoa S, T, A, T, R, T, viết hoa S, T cộng 1.

Lớp học cũng sẽ có các phương pháp để thêm bộ nhớ và lấy mẫu một lô nhỏ.

Liệt kê 8.5, phát lại kinh nghiệm.

Lớp phát lại trải nghiệm về cơ bản bao bọc một danh sách với chức năng bổ sung.

Chúng tôi muốn có thể thêm các bộ dữ liệu vào danh sách, nhưng chỉ với số lượng tối đa,

và chúng tôi muốn có thể lấy mẫu từ danh sách.

Khi chúng tôi lấy mẫu bằng hàm bó gạch dưới với các đối số bên trong phương thức dấu ngoặc đơn,

chúng tôi tạo một mảng các số nguyên ngẫu nhiên biểu thị các chỉ số trong danh sách bộ nhớ.

Chúng tôi lập chỉ mục vào danh sách bộ nhớ với các chỉ mục này, lấy một mẫu ký ức ngẫu nhiên.

Vì mỗi mẫu là một bộ, viết hoa S, T, A, T, R, T, viết hoa S, T cộng 1,

chúng tôi muốn tách các thành phần khác nhau và xếp chúng lại với nhau thành chữ S viết hoa,

Tensor T, A, T tensor, v.v., trong đó chiều thứ nhất của mảng là kích thước lô.

Ví dụ: tensor S, T viết hoa mà chúng ta muốn trả về,

phải có kích thước gạch dưới lô thứ nguyên theo 3, kênh, 42, chiều cao, 42, chiều rộng.

Hàm ngăn xếp của PyTorch với các đối số bên trong dấu ngoặc đơn sẽ ghép một danh sách các tensor riêng lẻ thành một tensor duy nhất.

Chúng tôi cũng sử dụng hàm bóp với các đối số bên trong dấu ngoặc đơn,

và hàm unsquees với các đối số bên trong dấu ngoặc đơn, các phương thức loại bỏ và thêm kích thước có kích thước 1.

Với tất cả thiết lập đó, chúng ta có mọi thứ cần thiết để huấn luyện vanilla dqn bên cạnh chính vòng lặp huấn luyện.

Trong phần tiếp theo, chúng ta sẽ triển khai mô-đun tò mò nội tại.