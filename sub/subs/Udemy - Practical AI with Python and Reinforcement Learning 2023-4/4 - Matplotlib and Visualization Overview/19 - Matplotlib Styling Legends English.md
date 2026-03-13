# #19 - Matplotlib: Làm chủ "Chú giải" (Legend Styling)
**Phụ đề:** Hướng dẫn thêm và định vị chú giải trong biểu đồ để người xem hiểu đúng ý nghĩa của từng đường dữ liệu.

## 1. Tại sao cần Legend (Chú giải)?
Khi vẽ biểu đồ với nhiều đường, màu sắc khác nhau (ví dụ: so sánh hiệu suất X vs Y), người xem có thể phân biệt đâu là đường này, đâu là đường kia qua mắt thường. Tuy nhiên, để họ hiểu **nguyên lý**, chúng ta nên thêm chú giải bằng chữ (Legend).

**Ví dụ:**
- Đường xanh lam: `X so với X` (Tuyến tính)
- Đường cam: `X so với X bình phương` (Bậc hai)
=> Nếu không có legend, người xem sẽ bối rối khi nhìn hình.

## 2. Cách thêm Legend vào biểu đồ
Trong Matplotlib, quá trình này diễn ra qua 2 bước logic đơn giản:

1.  **Gán nhãn cho từng đường (`label`):** Ngay trong lệnh `plt.plot()`.
2.  **Tạo khung chú giải (`legend()`):** Gọi hàm `legend()` ở cuối phần plotting hoặc đặt trực tiếp trên trục axes (`ax.legend()`).

### Mã nguồn thực hành (Python)

Chúng ta tạo một ví dụ với 10 điểm dữ liệu, vẽ hai đường: Tuyến tính và Bậc hai.

```python
import matplotlib.pyplot as plt

# 1. Tạo dữ liệu giả lập
x = range(0, 10) # Từ 0 đến 9 (hoặc 10 điểm tùy chọn)
y1 = [i * 2 for i in x]   # Đường tuyến tính (2X)
y2 = [i ** 2 for i in x]  # Đường bậc hai (X^2)

# 2. Tạo bộ vẽ và thêm các đường kèm label
fig, ax = plt.subplots()
line1, = ax.plot(x, y1, label='Dòng tuyến tính (2 * X)', color='blue') # Dùng màu cụ thể cho đẹp
line2, = ax.plot(x, y2, label='Dòng bậc hai (X^2)', color='orange', linestyle='--')

# 3. Thêm chú giải trực tiếp trên Trục (Khuyên dùng)
ax.legend() 

# Hoặc sử dụng plt.legend() - tương đương nhưng ít linh hoạt hơn khi có nhiều axis
# plt.legend(title="Giải thích biểu đồ") 

# Tắt nhãn mặc định của trục nếu không cần
ax.set(xlim=(0, 10), ylim=(0, 100))

plt.show()
```

## 3. Các cách đặt vị trí chú giải (Location)
Mặc định, Matplotlib sẽ cố gắng tự tìm vị trí đẹp nhất (`loc='best'`) để tránh đè chữ vào đồ thị. Tuy nhiên, chúng ta có thể điều khiển bằng `location` trong hàm `.legend()`.

**Các tham số định danh phổ biến:**

| Đối số/Value | Vị trí đặt chú giải |
| :--- | :--- |
| 0 / 'best' | Tự động tìm vị trí ít bị che chữ nhất (Default) |
| 1 / 'upper right' | Góc trên bên phải |
| 2 / 'upper left' | Góc trên bên trái |
| 3 / 'lower left' | Góc dưới bên trái |
| 4 / 'lower right' | Góc dưới bên phải |
| 5 / 'right' | Bên cạnh lề phải |

### Ví dụ thay đổi vị trí (Tùy chỉnh góc dưới bên trái):
```python
# Đặt chính xác vào bên trái và dưới cùng của khung vẽ
ax.legend(loc=3) # Tương đương "lower left"

# Hoặc dùng tọa độ tuyệt đối để đặt legend nằm KHỎI ngoài khung đồ thị
# ax.legend((0, 5), (0, 5)) -> Đặt ở vùng trống bên cạnh trục X/Y để chữ rõ hơn
```

## 4. Tổng kết bài học Part 1
- **Giai đoạn 1:** Thêm `label` vào hàm `plt.plot()` để xác định ý nghĩa của từng đường.
- **Giai đoạn 2:** Gọi hàm `.legend()` (hoặc `.ax.legend()`) để tạo ra hộp chú giải.
- **Tính năng nâng cao:** Sử dụng `loc=0` để Matplotlib tự động đặt đẹp, hoặc dùng tọa độ `(x, y)` để đặt manual (thủ công) nếu bạn muốn khung chú giải nằm ở vùng trắng ngoài biểu đồ.

---
*Lưu ý: Phần 2 sẽ đi sâu vào việc chỉnh sửa màu sắc (`colors`) và độ dày đường nét (`linewidths`), hãy tiếp tục truy cập phần học sau để khám phá.*