# Figure Object trong Matplotlib: Khái niệm, Nguyên lý và Ứng dụng

**Tác giả:** Pixiboss  
**Ngày công bố:** 19 tháng 5 năm 2024

---

## Tóm tắt (Abstract)

Bài viết này nghiên cứu sâu về **Figure Object** trong thư viện đồ họa khoa học Matplotlib của Python. Qua phân tích hệ thống đối tượng Figure và Axes, chúng ta hiểu rõ cơ chế kiểm soát định dạng cấp cao, vị trí trục tọa độ và khả năng điều chỉnh kích thước canvas. Kết quả cung cấp nền tảng lý thuyết vững chắc cho việc xây dựng đồ thị khoa học chuyên nghiệp.

---

## 1. Giới thiệu

Matplotlib là thư viện đồ họa 2D hàng đầu trong Python dành cho nghiên cứu khoa học, kỹ thuật và giáo dục [Hunter, 2007]. Hệ thống Object-Oriented (OO) của Matplotlib cung cấp cách tiếp cận linh hoạt hơn so với hàm API truyền thống. Bài viết tập trung vào:

1. **Structure of Figure** – Khung vẽ cơ bản
2. **Axes Positioning and Sizing** – Định vị bộ trục
3. **Mathematical Formalization** – Mô hình toán học minh họa

---

## 2. Khung Hình và Figure Object

### 2.1. Định nghĩa

```python
import matplotlib.pyplot as plt

# Tạo đối tượng Figure (kích thước mặc định: 432x288 pixel)
fig = plt.figure(figsize=(720, 288))  # đơn vị inch × DPI=72
```

Figure đại diện cho **canvas vẽ trống** – vùng hình học xám chứa trục tọa độ chưa hiển thị dữ liệu [Stewart, 2015].

### 2.2. Phương trình kích thước Figure

Khi cần điều chỉnh kích thước:

$$
\text{Width (pixels)} = \text{Width (inch)} \times \text{DPI} \\
\text{Height (pixels)} = \text{Height (inch)} \times \text{DPI}
$$

Ví dụ với DPI = 72:

$$
W = 10 \times 72 = 720, \quad H = 10 \times 72 = 720
$$

---

## 3. Thêm Trục vào Figure

### 3.1. Command `add_axes()`

```python
ax = fig.add_axes([left, bottom, width, height])
```

#### Định nghĩa các tham số:

| Tham số | Mô tả | Khoảng giá trị |
|---------|--------|-----------------|
| `left`  | Góc dưới trái (tọa độ X) | [0, 1] |
| `bottom` | Góc dưới trái (tọa độ Y) | [0, 1] |
| `width`  | Chiều rộng trục | [0, 1] |
| `height` | Chiều cao trục | [0, 1] |

### 3.2. Mô hình hóa vị trí bộ trục

$$
\text{axes_position} = (x_0, y_0, w, h)
$$

Trong đó:
- $(x_0, y_0)$ là góc dưới trái so với Figure canvas
- $w, h$ là tỷ lệ kích thước chiếm phần trăm của Figure

### 3.3. Ví dụ minh họa

```python
# Trục nằm ở góc dưới trái, chiếm toàn bộ canvas
ax1 = fig.add_axes([0, 0, 1, 1])

# Trục nửa bên phải
ax2 = fig.add_axes([0.5, 0, 0.5, 1])
```

---

## 4. Vẽ đồ thị trên Axes

### 4.1. Các bước thực hiện

1. **Tạo Figure** → `fig = plt.figure()`
2. **Thêm Axes** → `ax = fig.add_axes([...])`
3. **Vẽ đồ thị** → `ax.plot(x, y)`

### 4.2. Ví dụ minh họa mã nguồn đầy đủ

```python
import numpy as np
import matplotlib.pyplot as plt

# Bước 1: Tạo Figure
fig, ax = plt.subplots(figsize=(8, 6))

# Bước 2: Thêm Axes (kích thước tiêu chuẩn)
ax.add_axes([0.1, 0.1, 0.8, 0.8])

# Bước 3: Vẽ đồ thị
x = np.linspace(0, 10, 100)
y = x**2
ax.plot(x, y)
```

---

## 5. Các tính năng mở rộng của Figure Object

### 5.1. Figure-level Properties

Figure hỗ trợ điều chỉnh các thuộc tính cấp cao:

| Thuộc tính | Mô tả | Ví dụ |
|------------|--------|--------|
| `fig.dpi` | Số điểm mỗi inch | `dpi=300` (cao hơn) |
| `fig.size` | Kích thước pixel | `(12, 9)` inches |
| `fig.subplots()` | Tạo nhiều subplots | `fig = plt.figure()# fig.add_subplot(2, 1, i)` |

### 5.2. Multiple Axes trên một Figure

```python
fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_axes([0.1, 0.65, 0.35, 0.3])
ax2 = fig.add_axes([0.52, 0.65, 0.35, 0.3])
```

---

## 6. So sánh: Object-Oriented vs. Functional API

### 6.1. Functional API (ngắn gọn)

```python
plt.plot(x, y)
plt.show()
```

### 6.2. Object-Oriented API (linh hoạt hơn)

```python
fig, ax = plt.subplots()
ax.plot(x, y)
fig.savefig('output.png')
```

---

## 7. Kết luận

Figure Object trong Matplotlib là nền tảng kiến trúc quan trọng cho việc xây dựng đồ thị khoa học. Qua việc sử dụng `add_axes()` và điều chỉnh các tham số cấp cao, người dùng có thể:

- Kiểm soát kích thước Figure (inch × DPI)
- Định vị chính xác vị trí trục tọa độ
- Vẽ nhiều subplot trong một canvas

Các nguyên tắc này hỗ trợ tốt cho phát triển báo cáo khoa học chuyên nghiệp.

---

## 8. Tài liệu tham khảo

1. Hunter, J. D. (2007). *Matplotlib: A 2D Graphics Environment*. Computational Science & Informatics.
2. van der Walt, S., et al. (2014). *The NumPy Array: An n-dimensional homogeneous array*.
3. Matplotlib Documentation [https://matplotlib.org]. Truy cập ngày 19/5/2024.
4. Stéphanie, B. (2020). *Python Data Visualization with Matplotlib*. Apress.

---

**© Pixiboss – Bài viết được lưu giữ trên nền tảng khoa học mở.**