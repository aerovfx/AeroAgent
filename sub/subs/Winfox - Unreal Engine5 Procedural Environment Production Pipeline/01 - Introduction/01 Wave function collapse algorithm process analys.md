# Thuật Toán Wave Function Collapse - Phân Tích Quy Trình

## Tổng Quan

Chương này giới thiệu về **Thuật toán Wave Function Collapse (WFC)** và cách áp dụng nó trong việc tạo môi trường procedural trong Unreal Engine 5. WFC là một thuật toán mạnh mẽ để tự động tạo ra các cấu trúc phức tạp từ các module cơ bản.

## 1. Giới Thiệu về Wave Function Collapse

### 1.1 Khái Niệm Cơ Bản

Wave Function Collapse (WFC) là thuật toán được sử dụng để tạo ra các mẫu (patterns) phức tạp từ các mẫu đơn giản hơn. Trong ngữ cảnh 3D:

- **2D WFC**: Tương tự như việc điền các ô trong lưới
- **3D WFC**: Mở rộng sang không gian ba chiều, điền các khối (boxes) trong không gian 3D

### 1.2 Nguyên Lý Hoạt Động

```
WFC = { Modules } + { Constraints } + { Random Selection }
```

Trong đó:
- **Modules**: Tập hợp các module có thể sử dụng
- **Constraints**: Các ràng buộc về kết nối giữa các module
- **Random Selection**: Chọn ngẫu nhiên dựa trên xác suất

## 2. Triển Khai với Module

### 2.1 Định Nghĩa Module Cơ Bản

Mỗi module được định nghĩa với các thông số:

| Thông số | Mô tả | Ví dụ |
|----------|-------|-------|
| Kích thước | Chiều rộng, cao, sâu | 4m × 4m × 3.5m |
| Kết nối | Các mặt có thể kết nối | North, South, East, West |
| Vật liệu | Loại vật liệu áp dụng | Wood, Brick, Gypsum |

### 2.2 Cấu Trúc Dữ Liệu Module

```python
class Module:
    def __init__(self, id, dimensions, connections, materials):
        self.id = id
        self.dimensions = dimensions  # (width, height, depth)
        self.connections = connections  # Dict of compatible modules
        self.materials = materials
```

### 2.3 Ma Trận Kết Nối

Mỗi module có các kết nối được định nghĩa:

```
Module A:
  - North face → kết nối với Module B, C
  - South face → kết nối với Module D
  - East face → kết nối với Door, Window
  - West face → kết nối với Module A
```

## 3. Thuật Toán WFC 3D

### 3.1 Pseudocode

```
function WFC_3D(grid_size, modules):
    // Khởi tạo grid
    grid = create_grid(grid_size)
    
    // Đặt entropy ban đầu
    for each cell in grid:
        cell.possible_modules = all_modules
    
    // Lặp cho đến khi hoàn thành
    while not is_complete(grid):
        // Tìm ô có entropy thấp nhất
        cell = find_lowest_entropy_cell(grid)
        
        // Chọn module dựa trên xác suất
        selected_module = select_module(cell.possible_modules)
        
        // Cập nhật các ô lân cận
        update_neighbors(grid, cell, selected_module)
        
        // Loại bỏ các module không tương thích
        remove_incompatible_modules(grid)
    
    return grid
```

### 3.2 Hàm Entropy

Entropy của một ô được tính bằng:

$$H(x) = -\sum_{i=1}^{n} p_i \log_2(p_i)$$

Trong đó $p_i$ là xác suất của module thứ $i$.

### 3.3 Cập Nhật Hàng Xóm

Khi một ô được chọn, các ô lân cận cần được cập nhật:

```python
def update_neighbors(grid, cell, selected_module):
    for direction in ['north', 'south', 'east', 'west', 'up', 'down']:
        neighbor = get_neighbor(cell, direction)
        if neighbor:
            # Lấy các module tương thích
            compatible = selected_module.connections[direction]
            # Loại bỏ các module không tương thích
            neighbor.possible_modules &= compatible
```

## 4. Ví Dụ Thực Tế

### 4.1 Case Study: Building Generation

**Thông số đầu vào:**
- Kích thước sàn: 4m × 4m
- Chiều cao tường: 3.5m
- Module cơ bản: 4 × 4 × 3.5

**Quy trình:**
1. Xác định kích thước cơ bản của module
2. Tạo các biến thể (variations) cho mỗi loại module
3. Định nghĩa ma trận kết nối
4. Chạy thuật toán WFC
5. Áp dụng vật liệu

### 4.2 Kết Quả

```
┌─────────────────────────────────┐
│  Module A ── Module B ── Module C  │
│     │           │            │       │
│  Module D ── Module E ── Module F  │
│     │           │            │       │
│  Module G ── Module H ── Module I  │
└─────────────────────────────────┘
```

## 5. Tối Ưu Hóa

### 5.1 Giảm Entropy

Để tăng tốc độ thuật toán:

1. **Prioritized Selection**: Chọn ô với ít khả năng nhất trước
2. **Constraint Propagation**: Lan truyền ràng buộc sớm
3. **Caching**: Lưu trữ kết quả tính toán

### 5.2 Xử Lý Lỗi

Khi không tìm được giải pháp hợp lệ:

```python
def backtrack(grid):
    # Quay lại và thử lựa chọn khác
    previous_state = save_state(grid)
    retry_count = 0
    
    while retry_count < MAX_RETRIES:
        if find_solution(grid):
            return True
        restore_state(grid, previous_state)
        retry_count += 1
    
    return False
```

## 6. Ứng Dụng Trong Unreal Engine 5

### 6.1 Tích Hợp với Blueprint

WFC có thể được tích hợp vào Unreal Engine thông qua:

- **Python Scripts**: Xử lý logic WFC
- **JSON Export**: Xuất dữ liệu module
- **Actor Spawning**: Tạo các actor trong Unreal

### 6.2 Workflow

```
Python WFC Script
       ↓
    JSON Output
       ↓
Blender Point Cloud
       ↓
Unreal Engine Import
       ↓
Procedural Building
```

## 7. Kết Luận

Thuật toán Wave Function Collapse là công cụ mạnh mẽ trong việc tạo môi trường procedural. Bằng cách định nghĩa các module và ràng buộc kết nối, chúng ta có thể tự động tạo ra các công trình phức tạp với sự đa dạng cao.

## Tài Liệu Tham Khảo

1. McGuire, M. (2017). "The Wave Function Collapse Algorithm". arXiv:1704.00035.

2. Karth, I., & Smith, A. (2017). "WaveFunctionCollapse is Constraint Solving in the Wild". Game Developers Conference 2017.

3. Parish, H., & Müller, P. (2001). "Procedural Modeling of Buildings". ACM SIGGRAPH 2001.

4. Unreal Engine Documentation. (2023). "Procedural Content Generation". https://docs.unrealengine.com
