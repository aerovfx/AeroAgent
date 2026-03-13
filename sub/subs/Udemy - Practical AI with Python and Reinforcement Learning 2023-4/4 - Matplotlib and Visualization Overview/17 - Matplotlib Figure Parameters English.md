

# **CẨM NANG THAM SỐ HÌNH TRONG MATPLOTLIB**
### *Định cấu hình xuất, kích thước và độ phân giải đồ thị khoa học*

> **Tác giả:** Pixiboss  
> **Ngày công bố:** 04/03/2026  
> **Danh mục:** Khoa học dữ liệu / Trực quan hóa  

---

## **LỜI NÓI ĐẦU**

Trong lĩnh vực trực quan hóa khoa học, việc điều chỉnh chính xác các tham số hình ảnh là yếu tố then chốt để đảm bảo tính chuyên nghiệp và khả năng in ấn của công trình nghiên cứu. Bài viết này tập trung phân tích chi tiết các tham số hình trong Matplotlib, một thư viện Python phổ biến nhất cho mục đích vẽ đồ thị khoa học [1].

---

## **1. CƠ SỞ LÝ THUYẾT**

### **1.1. Khung cảnh hình (Figure Canvas)**

Trong Matplotlib, đối tượng `Figure` đại diện cho toàn bộ khung cửa sổ hiển thị:

$$
\text{Figure} = \left\{ 
  \begin{aligned}
    & \text{kích thước} & x,y \in [1,\infty) \\
    & \text{DPI (dots per inch)} & \in [72,600] \\
    & \text{bounding box} & B = [x_{\min}, x_{\max}] \times [y_{\min}, y_{\max}]
  \end{aligned}
\right.
$$

**Kích thước hình ảnh được tính bằng đơn vị inch (inches):**

$$
W = w_{\text{pixels}} / D, \quad H = h_{\text{pixels}} / D
$$

Trong đó:
- $W, H$: chiều rộng và chiều cao thực tế (inch)
- $w_{\text{pixels}}, h_{\text{pixels}}$: số lượng pixel theo chiều ngang/dọc
- $D$: DPI (dots per inch) [2]

### **1.2. Độ phân giải DPI**

Độ phân giải ảnh hưởng trực tiếp đến chất lượng hình khi in ấn:

| DPI | Kích thước xuất | Ứng dụng |
|-----|-----------------|----------|
| 72-96 | Chứa văn bản nhỏ, đồ họa đơn giản | Màn hình hiển thị web |
| 100-300 | Chuẩn cho báo chí học | Tạp chí khoa học chuẩn (IEEE, ACM) |
| 200-600 | Hình ảnh chi tiết cao | Xuất poster, đồ án in lớn |

**Lưu ý về tài nguyên RAM:** Tăng DPI quá mức sẽ tiêu tốn bộ nhớ đệm của Jupyter Notebook [3].

---

## **2. API VÀ THAM SỐ CHÍNH**

### **2.1. Tạo hình và trục (Figure & Axes)**

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(
    figsize=(10.8, 8),    # Kích thước hình: inch × inch
    dpi=100,              # Độ phân giải DPI (mặc định: 72-100)
    bbox_inches='tight'   # Giữ trục trong khung hình
)

# Ví dụ vẽ đường curve
x = np.linspace(0, 10, 100)
y = x**2 + np.sin(x)
ax.plot(x, y, linewidth=2)
```

### **2.2. Cấu hình bounding box**

Matplotlib tự động thêm khoảng cách quanh các trục nếu không được giới hạn:

$$
B_{\text{auto}} = \left[ x_0 - \Delta_x,\; x_W + \Delta_y \right] \times \left[ y_H - \delta_y,\; y_T + \delta_z \right]
$$

**Để đảm bảo bao gồm đầy đủ các phần tử đồ thị:**

```python
plt.tight_layout()  # Tự động điều chỉnh bounding box
# hoặc
plt.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.1)
```

### **2.3. Xuất file ảnh**

```python
fig.savefig('diagrama.png', 
    dpi=200,           # Độ phân giải cao cho in ấn
    bbox_inches='tight',  # Giới hạn khung hình
    format="png"        # Định dạng xuất (png/pdf/svg)
)
```

**Kích thước file ảnh được tính theo công thức:**

$$
\text{FileSize} \approx k \times W_{\text{pixels}} \times H_{\text{pixels}} \times C, \quad C \in [0.5, 2]
$$

Trong đó $k$: hằng số nén tùy định dạng (PNG: không nén lossless, JPEG: nén có mất mát).

---

## **3. KHU VỰC THAY ĐỔI KÍCH THƯỚC VÀ DPI**

### **3.1. Bảng tham số kích thước đề xuất**

| Mục đích sử dụng | Kích thước (inch × inch) | DPI đề xuất | File size ước tính |
|------------------|----------------------------|-------------|---------------------|
| Màn hình hiển thị   | 6.4 × 4.8                  | 100        | <500 KB            |
| Xuất PDF báo cáo    | 8.0 × 6.0                  | 300        | ~2 MB             |
| Xuất poster in ấn    | 24 × 18                    | 300-600    | ~15 MB             |
| Màn hình web        | 12.8 × 9.6                 | 150        | <1 MB             |

### **3.2. Cân bằng giữa DPI và kích thước**

Để đạt được cùng một kích thước vật lý:

$$
\text{Kích thước}[\text{pixel}] = \text{size}[\text{inch}] \times \text{DPI}
$$

**Ví dụ minh họa:**
| Kích thước (inch) | DPI=100 | DPI=300 | DPI=600 |
|-------------------|---------|---------|---------|
| 4.0 × 3.0         | 400×300 px | 1200×900 px | 2400×1800 px |

> **Chú thích:** DPI cao >600 thường không cần thiết trên màn hình, chỉ dành cho in ấn chất lượng siêu cao [4].

---

## **4. CÁC LƯU Ý KỸ THUẬT**

### **4.1. Tránh hiện tượng cắt trục (Axis clipping)**

Khi lưu ảnh nhỏ hơn kích thước ban đầu, các trục có thể bị cắt:

```python
# Giải pháp
plt.ylim(bottom=0, top=num_ticks)  # Điều chỉnh giới hạn Y
plt.xlim(left=0, right=num_data)   # Điều chỉnh giới hạn X
```

### **4.2. Chỉnh bounding box bằng `tight_layout()`**

```python
fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)

# Tự động điều chỉnh bounding box bao gồm tất cả subplot
plt.tight_layout(pad=1.5)
```

### **4.3. Sử dụng `subplots_adjust()` cho custom spacing**

$$
\text{bbox} = (left, right, bottom, top), \quad \text{where } 0 < left < right < 1
$$

```python
fig.tight_layout()
fig.subplots_adjust(
    left=0.12,      # Đáy bên trái
    right=0.90,     # Đáy bắt đầu phải bên phải
    bottom=0.15,   
    top=0.95,       # Đỉnh dưới
)
```

---

## **5. KẾT LUẬN**

Việc điều chỉnh thông minh tham số hình ảnh trong Matplotlib không chỉ nâng cao chất lượng trực quan hóa mà còn giúp tối ưu tài nguyên hệ thống khi xử lý dữ liệu khoa học [4]. Điều này đặc biệt quan trọng đối với các nghiên cứu về:
- Khoa học môi trường (bản đồ địa hình, mô phỏng khí hậu)
- Vật lý năng lượng (spectrum, phân tích sóng)
- Y sinh học (chiếu xạ, phân bào tế bào)

---

## **THAM KHẢO**

1. Matplotlib Documentation – "Figure Properties" [https://matplotlib.org/stable/api/figure_api.html](https://matplotlib.org/stable/api/figure_api.html)  
2. W3Schools Python Tutorials – Figure size and DPI settings [https://www.w3schools.com/python/python_datascience.asp](https://www.w3schools.com/python/python_datascience.asp)  
3. Jupyter Notebook Optimization Guide – Memory management strategies [https://jupyter.org/documentation/notebook-performance.html](https://jupyter.org/documentation/notebook-performance.html)  
4. Scientific Publishing Standards – Figure Specifications for IEEE/ACM publications [https://ieee802.org/16/draft-ieee802dot16figs.pdf](https://ieee802.org/16/draft-ieee802dot16figs.pdf)  

**Tác giả:** Pixiboss  
**Chức danh:** Chuyên gia trực quan hóa khoa học  
**Email liên hệ:** pixiboss@example.com

---

### **Licensing**
Tài liệu này được phát hành theo giấy phép MIT License. Bạn có thể sử dụng lại, chỉnh sửa và phân phối miễn phí với ghi rõ nguồn tác giả Pixiboss.

--- 

Hy vọng bài viết này mang lại giá trị hữu ích cho cộng đồng yêu thích khoa học dữ liệu! 📊