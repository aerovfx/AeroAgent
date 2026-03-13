# Sản Xuất Props Đèn Neon Trong Unreal Engine

## Tổng Quan

Chương này hướng dẫn cách sản xuất các props đèn neon (neon light props) trong Unreal Engine 5. Đèn neon là yếu tố trang trí quan trọng, tạo điểm nhấn cho môi trường game.

## 1. Giới Thiệu về Đèn Neon

### 1.1 Đặc Điểm

Đèn neon có các đặc tính:
- Phát sáng rực rỡ
- Nhiều màu sắc đa dạng
- Hiệu ứng phát sáng (glow/bloom)
- Tiết kiệm năng lượng (trong game)

### 1.2 Ứng Dụng Trong Game

- Biển quảng cáo
- Trang trí nội thất
- Chiếu sáng đường phố
- Hiệu ứng thành phố ban đêm

## 2. Thiết Kế Trong Blender

### 2.1 Tạo Geometry

```python
# Tạo ống neon trong Blender
import bpy
import math

def create_neon_tube(name, path_points, radius=0.02):
    """Tạo ống neon theo đường path"""
    
    # Tạo curve từ các điểm
    curve_data = bpy.data.curves.new(name='NeonCurve', type='CURVE')
    curve_data.dimensions = '3D'
    curve_data.bevel_depth = radius
    curve_data.bevel_resolution = 4
    
    # Tạo spline
    spline = curve_data.splines.new('POLY')
    spline.points.add(len(path_points) - 1)
    
    for i, point in enumerate(path_points):
        x, y, z = point
        spline.points[i].co = (x, y, z, 1)
    
    # Tạo object
    obj = bpy.data.objects.new(name, curve_data)
    bpy.context.collection.objects.link(obj)
    
    return obj
```

### 2.2 Các Loại Neon Phổ Biến

| Loại | Hình dạng | Ứng dụng |
|------|-----------|-----------|
| Straight | Thẳng | Khung cửa |
| Curved | Cong | Biển quảng cáo |
| Spiral | Xoắn | Trang trí |
| Letter | Chữ | Logo, tên |

## 3. Vật Liệu Trong Substance Designer

### 3.1 Tạo Glass Tube Material

```python
# Cấu trúc graph cho ống thủy tinh
glass_graph = {
    'base_color': {
        'type': 'gradient',
        'start': (200, 200, 200),
        'end': (220, 220, 220)
    },
    'roughness': {
        'type': 'level',
        'value': 0.1
    },
    'metallic': {
        'type': 'level',
        'value': 0.0
    },
    'normal': {
        'type': 'normal_from_height',
        'strength': 0.3
    },
    'transmission': {
        'type': 'level',
        'value': 0.9
    }
}
```

### 3.2 Tạo Emissive Layer

```python
def create_neon_emissive(color, intensity=5.0):
    """Tạy lớp phát sáng cho đèn neon"""
    
    # Màu sắc cơ bản (đã được gamma corrected)
    emissive_color = color
    
    # Tạo mask cho phần phát sáng
    mask = create_gradient(
        start=(0, 0, 0),
        end=(1, 1, 1),
        angle=90
    )
    
    # Áp dụng intensity
    emissive = multiply(emissive_color, intensity * mask)
    
    return emissive
```

### 3.3 Tạo Các Biến Thể Màu

```python
neon_colors = {
    'red': (255, 50, 50),
    'pink': (255, 100, 200),
    'blue': (50, 100, 255),
    'cyan': (50, 255, 255),
    'green': (50, 255, 100),
    'yellow': (255, 255, 50),
    'orange': (255, 150, 50),
    'white': (255, 255, 255),
    'purple': (150, 50, 255)
}
```

## 4. Tích Hợp Trong Unreal Engine

### 4.1 Tạo Material Trong Unreal

```cpp
// Unreal Material Graph cho Neon
// Domain: Surface
// Blend Mode: Opaque (hoặc Translucent)

// Kết nối nodes:
// Emissive Color = NeonColor * EmissiveStrength
// Base Color = (0, 0, 0) - đen vì tự phát sáng
// Roughness = 0.3
// Metallic = 0.0
```

### 4.2 Cấu Hình Post-Process

```cpp
// Bật bloom cho hiệu ứng phát sáng
PostProcessVolume {
    bOverride_BloomIntensity = true
    BloomIntensity = 2.0
    BloomThreshold = 0.8
    BloomScale = 1.0
}
```

### 4.3 Material Instance Parameters

```python
# Tạo Material Instance với các thông số
neon_material = {
    'parent': 'M_NeonLight',
    'vector_parameters': {
        'NeonColor': (1.0, 0.2, 0.2, 1.0)  # Red
    },
    'scalar_parameters': {
        'EmissiveStrength': 50.0,
        'FlickerFrequency': 0.0,  # 0 = không nhấp nháy
        'RoughnessValue': 0.3
    }
}
```

## 5. Hiệu Ứng Nhấp Nháy (Flicker)

### 5.1 Shader Code

```hlsl
// Custom node trong Unreal Material

float time = GetWorldTime();
float flicker = 1.0;

// Flicker cơ bản
if (FlickerFrequency > 0) {
    float noise = frac(time * FlickerFrequency);
    flicker = step(0.5, noise);
}

// Thêm variation ngẫu nhiên
float randomFlicker = frac(sin(dot(GetWorldPosition(), 
                                   float3(12.9898, 78.233, 45.5432))) 
                           * 43758.5453);
flicker = lerp(flicker, randomFlicker, 0.3);

return EmissiveStrength * flicker;
```

### 5.2 Điều Khiển Bằng Blueprint

```cpp
// Trong Blueprint Actor

void ANeonLight::Tick(float DeltaTime) {
    if (bIsFlickering) {
        float randomValue = FMath::RandRange(0.0, 1.0);
        float newIntensity = FMath::Lerp(
            MinFlickerIntensity, 
            MaxFlickerIntensity, 
            randomValue
        );
        
        MaterialInstance->SetScalarParameterValue(
            "EmissiveStrength", 
            newIntensity
        );
    }
}
```

## 6. Tối Ưu Hiệu Suất

### 6.1 Best Practices

| Kỹ thuật | Mô tả | Hiệu quả |
|----------|-------|---------|
| Stationary Lights | Sử dụng stationary thay vì movable | Giảm draw calls |
| Lightmass | Precompute lighting cho static neon | Tăng performance |
| LOD | Sử dụng LOD cho neon ở xa | Tăng FPS |
| Emissive Only | Chỉ dùng emissive, không dùng actual light | Giảm calculation |

### 6.2 Cấu Hình Light

```cpp
// Light Actor cho neon
PointLight {
    Intensity = 100.0  # Tùy thuộc vào kích thước
    LightColor = (255, 100, 100)
    AttenuationRadius = 300.0
    Cast Shadows = false  # Không cần shadow cho neon
    bUseInverseSquaredFalloff = false
    FalloffExponent = 1.0
}
```

## 7. Export Từ Blender Sang Unreal

### 7.1 FBX Export Settings

```
Format: FBX
Include:
├── Geometry
├── Materials
├── UVs
└── Normals

Apply Scalings: All LocaltoWorld
Axis Forward: Z
Axis Up: Y
```

### 7.2 Import Trong Unreal

```python
# Sử dụng Python API trong Unreal
import unreal

# Import mesh
task = unreal.AssetImportTask()
task.set_editor_property('automated', True)
task.set_editor_property('destination_path', '/Game/Props/Neon')
task.set_editor_property('filename', 'neon_sign.fbx')
task.set_editor_property('replace_existing', True)

unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
```

## 8. Kết Luận

Việc tạo props đèn neon đòi hỏi:
- Thiết kế geometry phù hợp
- Tạo vật liệu phát sáng
- Cấu hình post-processing cho hiệu ứng bloom
- Tối ưu hóa cho game performance

Với quy trình này, bạn có thể tạo các đèn neon sống động cho môi trường game của mình.

## Tài Liệu Tham Khảo

1. Unreal Engine Documentation. (2023). "Materials".

2. Blender Foundation. (2023). "Blender Manual - Materials".

3. ambientCG. (2023). "PBR Materials".

4. Google. (2023). "Light, Lens and Flash - Neon Lighting Techniques".
