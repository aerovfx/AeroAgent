# Cài Đặt Module Pandas Trong Python

## Tổng Quan

Chương này hướng dẫn cách cài đặt và sử dụng module **Pandas** trong Python, một thư viện quan trọng để xử lý dữ liệu trong quy trình sản xuất môi trường procedural.

## 1. Giới Thiệu về Pandas

### 1.1 Pandas là gì?

Pandas là thư viện Python mã nguồn mở, cung cấp:
- Cấu trúc dữ liệu hiệu quả (DataFrame, Series)
- Công cụ xử lý và phân tích dữ liệu
- Hỗ trợ đọc/ghi nhiều định dạng file khác nhau

### 1.2 Ứng Dụng Trong Pipeline

Trong khóa học này, Pandas được sử dụng để:
- Đọc dữ liệu từ file Excel
- Chuyển đổi dữ liệu sang định dạng JSON
- Merge và xử lý các file dữ liệu module

## 2. Cài Đặt Pandas

### 2.1 Yêu Cầu Hệ Thống

- Python 3.8 trở lên
- pip hoặc conda package manager

### 2.2 Cài Đặt Qua pip

```bash
# Cài đặt Pandas
pip install pandas

# Kiểm tra phiên bản
python -c "import pandas; print(pandas.__version__)"
```

### 2.3 Cài Đặt Trong Môi Trường Ảo

```bash
# Tạo môi trường ảo
python -m venv venv

# Kích hoạt môi trường
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Cài đặt Pandas
pip install pandas
```

## 3. Sử Dụng Pandas Cơ Bản

### 3.1 Đọc File Excel

```python
import pandas as pd

# Đọc file Excel
df = pd.read_excel('modules.xlsx', sheet_name='Sheet1')

# Hiển thị dữ liệu
print(df.head())

# Lấy thông tin cột
print(df.columns)
```

### 3.2 Chuyển Đổi Sang JSON

```python
import json

# Chuyển DataFrame sang JSON
json_data = df.to_json(orient='records', indent=2)

# Lưu vào file
with open('modules.json', 'w') as f:
    f.write(json_data)
```

### 3.3 Xử Lý Dữ Liệu Module

```python
# Tạo DataFrame cho module
modules_data = {
    'module_id': ['wall_01', 'wall_02', 'door_01'],
    'width': [100, 150, 80],
    'height': [300, 300, 220],
    'depth': [20, 20, 15],
    'material': ['brick', 'wood', 'metal']
}

df = pd.DataFrame(modules_data)

# Thêm cột tính toán
df['volume'] = df['width'] * df['height'] * df['depth']

# Lọc dữ liệu
high_modules = df[df['height'] > 250]

print(df)
```

## 4. Xử Lý File Excel Đa Sheet

### 4.1 Đọc Nhiều Sheet

```python
# Đọc tất cả các sheet
excel_file = pd.ExcelFile('building_data.xlsx')

# Lấy danh sách sheet names
print(excel_file.sheet_names)

# Đọc từng sheet
for sheet_name in excel_file.sheet_names:
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    # Xử lý dữ liệu sheet
    process_sheet(df, sheet_name)
```

### 4.2 Merge Dữ Liệu

```python
# Đọc các file
walls = pd.read_excel('walls.xlsx')
doors = pd.read_excel('doors.xlsx')
windows = pd.read_excel('windows.xlsx')

# Merge tất cả
all_modules = pd.concat([walls, doors, windows], ignore_index=True)

# Lưu ra JSON
all_modules.to_json('all_modules.json', orient='records')
```

## 5. Xử Lý Dữ Liệu Module Nâng Cao

### 5.1 Tạo Cấu Trúc Module

```python
def create_module_json(excel_path, output_path):
    # Đọc dữ liệu
    df = pd.read_excel(excel_path)
    
    # Chuyển đổi sang format module
    modules = []
    for _, row in df.iterrows():
        module = {
            'id': row['module_id'],
            'dimensions': {
                'width': row['width'],
                'height': row['height'],
                'depth': row['depth']
            },
            'connections': parse_connections(row['connections']),
            'materials': row['materials'].split(',')
        }
        modules.append(module)
    
    # Lưu JSON
    with open(output_path, 'w') as f:
        json.dump({'modules': modules}, f, indent=2)

def parse_connections(conn_str):
    """Parse connection string to dict"""
    connections = {}
    for conn in conn_str.split(';'):
        face, compatible = conn.split(':')
        connections[face] = compatible.split(',')
    return connections
```

### 5.2 Validate Dữ Liệu

```python
def validate_modules(df):
    """Kiểm tra dữ liệu module"""
    errors = []
    
    # Kiểm tra các cột bắt buộc
    required_cols = ['module_id', 'width', 'height', 'depth']
    for col in required_cols:
        if col not in df.columns:
            errors.append(f"Thiếu cột: {col}")
    
    # Kiểm tra giá trị không null
    for col in required_cols:
        if df[col].isnull().any():
            errors.append(f"Có giá trị null trong cột: {col}")
    
    # Kiểm tra giá trị dương
    for col in ['width', 'height', 'depth']:
        if (df[col] <= 0).any():
            errors.append(f"Kích thước phải > 0 trong cột: {col}")
    
    return errors
```

## 6. Tích Hợp Với Blender

### 6.1 Sử Dụng Pandas Trong Blender Python

```python
import pandas as pd
import bpy
import json

# Đọc dữ liệu module
df = pd.read_excel('//modules.xlsx')

# Tạo objects trong Blender
for _, row in df.iterrows():
    bpy.ops.mesh.primitive_cube_add(
        size=1,
        location=(row['x'], row['y'], row['z'])
    )
    obj = bpy.context.active_object
    obj.name = row['module_id']
    obj.scale = (
        row['width'] / 100,
        row['depth'] / 100,
        row['height'] / 100
    )
```

## 7. Best Practices

### 7.1 Quản Lý Dữ Liệu

| Practice | Mô tả |
|----------|-------|
| Backup | Luôn backup file Excel gốc |
| Validation | Kiểm tra dữ liệu trước khi xử lý |
| Logging | Ghi log quá trình xử lý |
| Error Handling | Xử lý lỗi graceful |

### 7.2 Tối Ưu Hiệu Suất

```python
# Sử dụng appropriate dtypes
df = df.astype({
    'module_id': 'string',
    'width': 'int32',
    'height': 'int32',
    'depth': 'int32'
})

# Chỉ đọc cần thiết
df = pd.read_excel('file.xlsx', usecols=['A', 'B', 'C'])
```

## 8. Kết Luận

Pandas là công cụ không thể thiếu trong pipeline xử lý dữ liệu module. Việc thành thạo Pandas sẽ giúp bạn:
- Xử lý dữ liệu hiệu quả
- Tự động hóa quy trình
- Giảm lỗi thủ công

## Tài Liệu Tham Khảo

1. Pandas Documentation. (2023). "pandas: powerful Python data analysis toolkit". https://pandas.pydata.org/

2. Python Software Foundation. (2023). "Python 3 Documentation". https://docs.python.org/3/

3. McKinney, W. (2017). *Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython*. O'Reilly Media.
