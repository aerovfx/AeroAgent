# 📊 Giới Thiệu Về Matplotlib - Thư Viện Trực Quan Hóa Dữ Liệu Python

![Matplotlib Logo](https://matplotlib.org/_images/logo.png)

**Tác Giả:** Pixiboss  
**Cập Nhật:** 2024

---

## 🎯 Mục Lục

| Bài | Tiêu Đề | Thời Lượng |
|-----|--|-|
| 1 | Giới Thiệu Matplotlib | [ ] |
| 2 | Hai Cách Tiếp Cận | [ ] |
| 3 | Phương Pháp Chức Năng | [ ] |
| 4 | Phương Pháp Hướng Đối Tượng | [ ] |
| 5 | Tùy Chỉnh Đồ Thị | [ ] |

---

## 📖 Nội Dung Chính

### 1. Tổng Quan Về Matplotlib

Matplotlib là một trong những thư viện trực quan hóa phổ biến nhất cho Python và được coi là nền tảng của hầu hết các thư viện hình ảnh đồ thị khác[^1][^2].

![Python Data Science Stack](https://matplotlib.org/_static/logo.png)

#### Tại Sao Sử Dụng Matplotlib?

| Lý Do | Mô Tả |
|--------|-------|
| Linh Hoạt | Cho phép tùy biến hầu hết mọi loại biểu đồ |
| Cơ Bản | Là nền tảng cho Seaborn, Bokeh, Plotly |
| Dễ Học | Lấy cảm hứng từ MATLAB |

---

### 2. Hai Cách Tiếp Cận Trong Matplotlib[^3]

Matplotlib cung cấp **hai phương pháp chính** để tạo biểu đồ:

#### 2.1. Phương Pháp Dựa Trên Chức Năng (Functional API)

```python
import matplotlib.pyplot as plt

# Tạo biểu đồ đơn giản
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
```

**Đặc điểm:**
- Phù hợp cho người mới bắt đầu
- Cú pháp ngắn gọn
- Dễ đọc và viết nhanh

#### 2.2. Phương Pháp Hướng Đối Tượng (Object-Oriented API)

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
fig.show()
```

**Đặc điểm:**
- Linh hoạt hơn cho các đồ thị phức tạp
- Dễ quản lý nhiều đồ thị
- Phù hợp cho sản xuất chuyên nghiệp

---

### 3. Các Loại Biểu Đồ Cơ Bản

#### 3.1. Biểu Đồ Hàm Số (Function Plot)

$$y = f(x)$$

```python
x = np.linspace(0, 10, 100)
y = 2 * x
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Biểu Đồ Hàm Số')
```

#### 3.2. Biểu Đồ Dữ Liệu Đếm (Discrete Data Points)

$$y_i = f(x_i), \quad i = 1, 2, \dots, n$$

```python
x_data = [1, 2, 3, 4]
y_data = [2, 4, 6, 8]
plt.plot(x_data, y_data, 'o-')
```

#### 3.3. Các Loại Đồ Thị Phổ Biến[^4]

| Loại | Mô Tả | Hàm Số |
|------|-------|--------|
| Line Plot | Đường thẳng kết nối điểm dữ liệu | `plt.plot()` |
| Scatter Plot | Điểm rời rạc không nối đường | `plt.scatter()` |
| Bar Chart | Biểu đồ cột | `plt.bar()` |
| Histogram | Phân bố tần suất | `plt.hist()` |

---

### 4. Tùy Chỉnh Đồ Thị

#### 4.1. Màu Sắc và Đường Nét[^5]

```python
colors = ['#FF0000', '#00FF00', '#0000FF']
styles = ['-', '--', '-.', ':']
plt.plot(x, y1, color=colors[0], linestyle='-', label='Dòng 1')
```

#### 4.2. Đặc Điểm Định Dạng

| Tham Số | Mô Tả | Ví Dụ |
|----------|-------|-------|
| `linewidth` | Độ dày đường | `lw=2.5` |
| `markersize` | Kích thước marker | `ms=8` |
| `alpha` | Độ trong suốt (transparency) | `a=0.7` |

---

### 5. Biểu Đồ Nhiều Ô Phụ

```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].plot(x, y)
axes[0, 1].scatter(x, y)
axes[1, 0].bar(x, y)
axes[1, 1].hist(y)
plt.tight_layout()
```

---

### 6. Seaborn - Thư Viện Nâng Cao[^6]

Matplotlib là nền tảng của **Seaborn** - thư viện trực quan hóa nâng cao:

```python
import seaborn as sns
sns.scatterplot(data=df, x='x', y='y', hue='category')
```

> ⚠️ Lưu ý: Seaborn xây dựng dựa trên Matplotlib. Cần hiểu Matplotlib trước khi học Seaborn.

---

### 7. Tài Liệu Tham Khảo

[^1]: https://matplotlib.org/stable/
[^2]: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html
[^3]: https://matplotlib.org/tutorials/introduction.html
[^4]: https://matplotlib.org/gallery/subplots_axes_and_figures/axes_demo.html
[^5]: https://matplotlib.org/users/color_cycle.html
[^6]: https://seaborn.pydata.org/tutorial/

---

### 8. Bài Tập Thực Hành

| Bài | Nhiệm Vụ | Mức Độ |
|------|------------|-------|
| Bài 1 | Vẽ đường cong hàm số $y = x^2$ | DỄ |
| Bài 2 | Tạo scatter plot với màu sắc khác nhau | TRUNG BÌNH |
| Bài 3 | So sánh cả hai phương pháp API | TRUNG BÌNH KHÓ |

---

## 🔍 Tổng Kết

| Phương Pháp | Phù Hợp Khi | Ưu Điểm | Hạn Chế |
|--------------|-------------|--------|---------|
| Functional | Người mới, đồ thị đơn giản | Nhanh, dễ đọc | Ít linh hoạt |
| Object-Oriented | Đồ thị phức tạp, sản xuất | Kiểm soát tốt | Nhiều dòng mã hơn |

---

## 📝 Ghi Chú Từ Tác Giả **Pixiboss**

> "Matplotlib là công cụ thiết yếu cho bất kỳ nhà khoa học dữ liệu Python nào. Bắt đầu với phương pháp chức năng để hiểu cơ bản, sau đó chuyển sang hướng đối tượng khi cần linh hoạt cao hơn."

---

## 📚 Tài Liệu Đọc Thêm

- [Matplotlib Tutorial - Official Documentation](https://matplotlib.org/)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [Stack Overflow Matplotlib Tags](https://stackoverflow.com/questions/tagged/matplotlib)

---

**Biểu đồ minh họa:** 

$$
\text{Độ chính xác} = \frac{\sum |predicted - actual|}{n}
$$

![Flowchart so sánh hai phương pháp](https://matplotlib.org/_images/flowchart.png)

---

### ✅ Kết Luận

Matplotlib cung cấp công cụ hoàn chỉnh để tạo đồ thị trong Python. Việc hiểu cả hai phương pháp sẽ giúp bạn tối ưu hóa quy trình trực quan hóa dữ liệu chuyên nghiệp. Hãy thực hành với các bài tập và khám phá thêm về Seaborn để nâng cao kỹ năng của bạn! 🚀