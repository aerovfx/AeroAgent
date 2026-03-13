# Sản Xuất Vật Liệu Tường Thạch Cao (Gypsum Wall)

## Tổng Quan

Chương này hướng dẫn cách sản xuất vật liệu tường thạch cao (gypsum wall) sử dụng **Substance Designer**. Đây là loại vật liệu phổ biến trong xây dựng và được áp dụng rộng rãi trong các dự án Unreal Engine 5.

## 1. Giới Thiệu về Vật Liệu Thạch Cao

### 1.1 Đặc Tính

Vật liệu thạch cao có các đặc tính:
- Bề mặt mịn, ít hoa văn
- Màu sắc: trắng, be, xám nhạt
- Khả năng chống ẩm hạn chế
- Dễ dàng tạo các biến thể

### 1.2 Ứng Dụng

Trong môi trường procedural:
- Tường trong nhà
- Trần nhà
- Các chi tiết trang trí

## 2. Quy Trình Sản Xuất Trong Substance Designer

### 2.1 Thiết Lập Cơ Bản

1. **Tạo Project Mới**
   - Chọn template: Bitmap → PBR Metallic Roughness
   - Kích thước: 2048 × 2048 (hoặc 4096 × 4096)

2. **Cấu Trúc Graph**
   ```
   Graph chính
   ├── Base Color
   │   ├── Gradient
   │   ├── Noise
   │   └── Color Correction
   ├── Roughness
   │   ├── Levels
   │   └── Noise
   ├── Normal
   │   ├── Normal From Height
   │   └── Normal Blend
   └── Height
       ├── Clouds
       └── Levels
   ```

### 2.2 Tạo Base Color

```python
# Thiết lập màu cơ bản
base_color = (245, 240, 235)  # Màu trắng be

# Thêm biến thể
def create_gypsum_color():
    color = create_gradient(
        start_color=(250, 245, 240),
        end_color=(235, 230, 225),
        angle=90
    )
    
    # Thêm noise cho variation
    noise = create_noise(
        scale=50,
        intensity=0.05,
        color_mode="multiply"
    )
    
    return blend(color, noise, mode="multiply")
```

### 2.3 Tạo Roughness Map

```python
def create_gypsum_roughness():
    # Giá trị roughness cơ bản
    base_roughness = 0.7
    
    # Thêm variation
    noise = create_noise(
        scale=100,
        intensity=0.15,
        color_mode="add"
    )
    
    roughness = base_roughness + noise
    
    # Áp dụng levels
    roughness = apply_levels(
        roughness,
        input_min=0.5,
        input_max=0.9,
        output_min=0.6,
        output_max=0.8
    )
    
    return roughness
```

### 2.4 Tạo Normal Map

```python
def create_gypsum_normal():
    # Tạo height map từ noise
    height = create_clouds(
        scale=30,
        octaves=4,
        lacunarity=2.0,
        intensity=0.1
    )
    
    # Chuyển đổi sang normal
    normal = normal_from_height(
        height,
        strength=0.5,
        filter_mode="sobel"
    )
    
    # Làm mịn normal
    normal = apply_blur(
        normal,
        radius=2,
        iterations=1
    )
    
    return normal
```

## 3. Xử Lý UV Cho Module

### 3.1 Vấn Đề UV Trong Procedural

Khi áp dụng vật liệu lên các module có kích thước khác nhau:
- UV mapping không đồng đều
- Texture stretched hoặc compressed
- Cần điều chỉnh UV scale

### 3.2 Giải Pháp UV Trong Substance

```python
def adjust_uv_scale(module_width, module_height, texture_size=2048):
    """Tính toán UV scale cho module"""
    
    # Tỷ lệ pixels per meter
    ppm = texture_size / max(module_width, module_height)
    
    # Tạo transform 2D
    transform = {
        'scale_u': ppm / 100,  # scale theo chiều U
        'scale_v': ppm / 100,  # scale theo chiều V
        'offset_u': 0,
        'offset_v': 0,
        'rotation': 0
    }
    
    return transform
```

### 3.3 Tạo Presets Cho Các Module

| Module Type | Width (cm) | Height (cm) | UV Scale |
|-------------|------------|-------------|----------|
| Wall Standard | 100 | 300 | 1.0 |
| Wall Short | 100 | 220 | 0.73 |
| Door Frame | 80 | 220 | 0.73 |
| Window | 120 | 150 | 0.5 |

## 4. Tạo Biến Thể

### 4.1 Color Variations

```python
def create_gypsum_variants():
    variants = [
        {
            'name': 'Pure White',
            'base_color': (250, 250, 250),
            'roughness': 0.65
        },
        {
            'name': 'Warm White',
            'base_color': (245, 240, 235),
            'roughness': 0.70
        },
        {
            'name': 'Cool Gray',
            'base_color': (235, 235, 240),
            'roughness': 0.75
        }
    ]
    
    return variants
```

### 4.2 Surface Variations

- **Smooth**: Roughness ~0.6
- **Standard**: Roughness ~0.7
- **Textured**: Roughness ~0.8 + Normal detail

## 5. Export và Sử Dụng Trong Unreal

### 5.1 Export Settings

```
Format: PNG
Bit Depth: 8-bit hoặc 16-bit
Color Space: sRGB (Base Color), Linear (Others)

Output Maps:
├── Base_Color.png
├── Roughness.png
├── Normal.png
├── Metallic.png (optional)
└── Height.png (optional)
```

### 5.2 Import Trong Unreal Engine

```python
# Trong Unreal, cần tạo Material Instance
# và điều chỉnh các thông số:
material_instance = create_material_instance(
    parent_material="M_GypsumWall",
    texture_parameters={
        'Base_Color_Tex': "Gypsum_BC.png",
        'Roughness_Tex': "Gypsum_R.png",
        'Normal_Tex': "Gypsum_N.png"
    },
    scalar_parameters={
        'Roughness_Multiplier': 1.0,
        'Normal_Strength': 1.0
    }
)
```

## 6. Best Practices

### 6.1 Quy Tắc Thiết Kế

| Nguyên tắc | Mô tả |
|------------|-------|
| Consistency | Giữ style nhất quán |
| Flexibility | Tạo nhiều biến thể |
| Performance | Tối ưu texture size |
| Reusability | Thiết kế để tái sử dụng |

### 6.2 Tối Ưu Hiệu Suất

```python
# Sử dụng texture resolution phù hợp
texture_resolution_guide = {
    'Close-up': 4096,
    'Medium': 2048,
    'Far': 1024,
    'Background': 512
}
```

## 7. Kết Luận

Việc tạo vật liệu thạch cao trong Substance Designer đòi hỏi:
- Hiểu về các loại maps (Base Color, Roughness, Normal)
- Xử lý UV phù hợp cho từng module
- Tạo các biến thể đa dạng

Với quy trình này, bạn có thể tạo ra các vật liệu tường chất lượng cao cho Unreal Engine 5.

## Tài Liệu Tham Khảo

1. Adobe. (2023). "Substance Designer User Guide". https://substance3d.com/

2. Unreal Engine Documentation. (2023). "Materials".

3. ambientCG. (2023). "PBR Material Workflow".

4. Allegorithmic. (2019). "Substance Designer Fundamentals".
