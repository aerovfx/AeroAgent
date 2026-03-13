# Giải Thích Chi Tiết Quy Trình NorthwoodWFC

## Tổng Quan

Chương này cung cấp giải thích chi tiết về quy trình **NorthwoodWFC** - một framework triển khai Wave Function Collapse cho việc tạo môi trường procedural trong Unreal Engine 5. Việc hiểu rõ quy trình này là nền tảng quan trọng cho các bước tiếp theo trong khóa học.

## 1. Giới Thiệu NorthwoodWFC

### 1.1 Background

NorthwoodWFC là một implementation cụ thể của thuật toán Wave Function Collapse, được phát triển để:
- Tạo các công trình kiến trúc procedural
- Quản lý kết nối giữa các module
- Hỗ trợ nhiều loại vật liệu khác nhau

### 1.2 Các Thành Phần Chính

| Thành phần | Chức năng |
|------------|-----------|
| Module Manager | Quản lý các module |
| Grid System | Hệ thống lưới 3D |
| Constraint Solver | Giải quyết ràng buộc |
| Material System | Hệ thống vật liệu |

## 2. Kiến Trúc Hệ Thống

### 2.1 Module Manager

Module Manager chịu trách nhiệm:
- Tải và lưu trữ thông tin module
- Quản lý dependencies giữa các module
- Cung cấp interface cho việc truy xuất module

```python
class ModuleManager:
    def __init__(self):
        self.modules = {}
        self.compatibility_matrix = {}
    
    def load_modules(self, json_path):
        with open(json_path, 'r') as f:
            data = json.load(f)
            for module in data['modules']:
                self.modules[module['id']] = Module(**module)
    
    def get_compatible_modules(self, face_direction, current_module):
        return self.compatibility_matrix[current_module][face_direction]
```

### 2.2 Grid System

Hệ thống lưới 3D lưu trữ trạng thái của mỗi ô:

```
Grid[ x ][ y ][ z ] = {
    'possible_modules': [module1, module2, ...],
    'selected_module': None,
    'material': None
}
```

**Kích thước grid:** được xác định bởi kích thước module và kích thước building mong muốn.

### 2.3 Constraint Solver

Constraint Solver xử lý các ràng buộc:

1. **Adjacency Constraints**: Ràng buộc về kết nối giữa các mặt
2. **Enclosure Constraints**: Ràng buộc về không gian kín
3. **Height Constraints**: Ràng buộc về chiều cao

```python
def solve_constraints(grid, x, y, z, selected_module):
    # Kiểm tra các mặt kết nối
    for direction in ['north', 'south', 'east', 'west', 'up', 'down']:
        neighbor = get_neighbor(x, y, z, direction)
        if neighbor:
            compatible = check_compatibility(selected_module, neighbor, direction)
            if not compatible:
                return False
    return True
```

## 3. Quy Trình Triển Khai

### 3.1 Bước 1: Khởi Tạo Grid

```python
def initialize_grid(width, height, depth, all_modules):
    grid = []
    for x in range(width):
        layer = []
        for y in range(height):
            row = []
            for z in range(depth):
                cell = {
                    'possible_modules': set(all_modules),
                    'selected': None,
                    'collapsed': False
                }
                row.append(cell)
            layer.append(row)
        grid.append(layer)
    return grid
```

### 3.2 Bước 2: Chọn Ô Để Collapse

Chọn ô có entropy thấp nhất (ít khả năng nhất):

```python
def find_cell_to_collapse(grid):
    min_entropy = float('inf')
    best_cell = None
    best_position = None
    
    for x, y, z in grid_positions(grid):
        cell = grid[x][y][z]
        if not cell['collapsed']:
            entropy = calculate_entropy(cell['possible_modules'])
            if entropy < min_entropy:
                min_entropy = entropy
                best_cell = cell
                best_position = (x, y, z)
    
    return best_position, best_cell
```

### 3.3 Bước 3: Collapse Module

Chọn một module dựa trên xác suất:

```python
def collapse_cell(grid, x, y, z):
    cell = grid[x][y][z]
    possible = list(cell['possible_modules'])
    
    if len(possible) == 0:
        return False  # Thất bại - không có giải pháp
    
    # Chọn ngẫu nhiên với xác suất
    weights = [module.weight for module in possible]
    selected = random.choices(possible, weights=weights)[0]
    
    cell['selected'] = selected
    cell['collapsed'] = True
    
    return True
```

### 3.4 Bước 4: Cập Nhật Hàng Xóm

```python
def propagate_constraints(grid, x, y, z):
    selected = grid[x][y][z]['selected']
    directions = ['north', 'south', 'east', 'west', 'up', 'down']
    
    for direction in directions:
        neighbor_pos = get_neighbor_position(x, y, z, direction)
        if neighbor_pos:
            nx, ny, nz = neighbor_pos
            neighbor = grid[nx][ny][nz]
            
            if not neighbor['collapsed']:
                # Lấy các module tương thích
                compatible = selected.compatible[direction]
                # Loại bỏ các module không tương thích
                neighbor['possible_modules'] &= compatible
                
                # Kiểm tra nếu không còn khả năng
                if len(neighbor['possible_modules']) == 0:
                    return False  # Cần backtrack
    
    return True
```

## 4. Xử Lý Point Cloud

### 4.1 Xuất Dữ Liệu Sang Point Cloud

Sau khi WFC hoàn thành, dữ liệu được xuất sang point cloud để import vào Blender/Unreal:

```python
def export_to_point_cloud(grid, output_path):
    points = []
    
    for x, y, z in grid_positions(grid):
        cell = grid[x][y][z]
        if cell['collapsed']:
            module = cell['selected']
            # Tính toán vị trí các đỉnh
            vertices = get_module_vertices(x, y, z, module)
            points.extend(vertices)
    
    # Xuất sang định dạng CSV
    save_as_csv(points, output_path)
```

### 4.2 Định Dạng Point Cloud

```
X, Y, Z, NormalX, NormalY, NormalZ, U, V, ModuleID
0, 0, 0, 0, 0, 1, 0, 0, wall_01
0, 100, 0, 0, 0, 1, 0.5, 0, wall_02
...
```

## 5. Tích Hợp Với Pipeline

### 5.1 Blender Integration

```python
# Import point cloud vào Blender
import bpy
import csv

def import_point_cloud(csv_path):
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Tạo vertices
            x, y, z = float(row['X']), float(row['Y']), float(row['Z'])
            # Tạo mesh cho module
            create_module_mesh(row['ModuleID'], (x, y, z))
```

### 5.2 Unreal Engine Integration

```
Point Cloud (Blender)
       ↓
    JSON Export
       ↓
Unreal Engine Blueprint
       ↓
    Actor Spawning
```

## 6. Tối Ưu Hóa và Best Practices

### 6.1 Tối Ưu Hiệu Suất

| Kỹ thuật | Mô tả | Lợi ích |
|----------|-------|---------|
| Early Termination | Dừng sớm khi không tìm thấy giải pháp | Tiết kiệm thời gian |
| Parallel Processing | Xử lý song song nhiều ô | Tăng tốc độ |
| Caching | Lưu kết quả tính toán | Giảm tính toán lặp |

### 6.2 Xử Lý Lỗi

```python
def wfc_with_backtrack(grid, max_retries=10):
    for attempt in range(max_retries):
        try:
            result = run_wfc(grid)
            if result:
                return result
        except ContradictionError:
            grid = reset_grid(grid)  # Reset và thử lại
    
    return None  # Thất bại sau nhiều lần thử
```

## 7. Kết Luận

NorthwoodWFC là một framework mạnh mẽ cho việc tạo môi trường procedural. Việc hiểu rõ các thành phần và quy trình sẽ giúp bạn:
- Tùy chỉnh thuật toán theo nhu cầu
- Tích hợp vào pipeline hiện có
- Xử lý các vấn đề phát sinh

## Tài Liệu Tham Khảo

1. McGuire, M. (2017). "The Wave Function Collapse Algorithm". arXiv:1704.00035.

2. Parish, H., & Müller, P. (2001). "Procedural Modeling of Buildings". SIGGRAPH 2001.

3. Unreal Engine Documentation. (2023). "Procedural Content Generation in Unreal Engine".

4. Blender Python API Documentation. (2023). "bpy - Blender Python API".
