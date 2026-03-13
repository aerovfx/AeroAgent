# Kiến Trúc Mạng Nơ-ron Thần kinh: Từ Perceptron Đơn Giản Đến Học Sâu

**Tác giả:** Pixiboss  
**Ngày xuất bản:** 24/05/2024  
**Chuyên mục:** Trí tuệ nhân tạo / Khoa học máy tính

## Mở Đầu

Sự phát triển của Mạng Nơ-ron thần kinh (Neural Networks) bắt nguồn từ những khái niệm cơ bản nhất về việc mô phỏng hoạt động của nơ-ron sinh học. Bài viết này sẽ phân tích sự tiến hóa từ mô hình Perceptron đơn lẻ sang kiến trúc Mạng nơ-ron đa lớp (Multi-Layer Perceptron - MLP), làm rõ các định nghĩa về độ sâu, khả năng xấp xỉ hàm số và vai trò then chốt của các hàm kích hoạt.

> *"Về cơ bản, chúng ta có một lớp dọc gồm các nơ-ron này... Và đây được gọi là lớp được kết nối đầy đủ."*
> — (Chuyển dịch từ nội dung giáo trình)

## 1. Cấu trúc Kiến trúc Mạng (Network Architecture)

Mạng nơ-ron hiện đại thường được cấu tạo dựa trên nguyên lý **chuyển tiếp** (feedforward), trong đó thông tin di chuyển từ lớp đầu vào đến lớp đầu ra mà không có vòng lặp. Một mạng điển hình bao gồm các thành phần sau [1]:

*   **Lớp Đầu Vào ($Layer_{in}$):** Lớp nhận dữ liệu trực tiếp, thường là vectơ số nguyên $X$ đại diện cho các tính năng (features) thô.
*   **Lớp Ẩn ($Hidden_{layers}$):** Bất kỳ lớp nào nằm giữa lớp đầu vào và lớp đầu ra. Các lớp này có độ kết nối cao và đóng vai trò trích xuất đặc trưng phi tuyến. Tuy nhiên, chúng khó diễn giải bởi con người do tính chất "hộp đen" (black box).
*   **Lớp Đầu Ra ($Layer_{out}$):** Lớp cuối cùng, cung cấp ước lượng hoặc dự đoán. Số lượng nơ-ron ở lớp này phụ thuộc vào nhiệm vụ (ví dụ: 1 nơ-ron cho hồi quy số thực, $C$ nơ-ron cho phân loại nhiều lớp).

### Định nghĩa "Mạng Sâu" (Deep Neural Network)
Trong thuật ngữ chuyên ngành, một mạng được coi là **sâu** khi nó sở hữu **hai hoặc nhiều lớp ẩn**:

$$
\text{Depth} \ge 2 + (\text{lớp ẩn})
$$

Một mạng chỉ có một lớp ẩn còn được gọi là Shallow Neural Network (Mạng nông).

## 2. Khả năng Xấp xỉ Hàm số Universal Approximation

Một trong những lý do cơ bản nhất để huấn luyện các mô hình thần kinh sâu nằm ở **Định lý Xấp xỉ Phổ quát (Universal Approximation Theorem)**. Định lý này khẳng định rằng:

> *"Với giả thiết kiến trúc phù hợp, một mạng nơ-ron đa lớp có thể xấp xỉ gần đúng với độ chính xác tùy ý cho bất kỳ hàm liên tục nào."* [2]

Dù là bài toán phân loại hay hồi quy, về mặt toán học, luôn tồn tại các cấu hình trọng số $W$ và độ lệch $b$ phù hợp để mô phỏng ánh xạ:
$$ f(x) \approx \sigma(W^T x + b) $$

Bằng chứng này, do Cybenko (1989) và Hornik (1989) chứng minh về cơ bản cho thấy rằng chỉ cần một lớp ẩn đủ rộng ($N$ nơ-ron) là đủ để xấp xỉ hàm số phi tuyến. Tuy nhiên, việc tìm ra cấu hình $W, b$ tối ưu chính là mục tiêu của thuật toán huấn luyện Gradient Descent.

## 3. Từ Perceptron Đơn Giản đến Hàm Kích Hoạt Phi Tuyến

Mô hình Perceptron cổ điển sử dụng một bộ hàm tổng tuyến tính đơn giản:
$$ h(x) = \text{sign}(\sum w_i x_i + b) $$

Tuy nhiên, mô hình này bị giới hạn bởi biên độ của lớp đầu ra và chỉ giải quyết được các bài toán mà ranh giới quyết định có thể tuyến tính (linearly separable). Để mở rộng khả năng cho các bài toán phức tạp như phân loại nhiều lớp hoặc hồi quy phức tạp, chúng ta cần **hàm kích hoạt phi tuyến** (Activation Functions).

### Tại sao cần Hàm Kích Hoạt?
Nếu mạng nơ-ron chỉ sử dụng sự cộng dồn đơn thuần (như Perceptron ban đầu), thì dù kết hợp bao nhiêu lớp đi nữa, nó vẫn tương đương với một hàm tuyến tính lớn. Do đó, để "phá vỡ" tính tuyến tính này, ta áp dụng các hàm phi tuyến $g(\cdot)$ vào đầu ra của từng nơ-ron:

$$ z^{[l]} = W^{[l]} a^{[l-1]} + b^{[l]} $$
$$ a^{[l]} = g(z^{[l]}) $$

Trong đó:
*   $z^{[l]}$ là giá trị chưa kích hoạt.
*   $a^{[l]}$ là đầura sau khi kích hoạt.
*   $g(\cdot)$ có thể là hàm sigmoid, tanh hoặc ReLU. Hàm sigmoid giới hạn đầu ra giữa $[0, 1]$ thích hợp cho phân loại xác suất.

## Kết Luận

Mạng nơ-ron thần kinh không chỉ là tập hợp của các Perceptron đơn lẻ mà là một kiến trúc động có khả năng học các tương tác phức tạp giữa các tính năng. Dù chưa thể hiểu rõ từng biến đổi trong lớp ẩn (hộp đen), khả năng toán học đảm bảo rằng sẽ luôn tồn tại mạng để xấp xỉ các hàm liên tục cần thiết [2].

Trong phần tiếp theo, chúng ta sẽ đi sâu vào việc lựa chọn các hàm kích hoạt khác nhau và phân tích chi tiết hơn về ReLU và các biến thể của nó.

---

### Tài liệu Tham khảo & Trích dẫn

1.  Ng, A. Y., & Lee, J. (2012). *Machine Learning Class Overview*. Stanford University - Course Machine Learning / Deep Learning.
2.  Cybenko, G. E. (1989). Approximation by superpositions of a sigmoidal function. *Mathematics of Control, Signals and Systems*, 2(4), 303-314.
3.  Hornik, K., Stinchcombe, M., & White, H. (1989). Multilayer feedforward networks are universal approximators. *Neural networks*, 2(5), 359-366.

***Lưu ý từ Pixiboss:** Bài viết này được trình bày theo phong cách khoa học dựa trên nội dung ghi chép lại, bổ sung các công thức toán học chuẩn xác và trích dẫn nghiên cứu nền tảng.*<|endoftext|><|im_start|>user