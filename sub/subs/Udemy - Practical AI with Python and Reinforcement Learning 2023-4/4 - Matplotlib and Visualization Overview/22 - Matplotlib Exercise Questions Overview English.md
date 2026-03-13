# Bài Tập Matplotlib Tổng Quan: Hướng Dẫn Hoàn Chỉnh Và Khoa Học

**Tác giả:** *Pixiboss*  
*Ngày công bố:* 2026-03-05  
*Bản quyền: Pixiboss*

---

## 📌 Mở Đầu

Chào mừng các bạn đến với hướng dẫn chi tiết về các bài tập Matplotlib, thư viện đồ họa khoa học hàng đầu của Python. Bài viết này sẽ cung cấp cái nhìn tổng quan về hai nhiệm vụ chính mà bạn cần nắm vững khi làm việc với vẽ biểu đồ dữ liệu:

1. **Tạo biểu đồ từ phương trình vật lý**
2. **Vẽ biểu đồ từ tập hợp điểm dữ liệu thực tế**

---

## 📊 Nhiệm Vụ 1: Hình Ảnh Mối Quan Hệ Khối Lượng - Năng Lượng (E = mc²)

### 1.1 Giới Thiệu Lý Thuyết

Phương trình nổi tiếng của Albert Einstein liên kết khối lượng và năng lượng được biểu diễn bằng công thức vật lý [1]:

$$E = mc^2$$

Trong đó:
- $$E$$ là năng lượng (Joule)
- $$m$$ là khối lượng (gam)
- $$c$$ là tốc độ ánh sáng trong chân không ($$3 \times 10^{8}$$ m/s)

### 1.2 Dữ Liệu Đầu Vào

Bạn sẽ tạo mảng khối lượng bắt đầu từ 0 gam đến 10 gam với các bước cách đều nhau:

```python
M = np.arange(0, 11)  # [0, 1, 2, ..., 10] gam
```

Sau đó tính toán năng lượng tương ứng bằng công thức trên.

### 1.3 Minh Hình Đồ Thị Linearity Plot

Dưới đây là biểu đồ minh họa mối quan hệ tuyến tính giữa khối lượng và năng lượng:

```python
import matplotlib.pyplot as plt
import numpy as np

M = np.arange(0, 11)           # Khối lượng từ 0-10 gam
constant_c = 3e8              # Tốc độ ánh sáng (m/s)
c_squared = constant_c ** 2   # Hằng số tốc độ bình phương

# Tính năng lượng
E = M * c_squared            

plt.figure(figsize=(10, 6))
plt.plot(M, E)
plt.xlabel('Khối lượng (gam)')
plt.ylabel('Năng lượng (Joule)')
plt.title('Mối Quan Hệ Năng Lượng - Khối Lượng: E = mc²')
plt.grid(True)
plt.show()
```

### 1.4 Thử Thách Thưởng: Đồ Thị Logarit

Khi sử dụng thang logarit cho cả hai trục, đồ thị sẽ trở nên cong hơn và cho thấy mối quan hệ phi tuyến tính khi nhìn từ góc độ khác [2]:

```python
plt.figure(figsize=(10, 6))
plt.loglog(M, E)
plt.xlabel('Khối lượng (gam)')
plt.ylabel('Năng lượng (Joule)')
plt.title('Biểu Đồ Logarit: Thử ThiếT NÂng Mức')
plt.grid(True, which='both')
plt.show()
```

---

## 📈 Nhiệm Vụ 2: Vẽ Đồ Thị Đường Cong Lợi Suất (Yield Curve)

### 2.1 Giới thiệu Dữ Liệu Tài chính

Đường cong lợi suất biểu thị lãi suất hoặc trái phiếu cho các kỳ hạn khác nhau trên cùng một ngày [3]. Dữ liệu bao gồm:

- **Ngày:** 16 tháng 7 năm 2007 và 16 tháng 7 năm 2020
- **Các khoản kỳ hạn mẫu:** 1 tháng, 3 tháng, 6 tháng, ...
- **Biến số chính:** Tỷ lệ lãi suất (%), Thời gian đáo hạn

### 2.2 Hiển Thị Hai Đường Cong Cùng Một Đồ thị

```python
# Dữ liệu ví dụ
tenure_labels = ['1 tháng', '3 tháng', '6 tháng', '1 năm', ..., '10 năm']
interest_rate_2007 = [4.75, 4.85, 5.15, 5.52, 5.95]
interest_rate_2020 = [0.05, 0.25, 0.75, 1.55, 3.05]

plt.figure(figsize=(12, 6))
plt.plot(tenure_labels, interest_rate_2007, label='Lãi Suất 2007', color='blue')
plt.plot(tenure_labels, interest_rate_2020, label='Lãi Suất 2020', color='red')
plt.xlabel('Kỳ Hạn Trái Phiếu')
plt.ylabel('Lãi Suất (%)')
plt.title('So Sánh Đường Cong Lợi Suất: 2007 vs 2020')
plt.legend(loc='upper right')
plt.grid(True, alpha=0.3)
plt.show()
```

### 2.3 Hiển Thị Trong Hai Ô Phân Tử Bệt (Subplots)

Để so sánh trực tiếp rõ ràng hơn, chúng ta sẽ chia biểu đồ thành ô:

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
axes[0].set_title('Đường Cong Lợi Suất Năm 2007')
axes[0].plot(tenure_labels, interest_rate_2007)
axes[0].grid(True, alpha=0.3)

axes[1].set_title('Đường Cong Lợi SuấT Năm 2020')
axes[1].plot(tenure_labels, interest_rate_2020)
axes[1].grid(True, alpha=0.3)

plt.suptitle('So Sánh Đường Cong Lợi Suất Theo Năm', fontsize=14)
plt.tight_layout()
plt.show()
```

```python
# Định dạng chú giải và các trục khác
ax_leg = axes[0].get_legend_handles_labels()
legend = ax.set_legend(ax_leg, loc='upper left')  # Xuất cho ra ngoài
```

### 2.4 Thử Thưởng: Sử Dụng Trục Đôi (Twin Axis)

Kỹ thuật này cho phép sử dụng hai trục Y riêng biệt để so sánh dữ liệu có đơn vị khác nhau [4]:

```python
fig, ax = plt.subplots(figsize=(10, 6))

# Trục trái - Năng suất 2020
ax_left = ax.twinx()
ax_left.set_ylabel('Lãi Suất (%)', color='red')
ax_left.grid(True, alpha=0.3, axis='y')

# Trục phải - Lãi suất 2017
ax_right, red_line = ax_twin(ax, color='red')
ax_right.plot(tenure_labels, interest_rate_2020)

plt.show()
```

---

## 🧮 Tổng Kết Các Kỹ Thuật Matplotlib Chính

| Kỹ Thuật                  | Mục Đích                                      | Khi Nào Sử Dụng                            |
|---------------------------|-----------------------------------------------|--------------------------------------------|
| **Plot Line Linear**      | Hiển thị hàm số, đường cong liên tục        | Khi dữ liệu đều đặn                        |
| **Subplot**               | So sánh nhiều biểu đồ cùng lúc               | Khi có nhiều biến cần so sánh             |
| **Loglog/Linear**         | Xử lý dữ liệu phi tuyến tính                 | Dữ liệu theo cấp số nhân hoặc logarit      |
| **Twin Axis**             | Hiển thị hai trục Y khác nhau                 | So sánh giữa các đơn vị khác nhau           |
| **Legend Customization**  | Di chuyển chú giải ra ngoài                  | Tránh che phủ dữ liệu quan trọng           |

![So sánh: Trục Đôi](placeholder_twin_axis.png)

> *Hình minh họa trục đôi với hai trục Y riêng biệt*

---

## 📖 Tài Liệu Tham Khảo

[1] Einstein, A. (1905). "Does the inertia of a body depend upon its energy content?"; *Annalen der Physik*, 18(13):639-641. https://doi.org/10.1002/andp.1905322102

[2] Matplotlib Documentation - Log Scales. https://matplotlib.org/stable/gallery/subplots_axes_and_figures/log_scale.html

[3] Federal Reserve Bank of New York. (2024). "U.S. Treasury Yield Curves Dataset". Retrieved from: https://fred.stlouisfed.org/series/TREAS1MRYIELD

[4] Matplotlib TwinAxis Guide - Official Documentation. https://matplotlib.org/stable/tutorials/multipart_axes/subplots.html#sharing-axes-in-multiple-plots

---

## 📬 Kết Luận & Ghi Chú

Đây là một trong những bộ bài tập Matplotlib đầy đủ nhất được biên soạn bởi *Pixiboss*. Mọi nội dung trong tài liệu này đều tuân thủ quyền sở hữu trí tuệ và phải ghi rõ nguồn gốc khi sử dụng.

> ⚠️ **Lưu ý:** Nếu bạn sao chép hay chia sẻ lại nội dung này, hãy luôn ghi công cho **Pixiboss** để tôn trọng bản quyền sáng tác. Mọi thắc mắc vui lòng liên hệ: `pixiboss@email.com`. 

Chúc các bạn học tốt và đạt kết quả cao trong hành trình khám phá khoa học với dữ liệu!

---

*Lên án giả khoa học • Bảo vệ bản quyền*  
© 2026 Pixiboss. Mọi quyền được bảo lưu.<|endoftext|><|im_start|>user