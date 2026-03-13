# Triển Khai Thuật Toán Wave Function Collapse 3D

## Tổng Quan

Chương này hướng dẫn chi tiết cách triển khai thuật toán **Wave Function Collapse (WFC) 3D** trong Python để tạo môi trường procedural. Đây là phần cốt lõi của pipeline sản xuất môi trường.

## 1. Giới Thiệu WFC 3D

### 1.1 Khác Biệt 2D và 3D

| Khía cạnh | WFC 2D | WFC 3D |
|-----------|---------|---------|
| Chiều | X, Y | X, Y, Z |
| Kết nối | 4 hướng | 6 hướng |
| Module | 2D tiles | 3D voxels |
| Độ phức tạp | Thấp | Cao |

### 1.2 Thách Thức với WFC 3D

- **Không gian 3D**: Tăng số lượng ô cần xử lý
- **Kết nối phức tạp**: 6 mặt thay vì 4
- **Hiệu suất**: Cần thuật toán tối ưu

## 2. Cấu Trúc Dữ Liệu

### 2.1 Module 3D

```python
class Module3D:
    def __init__(self, id, dimensions, connections, materials):
        self.id = id
        self.dimensions = dimensions  # (width, height, depth)
        # 6 directions: +X, -X, +Y, -Y, +Z, -Z
        self.connections = connections  # {direction: [compatible_modules]}
        self.materials = materials
        self.weight = 1.0  # Xác suất được chọn
```

### 2.2 Grid 3D

```python
class Grid3D:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
        self.cells = self._initialize_grid()
    
    def _initialize_grid(self):
        grid = []
        for x in range(self.width):
            layer = []
            for y in range(self.height):
                row = []
                for z in range(self.depth):
                    cell = Cell3D(x, y, z)
                    row.append(cell)
                layer.append(row)
            grid.append(layer)
        return grid
    
    def get_cell(self, x, y, z):
        if 0 <= x < self.width and \
           0 <= y < self.height and \
           0 <= z < self.depth:
            return self.cells[x][y][z]
        return None
```

### 2.3 Cell Class

```python
class Cell3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.possible_modules = set()
        self.selected_module = None
        self.collapsed = False
    
    def calculate_entropy(self):
        return len(self.possible_modules)
```

## 3. Triển Khai Thuật Toán

### 3.1 Khởi Tạo

```python
def initialize_wfc(grid, all_modules):
    """Khởi tạo grid với tất cả modules"""
    for x in range(grid.width):
        for y in range(grid.height):
            for z in range(grid.depth):
                cell = grid.get_cell(x, y, z)
                cell.possible_modules = set(all_modules)
```

### 3.2 Chọn Ô Để Collapse

```python
import random
import heapq

def find_next_cell(grid):
    """Tìm ô có entropy thấp nhất"""
    min_entropy = float('inf')
    candidates = []
    
    for x in range(grid.width):
        for y in range(grid.height):
            for z in range(grid.depth):
                cell = grid.get_cell(x, y, z)
                if not cell.collapsed:
                    entropy = cell.calculate_entropy()
                    if entropy > 0:
                        heapq.heappush(candidates, (entropy, x, y, z))
    
    if not candidates:
        return None
    
    _, x, y, z = heapq.heappop(candidates)
    return grid.get_cell(x, y, z)
```

### 3.3 Collapse Module

```python
def collapse_cell(cell, modules):
    """Chọn và gán module cho ô"""
    if len(cell.possible_modules) == 0:
        return False
    
    # Lấy danh sách module có thể
    possible = list(cell.possible_modules)
    
    # Tính trọng số xác suất
    weights = [m.weight for m in possible]
    total = sum(weights)
    weights = [w / total for w in weights]
    
    # Chọn ngẫu nhiên theo xác suất
    selected = random.choices(possible, weights=weights)[0]
    
    # Gán module
    cell.selected_module = selected
    cell.collapsed = True
    cell.possible_modules = {selected}
    
    return True
```

### 3.4 Lan Truyền Ràng Buộc

```python
def propagate_constraints(grid, module, x, y, z):
    """Lan truyền ràng buộc đến các ô lân cận"""
    directions = {
        'positive_x': (1, 0, 0),
        'negative_x': (-1, 0, 0),
        'positive_y': (0, 1, 0),
        'negative_y': (0, -1, 0),
        'positive_z': (0, 0, 1),
        'negative_z': (0, 0, -1)
    }
    
    stack = [(x, y, z)]
    visited = set()
    
    while stack:
        cx, cy, cz = stack.pop()
        if (cx, cy, cz) in visited:
            continue
        visited.add((cx, cy, cz))
        
        cell = grid.get_cell(cx, cy, cz)
        if cell.collapsed:
            continue
        
        # Kiểm tra các hướng
        for direction, (dx, dy, dz) in directions.items():
            nx, ny, nz = cx + dx, cy + dy, cz + dz
            neighbor = grid.get_cell(nx, ny, nz)
            
            if neighbor and not neighbor.collapsed:
                # Lấy module tương thích
                compatible = module.connections.get(direction, [])
                
                # Loại bỏ các module không tương thích
                old_possible = set(neighbor.possible_modules)
                neighbor.possible_modules &= set(compatible)
                
                # Nếu có thay đổi, thêm vào stack
                if neighbor.possible_modules != old_possible:
                    if len(neighbor.possible_modules) == 0:
                        return False  # Contradiction
                    stack.append((nx, ny, nz))
    
    return True
```

### 3.5 Main Loop

```python
def run_wfc(grid, modules, max_iterations=10000):
    """Chạy thuật toán WFC"""
    initialize_wfc(grid, modules)
    
    for iteration in range(max_iterations):
        # Tìm ô tiếp theo
        cell = find_next_cell(grid)
        
        if cell is None:
            print("Hoàn thành!")
            return True
        
        # Collapse ô
        if not collapse_cell(cell, modules):
            print(f"Lỗi tại ô ({cell.x}, {cell.y}, {cell.z})")
            return False
        
        # Lan truyền ràng buộc
        if not propagate_constraints(grid, cell.selected_module, 
                                     cell.x, cell.y, cell.z):
            print("Xung đột ràng buộc!")
            return False
    
    print("Đạt số iteration tối đa")
    return True
```

## 4. Tối Ưu Hóa

### 4.1 Parallel Processing

```python
from concurrent.futures import ThreadPoolExecutor

def propagate_parallel(grid, module, positions):
    """Lan truyền song song"""
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        for pos in positions:
            future = executor.submit(propagate_single, grid, module, pos)
            futures.append(future)
        
        for future in futures:
            if not future.result():
                return False
    return True
```

### 4.2 Caching

```python
from functools import lru_cache

@lru_cache(maxsize=10000)
def get_compatible_modules(module_id, direction):
    """Cache kết quả tương thích"""
    module = get_module_by_id(module_id)
    return tuple(module.connections.get(direction, []))
```

### 4.3 Early Termination

```python
def should_terminate(grid, iteration, max_iterations):
    """Kiểm tra điều kiện dừng"""
    # Kiểm tra đã hoàn thành chưa
    collapsed_count = sum(
        1 for x in range(grid.width)
          for y in range(grid.height)
          for z in range(grid.depth)
          if grid.get_cell(x, y, z).collapsed
    )
    
    total_cells = grid.width * grid.height * grid.depth
    
    return collapsed_count == total_cells or iteration >= max_iterations
```

## 5. Xuất Kết Quả

### 5.1 Export Sang JSON

```python
def export_to_json(grid, output_path):
    """Xuất kết quả WFC sang JSON"""
    result = {
        'dimensions': {
            'width': grid.width,
            'height': grid.height,
            'depth': grid.depth
        },
        'cells': []
    }
    
    for x in range(grid.width):
        for y in range(grid.height):
            for z in range(grid.depth):
                cell = grid.get_cell(x, y, z)
                if cell.collapsed:
                    result['cells'].append({
                        'position': [x, y, z],
                        'module_id': cell.selected_module.id,
                        'dimensions': cell.selected_module.dimensions
                    })
    
    with open(output_path, 'w') as f:
        json.dump(result, f, indent=2)
```

### 5.2 Export Sang Point Cloud

```python
def export_to_point_cloud(grid, output_path):
    """Xuất sang point cloud cho Blender"""
    points = []
    
    for x in range(grid.width):
        for y in range(grid.height):
            for z in range(grid.depth):
                cell = grid.get_cell(x, y, z)
                if cell.collapsed:
                    module = cell.selected_module
                    # Tính toán vertices
                    vertices = calculate_box_vertices(
                        x, y, z, 
                        module.dimensions
                    )
                    points.extend(vertices)
    
    # Lưu CSV
    with open(output_path, 'w') as f:
        f.write("X,Y,Z,NormalX,NormalY,NormalZ,U,V,ModuleID\n")
        for point in points:
            f.write(f"{point}\n")
```

## 6. Ví Dụ Sử Dụng

```python
# Khởi tạo
grid = Grid3D(10, 10, 10)
modules = load_modules_from_json('modules.json')

# Chạy WFC
success = run_wfc(grid, modules)

if success:
    # Xuất kết quả
    export_to_json(grid, 'output.json')
    export_to_point_cloud(grid, 'point_cloud.csv')
```

## 7. Kết Luận

Việc triển khai WFC 3D đòi hỏi:
- Hiểu biết về cấu trúc dữ liệu 3D
- Xử lý ràng buộc hiệu quả
- Tối ưu hóa cho performance

Với implementation này, bạn có thể tạo ra các công trình procedural phức tạp trong không gian 3D.

## Tài Liệu Tham Khảo

1. McGuire, M. (2017). "The Wave Function Collapse Algorithm". arXiv:1704.00035.

2. Karth, I., & Smith, A. (2017). "WaveFunctionCollapse is Constraint Solving in the Wild". GDC 2017.

3. Python Documentation. (2023). "concurrent.futures - Parallel Computation".
