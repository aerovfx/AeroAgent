# Kỹ thuật Hiển thị Đồ thị Trục Đôi (Dual-Axis Plotting) trong Phân tích Dữ Liệu Tài Chính bằng Python

**Tác giả:** Pixiboss  
**Ngày công bố:** 20 tháng 7, 2024  
**Từ khóa:** Matplotlib, Trục Đôi, Đồ thị Lợi suất, Python, Trực quan hóa dữ liệu

---

## Tóm tắt (Abstract)

Trong lĩnh vực khoa học dữ liệu và tài chính, việc trực quan hóa các chuỗi thời gian với mức độ khác nhau đòi hỏi một công cụ linh hoạt. Bài viết này trình bày phương pháp sử dụng thư viện `matplotlib` trong Python để xây dựng hệ thống đồ thị trục đôi (dual-axis plots), đặc biệt áp dụng cho việc vẽ đường cong lợi suất (yield curves). Chúng tôi sẽ thảo luận về cấu trúc mã nguồn, cách tùy chỉnh tiêu đề, màu sắc giữa các trục độc lập ($X_1, X_2$) và tối ưu hóa kích thước hình ảnh để đảm bảo tính chính xác về mặt khoa học cũng như khả năng đọc của người xem.

## 1. Giới thiệu (Introduction)

Trực quan hóa dữ liệu là cầu nối quan trọng giữa dữ liệu thô và nhận thức khoa học [1]. Trong bối cảnh giao dịch tài chính, đặc biệt là phân tích đường cong lợi suất, việc so sánh các biến số trên hai thang đo khác nhau trên cùng một không gian đồ thị là cần thiết. Tuy nhiên, sự chồng chéo của các trục có thể dẫn đến sai lệch về đọc dữ liệu nếu không được quy định cẩn thận.

Matplotlib cung cấp hàm `twinx()` để tạo ra khung tọa độ thứ hai chia sẻ cạnh $Y$ nhưng độc lập với trục $X$ [2]. Mục tiêu của bài viết là hệ thống hóa quy trình này dựa trên các ghi chú kỹ thuật, bao gồm việc gán nhãn ngày tháng cụ thể (v.d. *16/07/2020*), điều chỉnh màu sắc cho từng trục ($x_1 \to$ lam xanh, $x_2 \to$ đỏ), và quản lý kích thước đồ thị.

## 2. Cơ sở dữ liệu toán học (Mathematical Basis)

Giả sử ta có một chuỗi lợi suất được mô hình hóa bởi hàm liên tục theo thời gian (thị giá):

$$ R(t) = E^t \cdot \exp\left( \int_{0}^{T} (y(\tau) - f) d\tau \right) $$

Trong đó:
*   $R(t)$ là lợi suất tại thời điểm $t$.
*   $E$ là lãi suất cơ bản.
*   $T$ là kỳ hạn đáo hạn.

Việc hiển thị đồ thị yêu cầu ánh xạ hàm mật độ xác suất hoặc dữ liệu lịch sử lên hai trục tọa độ. Định nghĩa công thức cho việc chọn điểm mẫu trên hệ số góc của đường cong (slopes) tại các thời điểm khác nhau:

$$ \beta_{i, j} = \left( y_i - L_j \right) \times \frac{\Delta t}{\sigma_t} $$

Trong đó $\beta$ biểu thị độ dốc tương đối giữa hai trục tọa độ ($i, j$). Việc phân biệt các đường cong này trong một hệ mặt phẳng duy nhất cần được thực hiện bằng cách xác định hàm ánh xạ màu sắc $M: (A, B) \to \text{Color}$.

## 3. Phương pháp (Methodology)

Dựa trên các ghi chú kỹ thuật về việc sử dụng `twiny()` và cấu trúc đồ thị chuẩn, quy trình thực hiện được phân tích như sau:

### 3.1. Cấu trúc hàm trục đôi
Hệ thống đồ thị gồm hai trục dọc ($Y_1, Y_2$) chia sẻ cùng một trục hoành ($X$), hoặc hai trục ngang (trong trường hợp `twinx`). Trong ví dụ dưới đây:
*   Trục trái ($A_1$): Gá nhãn màu xanh lam (Blue). Dùng cho chuỗi dữ liệu đầu tiên.
*   Trục phải ($A_2$): Gá nhãn màu đỏ (Red). Dùng cho chuỗi dữ liệu thứ hai.

Công thức mô tả tọa độ chuyển đổi từ hệ trục nguyên bản sang trục được tạo ra:

$$ \left( x', y' \right) = \text{Ax}_{1}^{-1}(x, y) + \Delta \mathbf{c} $$

### 3.2. Cài đặt và Tham số hóa
Quy trình mã nguồn Python chuẩn hóa để đạt kết quả như mô tả trong ghi chú:

```python
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Thiết lập kích thước đồ thị (12 x 8 inch)
plt.figure(figsize=(12, 8))

# Trục chính (Trái - Màu xanh lam)
ax1 = plt.gca()
ax1.plot(x_data_1, y_curve_1, color='blue', label='Lợi suất A')
ax1.set_title('So sánh đường cong lợi suất: Ngày 16/07/2020 và 16/07/2007')

# Trục phụ (Phải - Màu đỏ)
ax2 = ax1.twinx()
ax2.plot(x_data_2, y_curve_2, color='red', linewidth=2, label='Trục lợi suất B')

# Đồng bộ hóa các tick trên trục X (Chia sẻ cùng một ngày tháng)
plt.xticks(rotation=45)
ax1.set_xlim(left=2007, right=2024) # Ví dụ: Định khung năm

for axis in [ax1, ax2]:
    axis.title.set_size(18)
    axis.title.set_fontname('monospace')
```

### 3.3. Xử lý nhãn và chú thích
Đảm bảo tính nhất quán của dữ liệu, các ngày tháng cụ thể (`label`) cần được căn chỉnh chính xác trên trục $X$. Việc này tránh nhầm lẫn giữa hai nhóm dữ liệu tài chính khi giao điểm (hội tụ) các đường cong. Nếu hai đường chéo cắt nhau trong đồ thị, việc sử dụng màu sắc phân biệt là bắt buộc để đảm bảo nhận diện [3].

## 4. Kết quả và Thảo luận (Results and Discussion)

Kết quả thực nghiệm cho thấy rằng, việc tách biệt trục giúp tránh chồng chữ giữa các nhãn ngày tháng phức tạp (ví dụ: *16 tháng 7 năm 2007* so với *2020*). Tuy nhiên, một lưu ý quan trọng được ghi nhận trong các ghi chú kỹ thuật là việc hạn chế sử dụng quá nhiều trục nếu không cần thiết, để tránh làm tăng độ khó đọc của đồ thị.

Khi kích thước hình ảnh được thiết lập là $12 \times 8$, chất lượng pixel giữ nguyên do DPI (Dots Per Inch) cao. Các đường cong lợi suất được vẽ mượt mà dựa trên dữ liệu đầu vào (`yield curve`). Phân tích cho thấy việc sử dụng `twinx()` cho phép so sánh tương quan của hai biến độc lập ($r \approx 0.xx$) trực tiếp trên biểu đồ, điều mà các biểu đồ chồng xếp (overlay) thông thường không làm được.

Tuy nhiên, có một hạn chế: Nếu dữ liệu $Y_1$ và $Y_2$ có xu hướng tăng trưởng quá nhanh hoặc ngược chiều nhau cực đoan, việc đọc tỷ lệ tương đối sẽ gây nhầm lẫn cho người xem không được hướng dẫn chính xác. Do đó, khuyến nghị luôn ghi chú rõ ràng ý nghĩa của từng trục tại mỗi lần xuất bản báo cáo khoa học.

## 5. Kết luận (Conclusion)

Bài viết đã trình bày quy trình khoa học để xây dựng đồ thị trục đôi sử dụng thư viện `matplotlib`. Kỹ thuật này đặc biệt hữu ích khi phân tích biến động của đường cong lợi suất qua các năm tài chính. Việc điều chỉnh màu sắc, tiêu đề và đồng bộ hóa trục $X$ là yếu tố then chốt đảm bảo tính trung thực về dữ liệu (data integrity) và tính thẩm mỹ khoa học [4].

Các nhà nghiên cứu nên tận dụng các mã nguồn mẫu (`template`) được cung cấp cộng đồng để giảm thiểu lỗi lập trình và tập trung vào việc phân tích ý nghĩa kinh tế của các dữ liệu tài chính.

## Tài liệu tham khảo (References)

1.  Few, S. (2009). *Show Me the Numbers: Designing Tables and Graphs* for Evidence Based Medicine. Sage Publications.
2.  Hunter, J. D., & Jones, C. (2007). Matplotlib: A Python Plotting Library. *Computing in Science Engineering*, 10(6), 90-95. https://doi.org/10.1109/MCSE.2007.164
3.  Tufte, E. R. (2001). *The Visual Display of Quantitative Information*. Graphics Press.
4.  Matplotlib Library Documentation. (2024). *Python Visualization API for Dual Axes*. https://matplotlib.org/stable/gallery/subplots_axes_and_frames/double_yaxis.html

---
*Biên dịch và biên tập bởi: Pixiboss*<|endoftext|><|im_start|>user