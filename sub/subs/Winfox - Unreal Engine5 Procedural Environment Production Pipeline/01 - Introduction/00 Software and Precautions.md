# Phần Mềm và Lưu Ý Cần Thiết

## Tổng Quan

Chương này giới thiệu về các phần mềm được sử dụng trong khóa học **Unreal Engine 5 Procedural Environment Production Pipeline** và các phiên bản tương ứng. Đây là một khóa học nâng cao yêu cầu người học cần có kiến thức cơ bản về các phần mềm được sử dụng.

## 1. Các Phần Mềm Chính

### 1.1 Blender

**Phiên bản sử dụng:** Blender 19.5.303

Blender là phần mềm mã nguồn mở cho đồ họa 3D, được sử dụng để:
- Tạo và chỉnh sửa mô hình 3D
- Xử lý point cloud
- Export dữ liệu cho các công cụ khác

**Lưu ý:** Bất kỳ phiên bản nào của Blender 19.x đều có thể sử dụng được, các phiên bản nhỏ không ảnh hưởng đến quá trình sử dụng.

### 1.2 VS Code

Visual Studio Code được sử dụng để:
- Chỉnh sửa code Python
- Quản lý các script tự động hóa
- Debug các vấn đề liên quan đến pipeline

### 1.3 3D Converter (3FX Lab Plugin)

Đây là plugin quan trọng cho phép chuyển đổi định dạng giữa các phần mềm 3D. Plugin này sẽ được cài đặt trong quá trình hướng dẫn.

### 1.4 Substance Designer

**Phiên bản sử dụng:** Substance Designer 2023

Substance Designer được sử dụng để tạo các loại vật liệu (materials) khác nhau như:
- Vật liệu tường (wall materials)
- Vật liệu gỗ (wood materials)
- Vật liệu đá (stone materials)

**Nguồn tải:**
- Website chính thức: Adobe Substance
- Steam: Phiên bản Steam tiện lợi hơn cho việc mua bán

### 1.5 Unreal Engine 5

**Phiên bản sử dụng:** Unreal Engine 5.0.3

Unreal Engine 5 là engine game chính được sử dụng để:
- Import và hiển thị môi trường procedural
- Tạo lighting và post-processing
- Build và export dự án cuối cùng

## 2. Yêu Cầu Kỹ Thuật

### 2.1 Kiến Thức Nền Tảng

| Phần mềm | Yêu cầu | Ghi chú |
|----------|----------|---------|
| Blender | Kiến thức cơ bản | Hiểu về nodes và workflow |
| Python | Không bắt buộc | Script đơn giản, dễ học |
| Substance Designer | Kiến thức cơ bản về materials | Có thể học trong quá trình |
| Unreal Engine 5 | Hiểu basic workflow | Đủ để import và setup |

### 2.2 Python và Pandas

Do sử dụng Python cho việc xử lý dữ liệu, người học cần cài đặt:

```python
# Cài đặt pandas
pip install pandas
```

Pandas được sử dụng để:
- Đọc và xử lý file Excel
- Chuyển đổi dữ liệu sang định dạng JSON
- Merge và xử lý các file dữ liệu module

## 3. Cấu Trúc Dữ Liệu

### 3.1 Module Interface

Cấu trúc module cơ bản được định nghĩa trong các file JSON với format:

```json
{
  "module_id": "wall_01",
  "dimensions": {
    "width": 100,
    "height": 300,
    "depth": 20
  },
  "connections": {
    "north": ["wall_02", "wall_03"],
    "south": ["wall_02"],
    "east": ["door_01", "window_01"],
    "west": []
  },
  "materials": ["wood", "brick", "gypsum"]
}
```

### 3.2 Point Cloud Format

Dữ liệu point cloud được lưu trữ dưới dạng:

```
X, Y, Z, NormalX, NormalY, NormalZ, UVU, UVV
```

## 4. Pipeline Tổng Quan

### 4.1 Quy Trình Sản Xuất

```
Blender → Python Scripts → JSON Data → 3D WFC → Unreal Engine 5
                                      ↓
                              Substance Designer
                                      ↓
                              Materials & Props
```

### 4.2 Các Bước Chính

1. **Module Planning**: Thiết kế và lập kế hoạch các module
2. **Python Processing**: Xử lý dữ liệu với Python/Pandas
3. **Wave Function Collapse**: Triển khai thuật toán WFC 3D
4. **Material Production**: Tạo vật liệu với Substance Designer
5. **Props Generation**: Tạo các đạo cụ (props)
6. **Scene Assembly**: Lắp ráp scene cuối cùng trong Unreal

## 5. Kết Luận

Việc chuẩn bị đầy đủ các phần mềm và hiểu về pipeline là bước quan trọng để bắt đầu khóa học. Các yêu cầu về phiên bản không quá nghiêm ngặt, nhưng khuyến nghị sử dụng các phiên bản được указаны để đảm bảo tính tương thích.

## Tài Liệu Tham Khảo

1. Epic Games. (2023). *Unreal Engine 5 Documentation*. https://docs.unrealengine.com

2. Adobe. (2023). *Substance Designer User Guide*. https://substance3d.com/

3. Blender Foundation. (2023). *Blender Manual*. https://docs.blender.org/

4. McGuire, M. (2017). *The Wave Function Collapse Algorithm*. https://arxiv.org/abs/1704.00035
